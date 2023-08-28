#Roller coaster ticketing AI system 
print("Welcome to Stem Cafe's Rollercoaster ride")
name = input("Please what is your name?")
print(f"Good day {name} I'll need you to answer this short questions very quickly")
height = int(input("What is your height in cm?"))
if (height >= 120):
  print ("You are eligible to ride our rollercoaster")
  age = int(input("How old are you?"))
  if (age < 12):
    print("Your ticket is $5")
    pic = input("Do you want your picture taken?")
    if(pic == "Yes"):
      print("Your total bill is $8")
    else:
       print("Your total bill is $5")
    
  if (age >= 12 and age <=18):
    print("Your ticket is $7")
    pic = input("Do you want your picture taken? Yes or No?")
    if(pic == "Yes"):
      print("Your total bill is $10")
    else:
      print("Your total bill is $7")
    
  if (age >= 19 and age <= 48):
    print("Your ticket is $12")
    pic = input("Do you want your picture taken?")
    if(pic == "Yes"):
      print("Your total bill is $15")
    else:
      print("Your total bill is $12")  
 
  if (age > 48 and age < 80):
    print("Your ticket is Free")
    pic = input("Do you want your picture taken?")
    if(pic == "Yes"):
      print("Your total bill is $3")
    else:
      print("Your total bill is Free") 
 
  if ( age > 80):
    print("Sorry but for your safety you are too old to ride our roller coaster")
else:
  print("I am sorry but you are not eligible to ride our roller coaster")
