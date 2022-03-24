# Conditional Structures
Basically Conditional Structures its a kind of structure where you can "that piece of code, just run if something happen, otherwise run this one"

```py
is_happy = bool(input())
have_money = bool(input())

if is_happy == True and have_money == True:
	print("Congratulations you really are a happy person")
elif is_happy == True and have_money = False:
	print("You can be happier")
elif is_happy == False and have_money == True:
	print("You are not happy but at least you have money")
else is_happy == False and have_money == False:
	print("Dude lucky i'm not you")
```
