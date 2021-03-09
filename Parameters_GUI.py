import tkinter as tk
from tkinter import ttk
import json


class MainApplication(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("Parameters")
        self.master.geometry("500x200")
        self.master.tk_setPalette(background="#000000")

        def get_json():
            with open("parameters.json") as f:
                d = json.load(f)
                name = par_ent.get()
                units = unit_ent.get()
                min = min_ent.get()
                max = max_ent.get()
                data = {"Name": name, "Units": units, "Min": min, "Max": max}
                data = {name: {"Units": units, "Min": min, "Max": max}}
                d.update(data)

            if (data[str(name)]["Min"]) == "":
                del data[str(name)]["Min"]
            if (data[str(name)]["Max"]) == "":
                del data[str(name)]["Max"]

            with open("parameters.json", "w") as f:
                json.dump(d, f, indent=4)

        lbls_frm = tk.Frame(self)
        lbls_frm.pack(padx=15, pady=15)

        par_lbl = tk.Label(lbls_frm, text="Parameters", fg="#c28e0e", width=15)
        par_lbl.pack(side="left", padx=2)
        unit_lbl = tk.Label(lbls_frm, text="Units", fg="#c28e0e", width=15)
        unit_lbl.pack(side="left", padx=2)
        min_lbl = tk.Label(lbls_frm, text="Minimum", fg="#c28e0e", width=15)
        min_lbl.pack(side="left", padx=2)
        max_lbl = tk.Label(lbls_frm, text="Maximum", fg="#c28e0e", width=15)
        max_lbl.pack(side="left", padx=2)

        ent_frm = tk.Frame(self)
        ent_frm.pack(padx=15, pady=15)

        par_ent = tk.Entry(ent_frm, bg="white", fg="#000000", width=15)
        par_ent.pack(side="left", padx=10)
        unit_ent = tk.Entry(ent_frm, bg="white", fg="#000000", width=15)
        unit_ent.pack(side="left", padx=10)
        min_ent = tk.Entry(ent_frm, bg="white", fg="#000000", width=15)
        min_ent.pack(side="left", padx=10)
        max_ent = tk.Entry(ent_frm, bg="white", fg="#000000", width=15)
        max_ent.pack(side="left", padx=10)

        but_frm = tk.Frame(self)
        but_frm.pack(padx=15, pady=20)

        sub_but = tk.Button(
            but_frm,
            text="Add to JSON",
            command=get_json,
            bg="black",
            fg="#c28e0e",
            width=10,
        )
        sub_but.pack(padx=15)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    app.mainloop()