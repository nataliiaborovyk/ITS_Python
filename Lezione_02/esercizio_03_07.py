'''
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive 
in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message 
saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. 
Each time you pop a name from your list, print a message to that person letting 
them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. 
Print your list to make sure you actually have an empty list at the end of your program.
'''

#esercizio_3-7
print("\n esercizio_ 3-7\n")


#dal esercizio 3-6
guest_list: list = ["Marilyn Monroe", "John F. Kennedy", "Jacqueline Kennedy"]
guest_list.insert(len(guest_list), "Anna")
guest_list.extend(["Marco", "Stefano"])

print(*guest_list, sep=", ")

print("\n\nI am so sorry, we have space only for 2 people\n")

for i in guest_list[2:]:
    print(f"Dear { guest_list[len(guest_list)-1] } we are so sorry, we can't invite you to diner")
    guest_list.pop()
    print(f"List: {guest_list} \n")

for i in guest_list:
    print(f"\nDear {i} would you like to come to diner?\n")

del guest_list
#print(guest_list)