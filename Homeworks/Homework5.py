import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class StartFrame(tk.Frame):

    def __init__(self, parent: tk.Tk):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.set_window()
        self.create_elements()
        self.pack(expand=1, fill="both")

    def create_elements(self):
        head_frame = tk.Frame(self)
        head_frame.pack(side="top")
        left_button = tk.Button(head_frame,
                                text="<",
                                width=10
                                )
        left_button.pack(side="left")

        page_count = tk.Entry(head_frame,
                              width=5,
                              justify="right")
        page_count.insert(0, "1")
        page_count.pack(side="left")
        count_of_pages_label = tk.Label(head_frame,
                                        text="/1741"
                                        )
        count_of_pages_label.pack(side="left")
        right_button = tk.Button(head_frame,
                                 text=">",
                                 width=10
                                 )
        right_button.pack(side="left")

        down_frame = tk.Frame(self)
        down_frame.pack(side="top", expand=1, fill="both")

        picture_frame = tk.Frame(down_frame)
        picture_frame.pack(side="left")
        picture = ImageTk.PhotoImage(Image.open("picture.png"))
        picture_label = tk.Label(picture_frame,
                                 image=picture)
        picture_label.image = picture
        picture_label.pack()
        # picture = tk.PhotoImage(picture_frame)

        text_frame = tk.Frame(down_frame)
        text_frame.pack(side="left")
        header_frame = tk.Frame(text_frame)
        header_frame.pack(side="top")
        main_label = tk.Label(header_frame,
                              text="Overland",
                              font=("Times New Roman", 40)
                              )
        main_label.pack()

        show_download_frame = tk.Frame(text_frame)
        show_download_frame.pack(side="top")
        show_button = tk.Button(show_download_frame,
                                text="Show",
                                width=10)
        show_button.pack(side="left")
        download_button = tk.Button(show_download_frame,
                                    text="Download",
                                    width=10)
        download_button.pack(side="left")

        subsection_frame = tk.Frame(text_frame)
        subsection_frame.pack(side="top")
        second_label = tk.Label(subsection_frame,
                                text="A squad-based survival strategy game with procedurally \n"
                                     "generated levels set in post-apocalyptic North America.",
                                font=("Times New Roman", 10))
        second_label.pack()

        list_frame = tk.Frame(text_frame)
        list_frame.pack(side="top")
        combobox = ttk.Combobox(list_frame)
        combobox.pack()

        buttons_frame = tk.Frame(text_frame)
        buttons_frame.pack(side="top")
        button_1 = tk.Button(buttons_frame,
                             text="genre:roguelite")
        button_1.pack(side="left")
        button_2 = tk.Button(buttons_frame,
                             text="genre:tactics")
        button_2.pack(side="left")
        button_3 = tk.Button(buttons_frame,
                             text="os:pc")
        button_3.pack(side="left")
        button_4 = tk.Button(buttons_frame,
                             text="players:1")
        button_4.pack(side="left")
        button_5 = tk.Button(buttons_frame,
                             text="theme:apocalypsis")
        button_5.pack(side="left")
        button_6 = tk.Button(buttons_frame,
                             text="type:videogame")
        button_6.pack(side="left")

    def set_window(self):
        width = 1000
        height = 400

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
