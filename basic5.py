for i in range(1,11):
    print(i,end="\t")

a=[1,2,3,4,5]
for i in a:
    print(i)
    
i=1
while i<11:
    print(i)
    i+=1

          
import random
d=[
   """
-----
|   |
| o |
|   |
-----
""","""

-----
|o  |
|   |
|  o|
-----
""","""

-----
|o  |
| o |
|  o|
-----
""","""

-----
|o o|
|   |
|o o|
-----
""","""

-----
|o o|
| o |
|o o|
-----
""","""

-----
|o o|
|o o|
|o o|
-----
 """
   ]
c="Yes"
while c=="Yes":
    c=input("Enter Yes to roll and No to Stop.")
    if c=="Yes":
        r=random.randint(0, 5)
        print(d[r])
        






























