"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados

# Configs da pagina
st.set_page_config(layout="wide" )
st.title("📚 Dashboard de Livros")
col1, col2, col3 = st.columns(3)

#Calculo das informacoes
livros = dados.ler_livros()
qtd_livros = len(livros)
preco_medio = dados.calcular_preco_medio(livros)
cinco_estrelas = dados.contar_cinco_estrelas(livros)

#Display dos dados
col3.metric("Total cinco estrelas", cinco_estrelas)
col2.metric("Preço médio", f"£{preco_medio}")
col1.metric("Total de Livros", qtd_livros)
st.dataframe(livros)
