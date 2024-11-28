import tkinter as tk

def add_item():  #Funkcija preces pievienošanai
    selected_item = dropdown_var.get()  #saglabā izvēlēto apģērbu no nolaižamās izvēlnes
    if selected_item == "Izvēlieties apģērbu": #cikls if, gadījumā, ja nospiesta poga "pievienot", kad izvēlnes logs ir tukšs
        label_message.config(text="Lūdzu izvēlieties apģērbu!", fg="red")
        return

    price = clothes[selected_item] #cikls, kas saskaita apģērba daudzumu
    try:
        quantity = int(entry_quantity.get())
        if quantity <= 0: #ja daudzums ir negatīvs vai nulle, raksta izvēlēties pareizo daudzumu
            raise ValueError
    except ValueError:
        label_message.config(text="Ievadiet korektu daudzumu!", fg="red")
        return

    items.append((selected_item, price, quantity)) #pievieno apģērbu, to cenu un daudzumu sarakstam
    update_summary()
    label_message.config(text=f"{selected_item} pievienots!", fg="green") #liecina par preces veiksmīgu pievienošanu
    entry_quantity.delete(0, tk.END) #dzēs informāciju no ievada laukiem, lai lietotājs varētu tālāk izvēlēties preces

def update_summary(): #funkcija kopsavilkuma atjaunošanai
    total = sum(price * quantity for _, price, quantity in items) #skaita summu
    delivery_fee = 0 if total > 100 else 5 #ja summa ir vairāk par 100 eiro, piegāde par brīvu, savukārt piegādes maksa 5 eiro
    discount = total * 0.1 if total > 100 else 0 #atlaide, ja summa ir vairāk par 100 eiro
    final_total = total - discount + delivery_fee #beigu summa

    summary_text = "\n".join([f"{name}: {quantity} x {price:.2f}€" for name, price, quantity in items]) #atjauno kopsavilkuma tekstu
    summary_text += f"\n\nKopējā summa: {total:.2f}€\nAtlaide: {discount:.2f}€\nPiegāde: {delivery_fee:.2f}€\nGalīgā summa: {final_total:.2f}€" #kopsavilkums
    label_summary.config(text=summary_text) #izvada kopsavilkumu

window = tk.Tk() #izveido galveno logu
window.title("Apģērbu pasūtīšanas sistēma") #loga nosaukums
window.geometry("700x500") #loga izmērs
window.config(bg="DeepSkyBlue")  #gaiši zils fons

clothes = { #apģērbu saraksts ar cenām
    "T-krekls - 15.99€": 15.99,
    "Džinsi - 49.99€": 49.99,
    "Sporta jaka - 39.99€": 39.99,
    "Kleita - 59.99€": 59.99,
    "Mētelis - 89.99€": 89.99,
    "Apavi - 79.99€": 79.99,
    "Cepure - 12.99€": 12.99,
    "Šalle - 19.99€": 19.99,
    "Ziemas zābaki - 99.99€": 99.99,
    "Treniņbikses - 29.99€": 29.99,
}

dropdown_var = tk.StringVar(window) #izveido mainīgo str
dropdown_var.set("Izvēlieties apģērbu") #izvēlēties apģērbu
label_dropdown = tk.Label(window, text="Izvēlieties apģērbu:", font="Verdana 14 bold", bg="gainsboro") #teksta dizains
label_dropdown.pack(pady=5) #pievieno vertikālu 5 pikseļu izvietojumu etiķetei(label)
dropdown_menu = tk.OptionMenu(window, dropdown_var, *clothes.keys()) #atver logu (dropdown) apģērba izvēlnei
dropdown_menu.config(font="Verdana 14", bg="white", fg="black") #loga dizains
dropdown_menu.pack() #padar dropdown redzamu

label_quantity = tk.Label(window, text="Ievadiet daudzumu:", font="Verdana 14 bold", bg="floral white",) #dizains daudzuma logam
label_quantity.pack(pady=5) #pievieno vertikālu 5 pikseļu izvietojumu logam
entry_quantity = tk.Entry(window, font="Verdana 14", bg="white", fg="black") #dizains pievienošanas logam
entry_quantity.pack(pady=5) #pievieno vertikālu 5 pikseļu izvietojumu logam

label_message = tk.Label(window, text="", font="Verdana 14", bg="floral white", fg="blue") #dizains paziņojumam
label_message.pack(pady=10) #pievieno vertikālu 10 pikseļu izvietojumu paziņojumam

btn_add = tk.Button(window, text="Pievienot preci", font="Verdana 14", bg="light sky blue", command=add_item) #poga preces pievienošanai un tās dizains
btn_add.pack(pady=15) #pievieno vertikālu 15 pikseļu izvietojumu pogai

label_summary = tk.Label(window, text="", font="Verdana 14", bg="light sky blue", justify="left") #kopsavilkums
label_summary.pack(pady=10) #pievieno vertikālu 10 pikseļu izvietojumu kopsavilkumam

items = [] #preču saraksts

window.mainloop()
