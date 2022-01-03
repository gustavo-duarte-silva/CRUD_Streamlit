import streamlit as st
import Controller as controller
import pandas as pd

st.title("CRUD-ESCOLA-BTOR")
user = st.sidebar.text_input(label='Login')
senha = st.sidebar.text_input(label='Senha', type='password')

if st.sidebar.checkbox("Logar"):
    if user=='btor' and senha =='123':
        st.sidebar.success("Seja Bem Vindo, Diretor!")
        page_aluno = st.selectbox('MENU',['Incluir', 'Alterar', 'Excluir', 'Consultar'])
        
        if page_aluno == "Incluir":
            st.title('CADASTRO ALUNO')
            with st.form(key='crud_escola'):
                input_name = st.text_input(label='Insira o Nome do Aluno')
                input_cpf = st.text_input(label='Digite seu CPF')
                input_data = st.date_input(label='Data de Nascimento')
                input_button_submit = st.form_submit_button("Enviar")
                                
            if input_button_submit:
                controller.incluir(input_name, input_cpf, input_data)
                st.success("Aluno Adicionado com Sucesso")

        if page_aluno == "Consultar":
            st.title('ALUNOS')
            lista_alunos = []
            for i in controller.status():
                lista_alunos.append([i.id, i.nome, i.cpf, i.data])
            df = pd.DataFrame(lista_alunos, columns = ['ID', 'Nome', 'CPF', 'DATA'])
            df.reset_index(drop=True, inplace=True)
            st.table(df)

        if page_aluno == "Alterar":
            st.title('ALTERAR')
            with st.form(key='Alterar'):
                alt_input_id = st.text_input(label="ID")
                alt_input_nome = st.text_input(label='Insira o Nome do Aluno')
                alt_input_cpf = st.text_input(label='Digite seu CPF')
                alt_input_data = st.date_input(label='Data de Nascimento')
                alt_input_button = st.form_submit_button("Enviar")
            if alt_input_button:
                controller.update(id=alt_input_id,nome=alt_input_nome, cpf=alt_input_cpf, data=alt_input_data)
                st.success("Aluno Alterado com Sucesso")
        
        if page_aluno == "Excluir":
            st.title('EXCLUIR')
            with st.form(key='excluir'):
                del_input_id = st.text_input(label="ID")
                del_input_button = st.form_submit_button("Enviar")
            if del_input_button:
                controller.delete(id=del_input_id)
                st.success("Aluno Deletado com Sucesso")

    else:
        st.error("Senha Invalida")
