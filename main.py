from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

messages = [
    {"role": "system", "content": "Eres un traductor experto. Responde únicamente con la traducción, sin explicaciones."}
]

while True:
    print("[1]. Traducir texto")
    print("[2]. Salir")
    opc = input("Seleccione una opcion: ")

    match(opc):
        case "1":

            idioma = input("Ingrese el idioma al cual desea traducir: ").strip()
            prompt = input("Ingrese texto a traducir: ").strip()

            messages.append({"role": "user", "content": f"Traduce a {idioma}: {prompt}"})

            r = client.chat.completions.create(
                model="deepseek-flash",
                messages=messages,
                max_tokens=500,
            )

            respuesta = r.choices[0].message.content

            messages.append({"role": "assistant", "content": respuesta})

            print(respuesta)
            print(f"Tokens de Entrada: {r.usage.prompt_tokens}")
            print(f"Tokens de Salida: {r.usage.completion_tokens}")
            print(f"Tokens gastados totales: {r.usage.total_tokens}")
        case "2":
            print("Saliendo de la aplicacion...")
            break
        case _:
            print("Opcion no valida. Vuelva a seleccionar una opcion") 





