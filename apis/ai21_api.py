import os
import requests
from dotenv import load_dotenv
import logging

# Configurar el nivel de registro
logging.basicConfig(level=logging.ERROR)

# Cargar las variables de entorno desde el archivo .env
load_dotenv()


def obtener_respuesta_ai21(prompt):
    """
    Función para obtener una respuesta de la API de AI21 Studio basada en un prompt dado.

    Args:
        prompt (str): Texto de entrada para generar la continuación.

    Returns:
        str: Texto generado por la API de AI21 o un mensaje de error.
    """
    try:
        # Obtener la clave de API de AI21 desde las variables de entorno
        ai21_api_key = os.getenv('AI21_API_KEY')
        if not ai21_api_key:
            logging.error("La clave de API de AI21 no está configurada.")
            return "Error: La clave de API de AI21 no está configurada."

        # Configurar los encabezados de la solicitud HTTP
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {ai21_api_key}'
        }

        # Crear el payload con los parámetros de la solicitud
        payload = {
            "prompt": prompt,
            "numResults": 1,
            "maxTokens": 150,
            "temperature": 0.7,
            # Puedes añadir más parámetros aquí si lo deseas
        }

        # Realizar la solicitud POST a la API de AI21 con un tiempo de espera (timeout)
        response = requests.post(
            "https://api.ai21.com/studio/v1/j2-large/complete",
            headers=headers,
            json=payload,
            timeout=10  # Tiempo de espera en segundos
        )

        # Comprobar si la solicitud fue exitosa (código de estado 200)
        response.raise_for_status()

        # Procesar la respuesta JSON
        data = response.json()

        # Verificar que la respuesta contiene los datos esperados
        completions = data.get('completions')
        if not completions or len(completions) == 0:
            logging.error("La respuesta de AI21 no contiene 'completions'.")
            return "Error: La respuesta de AI21 no contiene datos."

        # Extraer el texto generado de la respuesta
        texto_generado = completions[0]['data']['text'].strip()

        return texto_generado

    except requests.exceptions.HTTPError as http_err:
        # Manejar errores HTTP específicos
        logging.error(f"Error HTTP al obtener respuesta de AI21: {http_err}")
        return "Error al comunicarse con el servicio de AI21."
    except requests.exceptions.Timeout:
        # Manejar el caso de que la solicitud exceda el tiempo de espera
        logging.error("La solicitud a AI21 ha excedido el tiempo de espera.")
        return "Error: La solicitud ha excedido el tiempo de espera. Por favor, inténtalo de nuevo."
    except Exception as e:
        # Manejar cualquier otra excepción
        logging.error(f"Error al obtener respuesta de AI21: {e}")
        return "Ha ocurrido un error al obtener la respuesta de AI21. Por favor, inténtalo de nuevo más tarde."
