# 🧠 IA Image Generator - Flask + Replicate

Este proyecto es una API creada con **Python y Flask** que genera imágenes mediante **inteligencia artificial** utilizando el modelo `flux-schnell` de [Replicate](https://replicate.com/black-forest-labs/flux-schnell).

El usuario envía un *prompt* (descripción en texto), y el servidor devuelve una imagen generada por IA, guardada localmente.  
Perfecto como base para una red social creativa, una galería generativa o simplemente para aprender a trabajar con modelos de texto a imagen.

---

## ⚙️ ¿Qué hace esta API?

- Recibe un `prompt` en una petición POST.
- Llama a la API de Replicate usando el modelo `flux-schnell`.
- Guarda la imagen generada en la carpeta `/static`.
- Devuelve la URL de la imagen generada.

---

## 🚀 Tecnologías

- Python 3.x  
- Flask  
- Replicate SDK  
- python-dotenv

---

## 🧠 Autor

Desarrollado por **Pablo Vincenzo Vasta**  
Este proyecto forma parte de su portfolio como desarrollador web y apasionado de la IA 🤖🎨
---