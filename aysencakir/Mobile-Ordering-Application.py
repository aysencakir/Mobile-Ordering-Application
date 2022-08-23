import re
from datetime import date
user_info=None


class rApp:
    dine_in=[]
    delivery=[]
    pick_up=[]
    all_order=[]
    total_amount=0
    Ddate=" "
    Pdate=" "
    Deldate=" "
    id=1
    address=" "
    Delkm=0
  



    def Signup(self):
        creating_user=[]
        Name=input('Please enter your name: ')
        creating_user.append(Name)
        while True:
            phone=input('Please enter your mobile number: ')
            if str(phone[0])=='0' and len(phone)==10:
                creating_user.append(phone)
                break
            else :
                print('You have entered the number in invalid format. Please start again:')
        while True:
            password=input('Please enter your password: ')
            password_confirm = input('Please confirm your password: ')
            if password==password_confirm:
                if re.search('\d.*[A-Z]|[@#$].*\d',password) is not None:
                    creating_user.append(password)
                    break
                else:
                    print('You have entered the password in invalid format. Please start again:')
        while True:
            birthday=input('Please enter your Date of Birth #DD/MM/YYYY (No Space): ')
            if re.search('[/]',birthday) is not None:
                birthday=birthday.split('/')
                year_now=date.today().year
                if int(year_now- int(birthday[-1]))>=18:
                    creating_user.append(birthday)
                    break
                else:
                    print('You have entered the birthday in invalid format. Please start again:')
        rApp.address=input("Would you like to Enter your Address?(Y/N)")
        if rApp.address=="Y":
            ad=input("Please Enter your Address")
        return creating_user

    def dineIn(self,user_info):
        self.dineMenu(user_info)

    def checkout(self):
        print("Please Enter Y to proceed to Checkout or Enter N to cancel the Order:")
        check=input()
        if check=="Y" or check=="y":
            print("")
        elif check=="N" or check=="n":
            print("Order is canceled")
            self.Login_after(user_info)
        return check
    


    def orderOnline(self,user_info):
    
         print("Enter 1 for Self Pickup")
         print("Enter 2 for Home Delivery")
         print("Enter 3 to go to Previous Menu")
         OrderOnlineInput=input()
         if OrderOnlineInput=="1":
             self.onlineMenuS(user_info)  
         elif OrderOnlineInput=="2":
             self.onlineMenuD(user_info)
         elif OrderOnlineInput=="3":
             self.Login_after(user_info)
         return OrderOnlineInput


    def dineMenu(self,user_info):
        damount=0

        while True:
            print("Enter 1 for Noodles   Price AUD 2")
            print("Enter 2 for Sandwich  Price AUD 4")
            print("Enter 3 for Dumpling  Price AUD 6")
            print("Enter 4 for Muffins   Price AUD 8")
            print("Enter 5 for Pasta     Price AUD 10")
            print("Enter 6 for Pizza     Price AUD 20") 
            print("Enter 7 for Coffee    Price AUD 2")
            print("Enter 8 for Colddrink Price AUD 4")
            print("Enter 9 for Shake     Price AUD 6")
            print("Enter 10 for Checkout:")

            dinemenu=int(input())

            if dinemenu != 10:
                if dinemenu==6:
                    damount=damount+20
                elif dinemenu==7:
                    damount=damount+2
                elif dinemenu==8:
                    damount=damount+4
                elif dinemenu==9:
                    damount=damount+6
                else:
                    damount=damount+(dinemenu*2)
            
            if dinemenu==10:
                if self.checkout()=="Y":
               
                   print("Your total payble amount is:",(damount+(damount*1/10))," inclusing AUD ",(damount*1/10)," for Service Charges")

                   self.dineProc(user_info)

                   rApp.dine_in.append("A")
                   rApp.dine_in.append(rApp.id)
                   rApp.dine_in.append(rApp.Ddate)
                   rApp.dine_in.append("Dine in")
                   rApp.dine_in.append(damount+(damount*1/10))

               
                   rApp.all_order.append("A")
                   rApp.all_order.append(rApp.id)
                   rApp.all_order.append(rApp.Ddate)
                   rApp.all_order.append("Dine in")
                   rApp.all_order.append(damount+(damount*1/10))
                   rApp.total_amount=damount+(damount*1/10)+rApp.total_amount
                   print("Your order has been confirmed, and your order id is ‘A"+str(rApp.id).zfill(3),"\'")
                   rApp.id=rApp.id+1
            
                break
        



    def onlineMenuD(self,user_info):
        amountD=0
       
        while True:
            print("Enter 1 for Noodles   Price AUD 2")
            print("Enter 2 for Sandwich  Price AUD 4")
            print("Enter 3 for Dumpling  Price AUD 6")
            print("Enter 4 for Muffins   Price AUD 8")
            print("Enter 5 for Pasta     Price AUD 10")
            print("Enter 6 for Pizza     Price AUD 20")
            print("Enter 7 for Drinks Menu:") 

            onlinemenuD=int(input())
            if onlinemenuD==7:
              break
            else:
                if onlinemenuD==6:
                    amountD=amountD+20
                else:
                    amountD=amountD+(onlinemenuD*2)
        while True:
               print("Enter 1 for Coffee     Price AUD 2")
               print("Enter 2 for Colddrink  Price AUD 4")
               print("Enter 3 for Shake      Price AUD 6")
               print("Enter 4 for Checkout:")
               onlinemenuDd=int(input())
               if onlinemenuDd==4:
             
                    if self.checkout()=="Y":
                        print("Your total payble amount is:",amountD," and there will be an additional charges for Delivery")
                        self.delProc(user_info)
                        if rApp.Delkm>0 and rApp.Delkm<3:
                            amountD=amountD+5
                        elif rApp.Delkm>2 and rApp.Delkm<6:
                            amountD=amountD+10
                        elif rApp.Delkm>5 and rApp.Delkm<11:
                            amountD=amountD+18
                        elif rApp.Delkm>10:
                            break
                        if rApp.address=="N":
                            ad1=input("You have not mentioned your address, while signing up. \nPlease enter Y if would like to enter your address.\nEnter N if you would like to select other mod of order.")
                            if ad1=="Y":
                                ad2=input("Please enter your address")
                                rApp.delivery.append("A")
                                rApp.delivery.append(rApp.id)
                                rApp.delivery.append(rApp.Deldate)
                                rApp.delivery.append("Home Delivery")
                                rApp.delivery.append(amountD)

                                rApp.all_order.append("A")
                                rApp.all_order.append(rApp.id)
                                rApp.all_order.append(rApp.Deldate)
                                rApp.all_order.append("Home Delivery")
                                rApp.all_order.append(amountD)
                                rApp.total_amount=amountD+rApp.total_amount
                                print("Your order has been confirmed, and your order id is ‘A"+str(rApp.id).zfill(3),"\'")
                                rApp.id=rApp.id+1
                            elif ad1=="N":
                                rApp.Login_after(user_info)
                        if rApp.address=="Y":
                                
                                rApp.delivery.append("A")
                                rApp.delivery.append(rApp.id)
                                rApp.delivery.append(rApp.Deldate)
                                rApp.delivery.append("Home Delivery")
                                rApp.delivery.append(amountD)

                                rApp.all_order.append("A")
                                rApp.all_order.append(rApp.id)
                                rApp.all_order.append(rApp.Deldate)
                                rApp.all_order.append("Home Delivery")
                                rApp.all_order.append(amountD)
                                rApp.total_amount=amountD+rApp.total_amount
                                print("Your order has been confirmed, and your order id is ‘A"+str(rApp.id).zfill(3),"\'")
                                rApp.id=rApp.id+1
                        break
               else:
                amountD=amountD+(onlinemenuDd*2)
    
    def onlineMenuS(self,user_info):
        amountS=0
       
        while True:
            print("Enter 1 for Noodles   Price AUD 2")
            print("Enter 2 for Sandwich  Price AUD 4")
            print("Enter 3 for Dumpling  Price AUD 6")
            print("Enter 4 for Muffins   Price AUD 8")
            print("Enter 5 for Pasta     Price AUD 10")
            print("Enter 6 for Pizza     Price AUD 20")
            print("Enter 7 for Drinks Menu:") 

            onlinemenuS=int(input())
            if onlinemenuS==7:
              break
            else:
                if onlinemenuS==6:
                    amountS=amountS+20
                else:
                    amountS=amountS+(onlinemenuS*2)
        while True:
               print("Enter 1 for Coffee     Price AUD 2")
               print("Enter 2 for Colddrink  Price AUD 4")
               print("Enter 3 for Shake      Price AUD 6")
               print("Enter 4 for Checkout:")
               onlinemenuSd=int(input())
               if onlinemenuSd==4:
             
                    if self.checkout()=="Y":
                        print("Your total payble amount is:",amountS)
                        self.pickProc(user_info)
                    
                        rApp.pick_up.append("A")
                        rApp.pick_up.append(rApp.id)
                        rApp.pick_up.append(rApp.Pdate)
                        rApp.pick_up.append("Pick Up")
                        rApp.pick_up.append(amountS)

                        rApp.all_order.append("A")
                        rApp.all_order.append(rApp.id)
                        rApp.all_order.append(rApp.Pdate)
                        rApp.all_order.append("Pick Up")
                        rApp.all_order.append(amountS)
                       

                        rApp.total_amount=amountS+rApp.total_amount
                        print("Your order has been confirmed, and your order id is ‘A"+str(rApp.id).zfill(3),"\'")
                        rApp.id=rApp.id+1
                        break
               else:
                amountS=amountS+(onlinemenuSd*2)            

    def Login_after(self,user_info):
        print("Please enter 2.1 to Start Ordering")
        print("Please enter 2.2 to Print Statistics")
        print("Please enter 2.3 for Logout")
        entering = input()
   
        if entering=='2.1':
           print("Please enter 1 for Dine in")
           print("Please enter 2 for Order Online")
           print("Please enter 3 to go to Login Page")
           enter = input()
           if enter=="1":
              self.dineIn(user_info)
           elif enter=="2":
              self.orderOnline(user_info)
           elif enter=="3":
              self.main(user_info)     
        elif entering=="2.2":
                self.sot(user_info)
        elif entering=="2.3":
                 print("Logout successfully.")
                 exit()


    def dineProc(self,user_info):
      
        rApp.Ddate=input("Please enter the Date of Booking for Dine in: " )
        Dtime=input("Please enter the Time of Booking for Dine in: " )
        Dperson=input("Please enter the number of Persons: " )
        print("Thank you for entering the details, Your Booking is confirmed")

    def pickProc(self,user_info):
        rApp.Pdate=input("Please enter the Date of Pick Up: " )
        Ptime=input("Please enter the Time of Pick Up: " )
        Pperson=input("Please enter the name of Person: " )
        print("Thank you for entering the details, Your Booking is confirmed")

    def delProc(self,user_info):
        rApp.Deldate=input("Please enter the Date of Delivery: " )
        Deltime=input("Please enter the Time of Delivery: " )
        rApp.Delkm=int(input("Please enter the Distance from the Restaurant: " ))
        if rApp.Delkm>10:
            print("Distance from the restaurant is more than the applicable limits, you must be provided with the option to Pick up the Order.")

        print("Thank you for entering the details, Your Booking is confirmed")




    def sot(self,user_info):
        print("Please Enter the Option to Print the Statistics. \n1-All in Dine Orders \n2-All Pick Up Orders \n3-All Deliveries \n4-All Orders(Descedingly) \n5-Total Amount Spent on All Orders \n6-To Go to Previous Menu")
       
        sEnter=int(input())

        if sEnter==1:
            i=0
            j=0
            while i<(len(rApp.dine_in))/5:
                print(rApp.dine_in[j]+str(rApp.dine_in[j+1]).zfill(3),"\t",rApp.dine_in[j+2],"\t",rApp.dine_in[j+3],"\t",rApp.dine_in[j+4])
                j=j+5
                i=i+1

        elif sEnter==2:
            i=0
            j=0
            while i<(len(rApp.pick_up))/5:
                print(rApp.pick_up[j]+str(rApp.pick_up[j+1]).zfill(3),"\t",rApp.pick_up[j+2],"\t",rApp.pick_up[j+3],"\t",rApp.pick_up[j+4])
                j=j+5
                i=i+1
        elif sEnter==3:
            i=0
            j=0
            while i<(len(rApp.delivery))/5:
                print(rApp.delivery[j]+str(rApp.delivery[j+1]).zfill(3),"\t",rApp.delivery[j+2],"\t",rApp.delivery[j+3],"\t",rApp.delivery[j+4])
                j=j+5
                i=i+1
        elif sEnter==4:
            i=0
            j=0
            while i<(len(rApp.all_order))/5:
                print(rApp.all_order[j]+str(rApp.all_order[j+1]).zfill(3),"\t",rApp.all_order[j+2],"\t",rApp.all_order[j+3],"\t",rApp.all_order[j+4])
                j=j+5
                i=i+1
        elif sEnter==5:
            print(rApp.total_amount)
        elif sEnter==6:
            self.Login_after(user_info)

    def Login(self,user_info):
        number=input('Please Enter your Username (Mobile Number) : ')
        password=input('Please Enter your password: ')
        while user_info[1]!=number or user_info[2]!=password:
            print("You entered wrong information")
            number=input('Please Enter your Username (Mobile Number) : ')
            password=input('Please Enter your password: ')
        print("You have successfyully Signed in")

    def Entering(self):
        print('Please enter 1 for Sign up.')
        print('Please enter 2 for Logging.')
        print('Please enter 3 for Exit.')

    def main(self,user_info):
        while True:
            self.Entering()
            enter_info=int(input())
            if enter_info==1:
                user_info=self.Signup()
            elif enter_info==2:
                if user_info==None:
                    print('Please firstly sign up')
                    user_info = self.Signup()
                else:
                    self.Login(user_info)
                    self.Login_after(user_info)
                
            elif enter_info==3:
                print('Signout successfully.')
                exit()


if __name__ == '__main__':
    obj=rApp()
    obj.main(user_info)

        
