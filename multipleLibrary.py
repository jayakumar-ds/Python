class multipleFunctions():
    def oddEven():
        num5 = int(input("Enter the number"))
        if(num5%2==0):
            message = 'Even Number'
        else:
            message = 'Odd Number'
        return message
    def BMI():
         BMI = float(input("Enter the BMI Index:"))
         if(BMI<=18.5):
             print("Underweight")
             msg1 = "Underweight"
         elif(BMI<=24.9):
             print("Normal")
             msg1 = "Normal"
         elif(BMI<=29.9):
             print("OverWeight")
             msg1 = "OverWeight"
         else:
             print("Obesity")
             msg1 = "Obesity"
         return msg1     
    def subfields():
        lists = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are: ")
        for msg in lists:        
            print(msg)     
    def oddEven():
        num5 = int(input("Enter the number : "))
        if(num5%2==0):
            print(num5, "is Even Number")
        else:
            print(num5, "is Odd Number")

    def eligible():
        gender = input("Your Gender :")
        age = int(input("Your Age :"))
        if(gender=='male' and age>=21):
            msg = 'Your ELIGIBLE'
        elif(gender=='female' and age>=18):
            msg = 'Your ELIGIBLE'
        else:
            msg = 'NOT ELIGIBLE'
        return msg

    def find_Total_percentage(s1,s2,s3,s4,s5):
        total = s1+s2+s3+s4+s5
        percentage = total/500*100
    
        print("subject1= ",s1)
        print("subject2= ",s2)
        print("subject3= ",s3)
        print("subject4= ",s4)
        print("subject5= ",s5)
    
        print("Total : ",total)
        print("Percentage : ",percentage)

    def triangle(h1,h2,bh):
        height=int(input("Height :"))
        weight=int(input("Weight :"))
        af = (height*weight)/2
        print("Area of Triangle: ",af)
        pf = h1+h2+bh
        print("Height1:",h1)
        print("Height2:",h2)
        print("Breadth:",bh)
        print("Perimeter of Traingle: ",pf)