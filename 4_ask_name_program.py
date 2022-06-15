from email import message


name=input('Enter your name: ')
messages="His name is {}".format(name)
#messages="His name {}{}".format(f_name, l_name)
#messages="His name {1}{0}".format(f_name, l_name)
#messages= f"His name is (f_name, l_name)"
print(messages)