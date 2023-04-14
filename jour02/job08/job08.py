def job8(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine, kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine,navet")
    else:
        print("Pas defini")

job8("legume","ete")
job8("legume","hiver")
job8("fruits","ete")
job8("fruits","hiver")
job8("test","a")


    
