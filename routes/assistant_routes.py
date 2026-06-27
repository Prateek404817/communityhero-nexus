from flask import Blueprint, render_template, request, jsonify

from services.assistant_service import ask_assistant

bp = Blueprint("assistant", __name__)


@bp.route("/assistant")
def assistant():

    return render_template("assistant/assistant.html")


@bp.route("/assistant/chat", methods=["POST"])
def chat():

    message = request.json["message"]

    reply = ask_assistant(message)

    return jsonify({

        "reply": reply

    })