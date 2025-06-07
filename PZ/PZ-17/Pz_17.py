#В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
#его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
#приближенный к оригиналу (см. таблицу 1).

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Анкета Web-разработчика")

frame = tk.Frame(root, padx=10, pady=10)
frame.grid()

tk.Label(frame, text="Анкета Web-разработчика", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)

tk.Label(frame, text="Регистрационное имя").grid(row=1, column=0, sticky="e")
entry_username = tk.Entry(frame)
entry_username.grid(row=1, column=1, columnspan=2, sticky="we")

tk.Label(frame, text="Пароль").grid(row=2, column=0, sticky="e")
entry_password = tk.Entry(frame, show="*")
entry_password.grid(row=2, column=1, sticky="we")

tk.Label(frame, text="Подтвердите пароль").grid(row=2, column=2, sticky="w")
entry_confirm = tk.Entry(frame, show="*")
entry_confirm.grid(row=3, column=1, columnspan=2, sticky="we")

tk.Label(frame, text="Ваша специализация").grid(row=4, column=0, sticky="e")
specialization = ttk.Combobox(frame, values=["Web-мастер", "Backend", "Frontend", "Fullstack"])
specialization.current(0)
specialization.grid(row=4, column=1, columnspan=2, sticky="we")

tk.Label(frame, text="Пол").grid(row=5, column=0, sticky="e")
gender_var = tk.StringVar()
tk.Radiobutton(frame, text="М", variable=gender_var, value="M").grid(row=5, column=1, sticky="w")
tk.Radiobutton(frame, text="Ж", variable=gender_var, value="F").grid(row=5, column=1)

tk.Label(frame, text="Ваши навыки").grid(row=6, column=0, sticky="ne")
skills = [
    "знание HTML и CSS", "знание Perl", "знание ASP", "знание Adobe Photoshop",
    "знание JAVA", "знание JavaScript", "знание Flash"
]
skill_vars = []
skills_frame = tk.Frame(frame)
skills_frame.grid(row=6, column=1, columnspan=2, sticky="w")
for i, skill in enumerate(skills):
    var = tk.BooleanVar()
    tk.Checkbutton(skills_frame, text=skill, variable=var).grid(row=i, sticky="w")
    skill_vars.append(var)

tk.Label(frame, text="Дополнительные сведения о себе").grid(row=7, column=0, sticky="ne", pady=10)
extra_text = tk.Text(frame, height=5, width=40)
extra_text.grid(row=7, column=1, columnspan=2, pady=10)

tk.Button(frame, text="зарегистрировать").grid(row=8, column=1, sticky="e", pady=10)
tk.Button(frame, text="очистить форму").grid(row=8, column=2, sticky="w", pady=10)

root.mainloop()