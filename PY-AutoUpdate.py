import requests
import git
import os

# Nastav URL tvojho GitHub repozitára
repo_url = 'https://github.com/fattcat/AutoGit'

# Funkcia na stiahnutie poslednej verzie z GitHub
def download_latest_version():
    response = requests.get(f'{repo_url}/releases/latest')
    if response.status_code == 200:
        latest_release = response.url
        latest_version = latest_release.split("/")[-1]
        return latest_version
    else:
        return None

# Funkcia na aktualizáciu kódu
def update_code():
    repo_dir = 'AutoGit'  # Zmeň na adresár tvojho projektu
    if os.path.exists(repo_dir):
        repo = git.Repo(repo_dir)
        origin = repo.remotes.origin
        origin.pull()
    else:
        git.Repo.clone_from(repo_url, repo_dir)

# Získať aktuálnu verziu kódu
current_version = 'verzia-tvojho-aktualneho-kodu'

# Získať poslednú verziu z GitHub
latest_version = download_latest_version()

if latest_version and latest_version != current_version:
    print('Nová verzia kódu je dostupná. Aktualizácia...')
    update_code()
    print('Kód bol aktualizovaný na najnovšiu verziu.')
else:
    print('Kód je aktuálny.')
