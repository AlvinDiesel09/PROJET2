import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="KPI", layout="wide")

st.markdown(
    "<h1 style='text-align: center;'>📊 Indicateurs Clés de Performance (KPI)</h1>",
    unsafe_allow_html=True,
)
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")


# importation des données
df = pd.read_csv("data/test.csv")
print(df)

st.dataframe(df)


df_film_annuel = df.groupby(["startYear"]).size().reset_index(name="nombre_de_films")


# st.dataframe(df_film_annuel)

# st.subheader("Vue d'ensemble")
# for index, row in df.iterrows():
# st.metric(label=row["KPI"], value=f"{row['Valeur']} {row['Unité']}")

selected_years = st.slider(
    "Sélectionne une amplitude",
    min_value=(df_film_annuel["startYear"].min()),
    max_value=(df_film_annuel["startYear"].max()),
    value=(1980, 2020),
)

# Affichage de l'année sélectionnée
st.write("Vous avez sélectionné :", selected_years)

filtered_df = df_film_annuel[
    (df_film_annuel["startYear"] >= selected_years[0])
    & (df_film_annuel["startYear"] <= selected_years[1])
]

st.subheader(f"Évolution des films de {selected_years[0]} à {selected_years[1]}")
fig = px.line(
    filtered_df,
    x="startYear",
    y="nombre_de_films",
)

# Personnalisation des labels
fig.update_layout(xaxis_title="Année", yaxis_title="Nombre de films")

# Affichage du graphique dans Streamlit
st.plotly_chart(fig)
