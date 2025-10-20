1. Clone
2. Setup python environment and install packages from `requirements.txt`
3. Run using uvicorn `uvicorn app:app --reload`
4. Connect to web-socket by `ws://localhost:8000/ws` url.
5. Json examples for query:<br>
```{"type": "circle", "params": [5]}```<br>
```{"type": "triangle", "params": [3, 4, 5]}```
