# from Notes import Notes


from notes.note_abstract import NoteAbstract


class Note(NoteAbstract):
    # Для того, щоб вірно додати тег, потрібно попросити користувача вводити теги через пробіл в форматі "#tag #tag"
    def __init__(self, args):
        super().__init__(args)

    def update_all(self, args):
        if "id" in args:
            args.pop("id")
        # print()
        for key, value in args.items():
            self.__setattr__(key, value)
        return self

    def add_tag(self, tag):
        if self.tag == ["No tag`s"]:
            self.tag = tag.split(" ")
        else:
            self.tag.append(tag)

    def edit_tag(self, new_tag):
        self.tag = new_tag.split(" ")

    def edit_title(self, new_subject):
        self.subject = new_subject

    def edit_text(self, new_content):
        self.content = new_content

    def __str__(self):
        return f"id: {self.id}\tTags: {self.tags}\tsubject: {self.subject}\tContent: {self.content}"
