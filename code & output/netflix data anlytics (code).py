import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Load & Clean Data

df = pd.read_csv("netflix_titles.csv")

print("\n Missing Values:\n")
print(df.isnull().sum())

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df['release_year'] = df['release_year'].astype(int)

print("\n Data cleaned successfully\n")


# Movies vs TV Shows
print("\n==============================")
print(" Movies vs TV Shows")
print("==============================\n")

type_counts = df['type'].value_counts()
print(type_counts)

type_counts.plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

print("\n Insight:")
print("Movies significantly outnumber TV Shows on Netflix.\n")


# Releases Over Time
print("\n==============================")
print("Releases Over Time")
print("==============================\n")

year_counts = df['release_year'].value_counts().sort_index()
print(year_counts.tail(10))

year_counts.plot()
plt.title("Content Releases Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

print("\n Insight:")
print("Content on Netflix increases significantly after 2010.\n")


# Top Genres
print("\n==============================")
print(" Top Genres")
print("==============================\n")

genres = df['listed_in'].str.split(', ')
genres = genres.explode()
genre_counts = genres.value_counts()

print(genre_counts.head(10))

genre_counts.head(10).plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

print("\n Insight:")
print("Certain genres like Drama and International Movies dominate Netflix.\n")


# Top Countries
print("\n==============================")
print("Top Countries Producing Content")
print("==============================\n")

countries = df['country'].str.split(', ')
countries = countries.explode()
country_counts = countries.value_counts()

print(country_counts.head(10))

country_counts.head(10).plot(kind='bar')
plt.title("Top 10 Content Producing Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

print("\n Insight:")
print("The United States produces the most Netflix content, followed by other countries.\n")
