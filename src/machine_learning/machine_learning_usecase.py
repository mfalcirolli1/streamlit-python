from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

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
        pass

    def analytics(self, data_frame):
        # st.write(data_frame.info())

        st.write("### Quantidade")
        st.write(data_frame['delayed'].value_counts())

        st.write("### Porcentagem")
        st.write(data_frame['delayed'].value_counts(normalize=True))

        # Criar figura Matplotlib a partir do value_counts e renderizar com Streamlit
        # data_frame['delayed'].value_counts().plot(kind='bar', color=['green', 'red'])

        st.write("### Gráfico")
        vc = data_frame['delayed'].value_counts()
        fig, ax = plt.subplots()
        vc.plot(kind='bar', color=['green', 'red'], ax=ax)
        ax.set_xlabel('delayed')
        ax.set_ylabel('count')
        ax.set_title('Contagem de delayed')
        st.pyplot(fig)
        
        st.write(pd.crosstab(data_frame['num_stories'], data_frame['delayed']))

    