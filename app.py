from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

SERIAL_VALIDO = "TELTEC-2026-RESET-9X2A"

@app.route("/")
def home():
    return "TELTEC LICENSE SERVER ONLINE"

from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin")
def admin():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM licencas")

    licencas = cursor.fetchall()

    return render_template("admin.html", licencas=licencas)

@app.route("/ativar", methods=["POST"])
def ativar():

    dados = request.json

    serial = dados["serial"]
    hwid = dados["hwid"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM licencas WHERE serial=?",
        (serial,)
    )

    licenca = cursor.fetchone()

    if not licenca:
        return jsonify({
            "mensagem": "Serial inválido"
        })

    hwid_salvo = licenca[2]

    # já ativado em outro pc
    if hwid_salvo and hwid_salvo != hwid:
        return jsonify({
            "mensagem": "Serial já usado em outro computador"
        })

    # ativa
    cursor.execute("""
        UPDATE licencas
        SET hwid=?, ativado=1
        WHERE serial=?
    """, (hwid, serial))

    conn.commit()

    return jsonify({
        "mensagem": "Software ativado"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)