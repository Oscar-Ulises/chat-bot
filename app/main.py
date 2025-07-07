from fastapi import FastAPI
from pydantic import BaseModel
from app.openai_api import openai_chat
from app.memory import agregar_memoria, memoria

app = FastAPI()

prompt_del_sistema = {
    "role": "system",
    "content": "Eres un asistente profesional experto de la empresa de eventos deportivos ASDEPORTE. Responde de manera profesional."
}

class InputText(BaseModel):
    input_text: str

@app.post("/generate")
def generate(input: InputText):
    
    agregar_memoria("user", input.input_text)
    mensajes = [prompt_del_sistema] + memoria()
    respuesta = openai_chat(mensajes)
    agregar_memoria("assistant", respuesta)
    
    return {"response": respuesta}
