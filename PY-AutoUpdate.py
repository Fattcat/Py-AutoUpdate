import os
import subprocess
import requests

# Funkcia na kontrolu dostupnosti internetového pripojenia
def is_internet_available():
    try:
        response = requests.get("http://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False

# Funkcia na klonovanie alebo aktualizáciu repozitára
def update_repo(repo_url, local_dir):
    if os.path.exists(local_dir):
        try:
            subprocess.run(["git", "-C", local_dir, "pull"], check=True)
            print("Repozitár aktualizovaný.")
        except subprocess.CalledProcessError as e:
            print(f"Chyba pri aktualizácii repozitára: {e}")
    else:
        try:
            subprocess.run(["git", "clone", repo_url, local_dir], check=True)
            print("Repozitár klonovaný.")
        except subprocess.CalledProcessError as e:
            print(f"Chyba pri klonovaní repozitára: {e}")

# Kontrola dostupnosti internetového pripojenia
if is_internet_available():
    print("Internetové pripojenie je k dispozícii.")
    repo_url = "https://github.com/Fattcat/Py-AutoUpdate.git"
    local_dir = "MyFolder"
    update_repo(repo_url, local_dir)
else:
    print("Internetové pripojenie nie je k dispozícii. Kontrola verzií z GitHub sa nedá vykonať.")
