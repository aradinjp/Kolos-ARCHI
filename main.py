import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog

def zadanie_1():
    num1 = simpledialog.askinteger("Zadanie 1", "Podaj pierwszą liczbę (0-255)", minvalue=0, maxvalue=255)
    num2 = simpledialog.askinteger("Zadanie 1", "Podaj drugą liczbę (0-255)", minvalue=0, maxvalue=255)
    
    if num1 is not None and num2 is not None:
        bin_num1 = format(num1, '08b')
        bin_num2 = format(num2, '08b')
        
        result = num1 + num2
        bin_result = format(result, '09b')
        
        carryFlag = int(result > 255)
        
        messagebox.showinfo("Wynik", f"Pierwsza liczba w binarnym: {bin_num1}\nDruga liczba w binarnym: {bin_num2}\nWynik dodawania w binarnym: {bin_result}\nFlaga przeniesienia (CF): {carryFlag}")

def zadanie_2():
    ax = simpledialog.askinteger("Zadanie 2", "Podaj wartość rejestru AX")
    bx = simpledialog.askinteger("Zadanie 2", "Podaj wartość rejestru BX")
    
    if ax is not None and bx is not None:
        result = 1 if ax < bx else 0
        messagebox.showinfo("Wynik", f"Wartość tego rejestru to: {result}")

def zadanie_3():
    ram = simpledialog.askinteger("Zadanie 3", "Podaj wartość ram dla którego chcesz określić liczbę par SEGMENT:OFFSET")
    if ram is not None:
        pary = (ram // 16) + 1
        messagebox.showinfo("Wynik", f"Liczba tych par to: {pary}")


def zadanie_4():
    wiersz = simpledialog.askinteger("Zadanie 4", "Podaj indeks wiersza")
    kolumna = simpledialog.askinteger("Zadanie 4", "Podaj indeks kolumny")
    szerokosc = simpledialog.askinteger("Zadanie 4", "Podaj szerokość rozdzielczości (pierwsza liczba w rozdzielczości)")
    
    if wiersz is not None and kolumna is not None and szerokosc is not None:
        obraz = wiersz * szerokosc + kolumna + 655360
        messagebox.showinfo("Wynik", f"Wartość dziesiętna RAM to: {obraz}")
        
def zadanie_5():
    sp = simpledialog.askinteger("Zadanie 5", "Podaj wartosć rejestru SP przed wykonaniem")
    if sp is not None:
        result = sp - 4
        messagebox.showinfo("Wynik", f'Wartosc rejestru SP = {result}')

def main():
    root = tk.Tk()
    root.title("Zadania")
    
    label = tk.Label(root, text="Które zadanie potrzebujesz policzyć?")
    label.pack(pady=10)

    btn1 = tk.Button(root, text="Zadanie 1", command=zadanie_1)
    btn1.pack(pady=5)

    btn2 = tk.Button(root, text="Zadanie 2", command=zadanie_2)
    btn2.pack(pady=5)

    btn3 = tk.Button(root, text="Zadanie 3", command=zadanie_3)
    btn3.pack(pady=5)

    btn4 = tk.Button(root, text="Zadanie 4", command=zadanie_4)
    btn4.pack(pady=5)
    
    btn5 = tk.Button(root, text="Zadanie 5", command=zadanie_5)
    btn5.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
