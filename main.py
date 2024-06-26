import tkinter as tk
from tkinter import messagebox

def zadanie_1(entry1, entry2, result_label):
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    
    bin_num1 = format(num1, '08b')
    bin_num2 = format(num2, '08b')
    
    result = num1 + num2
    bin_result = format(result, '09b')
    
    carryFlag = int(result > 255)
    
    result_text = (f"Pierwsza liczba w binarnym: {bin_num1}\nDruga liczba w binarnym: {bin_num2}\n"
                   f"Wynik dodawania w binarnym: {bin_result}\nFlaga przeniesienia (CF): {carryFlag}")
    result_label.config(text=result_text)

def zadanie_2(entry1, entry2, result_label):
    ax = int(entry1.get())
    bx = int(entry2.get())
    
    result = 1 if ax < bx else 0
    result_label.config(text=f"Wartość tego rejestru to: {result}")

def zadanie_3(entry, result_label):
    ram = int(entry.get())
    pary = (ram // 16) + 1
    result_label.config(text=f"Liczba tych par to: {pary}")

def zadanie_4(entry1, entry2, entry3, result_label):
    wiersz = int(entry1.get())
    kolumna = int(entry2.get())
    szerokosc = int(entry3.get())
    
    obraz = wiersz * szerokosc + kolumna + 655360
    result_label.config(text=f"Wartość dziesiętna RAM to: {obraz}")

def zadanie_5(entry, result_label):
    sp = int(entry.get())
    result = sp - 4
    result_label.config(text=f'Wartość rejestru SP = {result}')

def main():
    root = tk.Tk()
    root.title("Zadania")
    
    label = tk.Label(root, text="Które zadanie potrzebujesz policzyć?")
    label.pack(pady=10)

    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    frame1 = tk.Frame(root)
    frame1.pack(pady=5)
    tk.Label(frame1, text="Zadanie 1: Podaj dwie liczby (0-255)").pack()
    entry1_1 = tk.Entry(frame1)
    entry1_1.pack()
    entry1_2 = tk.Entry(frame1)
    entry1_2.pack()
    btn1 = tk.Button(frame1, text="Oblicz", command=lambda: zadanie_1(entry1_1, entry1_2, result_label))
    btn1.pack()

    frame2 = tk.Frame(root)
    frame2.pack(pady=5)
    tk.Label(frame2, text="Zadanie 2: Podaj wartość rejestrów AX i BX").pack()
    entry2_1 = tk.Entry(frame2)
    entry2_1.pack()
    entry2_2 = tk.Entry(frame2)
    entry2_2.pack()
    btn2 = tk.Button(frame2, text="Oblicz", command=lambda: zadanie_2(entry2_1, entry2_2, result_label))
    btn2.pack()

    frame3 = tk.Frame(root)
    frame3.pack(pady=5)
    tk.Label(frame3, text="Zadanie 3: Podaj wartość ram").pack()
    entry3 = tk.Entry(frame3)
    entry3.pack()
    btn3 = tk.Button(frame3, text="Oblicz", command=lambda: zadanie_3(entry3, result_label))
    btn3.pack()

    frame4 = tk.Frame(root)
    frame4.pack(pady=5)
    tk.Label(frame4, text="Zadanie 4: Podaj indeks wiersza, kolumny i szerokość").pack()
    entry4_1 = tk.Entry(frame4)
    entry4_1.pack()
    entry4_2 = tk.Entry(frame4)
    entry4_2.pack()
    entry4_3 = tk.Entry(frame4)
    entry4_3.pack()
    btn4 = tk.Button(frame4, text="Oblicz", command=lambda: zadanie_4(entry4_1, entry4_2, entry4_3, result_label))
    btn4.pack()

    frame5 = tk.Frame(root)
    frame5.pack(pady=5)
    tk.Label(frame5, text="Zadanie 5: Podaj wartość rejestru SP").pack()
    entry5 = tk.Entry(frame5)
    entry5.pack()
    btn5 = tk.Button(frame5, text="Oblicz", command=lambda: zadanie_5(entry5, result_label))
    btn5.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
