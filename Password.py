password = int(input("Enter Password: "))
b = 7827156067 / password
a = password * int(b)
c = 7827156067
if a == c and password not in [1, c]:
  print("Success! Encryption Key Match")
else:
  print("Failure.. Encrypting Data")
 
