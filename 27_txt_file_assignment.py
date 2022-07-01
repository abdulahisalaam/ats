
def file_check_password():
   data = {}

   data['username'] = input("Enter Your Username here: ")
   data['firstname'] = input("Enter Firstname: ")
   data['lastname'] = input("Enter Lastname: ")
   data['password'] = input("Enter Password: ")
   data['confirm_password'] = input("Enter Password Again: ")



   print(data)
   dada = str(data)

   with open(f"{data['username']}.txt", 'w+') as n:
      n.write(dada)

if __name__ == "__main__":
   file_check_password()
   