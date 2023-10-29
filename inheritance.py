from __future__  import annotations


    
class ContactList(list["Contact"]):
    def search(self, name:str) -> list["Contact"]:
        matching_contacts : list["Contact"] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contact = ContactList()

    def __init__(self,name:str, email:str)->None:
        self.name = name
        self.email = email
        Contact.all_contact.append(self)

    def __repr__(self)-> str:
            return(
                f"{self.__class__.__name__}("
                f"{self.name!r}, {self.email!r})"f")"
            )
    

c1 = Contact("John A", "johna@gmail.com")
c2 = Contact("John B", "johnb@gmail.com")
c3 = Contact("Jenna C", "jenna@gmail.com")
print([c.name for c in Contact.all_contact.search('John')])





