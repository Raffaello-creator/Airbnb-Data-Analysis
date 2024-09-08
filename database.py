import sqlite3
import pandas as pd


def create_database(df, db_name='airbnb_data.db'):
    # Создаем подключение к базе данных SQLite
    conn = sqlite3.connect(db_name)

    # Записываем данные в таблицу базы данных
    df.to_sql('airbnb_data', conn, if_exists='replace', index=False)

    return conn


def execute_sql_query(conn, query):
    # Выполняем SQL-запрос и возвращаем результат в виде DataFrame
    return pd.read_sql(query, conn)


if __name__ == "__main__":
    # Загружаем очищенные данные
    df = pd.read_csv('data/cleaned_airbnb_data.csv')

    # Создаем базу данных
    conn = create_database(df)

    # Пример SQL-запроса: количество объявлений в каждом районе
    query = '''
    SELECT neighbourhood, COUNT(*) AS num_listings
    FROM airbnb_data
    GROUP BY neighbourhood
    ORDER BY num_listings DESC
    LIMIT 10;
    '''
    popular_neighbourhoods = execute_sql_query(conn, query)
    print(popular_neighbourhoods)

    # Закрываем соединение с базой данных
    conn.close()
