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



    # Создаем базу данных
    conn = create_database(df)
