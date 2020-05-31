start=1
left_side=[]
right_side=[]
last_seat=108
no_of_querys=int(input("enter no of querys: "))
while(start+6<last_seat):
    stop=start+6
    for i in range(start,stop):
        left_side.append(i)
    for i in range(stop+5,stop-1,-1):
        right_side.append(i)
    start=stop+6
while(no_of_querys>0):
    seat_no=int(input("enter seat no: "))
    if seat_no <last_seat:
        if seat_no in left_side:
            index=left_side.index(seat_no)
            if index%3==0:
                print(f"{right_side[index]} WS")
            elif index%3==1:
                print(f"{right_side[index]} MS")
            else:
                print(f"{right_side[index]} AS")
            no_of_querys=no_of_querys-1
        else:
            index=right_side.index(seat_no)
            if index%3==0:
                print(f"{left_side[index]} WS")
            elif index%3==1:
                print(f"{left_side[index]} MS")
            else:
                print(f"{left_side[index]} AS")
            no_of_querys=no_of_querys-1
    else:
        print(f"Sorry! The train does not contain a seat with no : {seat_no} please cheak the seat no...")
        
    
        
    


    
    
