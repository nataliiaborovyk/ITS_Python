'''
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, 
so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, 
stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with 
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.
'''


#esercizio_3-5
print("\n esercizio_3-5\n")

guest_list: list = ["Marilyn Monroe", "John F. Kennedy", "Jacqueline Kennedy"]

#versione 1
guest_list_refuse: list = guest_list[1]
print(f"{guest_list_refuse} can not come\n")

guest_list[1] = "Elton John"
print(*guest_list, sep=", ")

# versione 2
guest_list_refuse: list = guest_list[0]
print(f"\n{guest_list_refuse} can not come\n")

guest_list.remove("Marilyn Monroe")
guest_list.insert(0, "Wolt Disney")

print(*guest_list, sep=", ")
for i in guest_list:
    print(f"\nDear {i} would you like to come to diner?")

