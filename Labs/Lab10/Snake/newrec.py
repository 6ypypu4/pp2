import psycopg2
from config import host, user, password, db_name

def update(nickname, score):
    """Обновляет счет пользователя или создает нового пользователя, если он не существует."""
    try:
        # Подключение к базе данных
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        cur = conn.cursor()
        
        # Получение текущего рекорда пользователя, если он существует
        cur.execute("SELECT score FROM scores WHERE user_name = %s", (nickname,))
        current_score = cur.fetchone()

        # Если пользователь уже существует и его текущий рекорд меньше нового рекорда, обновляем его рекорд
        if current_score and current_score[0] < score:
            cur.execute("UPDATE scores SET score = %s WHERE user_name = %s", (score, nickname))
        # Если пользователь не существует, создаем новую запись
        elif not current_score:
            cur.execute("INSERT INTO scores (user_name, score) VALUES (%s, %s)", (nickname, score))

        # Фиксируем изменения в базе данных
        conn.commit()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка:", error)
    finally:
        # Закрываем соединение
        if conn is not None:
            conn.close()
