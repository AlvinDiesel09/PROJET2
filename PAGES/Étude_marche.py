import streamlit as st

st.set_page_config(page_title="Étude de Marché", layout="wide")

st.write(
    "<h1 style='text-align: center; font-size: 70px;'> 🔍 <u>Étude de Marché</u></h1>",
    unsafe_allow_html=True,
)
st.write("")
st.write("")
st.write("")
st.write("")
# st.subheader("Tendances Nationales Cinéma")
# st.write("indicateurs nationaux")
st.subheader("""📈 Analyse Cinématographique de la Creuse (23) """)
st.write("")
st.write("")
st.write(
    """Population totale : environ <span style="color: red;">**115 000 habitants**</span> 
    (52 % femme, 48 % homme)\n
Tendance : <span style="color: red;">**Déclin démographique depuis plusieurs décennies**</span>\n
Proportion de + de 60 ans : <span style="color: red;">**environ 35 %**</span> *(au-dessus de la moyenne nationale)*\n
Jeunes de moins de 20 ans : <span style="color: red;">**environ 17 %**</span> \n
Économie : <u>principalement rurale</u> *(agriculture, élevage, artisanat)*""",
    unsafe_allow_html=True,
)
st.write("")
st.write("")
st.write("")
st.write("")
st.subheader("""🎬 Salles de cinéma de la Creuse """)
st.write("")
st.write("")
st.write(
    """
<span style="color: red;">**12**</span> écrans pour <span style="color: red;">**7**</span> cinémas.\n
En 2024, les cinémas Creusois ont enregistré une fréquentation en hausse, avec plus de <span style="color: red;">**155 000 spectateurs**</span>.\n
<u>Tendance cinéma en France :</u>
         
<span style="color: red;">**50.1 %**</span> films francais\n 
<span style="color: red;">**34.2 %**</span>films américains\n 
<span style="color: red;">**11 %**</span> européens\n 
<span style="color: red;">**4.7 %**</span> % autres\n

Le genre le plus représenté est la comédie avec <span style="color: red;">**24 %**</span> puis thriller avec <span style="color: red;">**16 %**</span> 
ainsi que les films d’action avec <span style="color: red;">**16 %**</span>, SF avec <span style="color: red;">**9 %**</span>, 
comédie romantique <span style="color: red;">**8 %**</span> et fantastique <span style="color: red;">**8 %**</span>.\n

Les <span style="color: red;">**17 %**</span> pour les autres genres *(historique/horreur/drame/western/erotique/biographique)*.\n
Le genre préféré des femmes <span style="color: red;">**(28 %)**</span> s’orientent sur la comédie tandis que le genre préféré des hommes <span style="color: red;">**(21 %)**</span> sont les films d’actions.""",
    unsafe_allow_html=True,
)
st.write("")
st.write("")
st.write("")
st.write("")
st.subheader("""📊 Graphiques """)
st.write("")
st.write("")
st.write("")
graph1 = st.image("pictures\Miro.png", use_container_width=True)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
col1, col2, col3 = st.columns([1, 87, 1])
with col2:
    graph2 = st.image("pictures/graph1.png", use_container_width=True)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    graph2 = st.image("pictures\graph2.png", use_container_width=True)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.subheader("""💡 Conclusion """)
st.write("")
st.write(
    """L’étude de marché menée dans la Creuse met en lumière un territoire au profil démographique particulier, 
avec une population vieillissante (35 % de plus de 60 ans) et un contexte rural marqué.\n
Malgré un déclin démographique, la fréquentation des cinémas locaux a connu une hausse en 2024, atteignant plus de 155 000 entrées, 
ce qui témoigne d’un intérêt toujours présent pour le 7ème art.\n
Les goûts cinématographiques nationaux révèlent une préférence pour les comédies, 
particulièrement chez les femmes, et pour les films d’action chez les hommes, des tendances qu’il conviendra de vérifier localement. \n
Ces données constituent une base précieuse pour orienter l’analyse de la base de données, 
en ciblant notamment les genres susceptibles de séduire le public creusois, tout en tenant compte de la structure d’âge et du cadre de vie rural.
""",
    unsafe_allow_html=True,
)
