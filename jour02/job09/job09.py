def tri(a, b, c):
    if a<=b+c and b<=a+c and c<=a+b:
        if (a**2==b**2+c**2) or (b**2==a**2+c**2) or (c**2==a**2+b**2):
            print("constructible, triangle rectangle")
        elif (a==b==c):
            print("constructible, triangle équilatéral")
        elif (a==b!=c) or (a==c!=b) or (b==c!=a):
            if (a**2==2*b**2) or (b**2==2*a**2) or (c**2==2*b**2):
                print("constructible, triangle rectangle isocèle")
            else:
                print("constructible, triangle isocele")
        else:
            print("constructible, triangle quelconque")

    else:
        print("non constructible")



tri(8,8,8)
tri(5,5,8)