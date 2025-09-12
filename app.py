import streamlit as st
from agenda import Agenda

st.title("Gerenciador de Contatos 📔")
st.header("Bem-vindo ao seu gerenciador pessoal")
st.write("Use a barra lateral para adicionar, exibir ou remover contatos. As informações são salvas de forma segura e acessíveis a qualquer momento.")

# Inicializa o estado da sessão com a agenda
if 'agenda' not in st.session_state:
    st.session_state.agenda = Agenda()

# --- Menu na Barra Lateral ---
st.sidebar.title("Menu")
opcao = st.sidebar.radio("Escolha uma opção:", ["Adicionar Contato", "Exibir Contatos", "Remover Contato"])

# --- Lógica da Interface ---
if opcao == "Adicionar Contato":
    st.subheader("Adicionar Novo Contato")
    with st.form(key='adicionar_form'):
        nome = st.text_input("Nome: ")
        telefone = st.text_input("Telefone: ")
        email = st.text_input("Email: ")
        submit_button = st.form_submit_button(label="Salvar Contato")

    if submit_button:
        if nome and telefone:
            mensagem = st.session_state.agenda.adicionar_contato(nome, telefone, email)
            if mensagem.startswith("Erro"):
                st.error(mensagem)
            else:
                st.success(mensagem)
        else:
            st.error("O nome e o telefone são obrigatórios.")

elif opcao == "Exibir Contatos":
    st.subheader("Lista de Contatos")
    contatos = st.session_state.agenda.exibir_contatos()
    if contatos:
        for telefone, dados in contatos.items():
            st.markdown(f"**Nome:** {dados['nome']}")
            st.write(f"**Telefone:** {telefone}")
            st.write(f"**Email:** {dados['email']}")
            st.markdown("---")
    else:
        st.info("Nenhum contato na agenda.")

elif opcao == "Remover Contato":
    st.subheader("Remover Contato Existente")
    contatos = st.session_state.agenda.exibir_contatos()
    if contatos:
        # Cria uma lista para exibição (nome - telefone)
        lista_opcoes = [f"{dados['nome']} - {telefone}" for telefone, dados in contatos.items()]
        
        # Cria um mapeamento para obter o telefone a partir da opção selecionada
        mapa_opcoes = {f"{dados['nome']} - {telefone}": telefone for telefone, dados in contatos.items()}

        contato_selecionado = st.selectbox("Selecione o contato para remover:", lista_opcoes)

        if st.button("Remover"):
            telefone_para_remover = mapa_opcoes[contato_selecionado]
            mensagem = st.session_state.agenda.remover_contato(telefone_para_remover)
            if mensagem.startswith("Erro"):
                st.error(mensagem)
            else:
                st.success(mensagem)
                st.rerun()
    else:
        st.info("Não há contatos para remover.")