# apis/openai_api.py

import os
import openai


def obtener_respuesta_openai(prompt):
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Puedes usar "gpt-4" si tienes acceso
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150,
            n=1,
            stop=None,
        )

        texto_generado = response.choices[0].message.content.strip()
        return texto_generado

    except Exception as e:
        return f"Error al obtener respuesta de OpenAI:\n\n{e}"
