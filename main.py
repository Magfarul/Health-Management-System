print("Health Management System")
def getime():
    import datetime
    return datetime.datetime.now()
def startmenu():
    print("Enter 1 for read old data, 2 for add new data")
    read_new= input()
    if read_new=="1":
        print("Enter \n1:Munna \n2:Moon\n3:Mahin")
        old_name=input()
        if old_name=="1":
            print("Enter 1 for Food, 2 for excersice")
            m_food=input()
            if m_food == "1":
                food_m=open("MunnaFood.txt")
                print(food_m.read())
            elif m_food == "2":
                Ex_m=open("MunnaEx.txt")
                print(Ex_m.read())
        elif old_name=="2":
            print("Enter 1 for Food, 2 for excersice")
            mn_food=input()
            if mn_food == "1":
                food_mn=open("MoonFood.txt")
                print(food_mn.read())
            elif mn_food == "2":
                EX_mn=open("MoonEX.txt")
                print(EX_mn.read())
                
        elif old_name =="3":
            print("Enter 1 for Food, 2 for excersice")
            mh_food=input()
            if mh_food == "1":
                food_mh=open("MahinFood.txt")
                print(food_mh.read())
            elif mn_food == "2":
                EX_mh=open("MahinEX.txt")
                print(EX_mh.read())
                       
    elif read_new=="2":
        print("Enter \n1:Munna \n2:Moon\n3:Mahin")
        old_name=input()
        if old_name=="1":
            print("Enter 1 for Food, 2 for excersice")
            m_food=input()
            if m_food == "1":
                food_m=open("MunnaFood.txt","a")
                efood=input("Enter Food\n")
                food_m.write(str(getime())+":	"+ efood+"\n")
                food_m.close()
            
            elif m_food == "2":
                Ex_m=open("MunnaEx.txt","a")
                eEx=input("Enter Excersice")
                Ex_m.write(str(getime())+":	"+eEx+("\n"))
                Ex_m.close()
        elif old_name=="2":
            print("Enter 1 for Food, 2 for excersice")
            mn_food=input()
            if mn_food == "1":
                food_mn=open("MoonFood.txt","a")
                efood=input("Enter Food\n")
                food_mn.write(str(getime())+":	"+efood+"\n")
                food_mn.close()
            elif mn_food == "2":
                EX_mn=open("MoonEX.txt","a")
                eEx=input("Enter Excersice\n")
                EX_mn.write(str(getime())+":	"+eEx+"\n")
                EX_mn.close()
                
        elif old_name =="3":
            print("Enter 1 for Food, 2 for excersice")
            mh_food=input()
            if mh_food == "1":
                food_mh=open("MahinFood.txt","a")
                efoodmh=input("Enter Food\n")
                food_mh.write(str(getime())+":	"+efoodmh+"\n")
                food_mh.close()
                
                
            elif mn_food == "2":
                EX_mh=open("MahinEX.txt","r+")
                eEx=input("Enter Excersice\n")
                EX_mh.write(str(getime())+":	"+eEx+"\n")
                EX_mh.close()
    else:
    	startmenu()
		
 
startmenu()
               
        
             
            
		


