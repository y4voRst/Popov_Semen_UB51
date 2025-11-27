import tkinter as tk
from tkinter import messagebox, filedialog

# Функция для выполнения арифметической операции по введенным значениям и выбранной операции
def calculate():
    try:
        a = float(entry1.get())      # Получение первого числа из текстового поля
        b = float(entry2.get())      # Получение второго числа
        op = operation.get()         # Получение выбранного арифметического оператора
        if op == '+': 
            res = a + b              # Сложение
        elif op == '-': 
            res = a - b              # Вычитание
        elif op == '*': 
            res = a * b              # Умножение
        elif op == '/': 
            res = a / b if b != 0 else "Ошибка"  # Деление с защитой от деления на ноль
        label_result.config(text="Результат: " + str(res))  # Вывод результата в метку
    except:
        label_result.config(text="Ошибка ввода")  # Если ввод не число — вывести ошибку

# Функция для отображения выбранных пользователем чекбоксов в диалоговом окне
def show_selected():
    selected = []
    if var1.get(): selected.append("Первый")     # Проверка первого чекбокса
    if var2.get(): selected.append("Второй")     # Второго
    if var3.get(): selected.append("Третий")     # Третьего
    msg = "Выбрано: " + ", ".join(selected) if selected else "Ничего"  # Подготовка текста
    messagebox.showinfo("Выбор", msg)             # Показ всплывающего окна с выбранными

# Функция для выбора текстового файла и загрузки его содержимого в текстовое поле
def load_file():
    file = filedialog.askopenfilename(filetypes=[("txt", "*.txt")])  # Открыть диалог выбора файла
    if file:
        with open(file, "r", encoding="utf-8") as f:
            text_box.delete("1.0", tk.END)      # Очистить текстовое поле
            text_box.insert(tk.END, f.read())   # Вставить содержимое файла

root = tk.Tk()                       # Создаем главное окно приложения
root.title("Приложение")             # Задаем заголовок окна

# Создаем фрейм для кнопок, выступающих вкладками
tabs = tk.Frame(root)                
tabs.pack(expand=True, fill="both")  # Размещаем фрейм, растягивая его

# Кнопки для переключения между вкладками
btn_calc = tk.Button(tabs, text="Калькулятор", bg="lightblue", command=lambda: show_tab(calc_tab))
btn_choice = tk.Button(tabs, text="Выбор", bg="lightgreen", command=lambda: show_tab(choice_tab))
btn_text = tk.Button(tabs, text="Текст", bg="lightyellow", command=lambda: show_tab(text_tab))

btn_calc.pack(side="left", padx=5)    # Располагаем кнопки слева с промежутками
btn_choice.pack(side="left", padx=5)
btn_text.pack(side="left", padx=5)

# Создаем скрытые фреймы для вкладок
calc_tab = tk.Frame(root)
choice_tab = tk.Frame(root)
text_tab = tk.Frame(root)

# Функция для отображения нужной вкладки, скрывая остальные
def show_tab(tab):
    calc_tab.pack_forget()              # Скрыть калькулятор
    choice_tab.pack_forget()            # Скрыть выбор
    text_tab.pack_forget()              # Скрыть текст
    tab.pack(expand=True, fill="both")  # Показать выбранную вкладку

# Элементы вкладки "Калькулятор"
entry1 = tk.Entry(calc_tab, width=10)  # Поле ввода первого числа
entry1.pack(side="left", padx=5)
operation = tk.StringVar(value="+")    # Переменная для выбранной операции (по умолчанию '+')
# Выпадающее меню с операциями
tk.OptionMenu(calc_tab, operation, "+", "-", "*", "/").pack(side="left", padx=5)
entry2 = tk.Entry(calc_tab, width=10)  # Поле ввода второго числа
entry2.pack(side="left", padx=5)
tk.Button(calc_tab, text="=", command=calculate).pack(side="left", padx=5)  # Кнопка расчета
label_result = tk.Label(calc_tab, text="Результат:")  # Метка для вывода результата
label_result.pack(pady=10)

# Элементы вкладки "Выбор"
var1 = tk.BooleanVar()        # Переменные для состояний чекбоксов
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
# Чекбоксы с текстом и переменными
tk.Checkbutton(choice_tab, text="Первый", variable=var1).pack(anchor="w")
tk.Checkbutton(choice_tab, text="Второй", variable=var2).pack(anchor="w")
tk.Checkbutton(choice_tab, text="Третий", variable=var3).pack(anchor="w")
# Кнопка показать выбранные варианты
tk.Button(choice_tab, text="Показать", command=show_selected).pack(pady=10)

# Элементы вкладки "Текст"
tk.Button(text_tab, text="Загрузить", command=load_file).pack(pady=5)  # Кнопка загрузки файла
text_box = tk.Text(text_tab, wrap="word")   # Многострочное текстовое поле с переносом по словам
text_box.pack(expand=True, fill="both")     # Занимает все доступное пространство

show_tab(calc_tab)  # Отображаем вкладку калькулятора по умолчанию
root.mainloop()     # Запускаем главный цикл приложения, обработку событий
