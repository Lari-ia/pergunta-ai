import streamlit as st
import os
from openai import OpenAI
import random

# Inicializa o cliente da OpenAI com a variável de ambiente
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Palavras proibidas
palavras_proibidas = [
    "sexo", "genital", "beijo", "maconha", "drogas", "estupr", "lésbica", "gay", "trans",
    "pênis", "vagina", "violência", "arma", "suicídio", "morte", "assass", "xvideos",
    "porn", "bunda", "seios", "nude", "xvideo", "transar", "estupro", "criminoso", "terrorismo"
]

# Curiosidades infantis
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

# Função de segurança
def pergunta_segura(texto):
    texto = texto.lower()
    return not any(p in texto for p in palavras_proibidas)

# Nova função usando a API atualizada
def responder(pergunta, nome="amiguinho"):
    chamada = nome if nome.strip() else "amiguinho"

    prompt = f"""
Você é uma capivara fofa, chamada Kapibara, curiosa e gentil com crianças de 4 a 10 anos. 
Nunca fale sobre sexo, drogas, violência, morte, política, religião ou partes íntimas.
Fale com humor, carinho e explicações simples, como se estivesse em uma sala de aula divertida.

Sempre comece sua resposta com: "Oi, {chamada}!"

Pergunta da criança: {pergunta}
Resposta:
"""
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=200
    )
    return resposta.choices[0].message.content

# ---------------- INTERFACE ----------------

st.set_page_config(page_title="Pergunta Aí!", page_icon="🐾", layout="centered")

# Nome da criança (opcional, para boas-vindas)
nome = st.text_input("Meu nome é Kapibara, e o seu??")

# Imagem e título centralizado
st.markdown(f"""
<div style="display: flex; align-items: center; justify-content: center; gap: 20px; margin-top: 20px;">
    <img src="https://raw.githubusercontent.com/Lari-ia/pergunta-ai/main/kapibara.png" alt="Kapibara" width="130" style="border-radius: 12px;">
    <h1 style="color: #ffb703; font-size: 40px; margin: 0;">❓ Pergunta Aí!</h1>
</div>
""", unsafe_allow_html=True)

# Mensagem de boas-vindas
if nome:
    st.markdown(f"<p style='text-align: center; font-size: 18px;'>Oiê, {nome}! Eu sou a <strong>Kapibara</strong>, sua amiga. Vamos aprender muitas coisas legais juntos! 🌟🧠</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='text-align: center; font-size: 18px;'>Oiê! Eu sou a <strong>Kapibara</strong>, sua amiga. Vamos aprender muitas coisas legais juntos! 🌟🧠</p>", unsafe_allow_html=True)

# Campo de pergunta
st.markdown("### ✍️ Escreva sua pergunta aqui:")
pergunta = st.text_input(label="Digite sua pergunta:", label_visibility="collapsed")

# Se tiver pergunta
if pergunta:
    if pergunta_segura(pergunta):
        resposta = responder(pergunta, nome)
        st.success(resposta)
    else:
        st.warning("Hmm... essa pergunta não é legal de responder aqui. Que tal perguntar algo sobre animais ou o espaço? 🌈")

# Botão de curiosidade aleatória
if st.button("🎲 Surpreenda-me!"):
    st.info(random.choice(curiosidades))

# Rodapé
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Feito com carinho pela Kapibara e a Lari 💛</p>", unsafe_allow_html=True)
