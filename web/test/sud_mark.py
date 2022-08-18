print("Enter your cat marks")
"""
your cat 1 marks are converted to 14, 
cat2 and cat 3 are converted to 15 and 
6 marks is for your assignment.
14+15+15+6=50
It assumes you got 6 on assignment
"""
cat1 = int(input("cat1 (out of 50):"))
cat2 = int(input("cat2 (out of 50):"))
cat3 = int(input("cat3 (out of 30):"))
internal = ((cat1*14)/50 + (cat2*15)/50 + (cat3/2))+6
weit = int(input("Enter your internal weightage (eg:40):"))
internal *= weit/50
print(f"your internal mark is {internal}/{weit}")
min = (50-internal)*100/(100-weit)
print(f"minimum marks needed to pass in semester {min}/100")