# Netflix Exploratory Data Analysis (EDA)

## Overview

This project performs Exploratory Data Analysis (EDA) on the Netflix Titles dataset to uncover patterns in content distribution, genres, release trends, and country-wise production. The goal is to understand how Netflix’s content library has evolved over time and what factors dominate its catalog.

## Dataset

The dataset used in this project is the Netflix Titles dataset (commonly available on Kaggle). It contains information such as:

* Title
* Type (Movie/TV Show)
* Genre (`listed_in`)
* Country
* Release Year

Note: The dataset may contain missing values and duplicates, which are handled during preprocessing.

## Tools and Libraries

* Python
* Pandas (data cleaning and manipulation)
* Matplotlib (data visualization)
* NumPy (basic numerical operations)

## Data Cleaning

The following preprocessing steps were performed:

* Removed missing values using `dropna()`
* Removed duplicate records
* Converted data types where necessary (e.g., `release_year` to integer)

## Analysis Performed

### 1. Content Type Distribution

* Compared the number of Movies and TV Shows available on Netflix
* Used bar charts for visualization

### 2. Release Trends Over Time

* Analyzed how content production has changed over the years
* Identified trends in the number of releases

### 3. Genre Analysis

* Extracted individual genres from the `listed_in` column
* Counted frequency of each genre
* Visualized top 10 most common genres

### 4. Country-wise Content Production

* Split multiple country entries into individual values
* Identified top content-producing countries
* Visualized top 10 countries

## Key Insights

* Movies form a significant portion of Netflix’s content compared to TV Shows
* Content production shows a strong upward trend in recent years
* Certain genres (such as Drama and International Movies) appear frequently in the catalog
* The United States is among the leading producers of Netflix content, followed by other countries

Note: Insights may vary slightly depending on the version of the dataset used.

## Project Structure

```
EDA-Netflix-Project/
│
├── data/
│   └── netflix_titles.csv
│
├── code & output/
│   └── netflix data analytics.py
│   └── output.py
│
├── images/
│   └── (graphs and visualizations)
│
└── README.md
```

## How to Run

1. Clone the repository:

   ```
   git clone <your-repo-link>
   ```
2. Install required libraries:

   ```
   pip install pandas matplotlib numpy
   ```
3. Run the notebook:

   * Open in Jupyter Notebook or Google Colab
   * Execute all cells

## Conclusion

This project demonstrates fundamental data analysis skills including data cleaning, transformation, visualization, and interpretation. It provides insights into Netflix’s content distribution and highlights trends that can be useful for further analysis or business understanding.

## Future Improvements

* Use Seaborn for enhanced visualizations
* Perform sentiment or rating analysis
* Build a recommendation system based on genres
