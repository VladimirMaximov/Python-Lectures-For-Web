import tkinter as tk
from tkinter import messagebox
import random

class StartFrame(tk.Frame):
    def __init__(self, window: tk.Tk):
        tk.Frame.__init__(self, window)
        self.window = window
        self.set_window()
        self.set_elements()

    def set_elements(self):
        up_frame = tk.Frame(self.window)
        up_frame.pack(side="top", expand=1)

        down_frame = tk.Frame(self.window)
        down_frame.pack(side="top", fill="both", expand=1)

        left_label = tk.Label(up_frame, width=20, height=1, text="Левая граница: ",
                              font=("Times New Roman", 14))
        left_label.pack(side="left")

        from_entry = tk.Entry(up_frame, width=20,
                              font=("Times New Roman", 14))
        from_entry.pack(side="left")

        right_label = tk.Label(up_frame, width=20, height=1, text="Правая граница: ",
                               font=("Times New Roman", 14))
        right_label.pack(side="left")

        to_entry = tk.Entry(up_frame, width=20,
                            font=("Times New Roman", 14))
        to_entry.pack(side="left")

        def generate_number():
            try:
                left_border = int(from_entry.get())
                right_border = int(to_entry.get())

                if left_border <= 0 or right_border <= 0:
                    raise Exception("Числа должны быть больше 0")

                if left_border > right_border:
                    raise Exception("Левая граница должна быть меньше или равна правой")

                if right_border - left_border > 100:
                    messagebox.showinfo("Info", "Диапазон больше 100")

                messagebox.showinfo("Случайное число", str(random.randint(left_border, right_border)))

            except ValueError:
                messagebox.showerror("Error", "Введите натуральные числа!")

            except Exception as e:
                messagebox.showerror("Error", str(e))

        button_start = tk.Button(down_frame, text="Сгенерировать", font=("Times New Roman", 14),
                                 relief="solid", activebackground='black',
                                 activeforeground="white", command=generate_number)

        button_start.pack()


    def set_window(self):
        width = 1000
        height = 600

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        x = (screen_width - width) / 2
        y = (screen_height - height) / 2

        self.window.geometry(f"{width}x{height}+{int(x)}+{int(y)}")


def main():
    window = tk.Tk()
    StartFrame(window)
    window.mainloop()

if __name__ == "__main__":
    main()