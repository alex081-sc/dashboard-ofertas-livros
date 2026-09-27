"""Leitura dos arquivos CSV do projeto.
"""

from pathlib import Path
import csv
# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"

def ler_livros():
    livros = []
    try:
        with open(CAMINHO_LIVROS, "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha) 
    except:
        print(f"Ocorreu algum erro na leitura do arquivo")
    finally:
        if arquivo is not None:
            arquivo.close()
          
    
    return livros

def ler_livros_v2():
    try:
        with open("livros.csv", "r", encoding="utf-8") as arquivo:
            print(arquivo.readline())
    except:
        print(f"Ocorreu algum erro na leitura do arquivo")
    finally:
        if arquivo is not None:
            arquivo.close()
 
def ler_livros_v1():
    arquivo = None
    try:
        arquivo = open("livros.csv", "r", encoding="utf-8")
        print(arquivo.readline())
    except:
        print(f"Ocorreu algum erro na leitura do arquivo")
    finally:
        if arquivo is not None:
            arquivo.close()

def calcular_preco_medio(livros):
    media: float = 0
    for livro in livros:
        preco_original: str = livro["preco"]
        preco_orig_limpo: str = preco_original.replace("£", "")
        preco_num: float = float(preco_orig_limpo)
        media+= preco_num
    media /= len(livros)
    
    return(round(media, 2))

def contar_cinco_estrelas(livros):    
    contador=0
    for livro in livros:
        nota_limpa: str = livro["nota"].lower().strip()
        if nota_limpa == "five":
            contador+=1    
    return contador

def acha_mais_caro(livros):
    livro_mais_caro = None
    maior_preco = 0

    for livro in livros:
        preco_original: str = livro["preco"]
        preco_orig_limpo: str = preco_original.replace("£", "")
        preco_num: float = float(preco_orig_limpo)

        if preco_num > maior_preco:
            maior_preco = preco_num
            livro_mais_caro = livro     

    return livro_mais_caro

if __name__ == "__main__":
    livros = ler_livros()
    print(f"A quantidade de livros da coleção é de {len(livros)} livros.")
    print(calcular_preco_medio(livros))
    print(contar_cinco_estrelas(livros))
    print(acha_mais_caro(livros))
