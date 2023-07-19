from aiogram import Bot
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Sonic-Shop")

bot = Bot(token='6256199322:AAFLFp7LVBy7PxPeyN5ylGXonwcZ5p-3HHk')

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get('/')
async def start(request: Request):
    host = str(request.client.host)
    await bot.send_message(587247376, str(request.client.host))
    print(host)
    return templates.TemplateResponse("index.html", {"request": request})
