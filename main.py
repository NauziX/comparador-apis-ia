# main.py

from dotenv import load_dotenv
from apis.openai_api import obtener_respuesta_openai
from apis.huggingface_api import obtener_respuesta_huggingface


def obtener_entrada_usuario():
    prompt = input("Ingresa tu consulta: ")
    return prompt


def main():
    # Cargar las variables de entorno
    load_dotenv()

    consulta = obtener_entrada_usuario()

    # Obtener respuestas de las APIs
    respuesta_openai = obtener_respuesta_openai(consulta)
    respuesta_huggingface = obtener_respuesta_huggingface(consulta)

    # Mostrar los resultados
    print("\nRespuesta de OpenAI:")
    print(respuesta_openai)
    print("\nRespuesta de Hugging Face:")
    print(respuesta_huggingface)


if __name__ == "__main__":
    main()
