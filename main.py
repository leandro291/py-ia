from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)


while True:
    print("[1]. Traducir texto")
    print("[2]. Salir")
    opc = input("Seleccione una opcion: ")

    match(opc):
        case "1":

            texto = input("Ingrese texto a traducir: ").strip()

            r = client.chat.completions.create(
                model="deepseek-flash",
                messages=[
                        {
                            "role": "system", 
                            "content": "Eres un traductor experto. Traduce al inglés el texto que te envíe el usuario. Responde únicamente con la traducción, sin explicaciones."
                        },
                        {
                            "role": "user",
                            "content": texto
                        }
                    ],
                max_tokens=500,
            )

            print(r.choices[0].message.content)
        case "2":
            print("Saliendo de la aplicacion...")
            break
        case _:
            print("Opcion no valida. Vuelva a seleccionar una opcion") 





