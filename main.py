import json
import os
import tkinter as tk
from tkinter import messagebox

path = "main.json"

def save_to_json():
    text_data = entry.get().strip()

    if not text_data:
        messagebox.showwarning("Предупреждение", "Поле ввода пустое!")
        return

    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
        except json.JSONDecodeError:
            data = []
    else:
        data = []

    data.append(text_data)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    entry.delete(0, tk.END)
    messagebox.showinfo("Успех", "Информация успешно сохранена")

def show_data():
    if not os.path.exists(path):
        messagebox.showinfo("Информация", "Файл json еще не создан.")
        return

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        messagebox.showerror("Ошибка", "Не удалось прочитать файл.")
        return

    if not data:
        messagebox.showinfo("", "В файле пока нет записей.")
        return

    info_window = tk.Toplevel(root)
    info_window.title("Содержимое JSON файла")
    info_window.geometry("400x300")
    text_area = tk.Text(info_window, wrap=tk.WORD, font=("Arial", 10))
    text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    scrollbar = tk.Scrollbar(info_window, command=text_area.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_area.config(yscrollcommand=scrollbar.set)
    for i, item in enumerate(data, start=1):
        text_area.insert(tk.END, f"Запись №{i}: {item}\n")
    text_area.config(state=tk.DISABLED)
root = tk.Tk()
root.title("Сохранение в JSON")
root.geometry("400x200")
root.resizable(False, False)
label = tk.Label(root, text="Введите информацию:", font=("Arial", 11))
label.pack(pady=(20, 5))
entry = tk.Entry(root, width=40, font=("Arial", 11))
entry.pack(pady=5)
btns = tk.Button(root, text="Записать в файл", width=25, command=save_to_json)
btns.pack(pady=10)
btn = tk.Button(root, text="Показать всю информацию", width=25, command=show_data)
btn.pack(pady=5)
root.mainloop()


