from text import Text
from flask import Flask
from flask import request

app = Flask(__name__)

def validate_payload(payload, fields):
    errors = []
    for field in fields:
        if field not in payload:
            errors.append(f"Field '{field}' is required")
    return None if len(errors) == 0 else {"errors": errors}

@app.route('/evaluate', methods=['POST'])
def evaluate():
    payload = request.json

    valid = validate_payload(payload, ["originText", "toCompare"])
    if valid is not None:
        return valid, 400

    text = Text(payload['originText'])
    return {"textId": text.evaluate(payload['toCompare'])}


@app.route('/signature', methods=['POST'])
def signature():
    payload = request.json

    valid = validate_payload(payload, ["text"])
    if valid is not None:
        return valid, 400

    text = Text(payload['text'])
    return {"signature": text.signature.__dict__}