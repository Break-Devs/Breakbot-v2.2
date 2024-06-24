# Break Bot的启动脚本
# 自动初始化并启动各个功能
from breaker.Colors import gradient_text, reset, grey, light_cyan
from breaker.LoggerManager import logger
from breaker.ConfigManager import config_manager
from breaker.RoleManager import role_manager
from breaker.LocaleManager import locale_manager
from breaker.Utils import gen_env_file
from bot import start_bot

logger.success(f"{light_cyan}模块初始化完成，正在启动NoneBot。{reset}")
# 生成bot使用的env文件
gen_env_file()
start_bot()
