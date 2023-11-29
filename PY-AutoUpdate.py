import requests
import git
import os
import shutil
import subprocess

# Nastav URL tvojho GitHub repozitára
repo_url = 'https://github.com/fattcat/PY-AutoUpdate/AutoGit'

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
        current_commit = repo.head.object.hexsha

        # Skontrolovať, či sa obsah zmenil
        origin.fetch()
        if current_commit != origin.refs.master.commit.hexsha:
            print('Obsah sa zmenil. Aktualizácia...')
            shutil.rmtree(repo_dir)  # Vymazanie starého priečinku
            git.Repo.clone_from(repo_url, repo_dir)  # Stiahnutie nového obsahu
            print('Obsah bol aktualizovaný.')
        else:
            print('Obsah sa nezmenil. Nie je potrebná aktualizácia.')
    else:
        git.Repo.clone_from(repo_url, repo_dir)

        # Spustiť python skript, ak existuje
        script_path = os.path.join(repo_dir, 'your_script.py')
        if os.path.exists(script_path):
            subprocess.run(['python', script_path])

# Získať aktuálnu verziu kódu
current_version = '1.0.0'

# Získať poslednú verziu z GitHub
latest_version = download_latest_version()

if latest_version and latest_version != current_version:
    print('Nová verzia kódu je dostupná...\nPrebieha Aktualizácia...')
    update_code()
    print('Kód bol aktualizovaný na najnovšiu verziu.')
else:
    print('Kód je aktuálny.')
