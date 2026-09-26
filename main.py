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

            idioma = input("Ingrese el idioma al cual desea traducir: ").strip()
            prompt = input("Ingrese texto a traducir: ").strip()

            r = client.chat.completions.create(
                model="deepseek-flash",
                messages=[
                        {
                            "role": "system", 
                            "content": f"Eres un traductor experto. Traduce al {idioma} el texto que te envíe el usuario. Responde únicamente con la traducción, sin explicaciones."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                max_tokens=500,
            )

            print(r.choices[0].message.content)
            # print(r.model_dump_json(indent=2))
        case "2":
            print("Saliendo de la aplicacion...")
            break
        case _:
            print("Opcion no valida. Vuelva a seleccionar una opcion") 





