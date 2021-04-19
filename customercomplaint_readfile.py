#Customer Complaint System V 2.0
#Programmer Courtney 
#4/16/2021
#################################
#This program opens the custTest.txt
#Allowing the store manager to read from the files
########################################

########################################
#For final implementation the file name should be changed to somthing else
#For testing purposes it shall remain custTest.txt until testing is finished

f = open("custTest.txt", "r")
print(f.read())

f.close()
