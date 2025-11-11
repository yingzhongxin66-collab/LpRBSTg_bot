# main.py
import argparse
import asyncio
import logging
from telethon import TelegramClient
from src.config import BotConfig
from src.listener import Listener

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

async def start_bot():
    logging.info("🚀 Telegram 同步脚本启动中...")
    config = BotConfig()

    client = TelegramClient(config.SESSION_NAME, config.API_ID, config.API_HASH)
    await client.start()
    logging.info("🤖 Bot 已连接并登录成功。")
    logging.info(f"💡 当前心跳间隔：{config.HEARTBEAT_INTERVAL}s")
    logging.info(f"💤 转发延时：{config.FORWARD_DELAY}s")

    listener = Listener(client, config)
    try:
        await listener.start()
    except KeyboardInterrupt:
        logging.info("🛑 手动中断，Bot 已退出。")
    except Exception as e:
        logging.error(f"❌ 程序异常退出：{e}")
    finally:
        await client.disconnect()
        logging.info("✅ Bot 已正常退出。")
        logging.info("🧹 清理完成，终端即将关闭。")

if __name__ == "__main__":
    asyncio.run(start_bot())
