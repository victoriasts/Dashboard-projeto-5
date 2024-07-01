import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análise da venda de Veiculos, Histogramas e Gráficos')
     
car_data = pd.read_csv('vehicles_us.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão
     
if hist_button: # se o botão for clicado
          # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
         # criar um histograma
    fig = px.histogram(car_data, x="odometer")
     
         # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Criar gráfico de dispersão') # criar um botão
     
if disp_button: # se o botão for clicado
          # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
         
         # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")
     
         # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
