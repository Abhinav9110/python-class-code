with open ('abd.txt','r')as ab:
    c=0
    lines=ab.readlines()
    for l in lines:
        c=c+1
        print(l)
        print("No of lines in file abd.txt=",c)
