import streamlit as st
import pandas as pd
import yfinance as yf

def main():
    st.write("""
    # Histórico de Ações - IBOVESPA
         """)
    
    selectbox = st.selectbox("Selecione a Ação desejada: ", ["", "ITUB4.SA", "PETR4.SA"])
    if selectbox and selectbox != "":
        data = load_data(selectbox)
        st.write(data["nome"])
        st.line_chart(data["historico"][["Close"]])

@st.cache_data
def load_data(empresa):

    dados_acao = yf.Ticker(empresa)
    nome = dados_acao.info.get('longName', 'Nome não disponível')
    historico = dados_acao.history(
        period="1d",
        start="2021-01-01",
        end="2025-01-31"
    )
    return {"nome": nome, "historico": historico}


main()