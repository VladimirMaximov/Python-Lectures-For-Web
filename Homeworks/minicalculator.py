import tkinter as tk
from tkinter import messagebox


class StartFrame(tk.Frame):
    def __init__(self, window: tk.Tk):
        tk.Frame.__init__(self, window)
        self.window = window
        self.set_window()
        self.set_elements()
        self.pack()

    def set_elements(self):
        up_frame = tk.Frame(self.window)
        up_frame.pack(side="top", expand=1)

        down_frame = tk.Frame(self.window)
        down_frame.pack(side="top", fill="both", expand=1)

        left_label = tk.Label(up_frame, width=20, height=1, text="Число a: ",
                              font=("Times New Roman", 14))
        left_label.pack(side="left")

        from_entry = tk.Entry(up_frame, width=20,
                              font=("Times New Roman", 14))
        from_entry.pack(side="left")

        right_label = tk.Label(up_frame, width=20, height=1, text="Число b: ",
                               font=("Times New Roman", 14))
        right_label.pack(side="left")

        to_entry = tk.Entry(up_frame, width=20,
                            font=("Times New Roman", 14))
        to_entry.pack(side="left")

        def generate_number(operation: str):
            try:
                a = int(from_entry.get() if from_entry.get() != "" else 0)
                b = int(to_entry.get() if from_entry.get() != "" else 0)

                if a < 0 or b < 0:
                    raise Exception("Числа должны быть больше 0")

                if operation == "+":
                    messagebox.showinfo("Info", str(a + b))
                elif operation == "-":
                    messagebox.showinfo("Info", str(a - b))
                elif operation == "*":
                    messagebox.showinfo("Info", str(a * b))
                elif operation == "**":
                    messagebox.showinfo("Info", str(a ** b))
                elif operation == "//":
                    messagebox.showinfo("Info", str(a // b))
                else:
                    messagebox.showinfo("Info", str(a % b))


            except ValueError:
                messagebox.showerror("Error", "Введите натуральные числа!")

            except Exception as e:
                messagebox.showerror("Error", str(e))

        button_start1 = tk.Button(down_frame, text="a+b", font=("Times New Roman", 14),
                                  relief="solid", activebackground='black',
                                  activeforeground="white", command=lambda: generate_number("+"))
        button_start2 = tk.Button(down_frame, text="a-b", font=("Times New Roman", 14),
                                  relief="solid", activebackground='black',
                                  activeforeground="white", command=lambda: generate_number("-"))
        button_start3 = tk.Button(down_frame, text="a*b", font=("Times New Roman", 14),
                                  relief="solid", activebackground='black',
                                  activeforeground="white", command=lambda: generate_number("*"))
        button_start4 = tk.Button(down_frame, text="a**b", font=("Times New Roman", 14),
                                  relief="solid", activebackground='black',
                                  activeforeground="white", command=lambda: generate_number("**"))
        button_start5 = tk.Button(down_frame, text="a//b", font=("Times New Roman", 14),
                                  relief="solid", activebackground='black',
                                  activeforeground="white", command=lambda: generate_number("//"))
        button_start6 = tk.Button(down_frame, text="a%b", font=("Times New Roman", 14),
                                  relief="solid", activebackground='black',
                                  activeforeground="white", command=lambda: generate_number("%"))

        button_start1.pack()
        button_start2.pack()
        button_start3.pack()
        button_start4.pack()
        button_start5.pack()
        button_start6.pack()

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
