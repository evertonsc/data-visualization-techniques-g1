import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO

# =============== CONFIGURAÇÕES GERAIS ===============

# Definições de constantes para não ter que mudar em vários lugares caso o caminho mude. 
INPUT_CSV = os.path.join("data", "Gorjetas.csv")        # caminho do arquivo de entrada
OUT_DIR = "out"                                         # diretório de saída
os.makedirs(OUT_DIR, exist_ok=True)                     # cria o diretório de saída, se não existir         
sns.set_theme()                                         # personalização do estilo dos gráficos (background)

# =============== CARREGAMENTO DOS DADOS ===============

# Remove aspas externas de cada linha e converte aspas duplas duplicadas.
def _clean_csv_fullquoted(text: str) -> str:
    lines = text.splitlines()
    fixed = []
    for ln in lines:
        if len(ln) >= 2 and ln.startswith('"') and ln.endswith('"'):
            ln = ln[1:-1]                   # tira aspas do começo e do fim
        ln = ln.replace('""', '"')          # aspas duplas transforma em aspas simples
        fixed.append(ln)
    return "\n".join(fixed)


# Tentar ler o CSV. Se o arquivo estiver 'full-quoted' (tudo em 1 coluna), faz a limpeza e relê.
# Com xlsx não tive problemas com outro código adaptado para xlsx. Mas como a instrução era fazer com CSV, tive que fazer essa adaptação.
def load_data(path_csv: str) -> pd.DataFrame:
    # 1) tenta normal
    try:
        df = pd.read_csv(path_csv, encoding="utf-8", sep=",", quotechar='"')
    except UnicodeDecodeError:
        # fallback caso venha em latin1
        df = pd.read_csv(path_csv, encoding="latin1", sep=",", quotechar='"')

    # 2) se veio tudo em uma coluna só, faz a limpeza e relê
    if df.shape[1] == 1:
        with open(path_csv, "r", encoding="utf-8", errors="ignore") as f:
            raw = f.read()


        clean = _clean_csv_fullquoted(raw)
        df = pd.read_csv(StringIO(clean), encoding="utf-8", sep=",", quotechar='"')

    # normaliza nomes de colunas
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )
    return df



# =============== EXECUÇÃO PRINCIPAL ===============

dataframe = load_data(INPUT_CSV)

# Dados esperados do csv (que podem ser acessados no dataframe): total_conta, gorjeta, sexo, fumante, dia, tempo, quantidade

# =============== (a) DENSIDADE DE GORJETAS POR SEXO ===============
plt.figure(figsize=(10, 6))
sns.kdeplot(
    data=dataframe,
    x="gorjeta",
    hue="sexo",
    fill=True,
    common_norm=False,
    alpha=0.4,
    linewidth=2,        # deixei a linha mais grossa para destacar, pois são somente 2 densidades
)
plt.title("Densidade do valor de gorjetas por sexo")
plt.xlabel("Gorjeta (unidade monetária)")
plt.ylabel("Densidade")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "densidade_por_sexo.png"), dpi=200)
plt.close()

# =============== (b) DENSIDADE POR QUANTIDADE NA MESA ===============
plt.figure(figsize=(10, 6))
sns.kdeplot(
    data=dataframe,
    x="gorjeta",
    hue="quantidade",
    fill=True,
    common_norm=False,
    alpha=0.35,
    linewidth=1.2
)
plt.title("Densidade do valor de gorjetas por quantidade de pessoas na mesa")
plt.xlabel("Gorjeta (unidade monetária)")
plt.ylabel("Densidade")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "densidade_por_quantidade.png"), dpi=200)
plt.close()

# =============== (c) DENSIDADE POR DIA DA SEMANA ===============
plt.figure(figsize=(10, 6))
sns.kdeplot(
    data=dataframe,
    x="gorjeta",
    hue="dia",
    fill=True,
    common_norm=False,
    alpha=0.35,
    linewidth=1.2
)
plt.title("Densidade do valor de gorjetas por dia da semana")
plt.xlabel("Gorjeta (unidade monetária)")
plt.ylabel("Densidade")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "densidade_por_dia.png"), dpi=200)
plt.close()

print("Concluído! As imagens e o resumo foram salvos em:", OUT_DIR)
