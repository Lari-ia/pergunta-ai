import streamlit as st
import openai
import random

# 🔐 Sua chave da OpenAI
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

# 🚫 Lista de palavras proibidas
palavras_proibidas = [
    "sexo", "genital", "beijo", "maconha", "drogas", "estupr", "lésbica", "gay", "trans",
    "pênis", "vagina", "violência", "arma", "suicídio", "morte", "assass", "xvideos",
    "porn", "bunda", "seios", "nude", "xvideo", "transar", "estupro", "criminoso", "terrorismo"
]

# ✅ Lista de curiosidades seguras e infantis
curiosidades = [
    "Você sabia que a girafa dorme só 2 horas por dia? 🦒💤",
    "O polvo tem três corações! 💘💘💘",
    "As tartarugas podem respirar pelo bumbum! 🐢😄",
    "O pinguim tem um joelho escondido! 🐧🦵",
    "A língua de um tamanduá pode ter mais de 60 cm! 👅",
    "As formigas não têm pulmões! Elas respiram por buraquinhos no corpo 🐜",
    "O tubarão já existia antes dos dinossauros! 🦈🦖",
    "O camaleão muda de cor com o humor! 🦎🎭",
    "A Kapibara é o maior roedor do mundo e adora nadar! 🐾🌊",
    "Cavalos dormem em pé! 🐴💤"
]

# 🌟 Configuração inicial do app
st.set_page_config(page_title="Pergunta Aí!", page_icon="🐾", layout="centered")

# 💬 Campo para nome da criança
nome = st.text_input("Qual é o seu nome?", "")

# 👋 Saudação personalizada no topo
if nome:
    saudacao = f"Oiê, {nome}! Eu sou a <strong>Kapibara</strong>, sua amiga. Vamos aprender muitas coisas legais juntos! 🌟🧠"
else:
    saudacao = "Oiê! Eu sou a <strong>Kapibara</strong>, sua amiga. Vamos aprender muitas coisas legais juntos! 🌟🧠"

# 🖼️ Layout com imagem e título
col1, col2 = st.columns([1, 4])
with col1:
    st.image("kapibara.png", width=130)
with col2:
    st.markdown("<h1 style='color: #ffb703; font-size: 40px; margin-top: 35px;'>❓ Pergunta Aí!</h1>", unsafe_allow_html=True)

# ✨ Frase de boas-vindas personalizada
st.markdown(f"<p style='text-align: center; font-size: 18px;'>{saudacao}</p>", unsafe_allow_html=True)

# ✍️ Caixa de pergunta
st.markdown("### ✍️ Escreva sua pergunta aqui:")
pergunta = st.text_input(label="Digite sua pergunta:", label_visibility="collapsed")

# 🛡️ Função para verificar se a pergunta é segura
def pergunta_segura(texto):
    texto = texto.lower()
    return not any(p in texto for p in palavras_proibidas)

# 🤖 Função para responder com saudação personalizada
def responder(pergunta):
    chamada = nome if nome else "amiguinho"

    prompt = f"""
Você é uma capivara fofa, chamada Kapibara, gentil e divertida com crianças de 4 a 10 anos. 
Nunca fale sobre sexo, drogas, violência, morte, política, religião ou partes íntimas.
Fale com carinho, alegria e explicações simples, como se estivesse em uma sala de aula divertida.

Sempre inicie a resposta com: "Oi, {chamada}!" e depois responda a pergunta com entusiasmo.

Pergunta da criança: {pergunta}
Resposta:
"""
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=200
    )
    return resposta.choices[0].message["content"]

# 🎯 Lógica de resposta
if pergunta:
    if pergunta_segura(pergunta):
        resposta = responder(pergunta)
        st.success(resposta)
    else:
        st.warning("Essa pergunta não é legal de responder aqui. Que tal aprender por que as girafas têm o pescoço comprido? 🦒")

# 🎲 Botão de curiosidade aleatória
if st.button("🎲 Surpreenda-me!"):
    st.info(random.choice(curiosidades))

# 🖤 Rodapé
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Feito com carinho pela Kapibara e a Lari 💛</p>", unsafe_allow_html=True)
