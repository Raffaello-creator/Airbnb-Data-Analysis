import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3


def analyze_price_by_property_type(conn):
    query = '''
    SELECT room_type, AVG(price) AS avg_price
    FROM airbnb_data
    GROUP BY room_type
    ORDER BY avg_price DESC;
    '''
    return pd.read_sql(query, conn)


def plot_price_by_property_type(df):
    # Визуализируем среднюю цену по типам жилья
    plt.figure(figsize=(10, 6))
    sns.barplot(x='room_type', y='avg_price', data=df)
    plt.xticks(rotation=45)
    plt.title('Средняя цена по типам жилья на Airbnb')
    plt.xlabel('Тип жилья')
    plt.ylabel('Средняя цена')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Подключаемся к базе данных
    conn = sqlite3.connect('airbnb_data.db')

    # Анализируем зависимость цены от типа жилья
    price_by_property_type = analyze_price_by_property_type(conn)

    # Визуализируем результаты
    plot_price_by_property_type(price_by_property_type)

    # Закрываем соединение
    conn.close()
