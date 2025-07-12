How it Works

(main file: movie_rec_app.py)

The recommender uses a content-based filtering approach. It analyzes the genres of movies using TF-IDF (Term Frequency-Inverse Document Frequency) and calculates the cosine similarity between movies based on their genre vectors. When a user requests recommendations for a specific movie, the system finds other movies with similar genre profiles.


Setup and Installation:

1.Clone or Download: Get a copy of all the files in this project.

2.Install Python: Make sure you have Python installed on your system (Python 3.6+ is recommended).

3.Set up a Virtual Environment (Recommended):
    Open your terminal or command prompt and navigate to the project directory using the cd command.
    Create a virtual environment:
        python -m venv venv
    Now,to activate this if your on:
        windows run:
            .\venv\Scripts\activate
        On macOS and Linux:
            source venv/bin/activate

4.Install Dependencies: Open your terminal or command prompt, navigate to the project directory, and install the required libraries using pip:
        pip install pandas scikit-learn streamlit

5.then run through streamlit :
         streamlit run movie_rec_app.py




IF YOU HAVE DONE SETUP THEN:

How to Run the Application

1.Activate the Virtual Environment: If it's not already active, activate your virtual environment (see step 3 above).
    on windows:
        .\venv\Scripts\activate
2.Run the Streamlit App: In your terminal, from the project directory, run the following command:
        streamlit run movie_rec_app.py



Files Included
movie_rec_notebook.ipynb: A jupyter notebook for the project.
movie_rec_app.py: The main Python script for the Streamlit web application.
movies.csv: Dataset containing movie information, including genres.
links.csv: Dataset containing movie IDs and links to external databases.
ratings.csv: Dataset containing user ratings for movies.
tags.csv: Dataset containing user-generated tags for movies.
requirements.txt: Lists the necessary Python libraries to run the application.
README.md: This file.