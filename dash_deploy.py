import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Visualização dos dados")

arquivo = st.file_uploader("Escolha um arquivo CSV", type='csv')

if arquivo:
    df = pd.read_csv(arquivo)
    st.write(df)

    st.subheader('Selecione as colunas para o gráfico')
    opcoes = df.columns.tolist()
    opcoes_wo_data = [x for x in opcoes if x != 'Data']
    eixo_x = st.selectbox("eixo x", options=opcoes)
    eixo_y = st.selectbox("eixo y", options=opcoes_wo_data)

    if eixo_x and eixo_y:
        fig = px.line(df, x=eixo_x, y=eixo_y, title='Dados')
        st.plotly_chart(fig)

        st.subheader("gráfico de barra")
        fig2 = px.bar(df, x='Data', y='Vendas', title='Barra')
        st.plotly_chart(fig2)


# pip install streamlit==1.29.0
# pip install pandas
# pip install matplotlib
# pip install plotly
        
# pip list --format=freeze > requirements.txt