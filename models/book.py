class Book():

    def __init__(self, title, author, genre, checked_out=False):
        self.title = title
        self.author = author
        self.genre = genre
        self.checked_out = checked_out

    def status(self):
        return "Checked out" if self.checked_out else "Available"