import tkinter as tk
import mysql.connector as sql

HEIGHT = 393
WIDTH = 700

slownik1 = ["Piotr", "Dupa", "Penis"]
slownik2 = ["debil", "Arsch", "Kutas"]

root = tk.Tk()
root.title("Deutsch Mit Peppa Wutz")

#obsługa bazy danych

mydb = sql.connect(
    host = "localhost",
    user = "root",
    passwd = "Montekija3",
    database = "peppa2"
)

mcr = mydb.cursor()               #my cursor

mcr.execute("SELECT slowo, slowo_pol, tytul FROM ger, pol, odc WHERE idodc = odc_idodc AND idpol = pol_idpol")

myresult = mcr.fetchall()

dic_pol = {}
dic_ger = {}
i = 0


#wypelniamy slowniki
for row in myresult:
        dic_ger[i] = row[0]
        dic_pol[i] = row[1]
        i+=1

#funkcje

#wybieranie odcinka

def choose1(elem: any):
    final_list = []
    i = 0
    for i in range(3):

        final_list.append(elem[i])
        i+=1

    print(final_list)
    return final_list

def choose2(elem: any):
    final_list2 = []
    i = 0
    for i in range(3):

        final_list2.append(elem[i+3])
        i+=1

    print(final_list2)
    return final_list2

def choose_odc():
    
    window=tk.Tk()
    window.title("Wybierz odcinek!")
    window.geometry("250x200")
    
    label_1=tk.Label(window,text="Wybierz jeden lub kilka odcinków:")
    label_1.pack()

    #checkboxes
    check1 = tk.Checkbutton(window,  text = "TIEREN", command = lambda: choose1(dic_ger))
    check2 = tk.Checkbutton(window,  text = "KLEIDUNG", command = lambda: choose2(dic_ger))
    check3 = tk.Checkbutton(window,  text = "PFEIFEN", command = lambda: print(final_final))
    check1.pack()
    check2.pack()
    check3.pack()

    #buttons
    confirm_but = tk.Button(window, text = "potwierdz", bg = 'green', command = lambda: guess_the_world())
    confirm_but.place(rely = 0.65, relx = 0.5, anchor = 'n')

    exit_but = tk.Button(window, text = "anuluj", bg = 'red', command =  window.destroy)
    exit_but.place(rely = 0.8, relx = 0.5, anchor = 'n')

    window.mainloop()

#gra w zgadywanie
def guess_the_world():

    window = tk.Tk()
    window.title("Przetłumacz słowo!")
    window.geometry("250x200")

    x = 0

    label_1=tk.Label(window,text="Przetłumacz:")
    label_1.pack()

    label_2=tk.Label(window,text= dic_ger[x])
    label_2.pack()

    wpisz = tk.Entry(window)
    wpisz.place(relx = 0.5, rely = 0.5, relwidth = 0.8, anchor = 'n')

    
    def check(iks):
        if(wpisz.get() == dic_pol[iks]):
            print("DOBRZE")
            iks +=1

    #buttons
    confirm_but = tk.Button(window, text = "potwierdz", bg = 'green', command = lambda: check(x))
    confirm_but.place(rely = 0.65, relx = 0.5, anchor = 'n')
    
    exit_but = tk.Button(window, text = "wyjdź", bg = 'red', command =  window.destroy)
    exit_but.place(rely = 0.8, relx = 0.5, anchor = 'n')

def add_odc():
    print("Dodajesz odcinek!")

def add_slowo():
    print("Dodajesz słowo!")

def zmien_na_polski():
    print("Zmieniasz jezyk na polski.")

def zmien_na_niemiecki():
    print("Zmieniasz jezyk na niemiecki.")

def test():
    print("TO JEST TEST!")

#canvas
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#background
background_image = tk.PhotoImage(file = 'pobrane.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relheight = 1, relwidth = 1)

#DEUTSCH MIT PEPPA WUTZ
title = tk.Label(root, bg = 'pink', text = "DEUTSCH MIT PEPPA WUTZ", font = 500 )
title.place(relx = 0.5, y = 1, relwidth = 0.5, relheight = 0.15, anchor = 'n')


#frames
buttons_frame = tk.Frame(root, bg = 'pink', bd = 5)
buttons_frame.place(relx = 0.15, rely = 0.9, relwidth = 0.25, relheight = 0.1, anchor = 'n')

main_frame = tk.Frame(root, bg = 'pink', bd = 5)
main_frame.place(relx = 0.5, rely = 0.4, relwidth = 0.3, relheight = 0.2, anchor = 'n')

#buttons
wybierz_odc = tk.Button(main_frame, text="wybierz odcinek", bg='#AFEEEE', activebackground = 'pink', fg='black', command = lambda: choose_odc())
wybierz_odc.place(relheight = 1, relwidth = 1)

dodaj_odc = tk.Button(buttons_frame, text="dodaj odcinek", bg='red', activebackground = 'pink', fg='black', command = lambda: add_odc())
dodaj_odc.place(relheight = 1, relwidth = 0.5)

dodaj_slowo = tk.Button(buttons_frame, text="dodaj słowo", bg='#AFEEEE', activebackground = 'pink', fg='black', command = lambda: add_slowo())
dodaj_slowo.place(relx = 0.5, relheight = 1, relwidth = 0.5)

wyjdz = tk.Button(root, text = "WYJDŹ",  bg = 'red', command = root.destroy)
wyjdz.place(relx = 0.9, rely = 0.9)

#languages
R1 = tk.Radiobutton(root, text="polski", val = 0, command = lambda: zmien_na_polski())
R1.place( anchor = 'n', relx = 0.9, rely = 0, relwidth = 0.1)

R2 = tk.Radiobutton(root, text="deutsch", val = 1, command = lambda: zmien_na_niemiecki())
R2.place( anchor = 'n', relx = 0.9, rely = 0.05, relwidth = 0.1)


root.mainloop()
