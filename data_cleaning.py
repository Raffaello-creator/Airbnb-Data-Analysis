import pandas as pd
from database import *
from tkinter import filedialog, messagebox


def load_and_clean_data():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        messagebox.showinfo("Файл загружен", f"Файл {file_path} успешно загружен.")

        # Удаление дубликатов
        df.drop_duplicates(inplace=True)

        # Обработка пропущенных значений
        # Удалим строки с пропущенными значениями
        df.dropna(subset=['price', 'neighbourhood', 'room_type'], inplace=True)

        # Преобразуем цену в числовой формат, убирая символы валют
        df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

        conn = sqlite3.connect('airbnb_data.db')
        conn = create_database(df)
        return df
    else:
        messagebox.showerror("Ошибка", "Не удалось загрузить файл.")
        return None


