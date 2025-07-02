import re    #contacts: dict[str,list[str]]

class ContactManager:
    def __init__(self) -> None:
        self.contacts:dict[str,list[str]] = {}

    def create_contact(self, name:str, phone_numbers:list[str]) -> None:
        if name not in self.contacts:
            clean_phone_numbers: list = []
            for i in phone_numbers:
                i = i.strip()
                if re.fullmatch(r'[0-9]{10}', i):
                    clean_phone_numbers.append(i)
                else:
                    raise ValueError(f"Il numero di telefono {phone_numbers} non è scritto in formato giusto")
            self.contacts[name] = clean_phone_numbers
        else:
            raise ValueError("Errore: il contatto esiste già")
                      

    def add_phone_number(self, contact_name: str, phone_number: str) -> dict:
        if contact_name in self.contacts:
            phone_number = phone_number.strip()
            if re.fullmatch(r'[0-9]{10}', phone_number):
                if phone_number not in self.contacts[contact_name]:
                    self.contacts[contact_name].append(phone_number)
                    return {contact_name: self.contacts[contact_name]}
                else:
                    raise ValueError("Errore: il numero di telefono esiste già")
            else:
                raise ValueError(f"Il numero di telefono {phone_number} non è scritto in formato giusto")
        else:
            raise ValueError("Errore: il contatto non esiste") 
        
    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict:
        if contact_name in self.contacts:
            phone_number = phone_number.strip()
            if re.fullmatch(r'[0-9]{10}', phone_number):
                if phone_number in self.contacts[contact_name]:
                    self.contacts[contact_name].remove(phone_number)
                    return {contact_name: self.contacts[contact_name]}
                else:
                    raise ValueError("Errore: il numero di telefono non è presente")
            else:
                raise ValueError(f"Il numero di telefono {phone_number} non è scritto in formato giusto")
        else:
            raise ValueError("Errore: il contatto non esiste") 

    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> dict: 
        if contact_name in self.contacts:
            old_phone_number = old_phone_number.strip()
            new_phone_number = new_phone_number.strip()
            if re.fullmatch(r'[0-9]{10}', old_phone_number):
                if re.fullmatch(r'[0-9]{10}', new_phone_number):
                    if old_phone_number in self.contacts[contact_name]:
                        self.contacts[contact_name].remove(old_phone_number)
                        self.contacts[contact_name].append(new_phone_number)
                        return {contact_name: self.contacts[contact_name]}
                    else:
                        raise ValueError("Errore: il numero di telefono non è presente")
                else:
                    raise ValueError(f"Il numero di telefono {new_phone_number} non è scritto in formato giusto")
            else:
                raise ValueError(f"Il numero di telefono {old_phone_number} non è scritto in formato giusto")
        else:
            raise ValueError("Errore: il contatto non esiste")        

    def list_contacts(self) -> list[str]:
        lista_contatti:list = []
        for k in self.contacts.keys():
            lista_contatti.append(k)
        return lista_contatti
        #return list(self.contacts.keys())
    
    def list_phone_numbers(self, contact_name: str) -> list[str]: 
        if contact_name in self.contacts:
            return self.contacts[contact_name]
        else:
            raise ValueError("Errore: il contatto non esiste")
    
    def search_contact_by_phone_number(self, phone_number: str) -> list[str]:
        lista_contatti: list = []
        phone_number = phone_number.strip()
        if re.fullmatch(r'[0-9]{10}', phone_number):
            for k, v in self.contacts.items():
                if phone_number in v:
                    lista_contatti.append(k)
            return lista_contatti
        else:
            raise ValueError(f"Il numero di telefono {phone_number} non è scritto in formato giusto")

    def __str__(self) -> str:
        return "\nContatti:\n" + "\n".join(f"  {k}: {v}" for k, v in self.contacts.items())
    
    def __repr__(self) -> str:
        contacts: str =  ", ".join(f"  {k}: {v}" for k, v in self.contacts.items())
        return f"ContactManager({contacts})"


if __name__ == "__main__":
    c1:ContactManager = ContactManager()
    c1.create_contact("Anita Blum", ["1111111111"])
    print(c1)
    c1.create_contact("Anita Varga", ["2222222222"])
    print(c1)
    #c1.add_phone_number("Anita Blum", ["7769874678"])
    c1.add_phone_number("Anita Blum", "3333333333")
    print(c1)
    c1.remove_phone_number("Anita Blum", "     1111111111")
    print(c1)
    c1.update_phone_number("Anita Blum","3333333333", "4444444444")
    print(c1)
    print(c1.list_contacts())
    print(c1.list_phone_numbers("Anita Varga"))
    c1.add_phone_number("Anita Varga", "5555555555")
    print(c1.list_phone_numbers("Anita Varga"))
    print(c1.search_contact_by_phone_number("2222222222"))








