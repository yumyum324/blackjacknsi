import random
scbanque = 0
scjoueur = 0
tour = 0
while 0<1 :
    while True :
        lancer = int(input ("Combien de dés lancez-vous ? "))
        print()
        for a in range(lancer):
            dé= random.randint(1,6)
            print("Votre dé affiche : ", dé)
            scjoueur= scjoueur+dé
            tour = tour +1
        if scjoueur ==21 or scjoueur>21 :
            break
        elif scjoueur <21 :
            print()
            score = str(input("Votre score est en dessous de 21. Souhaitez-vous continuez ? (tapez oui ou non) : "))
            if score == "oui" :
                True
            else :
                break
    print()
    print("Votre score final est de : ", scjoueur)
    print()
    print("Au tour de la banque de jouer")
    print()
    for a in range(tour):
        dé= random.randint(1,6)
        print("Le dé de la banque affiche  : ", dé)
        scbanque = scbanque+dé
    print()
    print("Le score final de la banque est de : ", scbanque)
    print()
    if scjoueur > 21 and scbanque >21 :
        print ("La banque et vous avez dépassés 21.")
    elif scbanque >21 :
        print("La banque a dépassée 21")
    elif scjoueur > 21 :
        print("Vous avez dépassé 21")
    if scbanque < 21 and scjoueur < 21 :
        print("La banque et vous n'avez pas atteint 21.")
    elif scjoueur < 21:
        print ("Vous n'avez pas atteint 21.")
    elif scbanque < 21:
        print("La banque n'a pas atteint 21.")
    if scbanque ==21 :
        print("La banque a gagné")
    elif scjoueur== 21 :
        print("Vous avez gagné")
    tour = 0
    scbanque = 0
    scjoueur = 0
    restart = str(input("Voulez-vous rejouer ? (tapez oui ou non) : "))
    if restart =="oui":
        continue
    else :
        break
print("Merci d'avoir joué.")
