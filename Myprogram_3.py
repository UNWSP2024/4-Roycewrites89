#Royce Daniel 2/13/2026 "Banking assistant"
#Program asks for budget from user
#Program begins a loop asking user about expenses
#Program maintains running total for expenses
#Program Presents user with running total, showing them if they have gone over or under budget
accumilator = 0
Morenumbers = True
total = 0
Budget=int(input("What's the budget?"))
while Morenumbers == True:
    number=int(input("Enter an expense: "))
    total=total+number
    answer=input("Would you like to continue? (y/n): ")
    if answer == "y":
        Morenumbers=True
    else:
         Morenumbers = False


result = total-Budget
if total > Budget: print("You went", result , "over budget. Not great.")
if total <= Budget:print("You went", result, "under budget. Nice job!")