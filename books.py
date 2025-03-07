import logging
from fastapi import Body, FastAPI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/helloworld")
def Hello_World():
    logger.info("Hello World")  # ✅ Logs will be visible in the console

@app.get("/books")
async def read_all_books():
    logger.info("Fetching all books")
    return BOOKS

@app.get("/books/{book_title}")
async def read_book_by_title(book_title: str):
    logger.info(f"Searching for book: {book_title}")
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get("/books/")
async def read_category_by_query(category: str):
    logger.info(f"Fetching books in category: {category}")
    books_to_return = [book for book in BOOKS if book.get('category').casefold() == category.casefold()]
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    logger.info(f"Fetching books by author: {book_author} in category: {category}")
    books_to_return = [book for book in BOOKS if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold()]
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book: dict = Body()):
    logger.info(f"Adding new book: {new_book}")
    BOOKS.append(new_book)
    return {"message": "Book added successfully", "book": new_book}

@app.put("/books/update_book")
async def update_book(updated_book: dict = Body()):
    logger.info(f"Updating book: {updated_book}")
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            logger.info(f"Book updated: {updated_book}")
            return {"message": "Book updated successfully", "book": updated_book}
    logger.warning(f"Book not found for update: {updated_book.get('title')}")
    return {"error": "Book not found"}


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

'''
Get all books from a specific author using path or query parameters
'''

@app.get("/books/byauthor/{author}")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return
