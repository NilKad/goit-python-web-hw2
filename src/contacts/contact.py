from contacts.contact_abstract import ContactAbstact


class Contact(ContactAbstact):
    def __init__(self, args, id):
        super().__init__(args, id)

    def update_all(self, args):
        if "id" in args:
            args.pop("id")
        for key, value in args.items():
            self.__setattr__(key, value)
        return self

    def add_phones(self, phones):
        self.update_all(phones)
        return self

    def edit_phone(self, args):
        old_phone = args["phone_src"]
        new_phone = args["phone_dst"]
        for el in self.__phones:
            if old_phone == el.value:
                el.value = new_phone
        return self

    def del_phone(self, args):
        for x in args["phones"]:
            for el in self.__phones:
                if x == el.value:
                    self.__phones.remove(el)
                    break
            return self

    def is_contains_phone(self, phone):
        all_phones = str(self.phones)
        for el in all_phones:
            if phone in el:
                return True
        return False

    def __str__(self):
        res = f"{self.id}\t{self.first_name} {self.last_name}\t phones: { self.phones}\temail: {self.email} address: {self.address}\t birthday: {self.birthday} "
        return res
