import os
import socket
import tkinter as tk
from tkinter import scrolledtext
import shlex
import sys


def execute_command(event=None):
    # Забираем введённый текст из поля ввода
    cmd_line = entry.get().strip()
    if not cmd_line:
        return  # если строка пустая

    # Добавляем введённую строку в историю (поле вывода)
    output.insert(tk.END, f"> {cmd_line}\n")

    # shlex.split разбивает строку на аргументы, учитывая кавычки
        
    args = shlex.split(cmd_line)
    

    if not args:
        entry.delete(0, tk.END)
        return

    # Первая часть — это команда, остальное — её аргументы
    command = args[0]
    arguments = args[1:]

    if command == "ls":
        # Заглушка для команды ls
        output.insert(
            tk.END,
            f"[Заглушка] Выполнена команда: ls {arguments}\n"
        )

    elif command == "cd":
        # Заглушка для команды cd
        output.insert(
            tk.END,
            f"[Заглушка] Выполнена команда: cd {arguments}\n"
        )

    elif command == "exit":
        # Команда exit — завершает приложение
        root.destroy()
        sys.exit(0)

    else:
        output.insert(tk.END, f"Неизвестная команда: {command}\n")

    # Очищаем поле ввода
    entry.delete(0, tk.END)


# Получаем имя пользователя и имя хоста из ОС
username = os.getlogin()
hostname = socket.gethostname()
title = f"Эмулятор - [{username}@{hostname}]"


root = tk.Tk()
root.title(title)

# Поле для вывода 
output = scrolledtext.ScrolledText(root,         wrap=tk.WORD, height=20,   width=80     )
output.pack(padx=10, pady=10)

# Поле для ввода команд
entry = tk.Entry(root, width=80)
entry.pack(padx=10, pady=(0, 10))

# Привязываем нажатие Enter к выполнению команды
entry.bind("<Return>", execute_command)

root.mainloop()
