from breaker.ConfigManager import config_manager
from breaker.LoggerManager import logger
import httpx
import hashlib

cfg = config_manager.get_cfg()


class MaiApiHandler:
    token: str
    host: str
    salt_1: str = ""
    salt_2: str = ""
    salt_3: str = ""
    # 初始化api存储
    logout_api: str = ""
    
    def __init__(self) -> None:
        if cfg.network.enable_mai_backend:
            self.token = cfg.network.mai_backend_token
            self.host = cfg.network.mai_backend_url
            # 去除host末尾的/
            if self.host.endswith("/"):
                self.host = self.host[:-1]
            # 尝试认证并获取salt
            self.get_connect()

    def get_connect(self):
        token_data = {
            "token": self.token
        }
        res = httpx.post(f"{self.host}/mai-api/identification", json=token_data)
        if res.status_code == 200:
            print(res.json())
            salt_data: dict[str, str] = res.json()["result"]
            self.salt_1 = salt_data.get("salt_1", "")
            self.salt_2 = salt_data.get("salt_2", "")
            self.salt_3 = salt_data.get("salt_3", "")
    
    def obfucate(self, api: str, salt: str):
        return hashlib.md5((api + salt).encode("utf-8")).hexdigest()
    
    def init(self):
        # 初始化并混淆API
        if self.salt_1:
            self.logout_api = self.obfucate("logout", self.salt_1)
            
    


maiapi = MaiApiHandler()