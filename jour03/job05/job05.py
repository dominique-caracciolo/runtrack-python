for premier in range(2,1001):
    if all(premier%i!=0 for i in range(2,premier)):
       print (premier)