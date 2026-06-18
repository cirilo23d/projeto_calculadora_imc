import streamlit as st

#----------------------------------------------SIDEBAR
st.sidebar.title("Calculadora de IMC")
st.sidebar.image("imc.png")

#----------------------------------------------BODY
st.title("Calculadora de IMC")


peso = st.text_input("Digite seu peso: ")
altura = st.text_input("Digite sua altura: ")

if st.button("Calcuar"):
    peso = float(peso)
    altura = float(altura)

    imc = peso / (altura ** 2)

    if imc < 18.5:
        class_imc = "abaixo_peso" 
        st.warning(f"Seu IMC é {imc:.1f}! Você está abaixo do peso 😥")

    elif imc < 24.9:
        class_imc = "peso_saudavel"
        st.success(f"Seu IMC é {imc:.1f} Você está com o peso saudável! 😄")

    elif imc < 29.9:
         class_imc = "sobrepeso"
         st.warning(f"Seu IMC é {imc:.1f}! Você está com sobrepeso 😞")

    elif imc < 34.9:
        class_imc = "obesidade1"
        st.warning(f"Seu IMC é {imc:.1f}! Você está Obesidade Grau 1 😥")

    elif imc < 39.9:
        class_imc = "obesidade2"
        st.error(f"Seu IMC é {imc:.1f}! Você está Obesidade Grau 2 😥")

    else:
        class_imc = "obesidade3"
        st.error(f"Seu IMC é {imc:.1f}! Você está Obesidade Grau 3 🐘")

    st.markdown("---")
    st.image(f"{class_imc}.png")


    with open(f"{class_imc}.txt", "r", encoding="utf-8") as f:
        texto = f.read()

    st.markdown(texto)        