from abc import ABC, abstractmethod


class NoteAbstract(ABC):
    def __init__(self, args):
        for key, value in args.items():
            self.__setattr__(key, value)
    
    @abstractmethod
    def update_all(self, args):
        pass

    @abstractmethod
    def add_tag(self, tag):
        pass

    @abstractmethod
    def edit_tag(self, new_tag):
       pass

    @abstractmethod
    def edit_title(self, new_subject):
        pass
    @abstractmethod
    def edit_text(self, new_content):
        pass

