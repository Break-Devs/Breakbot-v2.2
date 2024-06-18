from breaker.RoleManager import role_manager
from breaker.ConfigManager import config_manager


def test_role():
    if role_manager.has_role(2913844577, "Role2"):
        print(1)


if __name__ =="__main__":
    test_role()