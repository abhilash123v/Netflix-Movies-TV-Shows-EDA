import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
netflix_data = pd.read_csv(r'H:\Codenera\Netflix_EDA_Project\data\netflix_titles.csv')


print("Dataset shape:", netflix_data.shape)
print(netflix_data.head())

#---------------
#Data Cleaning
#----------------
netflix_data["date_added"] = pd.to_datetime(netflix_data["date_added"], errors='coerce')
netflix_data["year_added"] = netflix_data["date_added"].dt.year
netflix_data["country"].fillna("Unknown", inplace=True)

#---------------
#GRAPH 1:Movies vs TV Shows
#----------------
plt.figure(figsize=(8, 5))
sns.countplot(x='type', data=netflix_data, palette='Set2')
plt.title('Distribution of Movies and TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

# -----------------------------

# GRAPH 2: Top 10 Countries

# -----------------------------

plt.figure()
top_country = netflix_data['country'].value_counts().head(10) 
top_country.plot(kind='bar')
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# -----------------------------

# GRAPH 3: Content Added Per year

# -----------------------------

plt.figure()
sns.countplot(x='year_added', data=netflix_data, palette='Set3')
plt.title("Content Added Per Year on Netflix")
plt.xlabel("Year Added")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()