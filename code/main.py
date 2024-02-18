# Il est important de noter que le rendu est propre à chaque machine, de plus, ce programme a été codé sous un pc Linux donc complétement différent de Windows. Le rendu peut donc apparaître 'moche'. Merci de votre compréhension !

from xor import *
from hill import *
from rsa import *
from tkinter import *

root = Tk()

root.title("Cryptologie")
root.minsize(1500, 700)
root.maxsize(1500, 700)
root.config(background='#0053b3')

Label(text="Bienvenue sur notre application de cryptologie en lien avec les minis projets de NSI !",bg='#0053b3', font=('carlito', 25)).pack(side=TOP)
Label(text="Choisissez votre méthode parmis XOR, Hill ou RSA",bg='#0053b3', font=('carlito', 30)).pack(side=TOP)

def xor_fenetre():
    root.destroy()
    root_xor = Tk()
    root_xor.title('XOR')
    root_xor.minsize(1500, 700)
    root_xor.maxsize(1500, 700)
    root_xor.config(background='#0053b3')
    
    def recuperer_cle():
        entree = cle_entree.get("1.0", "end-1c")
        global cle

    Label(text="Veuillez entrer votre clé : ", bg='#0053b3', font=('carlito', 20)).place(relx=0.5, rely=0.5, anchor=CENTER)
    cle_entree = Text(root_xor, height=1, width=20)
    cle_entree.place(relx=0.5, rely=0.55, anchor=CENTER)
    valider = Button(root_xor, text="Valider", command=recuperer_cle).place(anchor=CENTER, relx=0.5, rely=0.6)

    ###################

    def chiffrement():
        message = texte_a_chiffrer.get("1.0", "end-1c")
        print(message)
        texte_a_chiffrer.destroy()
        Label(text=f"Votre message chiffré : {chiffrement_xor(message, cle)}", bg='#0053b3', font=('carlito', 20)).pack(side=LEFT)

    Label(text="Veuillez entrer votre message à chiffrer : ", bg='#0053b3', font=('carlito', 20)).place(x=75, y=25)
    texte_a_chiffrer = Text(root_xor, height=20, width=60)
    texte_a_chiffrer.pack(side=LEFT, padx=120)
    bouton_chiffrement = Button(text="Chifre le message !", command=chiffrement).place(x=250, y=600)

    ###################

    def dechiffrement():
        message = texte_a_dechiffrer.get("1.0", "end-1c")
        print(message)
        texte_a_dechiffrer.destroy()
        Label(text=f"Votre message dechiffré : {dechiffrement_xor(message, cle)}", bg='#0053b3', font=('carlito', 20)).pack(side=RIGHT)

    Label(text="Veuillez entrer votre message à déchiffrer : ", bg='#0053b3', font=('carlito', 20)).place(x=910, y=25)
    texte_a_dechiffrer = Text(root_xor, height=20, width=60)
    texte_a_dechiffrer.pack(side=RIGHT, padx=120)
    Button(text="Déchifre le message !", command=dechiffrement).place(x=1100, y=600)

    ###################

    root_xor.mainloop()

def hill_fenetre():
    root.destroy()
    root_hill = Tk()
    root_hill.title('Hill')
    root_hill.minsize(1500, 700)
    root_hill.maxsize(1500, 700)
    root_hill.config(background='#0053b3')
    
    def recuperer_cle():
        entree = cle_entree.get("1.0", "end-1c")
        global cle
        cle = generer_matrice_cle(entree.upper())
        return

    Label(text="Veuillez entrer votre clé : ", bg='#0053b3', font=('carlito', 20)).place(relx=0.5, rely=0.5, anchor=CENTER)
    cle_entree = Text(root_hill, height=1, width=20)
    cle_entree.place(relx=0.5, rely=0.55, anchor=CENTER)
    valider = Button(root_hill, text="Valider", command=recuperer_cle).place(anchor=CENTER, relx=0.5, rely=0.6)

    ###################

    def chiffrement():
        message = texte_a_chiffrer.get("1.0", "end-1c")
        texte_a_chiffrer.destroy()
        Label(text=f"Votre message chiffré : {chiffrement_hill(message, cle)}", bg='#0053b3', font=('carlito', 20)).pack(side=LEFT)
        return

    Label(text="Veuillez entrer votre message à chiffrer : ", bg='#0053b3', font=('carlito', 20)).place(x=75, y=25)
    texte_a_chiffrer = Text(root_hill, height=20, width=60)
    texte_a_chiffrer.pack(side=LEFT, padx=120)
    bouton_chiffrement = Button(text="Chifre le message !", command=chiffrement).place(x=250, y=600)

    ###################

    def dechiffrement():
        message = texte_a_dechiffrer.get("1.0", "end-1c")
        texte_a_dechiffrer.destroy()
        Label(text=f"Votre message dechiffré : {dechiffrement_hill(message, cle)}", bg='#0053b3', font=('carlito', 20)).pack(side=RIGHT)
        return

    Label(text="Veuillez entrer votre message à déchiffrer : ", bg='#0053b3', font=('carlito', 20)).place(x=910, y=25)
    texte_a_dechiffrer = Text(root_hill, height=20, width=60)
    texte_a_dechiffrer.pack(side=RIGHT, padx=120)
    Button(text="Déchifre le message !", command=dechiffrement).place(x=1100, y=600)

    ###################

    root_hill.mainloop()

def rsa_fenetre():
    root.destroy()
    root_rsa = Tk()
    root_rsa.title('RSA')
    root_rsa.minsize(1500, 700)
    root_rsa.maxsize(1500, 700)
    root_rsa.config(background='#0053b3')

    
    def recuperer_cle_chiffrement():
        entree = cle_entree.get("1.0", "end-1c")
        global cle
        cle = generer_matrice_cle(entree)
        return

    Label(text="Veuillez entrer votre clé de chiffrement : ", bg='#0053b3', font=('carlito', 15)).place(relx=0.5, rely=0.4, anchor=CENTER)
    cle_entree = Text(root_rsa, height=1, width=20)
    cle_entree.place(relx=0.5, rely=0.45, anchor=CENTER)
    valider = Button(root_rsa, text="Valider", command=recuperer_cle_chiffrement).place(relx=0.5, rely=0.5, anchor=CENTER)

    ###################

    def recuperer_cle_dechiffrement():
        entree = cle_entree.get("1.0", "end-1c")
        global cle
        cle = generer_matrice_cle(entree)
        return

    Label(text="Veuillez entrer votre clé de dechiffrement : ", bg='#0053b3', font=('carlito', 15)).place(relx=0.5, rely=0.6, anchor=CENTER)
    cle_entree = Text(root_rsa, height=1, width=20)
    cle_entree.place(relx=0.5, rely=0.65, anchor=CENTER)
    valider = Button(root_rsa, text="Valider", command=recuperer_cle_dechiffrement).place(anchor=CENTER, relx=0.5, rely=0.7)

    ##################

    def chiffrement():
        message = texte_a_chiffrer.get("1.0", "end-1c")
        texte_a_chiffrer.destroy()
        Label(text=f"Votre message chiffré : {chiffrement_rsa(message)}", bg='#0053b3', font=('carlito', 20)).pack(side=LEFT)
        return

    Label(text="Veuillez entrer votre message à chiffrer : ", bg='#0053b3', font=('carlito', 20)).place(x=75, y=25)
    texte_a_chiffrer = Text(root_rsa, height=20, width=60)
    texte_a_chiffrer.pack(side=LEFT, padx=120)
    bouton_chiffrement = Button(text="Chifre le message !", command=chiffrement).place(x=250, y=600)

    ###################

    def dechiffrement():
        message = texte_a_dechiffrer.get("1.0", "end-1c")
        texte_a_dechiffrer.destroy()
        Label(text=f"Votre message dechiffré : {dechiffrement_hill(message, cle)}", bg='#0053b3', font=('carlito', 20)).pack(side=RIGHT)
        return

    Label(text="Veuillez entrer votre message à déchiffrer : ", bg='#0053b3', font=('carlito', 20)).place(x=910, y=25)
    texte_a_dechiffrer = Text(root_rsa, height=20, width=60)
    texte_a_dechiffrer.pack(side=RIGHT, padx=120)
    Button(text="Déchifre le message !", command=dechiffrement).place(x=1100, y=600)

    ###################

Button(text="XOR", width=50, height=20, command=xor_fenetre).pack(side=LEFT)
Button(text="Hill", width=50, height=20, command=hill_fenetre).place(relx=0.5, rely=0.5, anchor=CENTER)
Button(text="RSA", width=50, height=20, command=rsa_fenetre).pack(side=RIGHT)

root.mainloop()                                                                 