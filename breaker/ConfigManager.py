import os
import select
import shutil
from tkinter import NO
import tomllib
from breaker.LoggerManager import logger
from breaker.Colors import reset, grey
from dataclasses import dataclass


@dataclass
class CoreConf:
    bot_name: str
    version_name: str
    locale: str


@dataclass
class OnebotConf:
    onebot_host: str
    onebot_port: int


@dataclass
class DatabaseConf:
    roles_db_name: str
    db_type: int
    mysql_host: str
    mysql_port: int
    mysql_username: str
    mysql_password: str


@dataclass
class NetworkConf:
    enable_mai_backend: bool
    mai_backend_url: str
    mai_backend_token: str
    enable_break_api: bool
    break_api_host: str
    break_api_port: int


@dataclass
class Config:
    core: CoreConf
    onebot: OnebotConf
    database: DatabaseConf
    network: NetworkConf

class ConfigManager:
    def __init__(self) -> None:
        logger.info(f"{grey}正在初始化配置管理模块...{reset}")
        if not os.path.exists("config.toml"):
            # 如果配置文件不存在，则新建一个配置文件
            logger.warning("未找到config.toml配置文件，将新建配置文件。")
            shutil.copy("./static/config.example.toml", "config.toml")
        # 读取配置文件
        self.config = self.read_config()
    
    def read_config(self):
        """读取配置文件
        """
        try:
            with open("config.toml", "r", encoding="utf-8") as file:
                config_data = tomllib.loads(file.read())
                core_conf = CoreConf(
                    bot_name=config_data["core"]["bot_name"],
                    version_name=config_data["core"]["version_name"],
                    locale=config_data["core"]["locale"]
                )
                onebot_conf = OnebotConf(
                    onebot_host=config_data["onebot"]["onebot_host"],
                    onebot_port=config_data["onebot"]["onebot_port"]
                )
                database_conf = DatabaseConf(
                    roles_db_name=config_data["database"]["roles_db_name"],
                    db_type=config_data["database"]["db_type"],
                    mysql_host=config_data["database"]["mysql_host"],
                    mysql_port=config_data["database"]["mysql_port"],
                    mysql_username=config_data["database"]["mysql_username"],
                    mysql_password=config_data["database"]["mysql_password"]
                )
                network_conf = NetworkConf(
                    enable_mai_backend=config_data["network"]["enable_mai_backend"],
                    mai_backend_url=config_data["network"]["mai_backend_url"],
                    mai_backend_token=config_data["network"]["mai_backend_token"],
                    enable_break_api=config_data["network"]["enable_break_api"],
                    break_api_host=config_data["network"]["break_api_host"],
                    break_api_port=config_data["network"]["break_api_port"]
                )
                config = Config(
                    core=core_conf,
                    onebot=onebot_conf,
                    database=database_conf,
                    network=network_conf
                )
                file.close()
                return config
        except Exception as e:
            logger.error(f"Failed to read config: {str(e)}")
            return None
    
    def get_cfg(self) -> Config:
        """获取配置对象
        """
        if self.config:
            return self.config
        else:
            raise


config_manager = ConfigManager()