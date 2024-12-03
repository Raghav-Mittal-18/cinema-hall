print("                                   ---->#WELCOME TO MITTAL CINEMA HALL#<----")
print("seats in movie hall is")
seat1=[["seat1","seat2","seat3"],["seat4","seat5","seat6"],["seat7","seat8","seat9"]]
st1=0
st2=0
st3=0
st4=0
st5=0
st6=0
st7=0
st8=0
st9=0
seat=[[0,0,0],[0,0,0],[0,0,0]]
co=0
cs=0
cf=0
sum=0
for i in seat1[:]:
    print(i)
while True:
    print("press 1 for 'booking of seat'\npress 2 for 'cancelation of seat' \npress 3 for to check seats status \npress 4 for exit and bill")
    a=int(input("Enter your choice::"))
    if a==1:
        for i in range(1,10):
            print(f"enter {i} for booking seat{i}")
        print()  
        print("----------># MENU #<---------- \n1. Coca Cola(400ml,50Rs) \n2. chips and kurkure(50Rs) \n3. Sandwich(1pc,50Rs) \n4. Popcorn(50RS)")
        print()
        aa=int(input("how many tickets do you want to book ::"))
        for i in range(aa):
            n=int(input("enter  seat no. to book seat::"))
            no=int(input(f"How many things do you want to order for seat{n}::"))
            if n==1:
                if seat[0][0]==1:
                    print(f"{n} seat no. is already booked")
                elif seat[0][0]==0:
                    (seat[0][0])=1
                    print()
                    for j in range(no):
                        ra=int(input(f"what do you want to order for seat{n} \n press menu number::"))
                        st1=no
            elif n==2:
                if seat[0][1]==1:
                    print(f"{n} seat no. is already booked")
                elif seat[0][1]==0:
                    seat[0][1]=1
                    print()
                    for j in range(no):
                        ra=int(input(f"what do you want to order for seat{n} \n press menu number::"))
                            # sum+=no*50
                        st2=no
            elif n==3:
                if seat[0][2]==1:
                    print(f"{n} seat no. is already booked")
                elif seat[0][2]==0:
                    seat[0][2]=1
                    print()
                    for j in range(no):
                        ra=int(input(f"what do you want to order for seat{n} \n press menu number::"))
                            # sum+=no*50
                        st3=no
            elif n==4:
                if seat[1][0]==1:
                    print(f"{n} seat no. is already booked")
                elif seat[1][0]==0:
                    seat[1][0]=1
                    print()
                    for j in range(no):
                        ra=int(input(f"what do you want to order for seat{n} \n press menu number::"))
                            # sum+=no*50
                        st4=no
            elif n==5:
                if seat[1][1]==1:
                    print(f"{n} seat no. is already booked")
                elif seat[1][1]==0:
                    seat[1][1]=1
                    print()
                    for j in range(no):
                        ra=int(input(f"what do you want to order for seat{n} \n press menu number::"))
                        # if ra<=4 and ra>0:
                            # sum+=no*50
                        st5=no
            elif n==6:
                if seat[1][2]==1:
                    print(f"{n} seat no. is already booked")
                elif seat[1][2]==0:
                    seat[1][2]=1
                    print()
                    for j in range(no):
                        ra=int(input(f"what do you want to order for seat{n} \n press menu number::"))
                        # if ra<=4 and ra>0:
                        #     sum+=no*50
                        st6=no
            elif n==7:
                if seat[2][0]==1:
                    print(f"{n} seat no. is already booked")
                elif seat[2][0]==0:
                    seat[2][0]=1
                    print()
                    for j in range(no):
                        ra=int(input(f"what do you want to order for seat{n} \n press menu number::"))
                        # if ra<=4 and ra>0:
                        #     sum+=no*50
                        st7=no
            elif n==8:
                if seat[2][1]==1:
                    print(f"{n} seat no. is already booked")
                elif seat[2][1]==0:
                    seat[2][1]=1
                    print()
                    for j in range(no):
                        ra=int(input(f"what do you want to order for seat{n} \n press menu number::"))
                        # if ra<=4 and ra>0:
                        #     sum+=no*50
                        st8=no
            elif n==9:
                if seat[2][2]==1:
                    print(f"{n} seat no. is already booked")
                elif seat[2][2]==0:
                    seat[2][2]=1
                    print()
                    for j in range(no):
                        ra=int(input(f"what do you want to order for seat{n} \n press menu number::"))
                        # if ra<=4 and ra>0:
                        #     sum+=no*50
                        st9=no
            sum+=no*50
        print()
        print(f"your total food expense is::{sum}Rs")
        print()
        print("\n here 1 shows booked seats \n0 shows empty seats \n")
        for i in seat[:]:
            print(i)
    if a==2:
        aa=int(input("how many tickets do you want to cancel::"))
        for i in range(1,10):
            print(f"enter {i} to cancel seat{i}")

        for i in range(aa):
            n=int(input("enter seat no. to cancel seat::"))
            if n==1:
                if seat[0][0]==0:
                    print(f"{n} seat no. is already empty")
                elif seat[0][0]==1:
                    seat[0][0]=0
                    sum-=st1*50
                    cs-=300
            elif n==2:
                if seat[0][1]==0:
                    print(f"{n} seat no. is already empty")
                elif seat[0][1]==1:
                    seat[0][1]=0
                    sum-=st2*50
                    cs-=300
            elif n==3:
                if seat[0][2]==0:
                    print(f"{n} seat no. is already empty")
                elif seat[0][2]==1:
                    seat[0][2]=0
                    sum-=st3*50
                    cs-=300
            elif n==4:
                if seat[1][0]==0:
        
                    print(f"{n} seat no. is already empty")
                elif seat[1][0]==1:
                    seat[1][0]=0
                    sum-=st4*50
                    cs-=300
            elif n==5:
                if seat[1][1]==0:
                    print(f"{n} seat no. is already empty")
                elif seat[1][1]==1:
                    seat[1][1]=0
                    sum-=st5*50
                    cs-=300
            elif n==6:
                if seat[1][2]==0:
                    print(f"{n} seat no. is already empty")
                elif seat[1][2]==1:
                    seat[1][2]=0
                    sum-=st6*50
                    cs-=300
            elif n==7:
                if seat[2][0]==0:
                    print(f"{n} seat no. is already empty")
                elif seat[2][0]==1:
                    seat[2][0]=0
                    sum-=st7*50
                    cs-=300
            elif n==8:
                if seat[2][1]==0:
                    print(f"{n} seat no. is already empty")
                elif seat[2][1]==1:
                    seat[2][1]=0
                    sum-=st8*50
                    cs-=300
            elif n==9:
                if seat[2][2]==0:
                    print(f"{n} seat no. is already empty")
                elif seat[2][2]==1:
                    seat[2][2]=0
                    sum-=st9*50
                    cs-=300
        print()
        print(f"your total food expense is::{sum}Rs")
        print()
        print("here 1 shows booked seats\n0 shows empty seats")
        for i in seat[:]:
            print(i)
    if a==3:
        print("here 1 shows booked seats\n0 shows empty seats")
        for i in seat[:]:
            print(i)
    if a==4:
        for i in seat[:]:
            for j in i:
                if j==1:
                    co+=1 
        print(f"total bill(food expense+tickets cost)={sum+(co*300)}Rs")
        print("here 1 shows booked seats \n0 shows empty seats")
        for i in seat[:]:
            print(i)
        break