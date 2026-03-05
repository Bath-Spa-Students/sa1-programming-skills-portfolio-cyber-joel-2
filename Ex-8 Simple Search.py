names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
#Search For Name
search = input("Enter A Name To Search For: ").strip()
if search in names:
    print(f"{search} Found !!!")
else:
    print(f"{search} Not Found...")