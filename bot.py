import nonebot
from nonebot.adapters.onebot.v11.adapter import Adapter


def start_bot():
    # 初始化 NoneBot
    nonebot.init()

    # 注册适配器
    driver = nonebot.get_driver()
    driver.register_adapter(Adapter)

    nonebot.load_plugins("plugins/")
    nonebot.load_plugins("plugins/core")
    nonebot.run()


if __name__ == "__main__":
    start_bot()