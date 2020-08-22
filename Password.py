password = int(input("Enter Password: "))
b = int(7827156067) / int(password)
a = int(password) * int(b)
c = int(7827156067)
if a == c:
  print("Success! Encryption Key Match")
else:
  print("Failure.. Encrypting Data")
