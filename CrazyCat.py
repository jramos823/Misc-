#Cat displays message 

def crazycat():
    userinput = input("Enter for cat to say it! ")
    topborder = "_"
    bottomborder = "-"
    print("          {}".format(topborder * len(userinput)))
    print("        < {} >".format(userinput))
    print("          {}".format(bottomborder * len(userinput)))
    print("         /")
    print(" /\_/\  /") 
    print("( o.o )") 
    print(" > ^ <") 

