from dotenv import load_dotenv
import websocket
import json
import os
import requests

load_dotenv()

ntfy_host = os.environ["NTFY_HOST"]
gotify_host = os.environ['GOTIFY_HOST']
gotify_token = os.environ['GOTIFY_TOKEN']


def on_message(ws, message):
    msg = json.loads(message)
    querystring = {"title": msg['title'], "message": msg['message']}
    headers = {
        "Priority": "default",
    }
    response = requests.request(
        "POST", ntfy_host, headers=headers, params=querystring)
    print("websocket: " + message + "\n" + "Ntfy: " + response.text)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("Connection closed")


def on_open(ws):
    print("Opened Gotify websocket connection")


if __name__ == "__main__":
    wsapp = websocket.WebSocketApp("wss://" + str(gotify_host) + "/stream", header={"X-Gotify-Key": str(gotify_token)},
                                   on_open=on_open,
                                   on_message=on_message,
                                   on_error=on_error,
                                   on_close=on_close)
    wsapp.run_forever()
