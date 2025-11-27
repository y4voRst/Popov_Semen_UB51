import tkinter as tk
from tkinter import messagebox
import json
import requests

# Функция для получения данных о пользователе GitHub по имени (owner)
def get_repo_data():
    repo_name = entry.get()  # Считываем имя владельца репозитория из поля ввода
    if not repo_name:        # Проверяем, что строка не пустая
        messagebox.showerror("Ошибка", "Введите имя пользователя (owner)")
        return

    url = f"https://api.github.com/users/{repo_name}"  # Формируем URL запроса к GitHub API
    try:
        response = requests.get(url)  # Делаем GET-запрос
        data = response.json()        # Получаем данные в формате JSON

        # Поля, которые хотим получить из ответа
        fields = ['company', 'created_at', 'email', 'id', 'name', 'url']

        selected_data = {}
        for field in fields:
            selected_data[field] = data.get(field)  # Копируем нужные поля (если есть)

        # Сохраняем в JSON-файл с отступами и корректной кодировкой
        with open("file.json", 'w', encoding='utf-8') as f:
            json.dump(selected_data, f, ensure_ascii=False, indent=4)

        messagebox.showinfo("Успех", "Данные успешно сохранены в file.json")

    except requests.RequestException:
        messagebox.showerror("Ошибка", "Ошибка при обращении к API")

# Создание главного окна Tkinter
root = tk.Tk()
root.title("Попов Семён")

# Текстовая метка-инструкция
tk.Label(root, text="Введите имя пользователя (owner):").pack(padx=150, pady=10)

# Поле ввода имени пользователя
entry = tk.Entry(root, width=40)
entry.pack(padx=4, pady=3)

# Кнопка для запуска функции запроса данных
btn = tk.Button(root, text="Получить данные", command=get_repo_data)
btn.pack(padx=2, pady=15)

# Запуск основного цикла обработки событий
root.mainloop()
