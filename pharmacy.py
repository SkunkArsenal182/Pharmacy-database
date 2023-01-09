 
from database1 import *

print("------------------ MENU ------------------")


while True:
   print("Welcome to NewLife Pharmacy. Select an option to continue")
   options = """
1. Search Available medicine by symptoms          
2. Print medicine in alphabetical order  
3. Search Available medicine by brand
4. Search Available medicine by name
5. Add New medicine
6. Exit                               
                                  

Select An Option To Continue: """
  
   try:
       option = int(input(options))
       
       if option not in range(1,7):
           raise ValueError
       if option == 1:
          
           x = input("Enter Symptom Name: ")

           print("Available medicines are:")
           print("medicine name | manufacturer | price | Quantity | symptoms ")
           y = searchMedicineSymptom(x)
           for medicine in y:
               print(medicine)
           print("_____________________________\n\n")
          
       elif option == 2:
        
           
           print("Available medicines in store:")
           print("medicine name | manufacturer | price ")
           
           mycursor.execute("""SELECT Name,Manf,Price FROM Medicine ORDER BY Name; """)
           for medicine in mycursor:
                print(medicine[0],medicine[1],medicine[2],sep=" | ")
           print("____________________________\n\n")

       elif option == 3:
          
           x = input("Enter brand Name: ")
           print("Available Medicines are:")
           y = searchMedicineBrand(x)
           for medicine in y:
               print(medicine)

           print("\n\n")
          
       elif option == 4:
           
           x = input("Enter Medicine Name: ")
           print("Available Medicines are:")
           
           print("medicine name | manufacturer | price ") 
           y = searchMedicine(x)
           for medicine in y:
               print(medicine[0],medicine[1],medicine[2],sep="|")

           print("___________________________\n\n")
          
       elif option == 5:
           
           medicine = input("Medicine name:")
           Manf = input("manufacturer name:")
           
           try:
                
                mycursor.execute("""SELECT * FROM Medicine WHERE Name="{Name}" AND Manf="{Manf}" """.format(Name=medicine,Manf=Manf))
                
                for i in mycursor:
                    
                    raise Exception

              
                price = input("Price:")
                Quantity = input("Quantity:")
                Symptom = input("Symptom:")
                addRecord(medicine,Manf,price,Quantity,Symptom)

            
                except Exception:
                    print("Medicine Already Exists!")
                    x = input("Do you want to update quantity")
                    if x == "yes":
                        Quantity = input("Quantity:")
                        updateCase(Quantity,medicine,Manf) 

                    else:

                        continue
           print("Added medicine To store List")
           print("____________________________\n\n")


       elif option == 6:
           print("Entering Data...")
           mydb.commit()
           print("Done.")
           break
   except ValueError:
       print("Invalid Option, Try Again \n")
       continue
  
