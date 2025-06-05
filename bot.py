from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import BotCommand
from config import BOT_TOKEN
import handlers
import scheduler

application = ApplicationBuilder().token(BOT_TOKEN).build()

application.add_handler(CommandHandler("add", handlers.add))
application.add_handler(CommandHandler("list", handlers.list_all))
application.add_handler(CommandHandler("delete", handlers.delete))
application.add_handler(CommandHandler("edit", handlers.edit))

scheduler.application = application
scheduler.start_scheduler()

# 添加命令说明
async def set_bot_commands(app):
    commands = [
        BotCommand("add", "添加任务，如 /add 服务名 30d / 2w / 6m / 2025-12-01"),
        BotCommand("list", "查看你所有的续费任务"),
        BotCommand("delete", "删除一个任务（格式：/delete 任务ID）"),
        BotCommand("edit", "编辑任务字段（格式：/edit 任务ID 字段 新值）")
    ]
    await app.bot.set_my_commands(commands)

if __name__ == "__main__":
    import asyncio
    asyncio.run(set_bot_commands(application))
    application.run_polling()
