from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
import replicate
import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder = "static")
CORS(app)
REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')
replicate_client = replicate.Client(api_token = REPLICATE_API_TOKEN)

@app.route('/generate', methods=["POST"])
def generate_image():
    data = request.json
    prompt = data.get("prompt")
    style = data.get("style")

    style_descriptions = {
    "realista": "realismo extremo, iluminación natural, fondo coherente, ultra detalle, 8k",
    "anime": "anime style, cel shading, fondo tipo Studio Ghibli, colores planos pero vivos",
    "pixel": "pixel art, 8-bit, estética retro, paleta limitada, fondo simple tipo videojuego"
    }

    final_prompt = ""
    if style in style_descriptions:
        final_prompt = f"{prompt}, {style_descriptions[style]}"
    print(style)
    print(style_descriptions[style])
    print(f"Prompt final: {final_prompt}")
 
    if not prompt:
        return jsonify({
            "error": "Prompt is required"
        }), 400
    try:
        output = replicate_client.run(
            "black-forest-labs/flux-schnell",
            input = {"prompt" : final_prompt},
        )
        filename = f"output_{int(time.time())}.png"
        filepath = os.path.join("static", filename)
        os.makedirs("static", exist_ok=True)

        with open(filepath, "wb") as file:
            file.write(output[0].read())

            return jsonify({
                "url": url_for("static", filename=filename, _external=True),
            })
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
        
if __name__ == "__main__":
    print("Tu servidor esta corriendo en el http://localhost:5000")
    app.run(debug=True)

    