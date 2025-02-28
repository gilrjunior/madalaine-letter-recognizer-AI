from tkinter import *
from tkinter import ttk
from controller import *
from madalaine import Madaline

def interface():

    madaline = Madaline(0.0, [[],[]])

    geometry = "600x700"

    root = Tk()
    root.title("Madaline")
    root.geometry(geometry)
    root.configure(bg="#F0F0F0")

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("TFrame", background="#F0F0F0")

    style.configure("TLabel",
                    background="#F0F0F0",
                    foreground="#333333",
                    font=("Arial", 12))

    style.configure("Rounded.TEntry",
                    fieldbackground="white",
                    bordercolor="#CCCCCC",
                    lightcolor="#CCCCCC", 
                    foreground="#000000",
                    padding=5,
                    borderwidth=2,
                    relief="solid")

    style.layout("Rounded.TEntry",
        [
            ("Entry.border", {
                "sticky": "nswe",
                "children": [
                    ("Entry.padding", {
                        "sticky": "nswe",
                        "children": [
                            ("Entry.textarea", {"sticky": "nswe"})
                        ]
                    })
                ]
            })
        ]
    )
    
    style.configure("Red.TButton",
        foreground="white",
        background="#FF0000",
        padding=5,
        borderwidth=2,
        relief="solid",
        anchor="center"
    )

    style.map("Red.TButton",
        foreground=[("active", "black")],
        background=[("active", "white")]
    )


    style.layout("Red.TButton",
        [
            ("Button.border", {
                "sticky": "nswe",
                "children": [
                    ("Button.padding", {
                        "sticky": "nswe",
                        "children": [
                            ("Button.label", {"sticky": "nswe"})
                        ]
                    })
                ]
            })
        ]
    )

    container = ttk.Frame(root)
    container.pack(expand=True, fill="both")

    frm = ttk.Frame(container, padding=10, style="TFrame")
    frm.pack(anchor="center")

    learn_rate_label = ttk.Label(frm, text="Taxa de Aprendizado:")
    learn_rate_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    learn_rate_entry = ttk.Entry(frm, style="Rounded.TEntry", width=25, font=("Arial", 12))
    learn_rate_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    option_cb = ttk.Combobox(frm,
                             values=["Número de Ciclos", "Erro Tolerado"],
                             font=("Arial", 12),
                             width=15,
                             state="readonly")
    option_cb.current(0)
    option_cb.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    option_entry = ttk.Entry(frm, style="Rounded.TEntry", width=25, font=("Arial", 12))
    option_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    trn_frm = ttk.Frame(container, style="TFrame")
    trn_frm.pack(anchor="center")

    btn = ttk.Button(trn_frm,
                     text="Treinar",
                     style="Red.TButton",
                     command=lambda: start_training(learn_rate_entry, [option_cb, option_entry], madaline),
                     width=20)
    btn.grid(row=3, column=0, columnspan=2, padx=5, pady=20, sticky="w")

    matrix_frm = ttk.Frame(container, padding=10, style="TFrame")
    matrix_frm.pack(anchor="center")

    row = 4
    column = 0
    matrix = []

    for r in range(row, row+9):
        row_array = []
        for c in range(column, 7):
            value = IntVar()  
            matrix_cb = ttk.Checkbutton(matrix_frm, variable=value)
            matrix_cb.grid(row=r, column=c, padx=3, pady=3)
            row_array.append(value)
        matrix.append(row_array)
            
    mid_frm = ttk.Frame(container, style="TFrame")
    mid_frm.pack(anchor="center")

    clr_btn = ttk.Button(mid_frm,
                     text="Limpar",
                     style="Red.TButton",
                     command=lambda: clear_matrix(matrix),
                     width=20)
    clr_btn.grid(row=14, column=0, columnspan=2, padx=5, pady=10, sticky="w")

    preset_frm = ttk.Frame(container, style="TFrame")
    preset_frm.pack(anchor="center")

    preset_label = ttk.Label(preset_frm, text="Preset:")
    preset_label.grid(row=15, column=0, padx=5, pady=5, sticky="w")

    preset_cb = ttk.Combobox(preset_frm,
                             values=["A1", "B1", "C1", "D1", "E1", "J1", "K1",
                                     "A2", "B2", "C2", "D2", "E2", "J2", "K2",
                                     "A3", "B3", "C3", "D3", "E3", "J3", "K3"],
                             font=("Arial", 12),
                             width=15,
                             state="readonly")
    preset_cb.grid(row=15, column=1, padx=5, pady=5, sticky="w")

    preset_cb.bind("<<ComboboxSelected>>", lambda event: set_matrix_value(preset_cb, matrix))

    bottom_frm = ttk.Frame(container, style="TFrame")
    bottom_frm.pack(anchor="center")

    v_btn = ttk.Button(bottom_frm,
                     text="Identificar Letra",
                     style="Red.TButton",
                     width=20,
                     command=lambda: start_model(matrix, madaline, letter_text_label))
    v_btn.grid(row=16, column=0, columnspan=3, padx=5, pady= 10, sticky="w")

    letter_label = ttk.Label(bottom_frm, text="Letra", anchor="center", width=15)
    letter_label.grid(row=17, column=0, padx=5, pady=5, sticky="w")

    letter_text_label = ttk.Label(bottom_frm, text="?", font=("Arial", 12, "bold"), anchor="center", width=15)
    letter_text_label.grid(row=18, column=0, padx=5, pady=5, sticky="w")

    root.mainloop()
