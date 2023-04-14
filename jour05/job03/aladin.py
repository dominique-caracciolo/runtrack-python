def rectangle(L, C):
    x = "#"
    f = " "
    for i in range(1, L+1):
        for j in range(1, C+1):
            if j == 1 or j == C:
                if i != 1 and i != L:
                    print("|", end="")
                else:
                    print("+", end="")
            elif L and C == 1:
                print("|")
            elif i == 1 or i == L:
                print("-", end="")
            elif i  == j:
                    print(" ", end="")
            else:
                print(x, end="")
        print()

rectangle(10, 10)
