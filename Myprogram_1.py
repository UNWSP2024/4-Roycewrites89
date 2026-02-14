#Royce Daniel 2/13/2026 "cinema ticket vendor"
print("Welcome to Marcus theatre!")
showings=int(input("How many movies would you like to see?"))
total=0
for i in range(showings):
    film=(input("What movie would you like to see?"))
    number=int(input("How many tickets would you like for" + film+"?"))
    total = total + number

print("That's", total , "tickets. Enjoy the show!")
