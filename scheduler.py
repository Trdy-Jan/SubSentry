from apscheduler.schedulers.background import BackgroundScheduler
from db import get_tasks_due_in_days, get_persistent_tasks, get_repeat_tasks, update_repeat_task
from datetime import datetime, timedelta

application = None  # 由 bot.py 注入

def notify(task, text):
    application.bot.send_message(chat_id=task[1], text=text)

def check_tasks():
    today_str = datetime.today().strftime('%Y-%m-%d')

    for task in get_tasks_due_in_days(3):
        notify(task, f"🔔【{task[2]}】将在 3 天后续费（{task[3]}）")

    for task in get_persistent_tasks(today_str):
        notify(task, f"📌【{task[2]}】将在 {task[3]} 续费，请注意。")

    for task in get_repeat_tasks(today_str):
        notify(task, f"🔁【{task[2]}】定期提醒：今天是续费日（{task[3]}）")
        new_date = (datetime.strptime(task[3], '%Y-%m-%d') + timedelta(days=task[5])).strftime('%Y-%m-%d')
        update_repeat_task(task[0], new_date)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_tasks, 'interval', hours=24)
    scheduler.start()
