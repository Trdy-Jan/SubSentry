# 🔔 SubSentry - Telegram 续费提醒机器人

SubSentry 是一个基于 Python 的 Telegram 机器人，帮助你管理各种服务的续费提醒。支持按天、按周、按月或指定日期添加任务，还支持每日提醒、周期性循环提醒等高级功能。

---

## 🚀 功能特性

- ✅ 支持多种时间格式添加任务：`30d`、`2w`、`6m` 或 `2025-12-01`
- ✅ 支持每日提醒直到续费
- ✅ 支持每 N 天重复提醒（如每 180 天）
- ✅ 支持添加 / 删除 / 编辑任务
- ✅ 支持多用户使用（通过 Telegram user_id 绑定）
- ✅ 启动时自动设置命令菜单（无需手动配置）

---

## 🧩 示例指令

```bash
/add Netflix 30d                # 30 天后提醒续费
/add iCloud 2025-12-01         # 指定日期提醒
/edit 1 persistent_reminder 1  # 开启每日持续提醒
/edit 1 repeat_days 180        # 设置每 180 天提醒一次
/delete 1                      # 删除任务
/list                          # 查看所有任务
