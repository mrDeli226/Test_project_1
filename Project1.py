from tkinter import *
from tkinter import ttk
import random

Tasks = [
    {"text": "Задача: Создать калькулятор", 'done': False},
    {"text": "Задача: Написать генератор паролей", 'done': False},
    {"text": "Задача: Написать игру угадай число", 'done': False},
    {"text": "Задача: Созадть список дел", 'done': False},
    {"text": "Задача: Создать простой дневник", 'done': False}
]

def update_tasks_list():
    task_list.delete('1.0', END)

    if len(Tasks) == 0:
        task_list.insert(END, "Список задач пуст.")
        return
    
    for index, task in enumerate(Tasks, start=1):
        status = "[X]" if task['done'] else "[]"
        task_list.insert(END, f"{index}. {status} {task["text"]}\n")

def add_task():
    new_task = task_entry.get()
    if new_task.strip() == "":
        result_tabel["text"] = "Ошибка значения (возможно поле вода пусто)"
        return
    Tasks.append({"text": new_task, 'done': False})

    task_entry.delete(0, END)

    result_label["text"] = "Задача Добавленна успешно."

    update_tasks_list()

def choose_random_task():
    active_tasks = []

    for task in Tasks:
        if task['done'] == False:
            active_tasks.append(task)
    if len(active_tasks) == 0:
        result_label["text"] = "Нет активных задач."
        return
    random_task = random.choice(active_tasks)
    result_label["text"] = f"Твоя задача на час: {random_task['text']}"

def mark_task():
    task_number = number_entry.get()
    if task_number.isdecimal():
        task_index = int(task_number) - 1

        if 0 <= task_index < len(Tasks):
            Tasks[task_index]['done'] = True
            result_label["text"] = "Задача выполнена"
            update_tasks_list()
        else:
            result_label["text"] = "Задачаи с указанным номером нет."
    else:
        result_label["text"] = "Неправильное значение ввода. (введи номер задачи)"

def delete_task():
    global Tasks
    old_count = len(Tasks)
    Tasks = [task for task in Tasks if task['done'] == False]
    deleted_count = old_count - len(Tasks)
    result_label["text"] = f"Удаленно {deleted_count} задач(а)"
    update_tasks_list()

root = Tk() # Создаём окно root - название которое мы применяемм для работы с окном
root.title("Личное приложение") # Заголовок приложения
root.geometry("720x480+300+150") # Разрешение экрана (300х300+100+100) делаем смещение на 100

title_label = ttk.Label(root, text="Моё приложение для практики программирования на Python.")
title_label.pack(pady=12)

task_entry = ttk.Entry(root, width=60)
task_entry.pack(pady=5)

add_button = ttk.Button(root, text="Добавить новую задачу", command=add_task)
add_button.pack(pady=5)

random_button = ttk.Button(root, text="Выбрать случайную задачу.", command=choose_random_task)
random_button.pack(pady=5)

number_entry = ttk.Entry(root, width=20)
number_entry.pack(pady=5)

done_button = ttk.Button(root, text="Выполнить задачу", command=mark_task)
done_button.pack(pady=5)

delete_button = ttk.Button(root, text="Удалить выполненые задачи", command=delete_task)
delete_button.pack(pady=5)

task_list = Text(root, width=80, height=15)
task_list.pack(pady=10)

result_label = ttk.Label(root, text="Выбери действие.")
result_label.pack(pady=6)

update_tasks_list()

root.mainloop()