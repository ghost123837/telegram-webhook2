import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Vervang dit met jouw gegevens
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    alias = data.get("alias")
    soort = data.get("soort")
    hoeveelheid = data.get("hoeveelheid")
    prijs = data.get("prijs")

    message = f"""
📦 Nieuwe bestelling:
👤 Alias: {alias}
🌿 Soort: {soort}
⚖️ Hoeveelheid: {hoeveelheid}
💶 Prijs: €{prijs}
"""
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": message}
    )
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
