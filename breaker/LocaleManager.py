from breaker.LoggerManager import logger
from breaker.Colors import grey, reset
from breaker.ConfigManager import config_manager
import tomllib
import os

# 获取配置
cfg = config_manager.get_cfg()

class LocaleManager:
    locale: dict[str, dict]
    def __init__(self):
        logger.info(f"{grey}正在初始化文本管理模块...{reset}")
        self.locale_name = cfg.core.locale
        self.read_locale()
    
    def set_locale(self, locale_name: str):
        self.locale_name = locale_name
        self.read_locale()
    
    def read_locale(self):
        try:
            file_path = f"./locale/{self.locale_name}/locale.toml"
            with open(file_path, 'r', encoding="utf-8") as file:
                locale: dict[str, dict] = tomllib.loads(file.read())
                self.locale = locale
                file.close()
        except Exception as e:
            raise e
    
    def get_locale(self):
        return self.locale


locale_manager = LocaleManager()
default_text = "出现了预料之外的错误，请联系管理员。"