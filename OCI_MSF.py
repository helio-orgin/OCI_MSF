import os

os.system("pkg install figlet -y")
os.system("pkg install wget -y")
os.system("figlet -f big OCI")
print("Downloading Termux Black.... ")
os.system("wget https://github.com/Hax4us/TermuxBlack/raw/master/install.sh")
os.system("chmod +x install.sh")
os.system("bash install.sh -i")
print("Now we are going install Metaspliot. It takes mostly 5 to 15 min based on your internet speed")
# choice = input("You need 500 mb data to install Metasploit y/n:")
yes = ["y", "Y"]
no = ["n" ,"N"]
while True:
    choice = input("You need 500 mb data to install Metasploit y/n:")
    if choice in yes:
        os.system("git clone https://github.com/helio-orgin/OCI_MSF/blob/main/metasploit.sh")
        os.system("chmod +x metasploit.sh")
        os.system("./metasploit.sh")
        print("Thanks for using our tool ---->  Origin Cyber Info")
        break
    elif choice in no:
        print("Try this tool when you have sufficient data. Thankyou for using our tool")
        break
    else:
        print("Invalid input, try again")
