a=input("How old are you? ")
a=int(a)



if (a>=18):
    tic=input("How many tickets you want? ")
    tic=int(tic)
    if tic>=20:
        result=("Here you go with 2% discount",(tic*20)/100*98, "$")
        
    

       
        
    else:
        print("You have to pay ", tic*20, "$")

if a<=17:
    print("You are not old enough to buy tickets")
    print("Bring a adult with you")

   



