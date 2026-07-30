import asyncio

from langchain_openai import ChatOpenAI
# from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config import OPENROUTER_API_KEY


model = ChatOpenAI(
    model="google/gemini-2.5-flash",
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    temperature=0,
    max_tokens=2000,
)
parser = StrOutputParser()

capital_chain = (
    ChatPromptTemplate.from_template(
        "Cual y porque es la capital de {pais}?"
    )
    | model
    | parser
)

regular_extension_chain = (
    ChatPromptTemplate.from_template(
        "Resume el siguiente texto en 10 oraciones tomando lo mas importante: {texto}"
    )
    | model
    | parser
)

full_chain = capital_chain | (lambda text: {"texto": text}) | regular_extension_chain

async def main():
    resultado = await full_chain.ainvoke({"pais": "Argentina"})
    print(resultado)
    
if __name__ == "__main__":
    asyncio.run(main())