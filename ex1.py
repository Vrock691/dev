from collections import Counter
import numpy.random as npr

# Génération d'un tableau de 0 et de 1 de 10 elements
tab = []
for i in range(0, 10): 
    tab.append(npr.randint(0,2))

# Définition fonction fct_occ qui compte les elements dans des tableaux
def fct_occ(tableau):
    counter = Counter(tableau)
    tabcount = []
    for count in counter:
        tabcount.append({count: counter[count]})
    return tabcount

# Génération d'un tableau de 0 et de 6 de 5 elements
tab2 = []
for i in range(0, 5): 
    tab2.append(npr.randint(0,7))

print(fct_occ(tab))

# Détection d'un carré : 4 fois la même valeur avec une condition
# Détection d'un full : 2 fois une valeur et 3 fois une autre
# Détection d'une petite suite : 