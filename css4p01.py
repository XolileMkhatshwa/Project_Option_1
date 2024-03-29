#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:00:20 2024

@author: Xolile
"""

import pandas as pd
my_data = pd.read_csv("movie_dataset.csv")


# Renaming columns with spaces and creating a new dataframe
new_my_data = my_data.rename(columns ={'Revenue (Millions)':'Revenue_Millions'})




# Dropping rows with null values, with reference to Revenue volumn
new_my_data = new_my_data.dropna(subset=['Revenue_Millions'], how='all')


# Dropping unuseful columns
new_my_data =new_my_data.drop(columns = "Rank")
new_my_data =new_my_data.drop(columns = "Description")
new_my_data  =new_my_data.drop(columns = "Runtime (Minutes)")
new_my_data  =new_my_data.drop(columns = "Votes")
new_my_data = new_my_data.drop(columns = "Metascore")





"""
# Finding the most common Actor in all the movies (Q10)
name_column = 'Actors'



# Split the names using the comma as a separator and stack them into a new DataFrame
namesActors = new_my_data[name_column].str.split(',', expand=True).stack()

# Use value_counts to get the count of each unique name
name_counts = namesActors.value_counts()

# Print the result for verification
print(name_counts)

"""

#Highest rated movie in the dataset (Q1)

highest_rated_movie = my_data.loc[my_data['Rating'].idxmax()]['Title']

print(f"The highest rated movie is: {highest_rated_movie}")



# Calculating the average revenue (Q2)
average_revenue = new_my_data['Revenue_Millions'].mean()

# Print the result
print(f"The average revenue of all movies is: {average_revenue:.2f} million")




# Calculating the average revenue  from 2015 to 2017 (Q3)
# Convert the 'year' column to datetime for easy comparison
new_my_data['Year'] = pd.to_datetime(new_my_data['Year'], format='%Y')

# Filter the DataFrame for movies from 2015 to 2017
filtered_df = new_my_data[(new_my_data['Year'] >= '2015') & (new_my_data['Year'] <= '2017')]

# Calculate the average revenue for the selected movies
new_average_revenue = filtered_df['Revenue_Millions'].mean()

print(f'The average revenue of movies from 2015 to 2017 is: {new_average_revenue:.2f}')


# Movies released in the year 2016 (Q4)

release_year_column = 'Year'
target_year = 2016

# Use boolean indexing to filter rows based on the specific year
movies_in_2016 = my_data[my_data[release_year_column] == target_year]

# Use the shape attribute to get the number of rows (movies) in the filtered DataFrame
number_of_movies = movies_in_2016.shape[0]


# Print the result for verification
print(f"Number of movies released in {target_year}: {number_of_movies}")




# Movies directed by Christopher Nolan (Q5)

Director_names = 'Director'
Target_director = 'Christopher Nolan'

# Using boolean indexing to filter rows based on the specific year i.e 2016 in the DataFrame 'md'
Director = my_data[my_data[Director_names] == Target_director]


# Using the shape attribute to get the number of directed movies
Number_of_directed_movies = Director.shape[0]

# Now 'Number_of_directed_movies' contains the count of movies directed by Christopher Nolan

# Print the result for verification
print(f"The number of movies derected by {Target_director}: {Number_of_directed_movies}")





# Movies having a rating of at least 8.0 (Q6)

number_of_movies = my_data[my_data['Rating'] >= 8.0]

# Get the count of movies with a rating of at least 8.0
num_high_rated_movies = len(number_of_movies)

print(f"The number of movies with a rating of at least 8.0 is: {num_high_rated_movies}")

# Finding the median rating of movies directed by Christopher Nolan? (Q7)

# Filtering rows where the director is Christopher Nolan
nolan_movies = my_data[my_data['Director'] == 'Christopher Nolan']

# Checking if there are movies directed by Christopher Nolan
if nolan_movies.empty:
    print("No movies directed by Christopher Nolan found.")
else:
    # Calculating the median rating for Christopher Nolan's movies
    median_rating = nolan_movies['Rating'].median()
    print(f"The median rating of movies directed by Christopher Nolan is: {median_rating}")





# Finding the year with the highest average rating (Q8)


# Grouping the DataFrame by 'year' and calculating the mean rating for each year
average_ratings_by_year = my_data.groupby('Year')['Rating'].mean()

# Find the year with the highest average rating
highest_avg_rating_year = average_ratings_by_year.idxmax()

# Display the result
print(f"The year with the highest average rating is: {highest_avg_rating_year}")




# Calculating the percentage increase in number of movies made between 2006 and 2016 (Q9)

# Filtering data for the years 2006 and 2016
movies_2006 = my_data[my_data['Year'] == 2006]
movies_2016 = my_data[my_data['Year'] == 2016]

# Counting the number of movies for each year
num_movies_2006 = len(movies_2006)
num_movies_2016 = len(movies_2016)

# Calculating the percentage increase
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

# Print the result
print(f"Percentage increase in number of movies between 2006 and 2016 is: {percentage_increase:.2f}%")


# Finding how many unique genres are there in the dataset (Q11)

# Extracting unique genres from the 'Genre' column
unique_genres = my_data['Genre'].unique()

# Calculating the count of unique genres
num_unique_genres = len(unique_genres)

# Print the result
print(f'The number of unique genres in the dataset is: {num_unique_genres}')



# Question 12

# Create a new DataFrame containing only the numerical columns
correlation_matrix = my_data.corr()

# Calculate the correlation matrix

# Display the correlation matrix

print(correlation_matrix)



























































