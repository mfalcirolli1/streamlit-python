import streamlit as st
import time

def main():
    st.title("Streamlit - Título")

    st.header("Input")
    input = st.text_input("Digite uma entrada de texto aqui:")
    if input:
        st.write(f"Você digitou: {input}")

    st.header("Select")
    select = st.selectbox("Esse é meu select box", ["Selecione uma opção", "Opção 1", "Opção 2", "Opção 3"])
    if select and select != "Selecione uma opção":
        st.write(f"A opção selecionada é: {select}")

    st.header("Slider")
    slider = st.slider("Esse é meu slider", 0, 100, 20)
    if slider:
        st.write(f"O valor selecionado é: {slider}")

    st.header("Checkbox")
    checkbox = st.checkbox("Esse é meu checkbox")
    if checkbox:
        st.write("Ativado")
    else:
        st.write("Desativado")

    st.header("Botão")
    if st.button("Clique aqui!"):
        st.write("Botão clicado")

    st.header("Upload")
    upload = st.file_uploader("Escolha um arquivo", type=["pdf", "txt", "xlsx"])
    if upload:
        st.write(f"O enviado é: {upload.name} - {upload.type}")

    st.header("Gráficos")
    dados = {'eixo x': [1,2,3], 'eixo y': [25,78,91]}
    st.line_chart(dados)

    st.header("Spinner")
    with st.spinner("Aguarde..."):
        time.sleep(2)
        st.success("Carregado com sucesso")

    st.header("Labels")
    st.success("Sucesso")
    st.info("Informação")
    st.warning("Aviso")
    st.error("Erro")

main()