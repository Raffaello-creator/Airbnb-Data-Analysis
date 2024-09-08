import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Функция для отображения таблицы в новом окне с прокруткой
def show_table(df):
    # Создаем новое окно
    table_window = tk.Toplevel()
    table_window.title("Результаты запроса")

    # Создаем фрейм для Treeview и Scrollbar
    frame = tk.Frame(table_window)
    frame.pack(expand=True, fill='both')

    # Добавляем виджет Treeview
    tree = ttk.Treeview(frame, columns=list(df.columns), show='headings')
    tree.pack(side='left', expand=True, fill='both')

    # Добавляем вертикальный Scrollbar
    scrollbar_y = tk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar_y.set)
    scrollbar_y.pack(side='right', fill='y')

    # Добавляем горизонтальный Scrollbar
    scrollbar_x = tk.Scrollbar(table_window, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=scrollbar_x.set)
    scrollbar_x.pack(side='bottom', fill='x')

    # Устанавливаем колонки
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)

    # Добавляем строки в таблицу
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))


# Функция для отображения графика в новом окне с вертикальными названиями для оси X
def show_graph(df, x_column, y_column):
    graph_window = tk.Toplevel()
    graph_window.title("График")

    fig, ax = plt.subplots()

    # Построение графика
    ax.plot(df[x_column], df[y_column], marker='o')

    # Разворот меток оси X
    ax.set_xticklabels(df[x_column], rotation=90)

    # Установка подписей и заголовка
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(f'{y_column} по {x_column}')

    # Вставляем график в окно с помощью TkAgg
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill='both')
