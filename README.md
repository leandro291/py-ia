# py-ia

Traductor por consola a cualquier idioma usando la API de DeepSeek. Devuelve la respuesta en JSON, recuerda la conversación y muestra los tokens gastados.

## Características

- Traduce a cualquier idioma que elijas.
- Respuesta estructurada en JSON (traducción, idioma original, alternativas y nota).
- Memoria de conversación: el modelo recibe el historial completo.
- Contador de tokens de entrada, salida y totales por cada consulta.

## Requisitos

- Python 3.10+ (usa `match`)
- Una clave de API de [DeepSeek](https://platform.deepseek.com)

## Instalación

```bash
python -m venv .venv && source .venv/bin/activate
pip install openai python-dotenv
cp .env.example .env   # y poné tu clave en DEEPSEEK_API_KEY
```

## Uso

```bash
python main.py
```

```text
[1]. Traducir texto
[2]. Salir
Seleccione una opcion: 1
Ingrese el idioma al cual desea traducir: ingles
Ingrese texto a traducir: Hola, como estas?
{'traduccion': 'Hello, how are you?', 'idioma_original': 'español', 'alternativas': ['Hi, how are you?', 'Hello, how are you doing?'], 'nota': 'Traducción estándar y coloquial.'}
Tokens de Entrada: 87
Tokens de Salida: 60
Tokens gastados totales: 147
```

## Formato de respuesta

| Campo | Descripción |
|---|---|
| `traduccion` | Texto traducido |
| `idioma_original` | Idioma detectado del texto de entrada |
| `alternativas` | Otras traducciones posibles |
| `nota` | Comentario sobre la traducción |

## Configuración

| Variable | Descripción |
|---|---|
| `DEEPSEEK_API_KEY` | Clave de API de DeepSeek (archivo `.env`, ignorado por git) |
