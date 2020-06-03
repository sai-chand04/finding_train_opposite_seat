class seat:
    def seating(self,index):
        self.rem=index%3
        if self.rem==0:
            return "WS"
        elif self.rem==1:
            return "MS"
        else:
            return "AS"
        
        
    def result(self,left_seat_no,right_seat_no,number_of_querys):
        for i in range(0,number_of_querys):
            self.seat_no=int(input("ENTER SEAT NO: "))
            if self.seat_no in left_seat_no:
                self.index=left_seat_no.index(self.seat_no)
                self.value=right_seat_no[self.index]
            else:
                self.index=right_seat_no.index(self.seat_no)
                self.value=left_seat_no[self.index]
            print(f"{self.value} {seat.seating(self.index)}")
                
                
            
    def list_of_seat_no(self,starting,ending,number_of_querys):
        self.left_seat_no=[]
        self.right_seat_no=[]
        while(starting+6<ending):
            stop=starting+6
            for i in range(starting,stop):
                self.left_seat_no.append(i)
            for i in range(stop+5,stop-1,-1):
                self.right_seat_no.append(i)
            starting=stop+6
        seat.result(self.left_seat_no,self.right_seat_no,number_of_querys)
no_of_querys=int(input("ENTER NO_OF_QUERYS: "))
seat=seat()
seat.list_of_seat_no(1,108,no_of_querys)
