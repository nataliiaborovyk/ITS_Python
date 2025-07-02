class ContactManager:

    def __init__(self) -> None:
        self.contacts: dict[str, list[str]] = {}

    def create_contact(self, name: str, phone_numbers: list[str]) -> dict[str, list[str]]:
        if type(phone_numbers) != list:
            raise ValueError("Il tipo di telefono deve essere lista")
        if name not in self.contacts:
            self.contacts[name] = phone_numbers
            return {name: self.contacts[name]}
        else:
            raise ValueError("Errore: il contatto esiste già")
        
    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:
        if contact_name in self.contacts:
            if phone_number not in self.contacts[contact_name]:
                self.contacts[contact_name].append(phone_number)
                return {contact_name: self.contacts[contact_name]}
            else:
                raise ValueError("Errore: il numero di telefono esiste già" )
        else:
            raise ValueError("Errore: il contatto non esiste.")
        
    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:
        if contact_name in self.contacts:
            if phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(phone_number)
                return {contact_name: self.contacts[contact_name]}
            else:
                raise ValueError("Errore: il numero di telefono no è presente" )
        else:
            raise ValueError("Errore: il contatto non esiste.")
        
    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> dict[str, list[str]]:
        if contact_name in self.contacts:
            if old_phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(old_phone_number)
                self.contacts[contact_name].append(new_phone_number)
                #index : int = self.contacts[contact_name].index(old_phone_number)
                #self.contacts[contact_name][index] = new_phone_number
                return {contact_name: self.contacts[contact_name]}
            else:
                raise ValueError("Errore: il numero di telefono non è presente.")
        else:
            raise ValueError("Errore: il contatto non esiste.")
        
    def list_contacts(self) -> list[str]: 
        lista:list = []
        for k in self.contacts.keys():
            lista.append(k)
        return lista     #return list(self.contacts.keys())
    
    def list_phone_numbers(self, contact_name: str) -> list[str]:
        if contact_name in self.contacts:
            return self.contacts[contact_name]
        else:
            raise ValueError( "Errore: il contatto non esiste." )
        
    def search_contact_by_phone_number(self, phone_number: str) -> list:
        lista:list = []
        for k, v in self.contacts.items():
            if phone_number in v:
                lista.append(k)
            else:
                raise ValueError("Nessun contatto trovato con questo numero di telefono.")
        return lista
    
    def __str__(self) -> str:
        return ", ".join(f"{k}: {v}" for k, v in self.contacts.items())


c:ContactManager = ContactManager()
c.create_contact("Anna", ["1111111"])
print(c)

c.add_phone_number("Anna", "22222")
print(c)

c.remove_phone_number("Anna", "1111111")
print(c)

c.update_phone_number("Anna", "22222", "333333")
print(c)

print(c.list_contacts())
print(c.list_phone_numbers("Anna"))

print(c.search_contact_by_phone_number("333333"))