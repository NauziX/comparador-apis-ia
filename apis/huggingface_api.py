# apis/huggingface_api.py

import os
import requests


def obtener_respuesta_huggingface(prompt):
    try:
        API_URL = "https://api-inference.huggingface.co/models/gpt2"
        headers = {"Authorization": f"Bearer {
            os.getenv('HUGGINGFACE_API_TOKEN')}"}

        payload = {
            "inputs": prompt,
            "parameters": {"max_new_tokens": 150},
            "options": {"wait_for_model": True},
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, dict) and data.get("error"):
            return f"Error de Hugging Face: {data['error']}"

        texto_generado = data[0]["generated_text"]
        return texto_generado.strip()
    except Exception as e:
        return f"Error al obtener respuesta de Hugging Face: {e}"
