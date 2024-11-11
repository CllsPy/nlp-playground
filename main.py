import spacy
import streamlit as st
from spacy.tokenizer import Tokenizer
from utils import *
import en_core_web_sm
#python -m spacy download pt_core_news_sm
#from spacy.cli import download
#download("pt_core_news_sm")
#spacy.load("en_core_web_sm")
#nlp = spacy.load('pt_core_news_sm')

nlp = spacy.load('en_core_web_sm')
st.title(title_msg)

col1, col2, col3 = st.columns(3)

with st.sidebar:
	st.markdown("## Objetivo")
	st.write(desc_app)
	st.markdown("## Sumário")
	st.markdown(""" 
	
	- Tokenização
	- Pos (Parts Of Speach)
	- Contador de Caracteres
	- Lemmanization
	
	""")
	
	st.markdown("---")
	st.markdown(f"Feito por [CLL](https://github.com/CllsPy)")
	
def explain(text_input: str) -> str:
	
	answer  = []
	doc = nlp(text_input)

	for token in doc:
		answer.append((token.text, token.pos_,
			 spacy.explain(token.pos_)))

	return answer

with st.expander('Tokenização'):
	st.markdown(token_msg)
	
	st.info("Por favor insira seu texto abaixo")

	token_msg_ = st.text_area('Tokenizar')
	tokenizer_answer_ = nlp(token_msg_)
	st.button("Tokenizar", type="primary")

	if st.button:
		st.markdown(([w.text for w in tokenizer_answer_]))
	
with st.expander('Parte da Fala (POS)'):
	st.markdown(pos_msg)
	st.info("Por favor insira seu texto abaixo")
	msg = st.text_area('POS')
	st.button("Parts Of Speach", type="primary")

	if st.button:
		st.markdown(explain(msg))

with col1:
	with st.expander("Contador de Caracteres"):
		st.info("Por favor insira seu texto abaixo")
		text = st.text_area("Seu Texto")
		st.button("Contar", type="primary")
	
		if st.button:
			st.markdown(f'Você escreveu {len(text)} caracteres!')
	

with st.expander('Lemmanization'):
	st.markdown(lem_msg)
	st.info("Por favor insira seu texto abaixo")
	answer_lemm = []
	text_lem = st.text_area("Lemma")
	
	for token in nlp(text_lem): 
	  lemma = token.lemma_ 
	  answer_lemm.append((token.text, "-->", lemma))
	
	st.button("Lemmanitizar", type="primary")

	if st.button:
		st.markdown(answer_lemm)
	

	


