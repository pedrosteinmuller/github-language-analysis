import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def get_repositories_by_year(year, per_page=100, pages=10):
    repositories = []
    url = "https://api.github.com/search/repositories"

    for page in range(1, pages + 1):
        print(f"Coletando repositórios do ano {year}, página {page}...")
        params = {
            "q": f"created:{year}-01-01..{year}-12-31",
            "per_page": per_page,
            "page": page,
            "sort": "stars",
            "order": "desc"
        }
        response = requests.get(url, headers=HEADERS, params=params)

        if response.status_code == 200:
            data = response.json()
            repositories.extend(data["items"])
        else:
            print(f"Erro ao coletar dados: {response.status_code}")
            break

        time.sleep(5)

    return repositories

years = range(2019, 2024)
repo_data = []
for year in years:
    repo_data.extend(get_repositories_by_year(year))


df = pd.DataFrame(repo_data, columns=["id", "name", "language", "stargazers_count", "created_at"])
df.to_csv("github_repositories.csv", index=False)
print("Dados coletados e salvos em github_repositories.csv")