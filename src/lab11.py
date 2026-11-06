import pandas as pd

# Завдання для всіх варіантів
# 1. Завантажити дані з файлу data/sales_data.csv у DataFrame.
# 2. Вивести перші 5 рядків DataFrame, отримати загальну інформацію про нього та статистичні характеристики числових стовпців.

# Ваш код починається тут

# 1. Завантаження даних
df = pd.read_csv('data/sales_data.csv', parse_dates=['date'])

# 2. Первинний аналіз даних
print("Перші 5 рядків:")
print(df.head())
print("\nЗагальна інформація:")
df.info()
print("\nСтатистичні характеристики:")
print(df.describe())


# Подальший код для вашого варіанту

# Приклад виконання завдання (з лекції)
# Розкоментуйте та адаптуйте для свого варіанту

# # 3. Фільтрація даних
# filtered_df = df[(df['store_id'] == 1) & (df['quantity'] > 2)]
# print("\nВідфільтровані дані:")
# print(filtered_df)
#
# # 4. Сортування даних
# sorted_df = df.sort_values(by=['date', 'order_id'], ascending=[True, False])
# print("\nВідсортовані дані:")
# print(sorted_df)
#
# # 5. Групування та агрегування даних
# grouped_df = df.groupby(['store_id', 'product_id'])['quantity'].sum().reset_index()
# print("\nЗгруповані дані:")
# print(grouped_df)
#
# # 6. Додавання стовпця
# # Спочатку обробимо пропущені значення в 'price', щоб уникнути помилок
# df['price'] = df.groupby('store_id')['price'].transform(lambda x: x.fillna(x.mean()))
# df['total_amount'] = df['quantity'] * df['price']
# print("\nДані з новим стовпцем total_amount:")
# print(df)
#
# # 7. Видалення стовпців
# df_after_drop = df.drop(columns=['order_id', 'product_id'])
# print("\nДані після видалення стовпців:")
# print(df_after_drop)
#
# # 8. Обробка пропущених значень (вже частково зроблено)
# # df['price'] = df.groupby('store_id')['price'].transform(lambda x: x.fillna(x.mean()))
# print("\nДані після заповнення пропущених значень в 'price':")
# print(df)
#
# # 9. Створення зведеної таблиці
# df['month'] = df['date'].dt.month
# pivot_table = df.pivot_table(values='total_amount', index='store_id', columns='month', aggfunc='sum')
# print("\nЗведена таблиця:")
# print(pivot_table)