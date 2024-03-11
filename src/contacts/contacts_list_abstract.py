from abc import ABC, abstractmethod


class ContactListAbstracts(ABC):
    def __init__(self):
        self.data = []
        self.id = 0

    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def add(self, data):
        pass

    @abstractmethod
    def set(self, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def find(self, value):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def show_col(self, data):
        pass

    @abstractmethod
    def show_all(self, data):
        pass

    @abstractmethod
    def birthday(self, dates):
        pass
