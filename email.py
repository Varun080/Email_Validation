email = input(" Enter your Email : ")
k,j,d =0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] =="." )^ (email[-3] =="."):
                # ^ output will be true only if only one condition is true
                for i in email:
                    if i==i.isspace():
                        k =1
                    elif i.isalpha():
                        j =0
                    elif i.isdigit():
                        continue
                    elif (i == "_") or (i == ".") or (i == "@"):
                        continue
                    else:
                        d =1
                if (k == 1) or  (j == 1) or (d == 1):
                    print("Worng Email")
                else:
                    print(" Everything is good")
            else:
                print("Worng Email 4")
        else:
            print("Worng Email")
    else:
        print("Worng Email 2")

else:
    print("Worng Email 1")