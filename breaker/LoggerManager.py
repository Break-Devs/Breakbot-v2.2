import sys

import nonebot
from breaker.Colors import gradient_text, reset, grey, light_cyan
from nonebot import logger
from nonebot.log import default_format, default_filter
from nonebot.log import logger_id

class LoggerManager:
    def __init__(self) -> None:
        
        # 移除 NoneBot 默认的日志处理器
        logger.remove(logger_id)
        # 添加新的日志处理器
        logger.add(
            sys.stdout,
            level=0,
            diagnose=True,
            format="<g>{time:MM-DD HH:mm:ss}</g> [<lvl>{level}</lvl>] || {message}",
            filter=default_filter
        )
        logger.info(f"{grey}欢迎使用 {gradient_text("Break Bot v2.2", "F83600", "F9D423")} {grey}| {gradient_text("Mujirushi!!!", "E0C3FC", "FEF0F0", "8EC5FC")}{grey}.{reset}")
        

logger_manager = LoggerManager()
logger = nonebot.logger