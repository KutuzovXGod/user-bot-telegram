from pyrogram import Client, filters
from apscheduler.schedulers.background import BackgroundScheduler



api_id = 10728028
api_hash = "f0294cbc5ff01e1c9242fbe15a0d2f94"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

def job():
    spam = "Приветствуем! Проводим ремонт блоков питания/хэш плат для Asic майнеров любой сложности по оптимальным ценамНаходимся мы в г.Чехов, также майнер можно отправить в CDEK, в любую другу службу доставки или встретиться у метро Анино.Готовы ответить на любой ваш вопрос!"
    app.send_photo("hrbehshshs", "reklama.jpg") and app.send_message("hrbehshshs", spam)
    app.send_photo("Emcd_market", "reklama.jpg") and app.send_message("Emcd_market", spam)
    app.send_photo("mining_resell", "reklama.jpg")


scheduler = BackgroundScheduler()
scheduler.add_job(job, "interval", seconds=3600)

scheduler.start()
app.run()


app.stop()


