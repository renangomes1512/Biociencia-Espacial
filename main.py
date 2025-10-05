import streamlit as st

st.set_page_config(page_title="BioSpace", layout="wide")

# Configuração da página
st.set_page_config(
    page_title="BioSpace - Biociência Espacial",
    page_icon="🚀",
    layout="wide"
)

# CSS customizado (coloquei parte do seu CSS aqui)
st.markdown("""
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f9f9f9;
        }
        .hero {
            text-align: center;
            padding: 80px 20px;
            background: linear-gradient(rgba(255,255,255,0.8), rgba(255,255,255,0.8)), 
                        url('https://images.unsplash.com/photo-1446776811953-b23d57bd21aa') no-repeat center center;
            background-size: cover;
            border-radius: 15px;
        }
        .card {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin: 10px;
        }
        .section-title {
            text-align: center;
            font-size: 2rem;
            font-weight: bold;
            margin: 40px 0 20px;
        }
    </style>
""", unsafe_allow_html=True)

# HEADER / HERO
st.markdown("""
    <div class="hero">
        <h1>🚀 Biociência Espacial</h1>
        <p>Explorando a vida além da Terra — pesquisas pioneiras sobre adaptação biológica, evolução e a possibilidade de vida fora do nosso planeta.</p>
    </div>
""", unsafe_allow_html=True)

# ÁREAS DE PESQUISA
st.markdown('<div class="section-title">🔬 Classificação por Área Temática</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="card"><h3>🧫 Microbiologia Espacial</h3><p>Estudos sobre microrganismos em microgravidade.</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card"><h3>🧬 Fisiologia Humana</h3><p>Efeitos da microgravidade no corpo humano.</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="card"><h3>🌱 Botânica Espacial</h3><p>Cultivo de plantas para suporte de vida.</p></div>', unsafe_allow_html=True)

# DESCOBERTAS RECENTES
st.markdown('<div class="section-title">🛰️ Descobertas Recentes</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="card"><h4>2024 - Bactérias resistentes à radiação</h4><p>Cepas bacterianas que sobrevivem em níveis extremos.</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card"><h4>2024 - Cultivo em Microgravidade</h4><p>Técnicas de cultivo de vegetais em gravidade zero.</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="card"><h4>2023 - Mutações Adaptativas</h4><p>Alterações genéticas que facilitam a vida no espaço.</p></div>', unsafe_allow_html=True)

# MISSÕES
st.markdown('<div class="section-title">🚀 Missões Científicas</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="card"><b>BioLab ISS</b><br>Experimentos na ISS.<br>Status: <span style="color:green">Ativa</span></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card"><b>Mars BioSample</b><br>Coleta de amostras em Marte.<br>Status: <span style="color:orange">Planejada</span></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="card"><b>Europa Explorer</b><br>Investigação em luas de Júpiter.<br>Status: <span style="color:blue">Em Desenvolvimento</span></div>', unsafe_allow_html=True)

# FOOTER
st.markdown("""
    <hr>
    <center>
    <p>© 2025 BioSpace - Explorando a vida no universo 🌌</p>
    </center>
""", unsafe_allow_html=True)
