import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from datetime import datetime

# 📈 Configuration de la page
st.set_page_config(
    page_title="Analyse Cinématographique", page_icon="🎬", layout="wide"
)


st.title("🎬 Dashboard d'Analyse Cinématographique")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
main_df = pd.read_parquet("../data/main_df.parquet")
people_df = pd.read_parquet("../data/people_df.parquet")

main_df["startYear"] = (main_df["startYear"]).astype(int)

# st.dataframe(main_df)
# st.dataframe(people_df)


with st.sidebar:
    years = st.slider(
        "Sélectionner une période",
        1900,
        2025,
        (1980, 2010),
    )

    filtered_main = main_df.query("startYear >= @years[0] & startYear <= @years[1]")


###################  indicateur 1 ###################
def most_present_genres(df):
    df["genre"] = df["genres"].str.split(",")
    exploded = df.explode("genre")
    genre_counts = exploded["genre"].value_counts().reset_index()
    genre_counts.columns = ["genre", "count"]

    fig = px.histogram(
        genre_counts.sort_values(by="count", ascending=False).head(10),
        y="count",
        x="genre",
        color="genre",
        hover_name="genre",
        log_x=False,
        title=f"Répartition des genres de {years[0]} à {years[1]}",
    )
    fig.update_layout(
        xaxis_title="Genres",
        yaxis_title="Nombre de films",
    )
    return fig


st.plotly_chart(most_present_genres(filtered_main))


###################  indicateur 2 ###################
df = pd.merge(filtered_main, people_df, on="tconst", how="left")

# Supprimer tous les tconst de films d'animation
animation_tconsts = df[df["genres"].str.contains("animation", case=False, na=False)][
    "tconst"
].unique()
df = df[~df["tconst"].isin(animation_tconsts)].copy()

# Explosion des cast
df["cast"] = df["cast_list"]
df = df.explode("cast").copy()

# Filtrer acteurs et actrices
df = df[df["category"].isin(["actress", "actor"])]

# Compter les occurrences
cast_counts = df["cast"].value_counts().reset_index()
cast_counts.columns = ["cast", "count"]

# Plot
fig = px.histogram(
    cast_counts.head(20),
    y="count",
    x="cast",
    color="cast",
    hover_name="cast",
    log_x=False,
    title=f"Top 20 acteurs/actrices les plus présents de {years[0]} à {years[1]}",
)
fig.update_layout(
    xaxis_title="Acteurs/Actrices",
    yaxis_title="Nombre de films",
)
st.plotly_chart(fig)


###################  indicateur 3 ###################
