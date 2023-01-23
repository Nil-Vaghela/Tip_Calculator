def SpliBill():
    print("Welcome to the tip Calculator")
    Total_Bill = (input("What was the total bill? $"))
    Total_People = (input("how many people to split bill? "))
    Total_percantage_for_tip = (input("what percentage tip would you like to do "))

    Total_Bill_int = eval(Total_Bill)
    Total_People_int = eval(Total_People)
    Total_percantage_for_tip_int = eval(Total_percantage_for_tip)

    Bill_with_tip = (Total_Bill_int * Total_percantage_for_tip_int) / 100 
    Final_bill = (Bill_with_tip + Total_Bill_int) / Total_People_int

    print("Each person should pay: " + str("{:.1f}".format(Final_bill)))
SpliBill()