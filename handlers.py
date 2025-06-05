from telegram import Update
from telegram.ext import ContextTypes
from db import add_task, list_tasks, delete_task, edit_task
from datetime import datetime, timedelta
import re


async def list_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tasks = list_tasks(update.effective_user.id)
    if not tasks:
        await update.message.reply_text("无任务")
        return
    msg = "\n".join([f"#{t[0]} - {t[2]} 于 {t[3]} 续费" for t in tasks])
    await update.message.reply_text(msg)


async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("使用方法：/delete <任务ID>")
        return
    delete_task(context.args[0])
    await update.message.reply_text("任务已删除")


async def edit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 3:
        await update.message.reply_text("使用方法：/edit <任务ID> <字段> <新值>")
        return
    success = edit_task(context.args[0], context.args[1], ' '.join(context.args[2:]))
    await update.message.reply_text("任务已更新" if success else "更新失败")


def parse_due_date(raw: str) -> str:
    today = datetime.today()
    if re.match(r'^\d{4}-\d{2}-\d{2}$', raw):  # 绝对日期
        return raw
    elif raw.endswith('d'):
        days = int(raw[:-1])
        return (today + timedelta(days=days)).strftime('%Y-%m-%d')
    elif raw.endswith('w'):
        weeks = int(raw[:-1])
        return (today + timedelta(weeks=weeks)).strftime('%Y-%m-%d')
    elif raw.endswith('m'):
        months = int(raw[:-1])
        # 简单处理，按 30 天算一个月
        return (today + timedelta(days=30 * months)).strftime('%Y-%m-%d')
    else:
        raise ValueError("无效时间格式")


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("使用方法：/add 服务名 时间（如 30d, 2w, 6m 或 2025-12-01）")
        return
    service, raw_time = context.args[0], context.args[1]
    try:
        due = parse_due_date(raw_time)
    except:
        await update.message.reply_text("时间格式错误。支持格式：30d, 4w, 6m 或 YYYY-MM-DD")
        return
    add_task(update.effective_user.id, service, due)
    await update.message.reply_text(f"任务已添加：{service}，续费日期为 {due}")
