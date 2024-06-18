import os
import shutil
import tomllib

class ConfigManager:
    def __init__(self) -> None:
        if not os.path.exists("config.toml"):
            # 如果配置文件不存在，则新建一个配置文件
            shutil.copy("./static/config.example.toml", "config.toml")


config_manager = ConfigManager()