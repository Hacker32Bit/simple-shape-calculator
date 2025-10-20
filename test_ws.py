import json
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_websocket_circle():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text(json.dumps({"type": "circle", "params": [2]}))
        response = websocket.receive_json()
        assert response["type"] == "circle"
        assert round(response["area"], 5) == 12.56637


def test_websocket_triangle_right():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text(json.dumps({"type": "triangle", "params": [3, 4, 5]}))
        response = websocket.receive_json()
        assert response["type"] == "triangle"
        assert round(response["area"], 2) == 6.00
        assert response["is_right"] is True


def test_websocket_invalid_shape():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text(json.dumps({"type": "hexagon", "params": [1, 2, 3]}))
        response = websocket.receive_json()
        assert "error" in response
