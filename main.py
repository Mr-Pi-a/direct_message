import os

os.system("clear")
while True:
    print("                 \033[1;32;40mDirect message sender\033[1;32;40m  ")
    print("           \033[93mCHOOSE COUNTRY YOU WANNA SEND MESSAGE TO \033[93m")
    print("\033[92mOPTION 1...INDIA\033[92m")
    print("OPTION 2...PAKISTAN")
    print("OPTION 3...AMERICA")
    print("OPTION 4...CANADA")
    print("OPTION 5...GERMANY")
    print("OPTION 6...UNITED KINGDOM")
    print("OPTION 7...CUSTOM")
    q = input("\033[91m\n\nENTER OPTION ==>>>\033[91m\033[92m\033[92m ")

    while True:
        number = input("\033[91mENTER THE PHONE NUMBER===>>>\033[91m\033[92m\033[92m ").replace(" ", "")
        if number=="q":
            exit()
        if not len(number) == 10:
            print("\n          \033[91m Please enter a correct number ..!\033[91m\n")
            print("          \033[91m ENTER VALID 10 DIGIT NUMBER\n\n\033[91m")
        else:
            break

    if (q == "india" or q == "1"):
        new_number = "+91" + number
    elif (q == "pakistan" or q == "2"):
        new_number = "+92" + number
    elif (q == "america" or q == "3"):
        new_number = "+1" + number
    elif (q == "canada" or q == "4"):
        new_number = "+1" + number
    elif (q == "germany" or q == "5"):
        new_number = "+49" + number
    elif (q == "united kingdom" or q == "6"):
        new_number = "+44" + number
    elif q=="q":
        exit()
    elif (q == "custom" or q == "7"):
        custom_code = input("\033[91m\n\nENTER COUNTRY CODE==>>>\033[91m\033[92m\033[92m")
        if custom_code.startswith("+"):
            new_number = custom_code + number
        else:
            new_number = "+" + custom_code + number
    else:
        print("ERROR!!!")


    whatsapp = 'https://api.whatsapp.com/send?phone=' + new_number
    os.system("xdg-open " + whatsapp)
    os.system("clear")
    print("                    \033[1;32;40mDONE !!!!\033[1;32;40m")
    print("                   \033[91m|---------|\033[91m")
    print("\033[0m\033[0m")
