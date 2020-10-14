def int_input(number): #Function for handle error
    while True:
        try:
            userInput = int(input(number))
        except ValueError:
            print("Not a integer! Try again.")
            continue
        else:
            return userInput
            break

def search(list, n): #Function for linear search
    i = 0 
    while i < len(list): 
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1 
    return False

"""The Main Program"""

print("Welcome to Linear Search")
n = int_input("What you wanna search: ")
list = [5, 3, 6, 9, 0, 2, 8, 1, 4, 7]

pos = 0
if search(list, n):
    print("Found at", pos)
else:
    print("Not Found")