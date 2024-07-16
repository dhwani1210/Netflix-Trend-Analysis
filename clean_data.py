# Task 1: Decoding Netflix's Cinematic Data.
# Before we start our analysis, first, we need to view the dataset. 
# It is essential to view the data and check the columns. Let's take a look.

#--- Import Pandas ---
import pandas as pd
#--- Read in dataset ----
df = pd.read_csv(r'C:\Users\dhwan\OneDrive\Desktop\Data Analysis\Netflix\NetflixOriginals.csv', encoding='latin-1')

# ---WRITE YOUR CODE FOR TASK 1 ---
#--- Inspect data ---
print(df.head())

#Task 2: Unveiling the Datatypes in Netflix Originals Dataset.

# --- WRITE YOUR CODE FOR TASK 2 ---
dtype = df.dtypes

#--- Inspect data ---
print(dtype)

# Task 3: Lowercasing Netflix Originals.

# --- WRITE YOUR CODE FOR TASK 3 ---
df.columns = df.columns.str.lower()
#--- Inspect data ---
print(df)

# Task 4: Unveiling Null Values in Netflix Originals Dataset.
# --- WRITE YOUR CODE FOR TASK 4 ---
null_values = df.isnull().sum()

#--- Inspect data ---
print(null_values)

# Task 5: Bid Farewell to NaNs in Netflix Originals Dataset.
# df = df.dropna(axis=1) to drop column with missing values
df= df.dropna()
print(df.isnull().sum())

# Task 6: Tackling Duplicates in Netflix Originals Dataset.
duplicates = df[df.duplicated()]
print(duplicates)
# Task 7: Eliminating Duplicates for Netflix Insights.
print(df.info())
df = df.drop_duplicates()
print(df.info())

# Task 8: Converting Netflix Premiere object to Datetime
df['premiere'] = pd.to_datetime(df['premiere'])
# pd.to_datetime(df['premiere'], format='%Y-%m-%d')
print(df.dtypes)
print(df.head())

# Task 9: Unveiling the Cinematic Epochs with Year Extraction.
df['year'] = df['premiere'].dt.year

print(df.head())

# Task 10: Standardizing IMDb Score Column in Netflix Originals Dataset.
    #df.rename(columns={'imdb score': 'imdb_score'}, inplace=True) #to rename
df.columns = df.columns.str.replace(' ', '_').str.lower() #to remove spaces with underscore
print(df.columns)

# Task 11: Archiving Refined Netflix Originals Dataset.
df.to_csv(r'C:\Users\dhwan\OneDrive\Desktop\Data Analysis\Netflix\cleaned_netflix_originals_dataset.csv', index=False) #index = false removes row num while exporting
# ​
# Module 2
# Task 1: Data Download, Import, and Database Connection.
# Now we have successfully completed the Python tasks and are heading towards the SQL analysis. For that, we need to connect the database to our notebook. Let's get it done!

# # -- Load the sql extention ----
# %load_ext sql
# ​
# # --- Load your mysql db using credentials from the "DB" area ---
# %sql mysql+pymysql://<user>:<password>@localhost/<db_name>
# Task 2: Counting Cinematic Uniqueness: Distinct Titles in the Netflix Collection.
# Wow! We've successfully connected the database to the Jupyter notebook, allowing us to run SQL queries directly within the notebook. Now, let's check the count of different titles from the dataset. This will provide us with the number of unique content entries in the dataset. Let's work on it.

# '''%%sql
# <your-query>'''
# Task 3: Netflix Gems with IMDb Scores Above 7.
# Incredible!!! We now have an idea of how many different titles' data is in the dataset. Now, let's check the details of movies and shows with better reviews. This will help us focus on and analyze the more highly-rated shows and movies. Let's write an SQL query for that

# '''%%sql
# <your-query>'''
# Task 4: Counting Netflix Movies by Language.
# Thanks for finding the best movies and shows for me. Now, I'm interested in knowing the number of movies in each language. This task allows us to understand the distribution of movies across different languages in the dataset. Let's have a look!

# '''%%sql
# <your-query>'''
# Task 5: Unveiling the Average IMDb Scores in Netflix Originals.
# Oh, nice! We got the details of the movie distribution in each language. Now, let's find out the details of genres and their average rating. From this, we will get an idea of which genre people are loving more. Let's work on it!

# '''%%sql
# <your-query>'''
# Task 6: Netflix Genres with the Highest Average IMDb Scores.
# Fantastic!!! We successfully completed the last task and identified the best genre. Now, it's time to figure out the top 5 genres based on their ratings. This task will enable us to explore and highlight the highest-rated genres in the dataset. Let's rock it, buddy!

# '''%%sql
# <your-query>'''
# Task 7: Netflix Movies Surpassing Genre IMDb Score Averages.
# Wow! We have obtained the details of the top 5 genres from the last task. Now, I'd like to know the content details that are considered the best in their respective genre groups. This will help us identify content with above-average ratings within each genre. Let's write an SQL query for that.

# '''%%sql
# <your-query>'''
# Task 8: Counting Netflix Movies by Genre Before 2020.
# We successfully identified the best content in their genre groups. Now, let's find the number of contents in each genre that premiered before 2020. This task allows us to analyze the distribution of movies across different genres before the year 2020. Let's work on it.

# '''%%sql
# <your-query>'''
# Task 9: The Highest Rated Netflix Movie.
# Marvelous!!! We have obtained the number of movies in each genre before 2020. Now, let's find out the best content in the entire dataset. This task will help identify the top-rated show or movie. Let's take a look.

# '''%%sql
# <your-query>'''
# Task 10: Netflix Movies with Similar Premieres.
# Hurray! I've got the details of the top-rated content. Now, let's find movies with similar genres released within a week of each other. This task helps identify movies with related genres released in close timeframes. This is probably the most unique requirement. Let's work on it, buddy!

# '''%%sql
# <your-query>'''
# Task 11: Genre Dominance Through the Years: Unveiling Top-Ranked Genres.
# Incredible! We found out the contents premiered within weeks. Now, I'm interested in knowing the best genre in each year. This will help us identify the top-ranked genre based on ratings for each year. Let's work on it.

# '''%%sql
# <your-query>'''
# Task 12: Cinematic Excellence in Extended Narratives: Genre and Language Dynamics.
# Amazing! We have successfully identified the best genres in each year. Now, I'd like to know the details of genre, language, and their ratings for content with longer runtimes. This will help us analyze the performance of longer content within specific genres and languages on the platform. Let's rock it, buddy!

# '''%%sql
# <your-query>'''
# Congratulations! You've now gained skills in Python and SQL thorough the analysis of Netflix movies and shows. These experiences have finely developed your abilities in data manipulation, querying databases, and visualizing insights. Your journey not only showed patterns in what viewers like but also made you better at different aspects of data analytics.
