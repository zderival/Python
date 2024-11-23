age = int(input("Enter your age: "))
if age < 12:
    print('Your ticket price is:$8.')
elif age > 11 and age < 18:
    print('Your ticket price is:$10.')
elif age >= 18 and age < 65:
    member = str(input("Are you a member of the cinema club (yes or no): "))
    if member == "yes":
        print('Your ticket price is: $12')
    if member == "no":
        print('Your ticket price is: $15')
else:
    print('Your ticket price is: $10')
