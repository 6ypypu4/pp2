import psycopg2
from config import host, user, password, db_name

def create_table():
    """Обновляет счет пользователя или создает нового пользователя, если он не существует."""
    command ="""
        CREATE TABLE IF NOT EXISTS scores (
            id SERIAL PRIMARY KEY,
            user_name VARCHAR(32) NOT NULL,
            score INT NOT NULL
        )
        """
    try:
    #connect
        conn = psycopg2.connect(
        host = host,
        uer = user,
        password = password + "123",
        database = db_name
    )
        cur = conn.cursor()
        cur.execute(command)
    except:
        pass