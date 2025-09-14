# main.py
# -*- coding: utf-8 -*-
import os
from io import StringIO
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# =============== CONFIGURAÇÕES GERAIS ===============
INPUT_XLSX = os.path.join("data", "Gorjetas.xlsx")          # caminho do arquivo de entrada
OUT_DIR = "out"                                             # diretório de saída
os.makedirs(OUT_DIR, exist_ok=True)                         # cria o diretório se não existir

sns.set_theme(style="whitegrid", context="talk")            # estilo agradável

# =============== CARREGAMENTO DOS DADOS ===============
def carregar_dados(path_xlsx: str) -> pd.DataFrame:
    """
    Esta função lê o Excel, junta as linhas e faz o parse como CSV.
    """
    raw = pd.read_excel(path_xlsx, header=None, dtype=str)

    # pega a primeira coluna e junta todas as linhas não nulas
    lines = [str(x).strip() for x in raw.iloc[:, 0].tolist() if pd.notna(x)]
    csv_text = "\n".join(lines)
    df = pd.read_csv(StringIO(csv_text), quotechar='"')

    # normaliza nomes de colunas
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )
    return df

df = carregar_dados(INPUT_XLSX)

# Esperado: total_conta, gorjeta, sexo, fumante, dia, tempo, quantidade
# Converte tipos numéricos
for col in ["total_conta", "gorjeta"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce").astype("Int64")

# Ordenações úteis (opcional)
# Dias prováveis: Qui, Sex, Sáb, Dom — mas vamos respeitar a ordem que existir nos dados
ordem_dias = list(pd.Categorical(df["dia"]).categories)

# Checagens rápidas
assert df["gorjeta"].notna().any(), "Coluna 'gorjeta' está vazia após parsing."
assert df["sexo"].notna().any(), "Coluna 'sexo' está vazia após parsing."
assert df["quantidade"].notna().any(), "Coluna 'quantidade' está vazia após parsing."
assert df["dia"].notna().any(), "Coluna 'dia' está vazia após parsing."

# Resumo estatístico para apoiar a análise textual
resumo = {
    "por_sexo": df.groupby("sexo")["gorjeta"].agg(["count", "mean", "median", "std"]),
    "por_quantidade": df.groupby("quantidade")["gorjeta"].agg(["count", "mean", "median", "std"]),
    "por_dia": df.groupby("dia")["gorjeta"].agg(["count", "mean", "median", "std"]).reindex(ordem_dias)
}
# Exporta um CSV com três blocos
with open(os.path.join(OUT_DIR, "resumo_estatistico.csv"), "w", encoding="utf-8") as f:
    f.write("# Resumo de gorjetas por sexo\n")
    resumo["por_sexo"].to_csv(f)
    f.write("\n# Resumo de gorjetas por quantidade\n")
    resumo["por_quantidade"].to_csv(f)
    f.write("\n# Resumo de gorjetas por dia\n")
    resumo["por_dia"].to_csv(f)

# =============== (a) DENSIDADE DE GORJETAS POR SEXO ===============
plt.figure(figsize=(10, 6))
sns.kdeplot(
    data=df,
    x="gorjeta",
    hue="sexo",
    fill=True,
    common_norm=False,
    alpha=0.4,
    linewidth=1.5
)
plt.title("Densidade do valor de gorjetas por sexo")
plt.xlabel("Gorjeta (unidade monetária)")
plt.ylabel("Densidade")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "densidade_por_sexo.png"), dpi=200)
plt.close()

# =============== (b) DENSIDADE DE GORJETAS POR QUANTIDADE NA MESA ===============
plt.figure(figsize=(10, 6))
sns.kdeplot(
    data=df,
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

# =============== (c) DENSIDADE DE GORJETAS POR DIA DA SEMANA ===============
plt.figure(figsize=(10, 6))
# Se quiser garantir ordem dos dias, usa 'hue_order=ordem_dias' quando ordem_dias existir
hue_kwargs = {}
if all(pd.notna(ordem_dias)):
    hue_kwargs["hue_order"] = ordem_dias

sns.kdeplot(
    data=df,
    x="gorjeta",
    hue="dia",
    fill=True,
    common_norm=False,
    alpha=0.35,
    linewidth=1.2,
    **hue_kwargs
)
plt.title("Densidade do valor de gorjetas por dia da semana")
plt.xlabel("Gorjeta (unidade monetária)")
plt.ylabel("Densidade")
plt.tight_layout()
plt.savefig(os.path.join(OUT_DIR, "densidade_por_dia.png"), dpi=200)
plt.close()

print("Concluído! As imagens e o resumo foram salvos em:", OUT_DIR)
