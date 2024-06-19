from breaker.LoggerManager import logger
from breaker.ConfigManager import config_manager
from breaker.RoleManager import role_manager
from breaker.LocaleManager import locale_manager
from breaker.Utils import gen_env_file
from breaker.MaiApiHandler import maiapi
import httpx

maiapi.init()
print(maiapi.logout_api)

res = httpx.post(f"{maiapi.host}/mai-api/{maiapi.logout_api}", json={"user_id": 10907518})
print(res.json())