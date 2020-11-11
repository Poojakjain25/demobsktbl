print("Welcome aliens, we are hosting a basketball competition on 17th November. "
      "Kindly register yourself on or before 15th November to participate.")
x = input(" Please enter your name : ")
if x.isnumeric():
    print(" Please enter a valid name ")
else :
    pass
y = int(input(" Please enter your age  : "))
if y<10 :
    print(" Hey", x ,"! You are too young to participate. Kindly read the criteria ")
if y>=10 and y<=15 :
    h = int(input(" Please enter your height : "))
    if h>=120 and h<=140 :
        w = int(input(" Please enter your weight : "))
        if w>=20 and w<=40 :
            print("Hey" , x,"! You are eligible to participate in the basketball competition under junior category ")
        else :
            print(" Ohh! Looks like weight does not match with the required criteria. Kindly have a look at the eligibility conditions ")
    else :
        print(" Oops! Seems like Height criteria does not match. Kindly have a look at the eligibility conditions ")
elif y>15 and y<=22 :
    e = int(input(" Please enter your height : "))
    if e>140 and e<=165 :
        g = int(input(" Please enter your weight : "))
        if g>40 and g<=55 :
            print("Hey" , x,"! You are eligible to participate in the basketball competition under senior category ")
        else:
            print(" Ohh! Looks like weight does not match with the required criteria. Kindly have a look at the eligibility conditions ")
    else:
        print(" Oops! Seems like Height criteria does not match. Kindly have a look at the eligibility conditions ")
if y>22 :
    print(" Sorry", x ,"! You are not eligible to participate ")
