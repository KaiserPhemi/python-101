N = int(input("Enter number of key-value pair: "))

phoneBook = {}

if N >= 1:
    if N <= 10**5:
        for i in range(1, N+1):
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            phoneBook[name] = number
        
    else:
        pass
else:
    pass
print(phoneBook)

query = input().strip()


while query in phoneBook:
    if phoneBook[query]:
        print(query + "=" + phoneBook[query])

    else:
        print("Not found")
