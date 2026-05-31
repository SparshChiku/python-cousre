medical = input("medical cause y / n:")
if medical =="y":
    print("allowed")
else:
    att = int(input("atenddence:"))
    if att >= 75:
        print("allowed")
    else:
        print("not allowed")