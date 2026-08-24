import streamlit as st
import requests

st.set_page_config(page_title="Pokédex", page_icon="⚡")

# Dicionário obrigatório
tipos = {
    "grass": "🌿 Planta",
    "fire": "🔥 Fogo",
    "water": "💧 Água",
    "electric": "⚡ Elétrico",
    "psychic": "🔮 Psíquico",
    "fighting": "🥊 Lutador",
    "normal": "⚪ Normal",
    "ghost": "👻 Fantasma",
    "dragon": "🐉 Dragão"
}

def buscar_dados(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        return None

    return resposta.json()

def formatar_resultado(dados):
    return {
        "nome": dados["name"].title(),
        "altura": dados["height"] / 10,
        "peso": dados["weight"] / 10,
        "tipo": tipos.get(
            dados["types"][0]["type"]["name"],
            dados["types"][0]["type"]["name"]
        ),
        "imagem": dados["sprites"]["front_default"]
    }

st.title("⚡ Pokédex")
nome = st.text_input("Digite o nome do Pokémon")

if st.button("Buscar"):
    dados = buscar_dados(nome)

    if dados is None:
        st.error("Pokémon não encontrado!")
    else:
        p = formatar_resultado(dados)

        st.image(p["imagem"], width=180)
        st.subheader(p["nome"])
        st.write(f"**Tipo:** {p['tipo']}")
        st.write(f"**Altura:** {p['altura']} m")
        st.write(f"**Peso:** {p['peso']} kg")