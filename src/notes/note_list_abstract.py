from abc import ABC, abstractmethod


class NoteListAbstract(ABC):
    def __init__(self):
        self.__id = 0
        self.data = []

    @abstractmethod
    def add(self, args):
        pass

    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def find_by_tags(self, args):
        pass

    @abstractmethod
    def show_by_tags(self, args):
        pass

    @abstractmethod
    def sort_by_tag(self):
        pass

    @abstractmethod
    def show_by_id(self, id):
        pass

    @abstractmethod
    def find_by_subject(self, subject):
        pass

    @abstractmethod
    def show_by_subject(self, subject):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def show_all_notes(self, data):
        pass

    @abstractmethod
    def show_one(self, data):
        pass

    @abstractmethod
    def show_all(self, data):
        pass
