import streamlit as st
import pickle
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Voyage Analytics - Hotel Recommendations",
    layout="centered"
)

# Load the saved recommender artifacts
MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "hotel_recommender.pkl"

if not MODEL_PATH.exists():
    st.error(f"Model file not found: {MODEL_PATH}")
    st.stop()

with open(MODEL_PATH, "rb") as f:
    artifacts = pickle.load(f)

user_place_matrix = artifacts["user_place_matrix"]
user_similarity_df = artifacts["user_similarity_df"]
place_profile = artifacts["place_profile"]
top_popular_places = artifacts["top_popular_places"]


def recommend_hotels(user_code, top_n=5):
    if user_code not in user_similarity_df.index:
        return top_popular_places[:top_n]

    similar_users = (
        user_similarity_df[user_code]
        .sort_values(ascending=False)[1:11]
        .index
    )

    scores = (
        user_place_matrix.loc[similar_users]
        .sum()
        .sort_values(ascending=False)
    )

    return scores.head(top_n).index.tolist()


# App UI
st.title("🏨 Voyage Analytics - Hotel Recommendations")

st.write(
    "Enter a user code to get personalized place recommendations "
    "based on similar travelers' preferences."
)

user_code = st.number_input(
    "Enter user code",
    min_value=0,
    step=1
)

if st.button("Get Recommendations"):
    recommendations = recommend_hotels(int(user_code))

    st.subheader("Recommended Places:")

    for i, place in enumerate(recommendations, 1):
        st.write(f"{i}. {place}")

    st.subheader("Place Details:")

    details = place_profile[
        place_profile["place"].isin(recommendations)
    ]

    st.dataframe(details)
