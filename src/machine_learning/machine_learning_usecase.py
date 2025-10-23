from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

''' Evaluation
Atingir 95% de precisão em prever se uma features irá atrasar ou não a partir das informações das features anteriores
'''

''' Sumário

num_stories
Tipo: Numérica (inteiro)
O que representa: Número total de histórias (ou tarefas) que compõem a feature.
Impacto esperado: Quanto maior o número, maior a complexidade e maior a chance de atraso.

avg_story_points
Tipo: Numérica (inteiro)
O que representa: Média de pontos atribuídos às histórias da feature, refletindo esforço estimado ou complexidade.
Impacto esperado: Histórias com pontos altos indicam tarefas mais complexas, potencialmente aumentando o risco de atraso.

scope_changes
Tipo: Numérica (inteiro)
O que representa: Quantidade de mudanças no escopo da feature durante o desenvolvimento.
Impacto esperado: Mudanças frequentes podem causar retrabalho e atrasos.

bug_count
Tipo: Numérica (inteiro)
O que representa: Número de bugs encontrados durante o desenvolvimento ou testes antes da entrega.
Impacto esperado: Mais bugs normalmente indicam retrabalho adicional, aumentando o lead time.

dev_count
Tipo: Numérica (inteiro)
O que representa: Número de desenvolvedores que trabalharam na feature.
Impacto esperado: Mais devs podem acelerar o desenvolvimento, mas também aumentar complexidade de coordenação.

rework_ratio
Tipo: Numérica (decimal, 0.0 - 1.0)
O que representa: Proporção de histórias que precisaram de retrabalho (reabertas ou corrigidas).
Impacto esperado: Quanto maior o retrabalho, maior a probabilidade de atraso.

delayed
Tipo: Binária (0 ou 1)
O que representa: Indica se a feature atrasou (1) ou foi entregue dentro do prazo (0).
Impacto esperado: É a variável alvo do modelo — tudo o mais serve para prever ou explicar este resultado.
'''
class MachineLearningUseCase():

    def __init__(self):

        self.models = {
            "Logistic Regression": LogisticRegression(),
            "KNN": KNeighborsClassifier(),
            "Random Forest": RandomForestClassifier()
        }


    def analytics(self, data_frame):

        with st.expander("### Informações do DataFrame"):
            # st.write(data_frame.info())

            st.write("### Quantidade")
            st.write(data_frame['delayed'].value_counts())

            st.write("### Porcentagem")
            st.write(data_frame['delayed'].value_counts(normalize=True))

            # Criar figura Matplotlib a partir do value_counts e renderizar com Streamlit
            # data_frame['delayed'].value_counts().plot(kind='bar', color=['green', 'red'])

            with st.expander("### Gráfico 1"):
                st.write(pd.crosstab(data_frame['num_stories'], data_frame['delayed']))

                pd.crosstab(data_frame['num_stories'], data_frame['delayed']).plot(kind='bar', figsize=(10,6), color=['lightblue', 'salmon'])
                plt.title("Relação entre Quantidades de Histórias e Features Atrasadas ou No Prazo")
                plt.xlabel("Quantidade de Histórias")
                plt.ylabel("Features")
                plt.legend(["No Prazo", "Atrasado"])
                st.pyplot(plt)

            with st.expander("### Gráfico 2"):

                vc = data_frame['delayed'].value_counts()
                fig, ax = plt.subplots()
                vc.plot(kind='bar', color=['lightblue', 'salmon'], ax=ax)
                ax.set_xlabel('delayed')
                ax.set_ylabel('count')
                ax.set_title('Contagem de delayed')

                st.pyplot(fig)

            with st.expander("### Gráfico 3"):
                
                st.write("Percebe-se que features com maior número de histórias tendem" \
                " a ter maior probabilidade de retrabalho e consequentemente atrasar mais, Salvo alguns outliers.")

                plt.figure(figsize=(10,6))

                plt.scatter(data_frame["num_stories"][data_frame["delayed"] == 1],
                            data_frame["rework_ratio"][data_frame["delayed"] == 1], 
                            c="salmon")

                plt.scatter(data_frame["num_stories"][data_frame["delayed"] == 0],
                            data_frame["rework_ratio"][data_frame["delayed"] == 0], 
                            c="lightblue")
                
                plt.title("Relação entre Número de Histórias e Retrabalho")
                plt.xlabel("Número de Histórias")
                plt.ylabel("Retrabalho")
                plt.legend(["Atrasado", "No Prazo"])

                st.pyplot(plt)

            with st.expander("### Gráfico 4"):
                st.write("Lê-se, 'De 10 features com 2 bugs, 1 atrasou e 9 foram no prazo.'")

                pd.crosstab(data_frame['bug_count'], data_frame['delayed']).plot(kind='bar', figsize=(10,6), color=['lightblue', 'salmon'])
                plt.title("Relação entre Quantidades de Bugs e Features Atrasadas ou No Prazo")
                plt.xlabel("Quantidade de Bugs")
                plt.ylabel("Features")
                plt.legend(["No Prazo", "Atrasado"])
                st.pyplot(plt)

            with st.expander("### Gráfico 5"):
                st.write("Observa-se que features com mais mudanças de escopo tendem a atrasar mais.")

                pd.crosstab(data_frame['scope_changes'], data_frame['delayed']).plot(kind='bar', figsize=(10,6), color=['lightblue', 'salmon'])
                plt.title("Relação entre Mudanças de Escopo e Features Atrasadas ou No Prazo")
                plt.xlabel("Mudanças de Escopo")
                plt.ylabel("Features")
                plt.legend(["No Prazo", "Atrasado"])
                st.pyplot(plt)
            
            with st.expander("### Gráfico 6"):
                st.write("Matriz de Correlação entre as Features")

                st.write("Um valor próximo de +1 indica uma forte correlação positiva (ambas as variáveis aumentam juntas), " \
                "enquanto um valor próximo de -1 indica uma forte correlação negativa (uma aumenta conforme a outra diminui). " \
                "Um valor próximo de 0 indica que não há correlação significativa entre as variáveis. " \
                "Os coeficientes na diagonal principal são sempre 1, pois cada variável é perfeitamente correlacionada consigo mesma")

                matrix_correlacao = data_frame.corr()
                plt.figure(figsize=(15,10))

                sns.heatmap(matrix_correlacao,
                            annot=True, # mostra na lateral uma legenda com os valores
                            linewidths=0.5, # largura das linhas que separam os quadrados
                            fmt=".2f", # formatação das casas decimais
                            cmap='YlGnBu') # paleta de cores
                
                st.pyplot(plt)

            
    def preparing(self, data_frame):

        with st.expander("### Preparação dos Dados para o Modelo"):

            # https://scikit-learn.org/stable/machine_learning_map.html
            st.header("Variáveis Independentes e Dependente")
            
            # axis=0 para linhas, axis=1 para colunas
            X = data_frame.drop('delayed', axis=1) # X maiúsculo para variáveis independentes
            y = data_frame['delayed'] # y minúsculo para variável dependente

            st.write("#### Variáveis Independentes (X)")
            st.write(X.head())

            st.write("#### Variável Dependente (y)")
            st.write(y.head())

            st.header("Divisão entre Conjunto de Treinamento e Teste")
            # Isolar o conjunto de teste do conjunto de treino

            X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                                test_size=0.2) # 20% dos dados para teste # mantém a proporção original das classes

            st.write(f"#### Tamanho do Conjunto de Treinamento: {len(X_train)} e {len(y_train)}")
            st.write(f"#### Tamanho do Conjunto de Teste: {len(X_test)} e {len(y_test)}")



    def fit_and_score(self, X_train, X_test, y_train, y_test):
        
        pass
