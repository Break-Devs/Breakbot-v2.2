from breaker.RoleManager import role_manager


def test_role():
    role_manager.add_role(2913844577, "QQ", "Role1", "Role2")
    res = role_manager.get_role(2913844577, "QQ")
    print(res)


if __name__ == "__main__":
    test_role()