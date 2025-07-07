import requests

print("Chat ASDEPORTE (Ctrl+C para salir)")
while True:
    try:
        user_input = input("Tú: ")
        res = requests.post("http://localhost:8000/generate", json={"input_text": user_input})
        print("Bot:", res.json()["response"])
    except KeyboardInterrupt:
        break
