from datetime import datetime, timezone, timedelta
import os

import telebot
from celery import shared_task

from tracker.models import Habit

API_KEY = os.getenv('TELEGRAM_BOT_API')


@shared_task
def reminder_habits():
    now = datetime.now(tz=timezone.utc)

    bot = telebot.TeleBot(API_KEY)

    habits = Habit.objects.filter(time__lte=now)

    for habit in habits:
        chat_id = habit.author.telegram_id
        message = f'В {habit.time.strftime("%H:%M")} нужно {habit.action} в {habit.place}'

        try:
            response = bot.send_message(chat_id=chat_id, text=message)

            for i in range(7):
                day = i + 1
                if habit.periodisity == day:
                    habit.time += timedelta(days=day)
                    break
            return response

        except Exception as e:
            print(e)

        finally:
            habit.save()
