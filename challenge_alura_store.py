import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

loja1 = pd.read_csv(url1)
loja2 = pd.read_csv(url2)
loja3 = pd.read_csv(url3)
loja4 = pd.read_csv(url4)

lojas = {'Loja 1': loja1, 'Loja 2': loja2, 'Loja 3': loja3, 'Loja 4': loja4}

def fat_total(loja):
  faturamento = 0

  for i in loja['Preço']:
    faturamento += i
  return round(faturamento, 2)

def qtd_categoria(loja):
  categorias_unicas = list(set(loja['Categoria do Produto']))
  agrup_cat = []

  for cat in categorias_unicas:
    categoria = [c for c in loja['Categoria do Produto'] if c == cat]
    agrup_cat.append(categoria)

  dict_cat = {categorias_unicas[i]: len(agrup_cat[i]) for i in range(len(categorias_unicas))}

  return dict_cat

def mais_popular(loja):
  categorias = qtd_categoria(loja)

  for cat in categorias:
    if categorias[cat] == max(categorias.values()):
      return cat

def media_avaliacao(loja):
  soma = 0
  soma += sum([loja['Avaliação da compra'][i] for i in range(len(loja['Avaliação da compra']))])
  return round(soma / len(loja['Avaliação da compra']), 2)

def prod_num_vendas(loja):
  produtos_unicos = list(set(loja['Produto']))
  qtd_vendida = []

  for prod in produtos_unicos:
    produto = [p for p in loja['Produto'] if p == prod]
    qtd_vendida.append(len(produto))

  dict_prod = {produtos_unicos[i]: qtd_vendida[i] for i in range(len(produtos_unicos))}
  return dict_prod

def mais_vendido(loja):
  num_vendas = prod_num_vendas(loja)
  mais_vendido = max(num_vendas, key=num_vendas.get)

  return mais_vendido, num_vendas[mais_vendido]

def menos_vendido(loja):
  num_vendas = prod_num_vendas(loja)
  menos_vendido = min(num_vendas, key=num_vendas.get)

  return menos_vendido, num_vendas[menos_vendido]

def frete_custo_med(loja):
  soma = 0
  soma += sum([loja['Frete'][i] for i in range(len(loja['Frete']))])

  return round(soma/len(loja['Frete']), 2)

print(frete_custo_med(loja1))

def grafico_avaliação(conj_lojas):
  av_lojas = [media_avaliacao(conj_lojas[key]) for key in conj_lojas.keys()]
  fix, ax = plt.subplots()

  y_min = min(av_lojas) - 0.08
  y_max = max(av_lojas) + 0.08

  ax.bar(x = conj_lojas.keys(), height = av_lojas, label = 'blue')
  ax.set_ylabel('Valor das Avaliações')
  ax.set_title('Média de Avaliações de cada Loja')
  ax.set_ylim(y_min, y_max)
  for i, valor in enumerate(av_lojas):
    plt.text(i, valor + 0.01, f"{valor:.2f}", ha='center')
  plt.show()

def grafico_faturamento(conj_lojas):
  faturamentos = [fat_total(conj_lojas[key]) for key in conj_lojas.keys()]
  fig, ax = plt.subplots()

  ax.pie(faturamentos, labels=conj_lojas.keys(), autopct='%.2f%%')
  ax.set_title("Porcentagem do Faturamento de cada Loja sobre o Faturamento Total")
  plt.show()

def grafico_frete(conj_lojas):
  fig, ax = plt.subplots()

  for nome_loja, loja in conj_lojas.items():
    org_frete = np.sort(loja['Frete'])
    plt.plot(org_frete, label=nome_loja)

  ax.set_title("Fretes Organizados por Custo em cada Loja")
  ax.set_xlabel("Índice de Transação (Organizado pelo Custo do Frete)")
  ax.set_ylabel("Custo do Frete")
  ax.legend(title='Loja')
  ax.grid(True, linestyle='--', alpha=0.6)
  plt.show()

def visao_geral(conj_lojas):
  for nome_loja, loja in conj_lojas.items():
    print(f"\n\n===== {nome_loja} =====")
    print(f"Faturamento: {fat_total(loja)}")
    print(f"Categoria mais popular: {mais_popular(loja)}")
    print(f"Média avaliação: {media_avaliacao(loja)}")
    print(f"Produto mais vendido: {mais_vendido(loja)}")
    print(f"Produto menos vendido: {menos_vendido(loja)}")
    print(f"Custo médio do frete: {frete_custo_med(loja)}")

def graficos_gerais(conj_lojas):
  grafico_avaliação(conj_lojas)
  grafico_faturamento(conj_lojas)
  grafico_frete(conj_lojas)

visao_geral(lojas)
graficos_gerais(lojas)
