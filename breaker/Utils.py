import os
import shutil
from breaker.LoggerManager import logger
from breaker.ConfigManager import config_manager
from breaker.Colors import grey, reset

cfg = config_manager.get_cfg()


def gen_env_file():
    logger.info(f"{grey}生成.env文件。")
    with open(".env", "w+", encoding="utf-8") as env:
        env_file = \
f"""HOST={cfg.onebot.onebot_host}
PORT={cfg.onebot.onebot_port}
COMMAND_START=[""]
COMMAND_SEP=["."]
DRIVER=~fastapi+~httpx+~websockets
"""
        env.write(env_file)
        env.close()