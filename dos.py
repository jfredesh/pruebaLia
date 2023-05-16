import tkinter as tk
import random

class MathTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Prueba de Matemáticas")
        self.root.configure(bg=COLOR_GOLD)

        self.questions_left = 10
        self.correct_count = 0
        self.incorrect_count = 0

        self.label_question = tk.Label(self.root, text="", font=("Arial", 24), bg=COLOR_GOLD, fg=COLOR_PURPLE)
        self.label_question.pack(pady=20)

        self.entry_answer = tk.Entry(self.root, font=("Arial", 18))
        self.entry_answer.pack(pady=10)

        self.label_feedback = tk.Label(self.root, text="", font=("Arial", 18), bg=COLOR_GOLD, fg=COLOR_PURPLE)
        self.label_feedback.pack(pady=10)

        self.button_confirm = tk.Button(self.root, text="Confirmar", command=self.check_answer, bg=COLOR_MAGENTA, fg="white")
        self.button_confirm.pack(pady=10)

        self.button_start = tk.Button(self.root, text="Comenzar", command=self.start_test, bg=COLOR_MAGENTA, fg="white")
        self.button_start.pack(pady=10)

        self.label_nota = tk.Label(self.root, text="", font=("Arial", 24), bg=COLOR_GOLD, fg=COLOR_PURPLE)
        self.label_nota.pack(pady=20)

        self.button_restart = tk.Button(self.root, text="Reiniciar", command=self.restart_test, bg=COLOR_MAGENTA, fg="white")

    def start_test(self):
        self.button_start.config(state=tk.DISABLED)
        self.ask_question()

    def ask_question(self):
        factor1 = random.randint(1, 9)
        factor2 = random.randint(1, 9)
        self.correct_answer = factor1 * factor2

        self.label_question.config(text=f"{factor1} x {factor2} = ")
        self.label_feedback.config(text="")

        self.entry_answer.delete(0, tk.END)
        self.entry_answer.focus()

        self.start_timer()

    def start_timer(self):
        self.timer = self.root.after(30000, self.timeout)

    def stop_timer(self):
        if self.timer:
            self.root.after_cancel(self.timer)

    def check_answer(self):
        self.stop_timer()

        user_answer = self.entry_answer.get()

        if user_answer.isdigit() and int(user_answer) == self.correct_answer:
            self.label_feedback.config(text="¡Correcto!", fg=COLOR_GREEN)
            self.correct_count += 1
        else:
            self.label_feedback.config(text="Incorrecto", fg=COLOR_RED)
            self.incorrect_count += 1

        self.questions_left -= 1

        if self.questions_left > 0:
            self.root.after(2000, self.ask_question)
        else:
            self.show_summary()

    def timeout(self):
        self.label_feedback.config(text="Tiempo agotado", fg=COLOR_RED)
        self.incorrect_count += 1
        self.questions_left -= 1
        if self.questions_left > 0:
            self.root.after(2000, self.ask_question)
        else:
            self.show_summary()
    def show_summary(self):
        self.label_question.config(text="Resumen:")
        self.label_feedback.config(text=f"Correctas: {self.correct_count}\nIncorrectas: {self.incorrect_count}", fg=COLOR_BLACK)
        self.label_nota.config(text=f"La nota final es: {round(self.correct_count * 0.7, 2)}", fg=COLOR_BLACK)
        self.entry_answer.config(state=tk.DISABLED)
        self.button_confirm.config(state=tk.DISABLED)
        self.button_restart.pack(pady=10)

    def restart_test(self):
        self.questions_left = 10
        self.correct_count = 0
        self.incorrect_count = 0
        self.label_nota.config(text="")
        self.button_restart.pack_forget()
        self.start_test()

# Colores y estilos
COLOR_GOLD = "#FFD700"
COLOR_PURPLE = "#800080"
COLOR_MAGENTA = "#FF00FF"
COLOR_GREEN = "green"
COLOR_RED = "red"
COLOR_BLACK = "black"

root = tk.Tk()
app = MathTest(root)
root.mainloop()

