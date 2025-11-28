import tkinter as tk
from tkinter import messagebox, filedialog
def calculate():
    try:
        a = float(entry1.get())      
        b = float(entry2.get())     
        op = operation.get()         
        if op == '+': 
            res = a + b              
        elif op == '-': 
            res = a - b              
        elif op == '*': 
            res = a * b
        elif op == '/': 
            res = a / b if b != 0 else "Ошибка"
        label_result.config(text="Результат: " + str(res)) 
    except:
        label_result.config(text="Ошибка ввода") 
def show_selected():
    selected = []
    if var1.get(): selected.append("Первый")    
    if var2.get(): selected.append("Второй")     
    if var3.get(): selected.append("Третий")     
    msg = "Выбрано: " + ", ".join(selected) if selected else "Ничего"  
    messagebox.showinfo("Выбор", msg)             
def load_file():
    file = filedialog.askopenfilename(filetypes=[("txt", "*.txt")]) 
    if file:
        with open(file, "r", encoding="utf-8") as f:
            text_box.delete("1.0", tk.END)     
            text_box.insert(tk.END, f.read())  

root = tk.Tk()                      
root.title("Приложение")            
tabs = tk.Frame(root)                
tabs.pack(expand=True, fill="both") 
btn_calc = tk.Button(tabs, text="Калькулятор", bg="lightblue", command=lambda: show_tab(calc_tab))
btn_choice = tk.Button(tabs, text="Выбор", bg="lightgreen", command=lambda: show_tab(choice_tab))
btn_text = tk.Button(tabs, text="Текст", bg="lightyellow", command=lambda: show_tab(text_tab))

btn_calc.pack(side="left", padx=5)  
btn_choice.pack(side="left", padx=5)
btn_text.pack(side="left", padx=5)
calc_tab = tk.Frame(root)
choice_tab = tk.Frame(root)
text_tab = tk.Frame(root)
def show_tab(tab):
    calc_tab.pack_forget()             
    choice_tab.pack_forget()           
    text_tab.pack_forget()              
    tab.pack(expand=True, fill="both")  

entry1 = tk.Entry(calc_tab, width=10) 
entry1.pack(side="left", padx=5)
operation = tk.StringVar(value="+")   
tk.OptionMenu(calc_tab, operation, "+", "-", "*", "/").pack(side="left", padx=5)
entry2 = tk.Entry(calc_tab, width=10) 
entry2.pack(side="left", padx=5)
tk.Button(calc_tab, text="=", command=calculate).pack(side="left", padx=5)  
label_result = tk.Label(calc_tab, text="Результат:")  
label_result.pack(pady=10)

var1 = tk.BooleanVar()        
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
tk.Checkbutton(choice_tab, text="Первый", variable=var1).pack(anchor="w")
tk.Checkbutton(choice_tab, text="Второй", variable=var2).pack(anchor="w")
tk.Checkbutton(choice_tab, text="Третий", variable=var3).pack(anchor="w")
tk.Button(choice_tab, text="Показать", command=show_selected).pack(pady=10)

tk.Button(text_tab, text="Загрузить", command=load_file).pack(pady=5)  
text_box = tk.Text(text_tab, wrap="word")   
text_box.pack(expand=True, fill="both")    

show_tab(calc_tab)  
root.mainloop()    
