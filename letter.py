letter='''Dear <NAME>,Gretting from abc company house.Iam Happy to tell you about selesction
You are seecyted !
Thanks a lot!
Bill
Dte:<DATE>'''
name=input("Enter a name \n")
date=input("Enter aDate \n")
letter= letter.replace("<NAME>",name)
letter=letter.replace("<DATE",date)
print(letter)
