# Movie Recommendation System Using Content-Based Filtering

**Maulana P. R.**  
**Project Domain**: Movie Recommendation System

---

## Project Overview

### Background

The entertainment industry offers a vast collection of movies to choose from, making it difficult for users to decide what to watch next. Personalized movie recommendations can alleviate this issue by suggesting films based on users' preferences. Content-based filtering is a common technique used to recommend movies by analyzing their features such as genres, plot overviews, and other attributes. In this project, we employ content-based filtering to recommend similar movies based on a movie's genre and overview.

### Importance of the Problem

With the rise of streaming platforms, the volume of available content can overwhelm users. A robust recommendation system helps users discover movies that match their tastes, improving their viewing experience. This is particularly important in an industry where new movies are constantly being produced, and recommendations help maintain user engagement by providing relevant suggestions based on a user’s interests.

### Related Research

Content-based filtering has been widely used in recommendation systems. Various techniques, such as cosine similarity and term frequency-inverse document frequency (TF-IDF), have been employed to compare the content of movies and suggest similar items. Recent advancements explore hybrid models that combine collaborative filtering and content-based methods to enhance recommendation accuracy.

**References**:
- Jannach, D., & Adomavicius, G. (2016). *Recommendation Systems: Challenges and Opportunities*. Springer.
- Burke, R. (2007). *Hybrid Recommender Systems: Survey and Experiments*. User Modeling and User-Adapted Interaction.
- Lops, P., De Gemmis, M., & Semeraro, G. (2011). *Content-based Recommender Systems: State of the Art and Trends*. In Recommender Systems Handbook.

---

## Business Understanding

### Problem Statements

The key problem addressed is the inability of users to easily discover relevant movies from large libraries. The goal is to create a recommendation system that:

- **Challenge 1**: Helps users quickly find movies based on their preferences.
- **Challenge 2**: Handles large amounts of movie data efficiently.
- **Challenge 3**: Provides accurate and personalized movie suggestions.

### Goals

The main objectives of this project are:

- **Goal 1**: Build a content-based movie recommendation system using movie features.
- **Goal 2**: Develop a tool that can provide recommendations based on a given movie title.
- **Goal 3**: Achieve accurate recommendations by leveraging movie genre and overview.

### Solution Statement

To solve this problem, we implemented the following solutions:

- **Solution 1**: The dataset was processed, and movie features such as genres and overviews were combined to create a "tags" feature for each movie.
- **Solution 2**: Count Vectorization was applied to convert textual data into numerical features for machine learning models.
- **Solution 3**: Cosine similarity was calculated between the "tags" of each movie to identify similar movies.
- **Solution 4**: A recommendation function was created to suggest the top 5 most similar movies.

---

## Data Understanding

### Data Source

The dataset used for this project was the **Movie Dataset** from Kaggle, which contains 10k top-rated TMDB movies till 26-July-2022. The Dataset contains the following things:
- ID: Movie ID number on the website.
- title: Movie name
- genre: Movie genre (crime, adventure, etc.)
- original_language: Original language in which the movie is released
- overview: Summary of the movie
- popularity: Movie Popularity
- release_date: Movie release date
- vote_average: Movie vote average
- vote_count: Movie vote count, which was uploaded and processed for movie recommendation purposes.

[Download the Movie Dataset](https://www.kaggle.com/datasets/ahsanaseer/top-rated-tmdb-movies-10k/data)

### Features in the Dataset

The dataset contains the following important features:

- **id**: Unique identifier for each movie.
- **title**: Title of the movie.
- **genre**: Genre of the movie.
- **overview**: Overview or plot summary of the movie.
- **tags**: A combined field of movie genre and overview, used to create a textual representation of each movie.

### Exploratory Data Analysis (EDA)

During the initial exploration, some key observations included:

- **Textual Features**: The 'tags' column was constructed by combining movie genres and overviews to create a comprehensive text feature.
- **Data Format**: Movies had textual data, which was transformed into numeric vectors using Count Vectorization for similarity calculations.

---

## Data Preparation

### Data Cleaning

The data underwent basic preprocessing steps such as:

- Combining the 'genre' and 'overview' columns to create a new feature called **tags**.
- No missing data or duplicates were detected in the dataset, which simplified the cleaning process.

### Feature Engineering

**Tags** were created by concatenating the 'genre' and 'overview' columns, which gave a textual description of each movie. This feature was then transformed into a numerical representation using **Count Vectorization**, which helps in identifying relationships between words in the movie descriptions.

### Vectorization and Similarity Calculation

- **CountVectorizer**: This tool was used to convert text into a matrix of token counts, which formed the basis for measuring similarity between movies.
- **Cosine Similarity**: This metric was used to calculate the similarity between movies based on the vectors generated by CountVectorizer.

---

## Modeling

### Algorithm Used

The key algorithm used for generating movie recommendations is **Cosine Similarity**, which is applied to the vectorized representations of movie tags. This method measures the cosine of the angle between two vectors in a multi-dimensional space, providing a metric of similarity.

### Recommendation Function

A function was developed to recommend movies. Given a movie title, the function:

- Finds the index of the movie in the dataset.
- Calculates the cosine similarity between the movie and all other movies in the dataset.
- Returns the top 5 most similar movies based on the similarity score.

---

## Evaluation

### Evaluation Metrics

The effectiveness of the recommendation system was evaluated qualitatively, as the project does not include explicit user feedback or ratings. Instead, recommendations were manually tested with movie titles such as "Iron Man," "The Shawshank Redemption," and "The Godfather" to assess the quality of the suggestions.

### Results

The recommendation function was tested with the following movies:

- **"Iron Man"**: Recommended movies included "The Dark Knight," "The Avengers," and other action-packed superhero films.
- **"The Shawshank Redemption"**: Recommended similar films such as "The Green Mile" and "Schindler's List."
- **"The Godfather"**: Suggestions included "Scarface" and other classic crime films.

### Model Selection

The content-based filtering method using cosine similarity worked well, providing highly relevant movie suggestions based on the content of the movies.

---

## Conclusion

The movie recommendation system successfully generates relevant movie suggestions using a content-based filtering approach. By combining movie genres and overviews into a textual feature and calculating cosine similarity, the system provides recommendations based on movie content.

### Future Work

Future improvements for this project could include:

- **Collaborative Filtering**: Incorporating user ratings and behavior data to provide more personalized recommendations.
- **Hybrid Recommendation System**: Combining content-based filtering with collaborative filtering for enhanced accuracy.
- **Real-Time Application**: Developing a real-time recommendation system within a web or mobile app for user interactions.

---

## Business Understanding Impact

### Has the Model Addressed the Problem Statement?

Yes, the content-based recommendation system addresses the problem of movie discovery. By recommending movies based on the genre and plot summary of a given movie, it helps users discover films they may enjoy without needing external ratings or user behavior data.

### Has the Model Achieved the Expected Goals?

The project has met the goals outlined in the Business Understanding section:

- **Goal 1**: A content-based recommendation model was built using movie features, such as genre and overview.
- **Goal 2**: A functional tool was created to recommend movies based on user input (a movie title).
- **Goal 3**: The recommendation system successfully provided relevant suggestions with high accuracy.

### Has the Solution Statement Had an Impact?

Yes, the solution provides a straightforward and effective way for users to discover new movies based on content features. The implementation of cosine similarity for content-based recommendations has proven effective and provides a foundation for building a more sophisticated recommendation system in the future.

---

