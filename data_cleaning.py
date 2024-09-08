import pandas as pd


def load_and_clean_data(file_path):
    # Загружаем данные из CSV
    df = pd.read_csv(file_path)

    # Удаление дубликатов
    df.drop_duplicates(inplace=True)

    # Обработка пропущенных значений
    # Удалим строки с пропущенными значениями
    df.dropna(subset=['price', 'neighbourhood', 'room_type'], inplace=True)

    # Преобразуем цену в числовой формат, убирая символы валют
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

    # Вернем очищенные данные
    return df


if __name__ == "__main__":
    file_path = 'data/AB_NYC_2019.csv'
    cleaned_data = load_and_clean_data(file_path)

    # Сохраняем очищенные данные
    cleaned_data.to_csv('data/cleaned_airbnb_data.csv', index=False)
