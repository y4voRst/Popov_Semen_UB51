import tkinter as tk
from tkinter import messagebox
import json
import requests

def get_repo_data():
    repo_name = entry.get() 
    if not repo_name:        
        messagebox.showerror("Ошибка", "Введите имя пользователя (owner)")
        return

    url = f"https://api.github.com/users/{repo_name}"  
    try:
        response = requests.get(url) 
        data = response.json()       

        fields = ['company', 'created_at', 'email', 'id', 'name', 'url']

        selected_data = {}
        for field in fields:
            selected_data[field] = data.get(field)  

        with open("file.json", 'w', encoding='utf-8') as f:
            json.dump(selected_data, f, ensure_ascii=False, indent=4)

        messagebox.showinfo("Успех", "Данные успешно сохранены в file.json")

    except requests.RequestException:
        messagebox.showerror("Ошибка", "Ошибка при обращении к API")

root = tk.Tk()
root.title("Попов Семён")

tk.Label(root, text="Введите имя пользователя (owner):").pack(padx=150, pady=10)

entry = tk.Entry(root, width=40)
entry.pack(padx=4, pady=3)

btn = tk.Button(root, text="Получить данные", command=get_repo_data)
btn.pack(padx=2, pady=15)

root.mainloop()
