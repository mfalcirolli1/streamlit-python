import streamlit as st
import pandas as pd
import charset_normalizer as cn
from machine_learning_usecase import MachineLearningUseCase

class App():

    def __init__(self):
        st.title("Machine Learning App")


    def run(self):
        st.header("Welcome to the Machine Learning Application")
        st.write("This application demonstrates a simple machine learning model using Streamlit.")

        file = st.file_uploader("Upload your dataset here", type=["txt"])

        if file:
            st.success(f"File {file.name} uploaded successfully!")

            try:
                df = pd.read_csv(file, encoding='utf-8')
                st.subheader("Preview of uploaded data")
                st.dataframe(df.head())

                # Machine Learning usa Variáveis independentes para prever o valor de uma Variável Dependente
                MachineLearningUseCase().analytics(df)                

            except Exception as e:
                st.error(f"Não foi possível ler o arquivo CSV: {e}")


if __name__ == "__main__":
    app = App()
    app.run()