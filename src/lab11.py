import pandas as pd

def main():
  print("--- 1. Завантаження даних ---")
  # Завантажуємо табличні дані з файлу data/sales_data.csv у DataFrame
  df = pd.read_csv("data/sales_data.csv")
  print("Дані успішно завантажено!\n")

  print("--- 2. Первинний аналіз даних ---")
  # Вивести перші 5 рядків, загальну інформацію та статистичні характеристики
  print("Перші 5 рядків DataFrame:")
  print(df.head(), "\n")

  print("Загальна інформація про DataFrame:")
  df.info()
  print()

  print("Статистичні характеристики числових стовпців:")
  print(df.describe(), "\n")

  print("--- 3. Фільтрація даних (Варіант 1) ---")
  # Вибрати рядки, де store_id дорівнює 2 і quantity менше 3
  filtered_df = df[(df["store_id"] == 2) & (df["quantity"] < 3)]
  print(f"Знайдено рядків: {len(filtered_df)}")
  print(filtered_df.head(), "\n")

  print("--- 4. Сортування даних (Варіант 1) ---")
  # Відсортувати дані за стовпцем quantity у порядку спадання
  sorted_df = df.sort_values(by="quantity", ascending=False)
  print(sorted_df.head(), "\n")

  print("--- 5. Групування та агрегування (Варіант 1) ---")
  # Згрупувати дані за product_id та обчислити середню ціну (price) для кожного товару
  grouped_df = df.groupby("product_id")["price"].mean().reset_index()
  print(grouped_df, "\n")

  print("--- 6. Додавання нового стовпця (Варіант 1) ---")
  # Додати стовпець total_cost, який містить загальну вартість замовлення (добуток quantity та price)
  df["total_cost"] = df["quantity"] * df["price"]
  print(df[["order_id", "quantity", "price", "total_cost"]].head(), "\n")

  print("--- 7. Видалення стовпців (Варіант 1) ---")
  # Видалити стовпець date
  df_dropped = df.drop(columns=["date"])
  print("Стовпці після видалення 'date':", df_dropped.columns.tolist(), "\n")

  print("--- 8. Обробка пропущених значень (Варіант 1) ---")
  # Замінити пропущені значення (NaN) у стовпці quantity на 0
  print(
      "Кількість пропущених значень у quantity до заміни:",
      df["quantity"].isnull().sum(),
  )
  df["quantity"] = df["quantity"].fillna(0)
  print(
      "Кількість пропущених значень у quantity після заміни:",
      df["quantity"].isnull().sum(),
      "\n",
  )

  print("--- 9. Створення зведеної таблиці (pivot table) (Варіант 1) ---")
  # Створити зведену таблицю, де в рядках буде store_id, у стовпцях – product_id,
  # а в комірках – сумарна кількість проданих товарів (quantity)
  pivot_df = df.pivot_table(
      index="store_id",
      columns="product_id",
      values="quantity",
      aggfunc="sum",
      fill_value=0,
  )
  print(pivot_df)


if __name__ == "__main__":
  main()
