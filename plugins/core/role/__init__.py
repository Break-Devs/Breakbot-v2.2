from math import e
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment, PrivateMessageEvent
from nonebot_plugin_alconna import on_alconna, Arparma
from arclet.alconna import Alconna, Subcommand, Args, Option, Arg
from breaker.RoleManager import role_manager
from breaker.LocaleManager import locale_manager

role_cmd = on_alconna(
    Alconna(
        "role",
        Subcommand("get",
                   Args(Arg("uid", int, -1))
                   ),
        Subcommand("add",
                   Args["uid", int]["role", str])
        
    )
)

@role_cmd.handle()
async def _(bot: Bot, event: GroupMessageEvent | PrivateMessageEvent, result: Arparma):
    if result.find("get"):
        uid = result.query[int]("uid")
        if uid:
            if uid == -1:
                # 输入默认参数，查询用户自己的数据
                uid = event.user_id
            # 通过角色数据库模块查询自己的角色权限
            roles_list = role_manager.get_role(uid)
            # 生成返回信息
            if not roles_list:
                if uid == event.user_id:
                    msg = locale_manager.get("role.roleUserGotNoRoleMessage")
                else:
                    msg = locale_manager.get("role.roleOtherUserGotNoRoleMessage").format(uid)
                await role_cmd.finish(MessageSegment.at(event.user_id) + MessageSegment.text(" "+msg))
            # 有权限则返回权限信息
            roles_str = ", ".join(roles_list)
            if uid == event.user_id:
                msg = locale_manager.get("role.roleUserGotMessage").format(roles_str)
            else:
                msg = locale_manager.get("role.roleOtherUserGotMessage").format(uid, roles_str)
            await role_cmd.finish(MessageSegment.at(event.user_id) + MessageSegment.text(" "+msg))
    if result.find("add"):
        if role_manager.has_role(event.user_id, "admin"):
            uid = result.query[int]("uid")
            role = result.query[str]("role")
            
            role_manager.add_role(uid, role) # type: ignore
            msg = locale_manager.get("role.AddRoleSuccessMessage")
        else:
            msg = locale_manager.get("role.NoPermissionMessage")
        await role_cmd.finish(MessageSegment.at(event.user_id) + MessageSegment.text(" "+msg))