<div align="center">
    <img src="/static/img/dxdoublebreakstar.png" alt="logo" />
    <h1 style="font-size:3em;">Breakbot v2.2<img src="static/img/dx.png" width="5%" /></h1>
    <img src="https://img.shields.io/badge/python-3.12%2B-blue?logo=python&logoColor=edb641" alt="Static Badge">
    <img src="https://img.shields.io/badge/Nonebot-2-green" alt="Static Badge">
    <img src="https://img.shields.io/badge/Dev-Alpha_2.2.0001-orange" alt="Static Badge">
    <p>由Break开发组编写的Python Bot，希望你能用的开心！</p>
</div>

## 使用

安装：

```shell
poetry install
```

更新：

```shell
poetry update
```
使用

```shell
poetry run python start.py
```

## 配置文件参考

> 一般来讲，初始配置文件会由Bot自行生成，但是在配置文件有更新时（或者你就是更喜欢自己来一点）需要手动修改/添加配置。

```toml
# config.toml
# Break Bot 2 的基础配置文件

[core] # ! Break Bot的核心配置
# Bot的名称
bot_name = "Break Bot"
# 版本号
version_name = "Mujirushi 1.0"
# 自定义文本配置
locale = "break"

[onebot] # ! Onebot v11连接相关的配置
onebot_host = "127.0.0.1"
onebot_port = 8080

[database] # ! 数据库相关的配置
# 角色权限数据库的路径，一般不需要改动
roles_db_name = "./database/roles.db"
# 用户数据库的类型，0为sqlite，1为mysql
# 如使用mysql则需要设置数据库主机、端口、用户名、密码
db_type = 0
mysql_host = "127.0.0.0"
mysql_port = 3306
mysql_username = ""
mysql_password = ""

[network] # ! 网络通信相关的配置
# 是否连接启用mai.py后端的功能（以及相关的插件）？
enable_mai_backend = false
mai_backend_host = "127.0.0.1"
mai_backend_port = 56000
mai_backend_token = ""
# 是否开启break API的Http通信功能？
# 启动break API后会在本地开启一个网络服务端并允许你通过其进行联网通信。
# 这个网络服务端一般用于同其他服务进行联动，如Minecraft服务器插件
# 将端口设置为0之后可以直接在host中填入URL
enable_breal_api = false
break_api_host = "0.0.0.0"
break_api_port = 56002

```