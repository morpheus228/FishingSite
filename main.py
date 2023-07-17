from fastapi import FastAPI, Request

app = FastAPI(title="Sonic-Shop")

@app.get('/')
async def add_telegram_user(request: Request):
    client_host = request.client.host
    return {"client_host": client_host}