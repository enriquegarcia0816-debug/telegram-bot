from telegram import Bot
from telegram.ext import Application
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from zoneinfo import ZoneInfo
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

scheduler = AsyncIOScheduler(timezone=ZoneInfo("America/El_Salvador"))

async def enviar_recordatorio_ingreso():
    await bot.send_message(
        chat_id=CHAT_ID,
        text="""🌞 Buenos días equipo.

📸 Favor enviar su foto de ingreso.
📍 Compartan su ubicación en tiempo real.

¡Mucho éxito en las ventas! 💙"""
    )

async def enviar_recordatorio_9():
    await bot.send_message(
        chat_id=CHAT_ID,
        text="""⏰ Recordatorio.

Si aún no has enviado tu foto y ubicación, por favor hazlo lo antes posible."""
    )

async def enviar_reporte():
    await bot.send_message(
        chat_id=CHAT_ID,
        text="""📊 Equipo, favor enviar el reporte de ventas del día.

✅ Activaciones
✅ Portabilidades
✅ Smartphones
✅ Smart Financiados
✅ PaqueTigos

¡Gracias por su esfuerzo! 💪"""
    )

async def main():
    scheduler.add_job(enviar_recordatorio_ingreso, "cron", day_of_week="mon-fri", hour=8, minute=0)
    scheduler.add_job(enviar_recordatorio_9, "cron", day_of_week="mon-fri", hour=9, minute=0)
    scheduler.add_job(enviar_reporte, "cron", day_of_week="mon-fri", hour=18, minute=0)

    scheduler.start()

    app = Application.builder().token(BOT_TOKEN).build()

    print("Bot iniciado correctamente...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
