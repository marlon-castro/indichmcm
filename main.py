import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")

st.title('HOSPITAL MUNICIPAL - DR CLEMENTINO MOURA - SOCORRÃO II')
st.title('Projeto Gestão com Pessoas')

# Tabela do RH
st.header('Tabela dos Indicadores RH')
df = pd.read_excel('rh indicadores.xlsx')
df

# Título da aplicação
st.header('Gráfico de Indicadores RH')

# Criando um DataFrame
data = {

  'Mês': ['Outubro', 'Novembro', 'Dezembro', 'Janeiro', 'Fevereiro'],
  'Setores': [5, 10, 40, 15, 10]

}

df = pd.DataFrame(data)

# Criando o gráfico de barras
fig = px.bar(df, 
  x='Mês', 
  y='Setores', 
  title='Gráfico de Barras', 
  color='Setores')

# Exibindo o gráfico
st.plotly_chart(fig)


# Título da aplicação
st.header('Gráfico de Percentual RH')

# Dados dos indicadores
labels = ['Outubro', 'Novembro', 'Dezembro', 'Janeiro', 'Fevereiro']
sizes = [5, 10, 40, 15, 10]

# Criando o gráfico de pizza
fig = px.pie(values=sizes, names=labels, title='Gráfico de Pizza')

# Exibindo o gráfico
st.plotly_chart(fig)



# Tabela do NEP
st.header('Tabela dos Indicadores NEP')
df = pd.read_excel('nep indicadores.xlsx')
df

# Título da aplicação
st.header('Gráfico de Indicadores NEP')

# Criando um DataFrame
data = {

  'Mês': ['Outubro', 'Novembro', 'Dezembro', 'Janeiro', 'Fevereiro'],
  'Funcionários Participantes': [540, 254, 179, 21, 555]

}

df = pd.DataFrame(data)

# Criando o gráfico de barras
fig = px.bar(df, 
  x='Mês', 
  y='Funcionários Participantes', 
  title='Gráfico de Barras', 
  color='Funcionários Participantes')

# Exibindo o gráfico
st.plotly_chart(fig)


# Título da aplicação
st.header('Gráfico de Percentual NEP')

# Dados dos indicadores
labels = ['Outubro', 'Novembro', 'Dezembro', 'Janeiro', 'Fevereiro']
sizes = [540, 254, 179, 21, 555]

# Criando o gráfico de pizza
fig = px.pie(values=sizes, names=labels, title='Gráfico de Pizza')

# Exibindo o gráfico
st.plotly_chart(fig)



# Tabela do USST
st.header('Tabela dos Indicadores USST')
df = pd.read_excel('usst indicadores.xlsx')
df

# Título da aplicação
st.header('Gráfico de Indicadores USST')

# Criando um DataFrame
data = {

  'Mês': ['Outubro', 'Novembro', 'Dezembro', 'Janeiro', 'Fevereiro'],
  'Ações Realizadas': [5, 8, 15, 4, 12]

}

df = pd.DataFrame(data)

# Criando o gráfico de barras
fig = px.bar(df, 
  x='Mês',
  y='Ações Realizadas', 
  title='Gráfico de Barras', 
  color='Ações Realizadas')

# Exibindo o gráfico
st.plotly_chart(fig)

# Título da aplicação
st.header('Gráfico de Percentual USST')

# Dados dos indicadores
labels = ['Outubro', 'Novembro', 'Dezembro', 'Janeiro', 'Fevereiro']
sizes = [0.5, 0.8, 0.6, 0.4, 1]

# Criando o gráfico de pizza
fig = px.pie(values=sizes, names=labels, title='Gráfico de Pizza')

# Exibindo o gráfico
st.plotly_chart(fig)

st.text('Hospital Municipal Dr Clementino Moura - Socorrão II')
st.text('Desenvolvido por Marcos Nunes e Marlon Castro')
st.text('Todos os direitos reservados - 2024')