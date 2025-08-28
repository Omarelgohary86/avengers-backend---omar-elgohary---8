print("welcome to the rabbit world")
A=[["🍀" , "🍀" , "🍀"] , ["🍀" , "🍀" , "🍀"] , ["🍀" , "🍀" , "🍀"]]
print(A[0])
print(A[1])
print(A[2])
print()
print("where should the rabbit do ? 🐇🐇🐇")
R=int(input("enter the row : "))
row=R-1
C=int(input("enter the column : "))
column=C-1
A[row][column]="🐇" 
print ("dones")
print(A[0])
print(A[1])
print(A[2])




#touple
z= ("omar","ali",4 , 5.6)
#set
z= {"omar","ali",4 , 5.6}


# dic
dic ={}
name = input("what is your name ? ")
place = input ("where are you from ? ")
age = input (f"how old are you {name} ? ")
dic["name"]=name
dic["place"]=place
dic["age"]=age
print (dic)
