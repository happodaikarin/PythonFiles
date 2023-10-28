from __future__  import annotations


class Contact:
    def __init__(self,name:str, email:str)->None:
        self.name = name
        self.email = email

class ContactList(list["Contact"]):
    def serch():




