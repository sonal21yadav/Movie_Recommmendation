# Movie Recommendation System
# Overview
This is a **Movie Recommendation System** built using Machine Learning that suggests movies similar to the one selected by the user.
The system uses **content-based filtering** and computes similarity between movies to recommend the top 5 most relevant options.
##  Live Features
-  Select a movie from the dropdown  
-  Get instant recommendations  
-  ML-based similarity model
##  How It Works
- Movie data is preprocessed and stored  
- A **similarity matrix** is generated using ML techniques  
- When a user selects a movie:
  - The system finds similar movies based on similarity scores  
  - Top 5 closest matches are displayed
#  Project Structure
Movie_recommendation/
│
├── app.py # Streamlit web app

├── movie_recommender.ipynb # Model building notebook

├── movies.pkl # Processed movie data

├── similarity.pkl # Similarity matrix (not uploaded due to size)

├── README.md # Project documentation
##  Technologies Used
- Python 
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit

