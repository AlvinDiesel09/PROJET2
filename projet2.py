import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from difflib import get_close_matches

st.set_page_config(page_title="Suggestion de Films", layout="wide")

# Initialisation session
if "favoris" not in st.session_state:
    st.session_state["favoris"] = []

# Sidebar pour les filtres de la page principale
with st.sidebar:
    logo = st.sidebar.image(
        "pictures\Logo Team Rocket.png", width=170, use_container_width=False
    )
    st.header("🔎 Recherche de film")
    film_input = st.text_input(
        "Quel film avez-vous aimé ?", placeholder="Ex: Inception"
    )
    selected_genre = st.selectbox(
        "Genre", ["Tous", "Science-Fiction", "Thriller", "Drame", "Aventure"]
    )
    min_year = st.slider("Année minimale", 1980, 2025, 2000)
    min_rating = st.slider("Note minimale", 0.0, 10.0, 7.5, 0.5)

# Titre centré
st.markdown(
    "<h1 style='text-align: center;font-size: 70px'>🎬 On mate quoi ?!</h1>",
    unsafe_allow_html=True,
)


# Mock Data
def suggere_films_mock(titre):
    mock_data = pd.DataFrame(
        {
            "title": ["Interstellar", "Tenet", "The Prestige", "Dune", "Arrival"],
            "rating": [8.6, 7.5, 8.5, 8.1, 7.9],
            "startYear": [2014, 2020, 2006, 2021, 2016],
            "genre": [
                "Science-Fiction",
                "Thriller",
                "Drame",
                "Science-Fiction",
                "Science-Fiction",
            ],
            "poster_url": [
                "https://fr.web.img6.acsta.net/pictures/14/09/24/12/08/158828.jpg",
                "https://image.tmdb.org/t/p/w300/k68nPLbIST6NP96JmTxmZijEvCA.jpg",
                "https://m.media-amazon.com/images/M/MV5BMjA4NDI0MTIxNF5BMl5BanBnXkFtZTYwNTM0MzY2._V1_.jpg",
                "https://image.tmdb.org/t/p/w300/d5NXSklXo0qyIYkgV94XAgMIckC.jpg",
                "https://image.tmdb.org/t/p/w300/x2FJsf1ElAgr63Y3PNPtJrcmpoe.jpg",
            ],
            "trailer_url": [
                "https://www.youtube.com/embed/zSWdZVtXT7E",
                "https://www.youtube.com/embed/L3pk_TBkihU",
                "https://www.youtube.com/embed/o4gHCmTQDVI",
                "https://www.youtube.com/embed/n9xhJrPXop4",
                "https://www.youtube.com/embed/tFMo3UJ4B4g",
            ],
            "overview": [
                "Un groupe d'explorateurs utilise un trou de ver pour franchir les limites de la galaxie.",
                "Un agent tente de manipuler le temps pour sauver le monde.",
                "Deux magiciens rivaux se livrent une guerre de l’illusion au XIXe siècle.",
                "Un jeune noble mène une rébellion interstellaire sur une planète désertique.",
                "Des extraterrestres débarquent sur Terre et une linguiste tente de communiquer avec eux.",
            ],
        }
    )

    filtered = mock_data[
        (mock_data["startYear"] >= min_year) & (mock_data["rating"] >= min_rating)
    ]

    if selected_genre != "Tous":
        filtered = filtered[filtered["genre"] == selected_genre]

    # Recherche floue
    all_titles = mock_data["title"].tolist()
    match = get_close_matches(titre, all_titles, n=1, cutoff=0.5)
    if match:
        return filtered, match[0]
    else:
        return filtered, titre


# Affichage suggestions
if film_input:
    suggestions, matched_title = suggere_films_mock(film_input)
    st.markdown(
        f"<h3 style='text-align: center;'>📽️ Suggestions basées sur : <em>{matched_title}</em></h3>",
        unsafe_allow_html=True,
    )

    if suggestions.empty:
        st.warning("Aucune suggestion ne correspond aux filtres.")
    else:
        st.markdown(
            "<div style='display: flex; flex-wrap: wrap; justify-content: center; gap: 40px;'>",
            unsafe_allow_html=True,
        )
        for i, row in suggestions.iterrows():
            is_fav = row["title"] in st.session_state["favoris"]
            with st.container():
                col = st.columns([1])[0]
                with col:
                    st.markdown(
                        f"<div class='card' style='width:220px; text-align:center;'>",
                        unsafe_allow_html=True,
                    )
                    st.image(row["poster_url"], width=200)
                    st.markdown(
                        f"**{row['title']}**<br>⭐ {row['rating']} • 📅 {row['startYear']}<br>🎞️ {row['genre']}",
                        unsafe_allow_html=True,
                    )
                    st.caption(row["overview"])
                    with st.expander("🎬 Bande-annonce"):
                        st.video(row["trailer_url"])
                    fav_button = st.button(
                        "❤️ Ajouter aux favoris" if not is_fav else "✅ Déjà ajouté",
                        key=f"fav_{i}",
                    )
                    if fav_button and not is_fav:
                        st.session_state["favoris"].append(row["title"])
                    st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Affichage des favoris (déplacé dans la sidebar ou dans une page séparée si nécessaire)
with st.sidebar:
    st.subheader("❤️ Mes favoris")
    if not st.session_state["favoris"]:
        st.info("Aucun film favori encore ajouté.")
    else:
        for fav in st.session_state["favoris"]:
            st.markdown(f"- {fav}")
