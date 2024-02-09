def checkIP(IP):
    dot=0
    for i in IP:
        if i == ".":
            dot=dot+1

    if dot == 3:
        return True
    else:
        return False
    
if checkIP('10.10.10.10.10'):
    print("ok")
else:
    print("not ok")