class Publication: # Parent Class
  def __init__(self, title, author):  # Attributes 
    self.title = title
    self.author = author
    
  def get_title(): #getters and start of methods
    return self.title
  def get_author():
    return self.author
  def set_title(): #setter
    self.title = title
  def set_author():
    self.author = author
  def display_info():
    print("Title", self.title)
    print("Author", self.author)
    
class Book(Publication):
  def __init__(self, title, author, number_of_pages):
    self.title = title
    self.author = author
    self.number_of_pages = number_of_pages
  
  def get_number_of_pages():
    return self.number_of_pages
  def set_number_of_pages():
    if number_of_pages <= 0:
      print("Number of pages must be positive.")
    else:
      self.number_of_pages = number_of_pages
    
class Book(Publication):
  def __init__(self, title, author, issue_number):
    self.title = title
    self.author = author
    self.issues_number = issue_number
  
  def get_issue_number():
    return self.issues_number
  def set_issue_number():
    self.issues_number = issue_number

pub1 = Publication()
book1 = Book()
mag1 = Magazine()

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number)
