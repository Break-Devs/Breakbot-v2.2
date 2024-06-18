import os
import sqlite3
from nonebot.log import logger


class RoleManager:
    """用于和SQLite数据库进行交互来实现用户角色管理的权限管理器
    """
    def __init__(self) -> None:
        logger.info("正在初始化角色管理模块...")
        # 存储本地的数据库路径
        self.role_db_path = "./database/roles.db"
        
        # 如果没有检测到roles数据库文件，则初始化一个新的数据库文件。
        if not os.path.exists("./database/roles.db"):
            logger.warning("未找到roles.db数据库文件，将新建数据库连接。")
            self.init_roles_db()
    
    def init_roles_db(self):
        """初始化一个roles数据库
        """
        # 生成数据库连接
        conn = sqlite3.connect("./database/roles.db")
        # 创建指针
        cur = conn.cursor()
        # 设置 WAL 模式
        cur.execute('PRAGMA journal_mode=WAL;')
        # 执行新建命令
        cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
        type TEXT,
        uid TEXT,
        roles TEXT
        )
        ''')
        conn.commit()
        cur.close()
        conn.close()
        logger.success("新建表成功")
    
    def get_role(self, uid: str | int, type: str = "QQ") -> list:
        """用于获取用户所拥有的角色权限
        """
        roles = []
        conn = sqlite3.connect(self.role_db_path)
        cursor = conn.cursor()
        try:
            
            cursor.execute('''
                SELECT roles FROM users WHERE uid = ? AND type = ?
            ''', (str(uid), type))
            
            row = cursor.fetchone()
            if row:
                roles = row[0].split(',')
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            cursor.close()
            conn.close()
        
        return roles

    def add_role(self, uid: str | int, *roles: str, type: str = "QQ"):
        """用于增加用户的角色权限
        """
        conn = sqlite3.connect(self.role_db_path)
        cursor = conn.cursor()
        try:
            # 获取已有的角色
            cursor.execute('''
                SELECT roles FROM users WHERE uid = ? AND type = ?
            ''', (str(uid), type))
            
            row = cursor.fetchone()
            if row:
                existing_roles = row[0].split(',')
                updated_roles = list(set(existing_roles + list(roles)))
                cursor.execute('''
                    UPDATE users SET roles = ? WHERE uid = ? AND type = ?
                ''', (','.join(updated_roles), str(uid), type))
            else:
                cursor.execute('''
                    INSERT INTO users (uid, type, roles) VALUES (?, ?, ?)
                ''', (str(uid), type, ','.join(roles)))
            conn.commit()

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            cursor.close()
            conn.close()
    
    def delete_role(self, uid: str | int, *roles: str, type: str = "QQ"):
        """用于删除用户的角色权限
        """
        conn = sqlite3.connect(self.role_db_path)
        cursor = conn.cursor()
        try:
            # 获取已有的角色
            cursor.execute('''
                SELECT roles FROM users WHERE uid = ? AND type = ?
            ''', (str(uid), type))
            
            row = cursor.fetchone()
            if row:
                existing_roles = row[0].split(',')
                updated_roles = list(set(existing_roles) - set(roles))
                cursor.execute('''
                    UPDATE users SET roles = ? WHERE uid = ? AND type = ?
                ''', (','.join(updated_roles), str(uid), type))
            conn.commit()

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            cursor.close()
            conn.close()
    
    def has_role(self, uid: str | int, role: str, type: str = "QQ") -> bool:
        """用于检测用户是否具有某一权限
        """
        conn = sqlite3.connect(self.role_db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('''
                SELECT roles FROM users WHERE uid = ? AND type = ?
            ''', (str(uid), type))
            
            row = cursor.fetchone()
            if row:
                roles = row[0].split(',')
                return role in roles
            else:
                return False

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()
            conn.close()
    
    def enable_wal_mode(self):
        """启用数据库的WAL模式
        """
        conn = sqlite3.connect(self.role_db_path)
        cursor = conn.cursor()
        try:
            cursor.execute('PRAGMA journal_mode=WAL;')
            conn.commit()
            logger.success("已启用数据库的WAL模式")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            cursor.close()
            conn.close()


role_manager = RoleManager() 