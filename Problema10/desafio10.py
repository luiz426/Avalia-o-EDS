import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter

def gerar_grafico(lista_datas, nome_arquivo):
    contagem = Counter(lista_datas)
    datas = list(contagem.keys())
    quantidades = list(contagem.values())
    
    plt.figure(figsize=(6, 4))  # Garante novo gráfico a cada chamada
    plt.bar(datas, quantidades)
    plt.xlabel("Data")
    plt.ylabel("Atendimentos")
    plt.title("Atendimentos por Dia")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(nome_arquivo)
    plt.close()  # Evita sobreposição entre gráficos
    print(f" Gráfico salvo como {nome_arquivo}")

# Exemplo variação 1
dados1 = ["01/06/2025", "01/06/2025", "02/06/2025"]
gerar_grafico(dados1, "grafico1.png")

# Exemplo variação 2
dados2 = ["03/06/2025", "03/06/2025", "03/06/2025", "04/06/2025"]
gerar_grafico(dados2, "grafico2.png")

# Exemplo variação 3
dados3 = ["05/06/2025", "06/06/2025", "06/06/2025", "06/06/2025", "06/06/2025"]
gerar_grafico(dados3, "grafico3.png")
