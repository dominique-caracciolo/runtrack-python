liste = ["pomme", "orange", "cerise", "banane"]

def invert():
    temp=liste[0]
    liste[0] = liste[-1]
    liste[-1]=temp
    print(liste)              

invert()
invert()
print(liste)