'''
3-6. More Guests: You just found a bigger dinner table, so now more space 
is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call
 to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
'''


#esercizio_3-6
print("\n esercizio_3-6\n")

guest_list: list = ["Marilyn Monroe", "John F. Kennedy", "Jacqueline Kennedy"]

print("I found a bigger table, so we have more avaible space\n")

guest_list.insert(len(guest_list), "Anna")
guest_list.extend(["Marco", "Stefano"])

print(*guest_list, sep=", ")

for i in guest_list:
    print(f"\nDear {i} would you like to come to diner?")

