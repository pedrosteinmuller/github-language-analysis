import pandas as pd

df = pd.read_csv("github_repositories.csv")
df = df.dropna(subset=["language"])

df["year"] = pd.to_datetime(df["created_at"]).dt.year
language_trends = df.groupby(["year", "language"]).size().reset_index(name="count")

language_trends.to_csv("language_trends.csv", index=False)
print("Dados processados e salvos em language_trends.csv")