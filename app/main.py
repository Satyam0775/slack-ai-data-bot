from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler
from app.slack_handler import slack_app
from app.config import PORT

flask_app = Flask(__name__)
handler = SlackRequestHandler(slack_app)


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)


@flask_app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=PORT, debug=False)