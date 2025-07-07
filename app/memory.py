chat_memoria = []

def agregar_memoria(role, content):
    
    chat_memoria.append({"role": role, "content": content})
    
    if len(chat_memoria) > 8:
        del chat_memoria[0:2]

def memoria():
    return chat_memoria
