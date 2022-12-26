contacts= {
"ABHINAV KUMAR": 7263738387,
"SURYA KANT": 8656789735,"KRISHNA KUMAR": 9859561235,"ARANAV KUMAR": 7656789735," JASVEER YADAV": 7656789735,
"NITHISH CHIDURALA": 9966629299,"JAIDEEP YADAV":8956147859,"ANKIT GUPTA":7858452369,"RACHIT AHARMA":7845256891,
"HEMANTH SAI KUMAR PENTAKOTA":7845253691,"ANVIT MIKKILI":7898541235,"SUBHAM PANDEY":7589632519,
"SURYANSHU KUMAR RAI":7895658125,"ABHISHEK YADAV":7852361589,"AMIT KUMAR YADAV":7458961235,"JOEL GEORGE PHILIP":8956147859
,"NIKHIL KUMAR":8956147859,"ALWIN GEORGE":8956147859,"POONAGANTI UDAY":7895623145,"NITHIN M":7485965412,"ROHAN KUMAR":8956147859,
"RISHAV KUMAR":6585961235}
def single_search():
	name=input("Enter contact name you want to search= ").upper()
	if name in contacts:
		print(f"\n{name}: {contacts[name]}")
	else:
	   b=input("\n This contact not found\nIf you want to add one, type 'Yes' else type 'No': ").lower()
	   if b=="yes":
	     new_contact(name)
	     print(f"{name}: {contacts[name]}")
	   elif b=="no":
	     	pass
	   else:
	     print("Enter  Yes or No")

def multiple_search():
	     result={}
	     s1=[]
	     s=0
	     name1=input("Enter  contact's name that you want to search seperated by commas‍= ").split(",")
	     for i in name1:
	     			i=i.upper()
	     			if i in contacts:
	     				result[i]=contacts[i]
	     			else:
	     				s1.append(i)
	     				s+=1
	     if s>0:
	     	c=(input(f"\nCouldn't find contacts {s1} . \nDo you wish to add them? Enter Yes or No: ")).lower()
	     	if c=="yes":
	     		for i in s1:
	     			new_contact(i)
	     			if i in contacts:
	     				result[i]=contacts[i]
	     		print()
	     		print(result)
	     	elif c=="no":
	     		print()
	     		if result=={}:
	     			pass
	     	else:
	     		print("\n")
	     else:
	     	print()
	     	print(result)
	     	
		
	     		
def new_contact(contact_name):
	     print()
	     contact_number=int(input("Enter their contact number: "))
	     contacts[contact_name]=contact_number
	     
choice=int(input("      --: Contacts of Section KOC03:-- \n\nChoose the option Below \n1.Search for a single contact \n2.List of all contacts\n3. Search for more than one contacts \n \nEnter your choice: "))

if choice==1:
	single_search()
	
elif choice==2:
	print()
	print(contacts)
	
elif choice==3:
	multiple_search()

else:
	print("Choose from the given options!")
