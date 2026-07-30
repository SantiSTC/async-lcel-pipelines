# Async LCEL Pipelines

Ejemplos simples de pipelines asíncronos utilizando **LangChain Expression Language (LCEL)**.

## Características

- Ejecución asíncrona con `asyncio`.
- Composición de prompts mediante `ChatPromptTemplate`.
- Encadenamiento de componentes utilizando el operador `|` de LCEL.
- Procesamiento de la salida con `StrOutputParser`.
- Ejecución secuencial de múltiples cadenas.
- Integración con OpenRouter mediante su API compatible con OpenAI.

## Instalación

Instalá las dependencias necesarias:

```bash
pip install langchain langchain-openai python-dotenv
```

## Variables de entorno

Creá un archivo `.env` a partir de `.env.example` y agregá tu clave de OpenRouter.

Ejemplo:

```env
OPENROUTER_API_KEY=<TU_OPENROUTER_API_KEY>
```

## Ejecución

```bash
python ejercicio_lcel.py
```

## ¿Qué demuestra este proyecto?

- Creación de cadenas con LCEL.
- Encadenamiento de múltiples prompts.
- Paso de la salida de una cadena como entrada de otra.
- Ejecución asíncrona utilizando `ainvoke()`.

---

## Autor

Desarrollado por **Santiago Iannello**.
