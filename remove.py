import os
import sys
import requests
from InquirerPy import inquirer
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_USERNAME or not GITHUB_TOKEN:
    print("Error: Pastikan environment variable GITHUB_USERNAME dan GITHUB_TOKEN sudah diatur.")
    sys.exit(1)

API_BASE_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_all_repositories() -> list[str]:
    repositories = []
    page = 1
    while True:
        url = f"{API_BASE_URL}/user/repos?per_page=100&page={page}"
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            if not data:
                break
                
            repositories.extend([repo["name"] for repo in data])
            page += 1
        except requests.RequestException as e:
            print(f"Gagal mengambil data repository: {e}")
            sys.exit(1)
            
    return repositories

def select_repositories_to_delete(repo_choices: list[str]) -> list[str]:
    if not repo_choices:
        return []
        
    selected_repos = inquirer.checkbox(
        message="Pilih repository yang ingin dihapus:",
        choices=repo_choices,
        instruction="Gunakan spasi untuk memilih dan Enter untuk konfirmasi."
    ).execute()
    return selected_repos

def delete_repository(repo_name: str) -> None:
    url = f"{API_BASE_URL}/repos/{GITHUB_USERNAME}/{repo_name}"
    try:
        response = requests.delete(url, headers=HEADERS, timeout=10)
        
        if response.status_code == 204:
            print(f"Berhasil: Repository '{repo_name}' telah dihapus.")
        else:
            print(f"Gagal: Tidak dapat menghapus '{repo_name}'. Status: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Gagal: Terjadi kesalahan saat menghubungi API untuk menghapus '{repo_name}': {e}")

def main() -> None:
    print("Mengambil daftar repository...")
    all_repos = get_all_repositories()

    if not all_repos:
        print("Tidak ada repository yang ditemukan di akun Anda.")
        return

    selected_to_delete = select_repositories_to_delete(all_repos)

    if not selected_to_delete:
        print("Tidak ada repository yang dipilih. Proses dibatalkan.")
        return

    print("\nProses penghapusan akan dimulai...")
    for repo in selected_to_delete:
        delete_repository(repo)
    print("\nProses selesai.")

if __name__ == "__main__":
    main()
