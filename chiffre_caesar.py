"""
Algoritme de Caesar:
j'ajoute 3 au code ascii pour effectuer le decalage.
Les cas a#mot = "bonjour" gerer: borne des lettres imprimables (exclusion des escape sequences)
Gestion des minuscules et des majuscules
plage ASCII pour les majuscules: 65 => 90 (valeur Hexa)
plage ASCII pour les minuscules:  97 => 122
les chiffres sont exclus

"""
import sys


def caesar(mot):
        if mot.isalpha():
                resultat = []
                for i in mot:
                        lettre = ord(i)
                        resultat += chr(lettre + 3)
                return resultat
        else:
                print("la valeur entree n'est pas compose que de lettres")
                sys.exit(1)
                
if __name__ == '__main__':
        print (caesar(sys.argv[1]))
