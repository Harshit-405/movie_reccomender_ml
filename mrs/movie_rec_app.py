import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load data 
try:
    movies_df = pd.read_csv('movies.csv')
except FileNotFoundError:
    st.error("Error: movies.csv not found. Make sure the file is in the same directory.")
    st.stop()

# Data Preprocessing and Model Building 
movies_df['genres'] = movies_df['genres'].fillna('')
tfidf = TfidfVectorizer(stop_words='english', analyzer='word', token_pattern='[^|]+')
tfidf_matrix = tfidf.fit_transform(movies_df['genres'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies_df.index, index=movies_df['title']).drop_duplicates()

# Recommendation Function 
def get_recommendations(title, cosine_sim=cosine_sim):
    if title not in indices:
        return None
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return movies_df['title'].iloc[movie_indices]

# Streamlit UI
st.title('Movie Recommender')

# Get the list of all movie titles for autocomplete
all_movie_titles = movies_df['title'].tolist()

movie_title_input = st.text_input('Enter a movie title:')

# Filter movie titles based on user input for autocomplete
if movie_title_input:
    filtered_titles = [title for title in all_movie_titles if movie_title_input.lower() in title.lower()]
    if filtered_titles:
        st.write("Possible matches:")
        # Display up to 10 possible matches
        for i, title in enumerate(filtered_titles[:10]):
            st.write(f"- {title}")


if movie_title_input:
    recommendations = get_recommendations(movie_title_input)

    if recommendations is not None:
        st.subheader(f'Recommendations for "{movie_title_input}":')
        for i, rec in enumerate(recommendations):
            st.write(f"{i+1}. {rec}")
    else:
        st.warning(f"Movie title '{movie_title_input}' not found in the dataset. Please check the title or select from the suggestions above.")