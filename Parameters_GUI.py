import tkinter as tk


class MainApplication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("Parameters")
        self.master.geometry("600x500")
        self.master.resizable(False, False)
        self.master.tk_setPalette(background="#c28e0e")

        labels_frame = tk.Frame(self)
        labels_frame.pack(padx=15, pady=15)

        tk.Label(labels_frame, text="Parameters", width=15).pack(side="left", padx=2)
        tk.Label(labels_frame, text="Units", width=15).pack(side="left", padx=2)
        tk.Label(labels_frame, text="Minimum", width=15).pack(side="left", padx=2)
        tk.Label(labels_frame, text="Maximum", width=15).pack(side="left", padx=2)

        entry_frame = tk.Frame(self)
        entry_frame.pack(padx=15, pady=0)

        tk.Entry(entry_frame, bg="white", width=15).pack(side="left", padx=10)
        tk.Entry(entry_frame, bg="white", width=15).pack(side="left", padx=10)
        tk.Entry(entry_frame, bg="white", width=15).pack(side="left", padx=10)
        tk.Entry(entry_frame, bg="white", width=15).pack(side="left", padx=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    app.mainloop()
