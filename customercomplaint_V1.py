#Customer Complaint System V 2
#Programmer Courtney 
#4/13/2021
#################################
#This program opens the custTest.txt
#and prompts the customer to enter their information
#along with a comment on the store.
########################################
#4/18/2021
#Re-formatted for better ease of use 
########################################
#For final implementation the file name should be changed to somthing else
#For testing purposes it shall remain custTest.txt until testing is finished
print("\n")
print("Contact Us!")
print("\n________________________________________________________\n")
print("\n")
#prompts customer to enter information (For manager to later be able to send feedback)
print("Name: \n")
  
with open("custTest.txt", "a") as f:
  f.write("\n______________________________________________________\n")
  f.write("Name: ")

  f.write(input())
  f.write("\n")

print("\n")
print("Contact info:")
print("\n") 

with open("custTest.txt", "a") as f:
  f.write("Contact info:")
  f.write(input())
  
  f.write("\n--------------------------------------------------------\n")
  f.write("\n")
print("\n")
#prompts customer to enter comment (For manager to later be able to send feedback)
print("Please enter your comment: \n")

with open("custTest.txt", "a") as f:
    f.write("Customer Comment/Complaint:")
    f.write("\n")
    f.write(input())
    f.write("\n_____________________________________________\n")

f.close()
