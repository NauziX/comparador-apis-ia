# main.py


import os
from dotenv import load_dotenv
from apis.openai_api import obtener_respuesta_openai
from apis.ai21_api import obtener_respuesta_ai21


def obtener_entrada_usuario():
    prompt = input("Ingresa tu consulta: ")
    return prompt


def main():
    # Cargar las variables de entorno
    load_dotenv()

    consulta = obtener_entrada_usuario()

    # Obtener respuestas de las APIs
    respuesta_openai = obtener_respuesta_openai(consulta)
    respuesta_ai21 = obtener_respuesta_ai21(consulta)

    # Mostrar los resultados
    print("\nRespuesta de OpenAI:")
    print(respuesta_openai)
    print("\nRespuesta de ai21")
    print(respuesta_ai21)


if __name__ == "__main__":
    main()
