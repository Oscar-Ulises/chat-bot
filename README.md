# 🏃 Asistente Virtual ASDEPORTE

Este proyecto implementa un asistente profesional para la empresa **ASDEPORTE**, especializada en organización de eventos deportivos. 

---

## 🚀 Tecnologías utilizadas

- FastAPI
- OpenAI API
- Docker
- Uvicorn
- Python 3.10

---

## 📁 Estructura del proyecto

```
.
├── app/
│   ├── main.py
│   ├── memory.py
│   └── openai_api.py
├── cli/
│   ├── chat_cli.py
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

---

## ▶️ Cómo ejecutar

### Localmente con Uvicorn

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Luego abre tu navegador en: [http://localhost:8000/docs](http://localhost:8000/docs)

## 📥 Endpoint:

### `POST /generate`

**Input JSON:**

```json
{
  "input_text": "¿Qué hace AsDeporte?"
}
```

**Output JSON:**

```json
{
  "response": "Es un empresa que se especializa en la organización de eventos deportivos..."
}
```

---

## 🔐 Variables de entorno

Modifica la API de OpenAI que se encuentra en el archivo '.env':

```
OPENAI_API_KEY='tu_clave'
```

---

## 📌 Licencia

Uso interno de ASDEPORTE. No distribuir sin autorización.
