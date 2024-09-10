
from database import *
from data_cleaning import *
import sqlite3
from visuals import *

# Основное окно приложения
def main():
    # Создаем окно
    root = tk.Tk()
    root.title("Анализ данных Airbnb")
    root.geometry("400x300")

    # Загрузка файла
    load_btn = tk.Button(root, text="Загрузить файл CSV", command=lambda: load_and_clean_data())
    load_btn.pack(pady=20)

    # Подключаемся к базе данных
    conn = sqlite3.connect('airbnb_data.db')

    # Словарь с запросами
    queries = {
        "Средняя цена по районам": '''
                SELECT neighbourhood, AVG(price) AS avg_price
                FROM airbnb_data
                GROUP BY neighbourhood
                ORDER BY avg_price DESC
            ''',
        "Количество объявлений по районам": '''
                SELECT neighbourhood_group, COUNT(*) AS listings_count
                FROM airbnb_data
                GROUP BY neighbourhood_group
                ORDER BY listings_count DESC
            ''',
        "Топ 10 самых дорогих объявлений": '''
                SELECT name, neighbourhood, price
                FROM airbnb_data
                ORDER BY price DESC
                LIMIT 10
            ''',
        "Средняя цена для каждого типа жилья": '''
            SELECT room_type, AVG(price) AS avg_price
            FROM airbnb_data
            GROUP BY room_type
            ORDER BY avg_price DESC;

        ''',
        "Среднее количество отзывов по районам": '''
            SELECT neighbourhood_group, AVG(number_of_reviews) AS avg_reviews
            FROM airbnb_data
            GROUP BY neighbourhood_group
            ORDER BY avg_reviews DESC;

        ''',
        "Количество объектов с минимальным количеством ночей больше 30": '''
            SELECT COUNT(*) AS long_term_listings
            FROM airbnb_data
            WHERE minimum_nights > 30;

        ''',
        "Распределение объектов по доступности": '''
            SELECT availability_365, COUNT(*) AS listings_count
            FROM airbnb_data
            GROUP BY availability_365
            ORDER BY availability_365 DESC;

        ''',
        "Средняя цена и количество отзывов по районам с типом жилья": '''
            SELECT neighbourhood, AVG(price) AS avg_price, AVG(number_of_reviews) AS avg_reviews
            FROM airbnb_data
            WHERE room_type = 'Entire home/apt'
            GROUP BY neighbourhood
            ORDER BY avg_price DESC;

        ''',
        "Количество объектов, которые имеют больше 100 отзывов и доступны более чем 300 дней в году:": '''
            SELECT name, neighbourhood, price
            FROM airbnb_data
            ORDER BY price DESC
            LIMIT 10
        ''',



    }

    # Функция для обработки выбранного запроса
    def on_query_select_graph(event):
        query_name = query_var.get()  # Получаем выбранное имя запроса
        query = queries.get(query_name)  # Получаем соответствующий запрос

        # Выполняем запрос и получаем DataFrame
        df = execute_sql_query(conn, query)

        # Показываем график на основе первых двух колонок
        show_graph(df, df.columns[0], df.columns[1])

    def on_query_select_table(event):
        query_name = query_var.get()  # Получаем выбранное имя запроса
        query = queries.get(query_name)  # Получаем соответствующий запрос

        # Выполняем запрос и получаем DataFrame
        df = execute_sql_query(conn, query)

        # Показываем таблицу
        show_table(df)

    # Метка и выпадающее меню для выбора запроса
    tk.Label(root, text="Выберите запрос:").pack(pady=10)

    query_var = tk.StringVar()
    query_dropdown = ttk.Combobox(root, textvariable=query_var, values=list(queries.keys()),width=100)
    query_dropdown.pack(pady=10)

    # Кнопка для выполнения запроса
    query_button = tk.Button(root, text="Вывести таблицу", command=lambda: on_query_select_table(None))
    query_button.pack(pady=10)

    # Кнопка для выполнения запроса
    query_button = tk.Button(root, text="Показать график", command=lambda: on_query_select_graph(None))
    query_button.pack(pady=10)

    root.mainloop()
    # Запускаем цикл приложения
    root.mainloop()




if __name__ == "__main__":
    main()
