import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="KPI", layout="wide")

st.markdown(
    "<h1 style='text-align: center;'>📊 Indicateurs Clés de Performance (KPI)</h1>",
    unsafe_allow_html=True,
)


# Exemple de données pour les KPI
data_kpi = {
    "KPI": [
        "Utilisateurs Actifs",
        "Films Recommandés",
        "Taux de Clics",
        "Nouveaux Inscrits",
    ],
    "Valeur": [1500, 5000, 0.25, 200],
    "Unité": ["utilisateurs", "films", "%", "inscrits"],
}
df_kpi = pd.DataFrame(data_kpi)

st.subheader("Vue d'ensemble")
for index, row in df_kpi.iterrows():
    st.metric(label=row["KPI"], value=f"{row['Valeur']} {row['Unité']}")

st.subheader("Évolution des Utilisateurs")
# Données fictives pour un graphique
data_users = {
    "Mois": ["Jan", "Fév", "Mar", "Avr", "Mai"],
    "Utilisateurs": [1000, 1100, 1300, 1450, 1500],
}
df_users = pd.DataFrame(data_users)
fig_users = px.line(
    df_users, x="Mois", y="Utilisateurs", title="Évolution Mensuelle des Utilisateurs"
)
st.plotly_chart(fig_users)

# Ajoutez vos autres KPI, graphiques, etc. ici
