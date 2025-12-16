import tkinter as tk

# Functie om een cijfer toe te voegen aan de invoer
def toevoegen_cijfer(cijfer):
    invoer.insert(tk.END, cijfer)

# Functie om de berekening uit te voeren
def bereken():
    try:
        resultaat = eval(invoer.get())
        invoer.delete(0, tk.END)
        invoer.insert(tk.END, str(resultaat))
    except Exception as e:
        invoer.delete(0, tk.END)
        invoer.insert(tk.END, "Fout")

# Maak een tkinter-venster
venster = tk.Tk()
venster.title("Rekenmachine")

# Invoerveld
invoer = tk.Entry(venster, width=20)
invoer.grid(row=0, column=0, columnspan=4)

# Knoppen voor cijfers en operaties
knoppen = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

rij, kolom = 1, 0

for knop in knoppen:
    tk.Button(venster, text=knop, command=lambda k=knop: toevoegen_cijfer(k) if k != "=" else bereken()).grid(row=rij, column=kolom)
    kolom += 1
    if kolom > 3:
        kolom = 0
        rij += 1

# Start de GUI-loop
venster.mainloop()
