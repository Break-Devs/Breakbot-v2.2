import os
import sqlite3


class RoleManager:
    """用于和SQLite数据库进行交互来实现用户角色管理的权限管理器
    """
    def __init__(self) -> None:
        # 如果没有检测到roles数据库文件，则初始化一个新的数据库文件。
        if not os.path.exists("./database/roles.db"):
            self.init_roles_db()
    
    def init_roles_db(self):
        """初始化一个roles数据库
        """
        # 生成数据库连接
        conn = sqlite3.connect("./database/roles.db")
        # 创建指针
        cur = conn.cursor()
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
    
    def get_role(self, uid: str | int, type: str = "QQ") -> list:
        roles = []
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT roles FROM users WHERE uid = ? AND type = ?
            ''', (str(uid), type))
            
            row = cursor.fetchone()
            if row:
                roles = row[0].split(',')
            
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            if conn:
                conn.close()
        
        return roles

    def add_role(self, uid: str | int, type: str = "QQ", *roles):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Fetch existing roles
            cursor.execute('''
                SELECT roles FROM users WHERE uid = ? AND type = ?
            ''', (str(uid), type))
            
            row = cursor.fetchone()
            if row:
                existing_roles = row[0].split(',')
                # Add new roles to existing ones
                updated_roles = list(set(existing_roles + list(roles)))  # Remove duplicates
                cursor.execute('''
                    UPDATE users SET roles = ? WHERE uid = ? AND type = ?
                ''', (','.join(updated_roles), str(uid), type))
            else:
                # Insert new user with roles
                cursor.execute('''
                    INSERT INTO users (uid, type, roles) VALUES (?, ?, ?)
                ''', (str(uid), type, ','.join(roles)))

            # Commit changes
            conn.commit()

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        finally:
            cursor.close()
            conn.close()


role_manager = RoleManager()