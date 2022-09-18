from pyrogram import Client
from apscheduler.schedulers.background import BackgroundScheduler
import os


api_id = os.getenv("API_ID")
api_hash = os.getenv('API_HASH')

app = Client("my_account", api_id=api_id, api_hash=api_hash)
TEXT_MESSAGE = "\n".join(
    [
        "**Приветствуем!**",
        "Проводим ремонт блоков питания/хэш плат для Asic майнеров любой сложности по оптимальным ценам.",
        "Находимся мы в г. Чехов, также майнер можно отправить в CDEK, в любую другую службу доставки или встретиться у метро Аннино.",
        "Готовы ответить на любой ваш вопрос!",
    ])
INTERVAL_SEND_MESSAGE = 3600


def job():
    app.send_photo("hrbehshshs", "reklama.jpg") and app.send_message("hrbehshshs", TEXT_MESSAGE)
    app.send_photo("Emcd_market", "reklama.jpg") and app.send_message("Emcd_market", TEXT_MESSAGE)
    app.send_photo("mining_resell", "reklama.jpg")


scheduler = BackgroundScheduler()
scheduler.add_job(job, "interval", seconds=INTERVAL_SEND_MESSAGE)

scheduler.start()
app.run()

app.stop()
