class Publication:
    title = ""
    author = ""
    def __init__(self, title, author):
        self.__title = title
        self.__author = author
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def set_title(self, title):
        self.__title = title
    def set_author(self, author):
        self.__author = author
    def display_info(self):
        print(f"Title: {self.__title}\nAuthor: {self.__author}")

class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_pages = number_pages
    def get_number_of_pages(self):
        return f"Number of pages: {self.__number_pages}"
    def set_number_of_pages(self, number_pages):
        if number_pages > 0:
            self.__number_pages = number_pages
        else:
            print("Number of pages must be positive.")

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = issue_number
    def get_issue_number(self):
        return f"Issue number: {self.__issue_number}"
    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("Issue number must be positive.")


pub1 = Publication("Diary of a Wimpy Kid", "Jeff Kinney")
book1 = Book("Diary of a Wimpy Kid: Rodrick Rules", "Jeff Kinney", 217)
magazine1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())
print("\nMagazine Information:")
magazine1.display_info()
print(magazine1.get_issue_number())
