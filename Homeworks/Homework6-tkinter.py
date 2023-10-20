import tkinter as tk
from Homework6 import *


class StartFrame(tk.Frame):

    def __init__(self, parent: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.set_window()
        self.create_elements()
        self.pack(expand=1, fill="both")

    def create_elements(self):
        leftFrame = tk.Frame(self, background="white")
        leftFrame.pack(side="left", fill="y")
        text = tk.Text(leftFrame, width=10, height=20, bd=2, relief="solid", font=("Times New Roman", 14),
                       state=tk.DISABLED)
        text.pack(side="top", fill="both", expand=1)

        def create_disc():
            # Очищаем холст и перерисовываем все точки
            canv.delete("all")
            [create_point(point.x, point.y) for point in listOfPoints]

            # Ищем окружность и рисуем её
            if len(listOfPoints) != 0:
                disc: Disc = minDisc(listOfPoints)
                canv.create_oval(disc.center.x + disc.r, disc.center.y + disc.r,
                                 disc.center.x - disc.r, disc.center.y - disc.r)
            return True

        button = tk.Button(leftFrame, height=3, width=25, bd=2, relief="solid", activebackground='black',
                           text="Построить окружность", font=("Times New Roman", 14), activeforeground="white",
                           command=lambda: create_disc())
        button.pack(side="top", fill="both", pady=(1, 0))

        rightFrame = tk.Frame(self, background="white")
        rightFrame.pack(side="left", fill="both", expand=1)

        listOfPoints = []

        def insert_text():
            text.configure(state=tk.NORMAL)
            text.delete(1.0, tk.END)
            [text.insert(f"{i + 1}.0", str(listOfPoints[i]) + "\n") for i in range(len(listOfPoints))]
            text.configure(state=tk.DISABLED)

        def draw_point(x, y):
            canv.create_oval(x - 2, y - 2, x + 3, y + 3, fill="black")

        def create_point_and_append(x, y):
            listOfPoints.append(Point(x, y))
            insert_text()
            draw_point(x, y)

        def create_point(x, y):
            insert_text()
            draw_point(x, y)

        canv = tk.Canvas(rightFrame)
        canv.bind("<Button-1>", lambda e: create_point_and_append(e.x, e.y))
        canv.pack(fill="both", expand=1)

    def set_window(self):
        width = 1000
        height = 600

        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()

        x = (screen_width - width) / 2
        y = (screen_height - height) / 2

        self.parent.geometry(f"{width}x{height}+{int(x)}+{int(y)}")


def main():
    window = tk.Tk()
    StartFrame(window)
    window.mainloop()


if __name__ == "__main__":
    main()
