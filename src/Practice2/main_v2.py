import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import timedelta


acoes = ["ITUB4.SA", "PETR4.SA", "MGLU3.SA", "VALE3.SA", "GGBR4.SA"]

def main():
    st.write("""
    # Histórico de Ações - IBOVESPA
         """)
    
    st.sidebar.header("Filtros")

    acoes_selecionadas = st.sidebar.multiselect("Selecione as Ações desejadas: ", acoes)
    # acoes_selecionadas = st.multiselect("Selecione as Ações desejadas: ", acoes)

    if acoes_selecionadas:
        if len(acoes_selecionadas) == 1:
            data = load_single_data(acoes_selecionadas[0])
        else:
            data = load_multiple_data(acoes_selecionadas)

        data_inicial = data.index.min().to_pydatetime()
        data_final = data.index.max().to_pydatetime()

        periodo = st.sidebar.slider("Selecione o período", 
                                        min_value=data_inicial, 
                                        max_value=data_final, 
                                        value=(data_inicial, data_final),
                                        step=timedelta(days=1))

        dados_filtrados = data.loc[periodo[0]: periodo[1]]

        if len(acoes_selecionadas) == 1:
            st.line_chart(dados_filtrados[["Close"]])
        else:
            st.line_chart(dados_filtrados["Close"])

@st.cache_data
def load_single_data(acao):
    
    dados_acao = yf.Ticker(acao)
    historico = dados_acao.history(
        period="1d",
        start="2021-01-01",
        end="2025-01-31"
    )
    return historico


@st.cache_data
def load_multiple_data(acoes):
    
    dados_acao = yf.Tickers(" ".join(acoes))
    historicos = dados_acao.history(
        period="1d",
        start="2021-01-01",
        end="2025-01-31"
    )
    return historicos


main()