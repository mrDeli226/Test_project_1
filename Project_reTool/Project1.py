from tkinter import *
from tkinter import ttk
import random
import json
import os

Tasks = [
    {"text": "Задача: Создать калькулятор", 'done': False},
    {"text": "Задача: Написать генератор паролей", 'done': False},
    {"text": "Задача: Написать игру угадай число", 'done': False},
    {"text": "Задача: Созадть список дел", 'done': False},
    {"text": "Задача: Создать простой дневник", 'done': False}
]

# Код ошибки 01 - Ошибка: отстутсвие самого файла.
def json_chek_file():
    if os.path.exists("Tasks.json"):
        print("Файл существует проводим запрос на обновление списка")
        update_tasks_list()
    else:
        print("Код ошибки 01, процесс создания файла.")
        with open("Tasks.json", "w", encoding="utf-8") as file_cheker:
            json.dump(Tasks, file_cheker, ensure_ascii=False, indent=4)
        update_tasks_list()

def read_files():
    if os.path.exists("Tasks.json"):
        with open("Tasks.json", "r", encoding="utf-8") as file_read:
            return json.load(file_read)
    else:
        print("Code 01")
        json_chek_file()

def load_file():
    if Tasks == "1":
        print ("Hi")
    else:
        print ("NO")

def update_tasks_list():

    for_list=read_files()
    task_list.delete('1.0', END)

    if len(for_list) == 0:
        task_list.insert(END, "Список задач пуст.")
        return
    
    for index, task in enumerate(for_list, start=1):
        status = "[X]" if task['done'] else "[]"
        task_list.insert(END, f"{index}. {status} {task["text"]}\n")

def add_task():

    new_task = task_entry.get()

    if new_task.strip() == "":
       result_label["text"] = "Ошибка значения (возможно поле вода пусто)"
       return
    Save_up_tsk = read_files()
    Update_tasks=({"text": new_task, 'done': False})

    task_entry.delete(0, END) # не забывай - тут чистим строку ввода
   
    Save_up_tsk.append(Update_tasks)
    
    with open("Tasks.json", "w", encoding="utf-8") as task_add:
        json.dump(Save_up_tsk, task_add, ensure_ascii= False, indent=4)

    result_label["text"] = "Задача Добавленна успешно."

    update_tasks_list()

def choose_random_task(): #выбирираем рандомнную задачу
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
        Update_tasks = read_files()
        if 0 <= task_index < len(Update_tasks):
            
            Update_tasks[task_index]['done'] = True
            result_label["text"] = "Задача выполнена"
            with open("Tasks.json", "w", encoding="utf-8") as mark:
                json.dump(Update_tasks, mark, ensure_ascii=False, indent=4)
            update_tasks_list()
        else:
            result_label["text"] = "Задачаи с указанным номером нет."
    else:
        result_label["text"] = "Неправильное значение ввода. (введи номер задачи)"

def delete_task():
    Update_tasks = read_files()
    old_count = len(Update_tasks)
    Update_tasks = [task for task in Update_tasks if task['done'] == False]
    deleted_count = old_count - len(Update_tasks)
    with open("Tasks.json", 'w', encoding="utf-8") as delit_task:
        json.dump(Update_tasks, delit_task, ensure_ascii=False, indent=4)
    result_label["text"] = f"Удаленно {deleted_count} задач(а)"
    update_tasks_list()


root = Tk() # Создаём окно root - название которое мы применяемм для работы с окном
root.title("Личное приложение") # Заголовок приложения
root.geometry("720x600+300+150") # Разрешение экрана (300х300+100+100) делаем смещение на 100

#root.resizable(False, True) интересное решение

title_label = ttk.Label(root, text="Моё приложение для практики программирования на Python.")
title_label.pack(pady=12)

tasks_load = ttk.Button(root, text="Загрузить список задач", command=update_tasks_list)
tasks_load.pack(pady=5)

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

json_chek_file()


root.mainloop()