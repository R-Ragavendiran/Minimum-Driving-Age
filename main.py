print("Welcome to  Minimum Driving Age")
print("The minimum driving age is the minimum age at which a person may obtain a driver's license to lawfully drive a motor vehicle on public roads")

print("") #for free space

print("1.INDIA")
print("2.Chile")
print("3.Africa")
print("4.Americas")
print("5.Caribbean")
print("6.Asia")
print("7.Europe")
print("8.Oceania")
a=int(input("Enter Your Country Name :"))

print("") #for free space

if a==1:
    print("so,your are from India")
    b=int(input("enter your age :"))
    if b<=15:
        print("not eligeble for driving licence")
    elif b<=16:
        print("After getting a learner's licence, you will be allowed to practice driving on Indian roads provided you are accompanied/supervised by a person holding a valid driving licence. You can apply for this type of licence only by the age of 16.")
    elif b<=17:
        print("In essence, you need to be 17 years old to drive on public roads. You will need to be in possession of either a full driving licence or a provisional driving licence. In both cases you need to be insured and the car you're driving needs to have a current MoT and road tax")
    elif b>=18:
        print(" you will get  unrestricted license")
    else:
        print("Enter the correct age")

print("") #for free space   
if a==2:
    print("So,Your Are From Chile")
    c=int(input("Enter Your Age :"))
    if c<=16:
        print("Not Eligeble For Driving Licence")
    elif c<=18:
        print("You Will Get Licence With Parental Approval")
    elif c>=19:
        print(" You Will Get Professional License")
    else:
        print("Enter The Correct Age")

print("") #for free space   
if a==3:
    print("So,Your Are From Africa")
    d=int(input("Enter Your Age :"))
    if d<=14:
        print("Not Eligible")
    elif d<=17:
        print(" You can obtain a learners license and legally allowed to drive with supervision at age 15")
    elif d>=18:
        print("A full driving licensed will be fully granted by age 18")
    else:
        print("Enter the correct answer")
        
print("") #for free space   
if a==4:
    print("So,Your Are From Americas")
    d=int(input("Enter Your Age :"))
    if d<=13:
        print("Not eligible")
    elif d<=15:
        print("You can obtain a learner's permit in Alaska, Arkansas, Iowa, Kansas, North and South Dakota at just 14 years old")
    elif d<=17:
        print("The minimum age to drive in the USA is just 16 in some states only")
    elif d>=18:
        print("In Americas require you to be at least 18,you will get full professional license ")
    else:
        print("Enter The Correct Age")

print("") #for free space   
if a==5:
    print("So,Your Are From Caribbean")
    d=int(input("Enter Your Age :"))
    if d<=16:
        print("Not eligible")
    elif d==17:
        print("Although you can get a learner's permit aged 17")
    elif d>=18:
        print("you can only get licensed from the age of 18")
    else:
        print("Enter The Correct Answer")

print("") #for free space   
if a==6:
    print("So,Your Are From Asia")
    d=int(input("Enter Your Age :"))
    if d<=16:
        print("Not Eligible")
    elif d==17:
        print("The Philippines, Malaysia, and Indonesia are exceptions with a minimum driving age of 17")
    elif d>=18:
        print("The minimum driving age for most countries in Asia is 18 years old")
    else:
        print("Enter the correct Age")

print("") #for free space   
if a==7:
    print("So,Your Are From Europe")
    d=int(input("Enter Your Age :"))
    if d<=15:
        print("Not eligible")
    elif d<=17:
        print("Some countries do allow individuals to drive at 16 or 17 with supervision")
    elif d>=18:
        print("with a full licence only being granted at the age of 18")
    else:
        print("Enter the Correct Age")
        
print("") #for free space   
if a==8:
    print("So,Your Are From Oceania")
    d=int(input("Enter Your Age :"))
    if d<=13:
        print("Not Eligible")
    elif d<=15:
        print(" In only South Dakota is the youngest at just 14.5 years old")
    elif d==16:
        print("In Oceania Most states are from age 16")
    elif d==17:
        print(" In whilst New Jersey the oldest at Start from age 17")
    elif d>=18:
        print("You Will Get Unrestricted licence available at 18.You can't drive in Salvador if you are over 75 years.")
    else:
        print(" Enter The Correct Age")
elif a>=8:
    print("Enter Your Correct country Number")







 
