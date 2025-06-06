import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="Analyse Films", layout="wide")

# --- Titre
st.markdown(
    "<h1 style='text-align: center;'>🎬 Analyse approfondie des films</h1>",
    unsafe_allow_html=True,
)
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

# --- Chargement des données
main_df = pd.read_parquet("data/main_df.parquet")
cast_df = pd.read_parquet("data/people_df.parquet")
age_actors = pd.read_parquet("data/age_actors.parquet")
analyse_decennie = pd.read_parquet("data/analyse_decennie.parquet")

# --- Nettoyage
main_df["startYear"] = pd.to_numeric(main_df["startYear"], errors="coerce")
main_df["runtimeMinutes"] = pd.to_numeric(main_df["runtimeMinutes"], errors="coerce")
main_df["vote_average"] = pd.to_numeric(main_df["vote_average"], errors="coerce")
main_df["budget"] = pd.to_numeric(main_df["budget"], errors="coerce")
cast_df["startYear"] = pd.to_numeric(cast_df["startYear"], errors="coerce")


# --- Sélection des années
years = st.slider(
    "Sélectionner une période",
    int(main_df["startYear"].min()),
    int(main_df["startYear"].max()),
    (1980, 2020),
)
filtered_main = main_df[
    (main_df["startYear"] >= years[0]) & (main_df["startYear"] <= years[1])
]
filtered_cast = cast_df[
    (cast_df["startYear"] >= years[0]) & (cast_df["startYear"] <= years[1])
]


st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
# --- 1. Acteurs les plus présents
st.subheader("🎭 Acteurs les plus présents")

all_actors = filtered_cast["cast_list"].str.split(",", expand=True).stack()
actor_counts = all_actors.value_counts().reset_index()
actor_counts.columns = ["Acteur", "Apparitions"]
top_actors = actor_counts

fig1 = px.bar(
    top_actors,
    x="Acteur",
    y="Apparitions",
    text="Apparitions",
)
st.plotly_chart(fig1, use_container_width=True)
st.write("\n")
st.write("\n")
st.divider()
st.write("\n")
st.write("\n")
# --- 2. Durée moyenne des films au fil des années
st.subheader(f"🎬 Évolution annuelle du nombre de films")
duration_by_year = (
    filtered_main.groupby("startYear")["runtimeMinutes"].mean().reset_index()
)
fig2 = px.line(
    duration_by_year,
    x="startYear",
    y="runtimeMinutes",
    markers=True,
)
fig2.update_layout(xaxis_title="Année", yaxis_title="Durée (min)")
st.plotly_chart(fig2, use_container_width=True)
st.write("\n")
st.write("\n")
st.divider()
st.write("\n")
st.write("\n")


# --- 3. Âge moyen des acteurs (approximatif via startYear)
st.subheader("🧖‍♀️ Age moyen des Acteurs/Actrices")
# Supposons qu’un acteur débute vers 20 ans → approximatif

age_estimate = age_actors["age"]
st.metric(" ", f"{int(age_estimate.mean())} ans")

st.write("\n")
st.write("\n")
st.divider()
st.write("\n")
st.write("\n")
# --- 54. Films les mieux notés
st.subheader("🌟 Top 10 des films les mieux notés")
st.write("\n")
st.write("\n")
top_movies = (
    filtered_main.sort_values(by="vote_average", ascending=False)
    .dropna(subset=["vote_average"])
    .head(10)
)
top_movies_subset = top_movies[
    ["primaryTitle", "startYear", "vote_average", "genres", "runtimeMinutes"]
].rename(
    columns={
        "primaryTitle": "Titre du film",
        "startYear": "Année de sortie",
        "vote_average": "Note moyenne",
        "genres": "Genres",
        "runtimeMinutes": "Durée (minutes)",
    }
)

st.dataframe(top_movies_subset)

st.write("\n")
st.write("\n")
st.divider()
st.write("\n")
st.write("\n")

# --- 55. Nombre de films par décennie
st.subheader("📊 Nombre de films par décennie")

fig3 = px.bar(
    analyse_decennie,
    x="decennie",
    y="originalTitle",
    text="originalTitle",
    labels={"decennie": "Décennie", "originalTitle": "Nombre de films"},
    template="plotly_white",
)

# Mise à jour de l'apparence
fig3.update_layout(
    xaxis_title="Décennie",
    yaxis_title="Nombre de films",
    uniformtext_minsize=8,
    uniformtext_mode="hide",
)

st.plotly_chart(fig3, use_container_width=True)
