from abc import ABC, abstractmethod
from contacts.address import Address
from contacts.birthday import Birthday
from contacts.email_cl import Email_str
from contacts.first_name import First_name
from contacts.last_name import Last_name
from contacts.phone import Phone


class ContactAbstact(ABC):
    def __init__(self, args, id):
        self.__id = id
        self.__phones = set()
        for key, value in args.items():
            self.__setattr__(key, value)

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = First_name(value)

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = Last_name(value)

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = Address(value)

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        self.__birthday = Birthday(value)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = Email_str(value)

    @property
    def phones(self):
        def __str__(self):
            res = set()
            for el in self.__phones:
                res.add(str(el))
            return res

        return __str__(self)

    @phones.setter
    def phones(self, value):
        phone_in_set = str(self.phones)
        for el in value:
            print("----Phone: ", el)
            if el not in phone_in_set:
                self.__phones.add(Phone(el))

    @property
    def id(self):
        return self.__id

    @id.setter
    def _id(self, id):
        self.__id = id

    @abstractmethod
    def update_all(self, args):
        pass

    @abstractmethod
    def add_phones(self, phones):
        pass

    @abstractmethod
    def edit_phone(self, args):
        pass

    @abstractmethod
    def del_phone(self, args):
        pass

    @abstractmethod
    def is_contains_phone(self, phone):
        pass
