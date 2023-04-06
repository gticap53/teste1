import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Configuração da credencial do Firebase
cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Cria uma instância do banco de dados Firestore
db = firestore.client()

# Cria um formulário Streamlit
st.write("# Formulário de Registro")
nome = st.text_input("Nome")
data_nascimento = st.date_input("Data de Nascimento")
cpf = st.text_input("CPF")

# Função para enviar os dados do formulário para o Firestore
def enviar_dados_firestore(nome, data_nascimento, cpf):
    doc_ref = db.collection(u'usuarios').document()
    doc_ref.set({
        u'id': doc_ref.id,
        u'nome': nome,
        u'data_nascimento': data_nascimento,
        u'cpf': cpf
    })

# Botão para enviar dados do formulário
if st.button("Enviar"):
    enviar_dados_firestore(nome, data_nascimento, cpf)
    st.success("Dados enviados com sucesso!")
