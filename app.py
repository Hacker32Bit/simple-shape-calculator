import json
import logging
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from shapes import calculate_area, ShapeFactory, Triangle

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    logging.info("Client connected via WebSocket")

    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            try:
                message = json.loads(data)
                shape_type = message.get("type")
                params = message.get("params", [])

                if not shape_type:
                    await websocket.send_json({"error": "Missing 'type' field"})
                    continue

                # Create shape and calculate area
                shape = ShapeFactory.create_shape(shape_type, *params)
                result = {"type": shape_type, "area": shape.area()}

                # Check if triangle is right
                if isinstance(shape, Triangle):
                    result["is_right"] = shape.is_right()

                await websocket.send_json(result)

            except Exception as e:
                await websocket.send_json({"error": str(e)})

    except WebSocketDisconnect:
        logging.info("Client disconnected")
