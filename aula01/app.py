"""Dashboard de Livros: app Streamlit.
"""

import streamlit as st
import dados

# Configs da pagina
st.set_page_config(layout="wide" )
st.title("📚 Dashboard de Livros")
col1, col2, col3, col4 = st.columns(4)

#Calculo das informacoes
livros = dados.ler_livros()
qtd_livros = len(livros)
preco_medio = dados.calcular_preco_medio(livros)
cinco_estrelas = dados.contar_cinco_estrelas(livros)
maior_livro = dados.acha_mais_caro(livros)

#Display dos dados
col4.metric( label="Livro mais caro", value=maior_livro["preco"], delta=maior_livro["titulo"], delta_color="off")
col3.metric("Total cinco estrelas", cinco_estrelas)
col2.metric("Preço médio", f"£{preco_medio}")   
col1.metric("Total de Livros", qtd_livros)
st.dataframe(livros)
