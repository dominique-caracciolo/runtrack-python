#for x in range(0, 101):
#    if x is 26:
#        continue
#    elif x is 37:
#        continue
#    elif x is 88:
#        continue
#    print(x)


i=[26,37,88]
for x in range(0,101):
    if x in i:
        continue
    print(x)
