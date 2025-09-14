import os
import io
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# =============== CONFIGURAÇÕES GERAIS ===============

# Definições de constantes para não ter que mudar em vários lugares caso o caminho mude. 
INPUT_CSV = os.path.join("data", "Gorjetas.csv")        # caminho do arquivo de entrada
OUT_DIR = "out"                                         # diretório de saída
os.makedirs(OUT_DIR, exist_ok=True)                     # cria o diretório de saída, se não existir
sns.set_theme()                                         # personalização do estilo dos gráficos (background)


# =============== FUNÇÕES DE SUPORTE ===============

# Remove aspas externas de cada linha e converte aspas duplas duplicadas.
def _clean_csv_fullquoted(text: str) -> str:
    lines = text.splitlines()
    fixed = []
    for ln in lines:
        ln = ln.strip("\ufeff").rstrip()                # remove espaços extras
        if len(ln) >= 2 and ln.startswith('"') and ln.endswith('"'):
            ln = ln[1:-1]                               # tira aspas do começo e do fim
        ln = ln.replace('""', '"')                      # aspas duplas transforma em aspas simples
        fixed.append(ln)
    return "\n".join(fixed)


# Tentar ler o CSV. Se o arquivo estiver 'full-quoted' (tudo em 1 coluna), faz a limpeza e relê.
# Com xlsx não tive problemas com outro código adaptado para xlsx. Mas como a instrução era fazer com CSV, tive que fazer essa adaptação.
def _read_csv(path_csv: str) -> pd.DataFrame:
    # 1) tenta leitura direta com vírgula
    for enc in ("utf-8", "latin1"):
        try:
            df = pd.read_csv(path_csv, encoding=enc, sep=",", quotechar='"')
            if df.shape[1] > 1:
                return df
        except Exception:
            pass

    # 2) tenta detectar delimitador com Sniffer
    with open(path_csv, "r", encoding="utf-8", errors="ignore") as f:
        sample = f.read(4096)

    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
        delim = dialect.delimiter
    except Exception:
        # fallback mais comum no BR quando falha
        delim = ";"

    for enc in ("utf-8", "latin1"):
        try:
            df = pd.read_csv(path_csv, encoding=enc, sep=delim, quotechar='"')
            if df.shape[1] > 1:
                return df
        except Exception:
            pass

    # 3) trata caso full-quoted
    with open(path_csv, "r", encoding="utf-8", errors="ignore") as f:
        raw = f.read()
    clean = _clean_csv_fullquoted(raw)

    for sep in (",", ";"):
        try:
            df = pd.read_csv(io.StringIO(clean), encoding="utf-8", sep=sep, quotechar='"')
            if df.shape[1] > 1:
                return df
        except Exception:
            continue

    # Se nada deu certo, lê como 1 coluna mesmo
    return pd.read_csv(io.StringIO(clean), header=None, names=["_raw"])




# =============== CARREGAMENTO DOS DADOS ===============
def load_data(path_csv: str) -> pd.DataFrame:
    df = _read_csv(path_csv)
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
    fill=True,                                          # preenche a área sob a curva
    common_norm=False,                                  # compara as formas das distribuições (picos, dispersão) sem distorção pelo tamanho do grupo.
    alpha=0.4,                                          # Transparência
    linewidth=2,                                        # deixei a linha mais grossa para destacar
    palette={"Homem": "blue", "Mulher": "purple"}       # cores personalizadas para cada sexo
)
plt.title("Densidade do valor de gorjetas por sexo")
plt.xlabel("Gorjeta (unidade monetária)")
plt.ylabel("Densidade")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "densidade_por_sexo.png"), dpi=200)
plt.close()

# =============== (b) DENSIDADE DE GORJETAS POR QUANTIDADE DE PESSOAS NA MESA ===============
plt.figure(figsize=(10, 6))
sns.kdeplot(
    data=dataframe,
    x="gorjeta",
    hue="quantidade",
    fill=True,                                          # preenche a área sob a curva
    common_norm=False,                                  # compara as formas das distribuições (picos, dispersão) sem distorção pelo tamanho do grupo.
    alpha=0.35,                                         # Transparência
    linewidth=1.2,
)
plt.title("Densidade do valor de gorjetas por quantidade de pessoas na mesa")
plt.xlabel("Gorjeta (unidade monetária)")
plt.ylabel("Densidade")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "densidade_por_quantidade.png"), dpi=200)
plt.close()

# =============== (c) DENSIDADE DE GORJETAS POR DIA DA SEMANA ===============
plt.figure(figsize=(10, 6))
sns.kdeplot(
    data=dataframe,
    x="gorjeta",
    hue="dia",
    fill=True,                                          # preenche a área sob a curva
    common_norm=False,                                  # compara as formas das distribuições (picos, dispersão) sem distorção pelo tamanho do grupo.
    alpha=0.35,                                         # Transparência
    linewidth=1.2,
)
plt.title("Densidade do valor de gorjetas por dia da semana")
plt.xlabel("Gorjeta (unidade monetária)")
plt.ylabel("Densidade")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "densidade_por_dia.png"), dpi=200)
plt.close()

print("Concluído! As imagens foram salvas em:", OUT_DIR)
