#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 08:45:15 2017

@author: aymeric
"""
from random import randrange
sommeJoueur = 100
continuerJeux = True

print("********** Début du jeu **********\n\n\n")

while continuerJeux == True and sommeJoueur > 0:
    # Saisie de la mise et du numéro
    print("Vous possédez " + str(sommeJoueur) +"€")
    numeroMise = -1
    while numeroMise < 0 or numeroMise > 50:
        try:
            numeroMise = int(input("Sur quel numéro voulez-vous miser?\n"))
            assert 0 <= numeroMise
            assert numeroMise < 50
        except AssertionError:
            print("Vous devez choisir misez sur un numéro compris entre 0 et 49!")
        except ValueError:
            print("Veuillez saisir un numéro entier entre 0 et 49!")
    montantMise = -1
    while montantMise < 0 or montantMise > sommeJoueur:
        try:
            montantMise = input("Quel montant voulez-vous miser?\n")
            montantMise = float(montantMise)
            assert montantMise < sommeJoueur
        except ValueError:
            print("Veuillez saisir la somme que vous voulez miser.")
        except AssertionError:
            print("La banque ne fait pas de crédits!")
        if montantMise < 0:
            print("Saisir une mise positive!")

    # Tirage
    numeroTire = randrange(50)
    print("Le numéro tiré est le " + str(numeroTire))
    if numeroTire == numeroMise:
        montantGagne = montantMise * 3
        sommeJoueur += montantGagne
        print("Vous gagnez "+ str(montantGagne) + "€.")
    if numeroTire % 2 == numeroMise % 2:
        montantGagne = montantMise * 0.5
        sommeJoueur -= montantGagne
        print("Vous perdez "+ str(montantGagne) + "€.")
    else:
        print("Vous perdez votre mise!")
        sommeJoueur -= montantMise

    # Nouveau jeu
    print("Il vous reste " + str(sommeJoueur) + "€ !")
    if input("Appuyer sur la touche 'q' pour quitter la table!\n\
Sinon, appuyer sur n'importe quelle touche pour continuer\n") == ('q' or 'Q'):
        continuerJeux = False
    elif sommeJoueur == 0:
        print("Désolé, votre crédit est épuisé!")
    else:
        print("Vous continuez à jouer")

print("********** Fin du Jeu **********")