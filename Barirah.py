import streamlit as st
import json
from PIL import Image

class MyPersonalLibrary:
    def __init__(self):
        self.books = []
        self.data_file = "mini_books.json"
        self.load_books()

    def load_books(self):
        try:
            with open(self.data_file, "r") as file:
                self.books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_books(self):
        with open(self.data_file, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self):
        st.subheader("Add a New Book")
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Science", "Fantasy", "Biography"])
        has_read = st.radio("Have you read this book?", ("Yes", "No"))

        book_cover = st.file_uploader("Upload Book Cover (optional)", type=["jpg", "png", "jpeg"])

        if st.button("Add Book"):
            if title and author:
                book = {
                    "title": title,
                    "author": author,
                    "genre": genre,
                    "read": has_read == "Yes",
                    "cover": book_cover if book_cover else None,
                }
                self.books.append(book)
                self.save_books()
                st.success("Your new book has been added!")
            else:
                st.warning("Please provide at least the book title and author.")

    def display_books(self):
        if not self.books:
            st.write("Your library is currently empty!")
            return

        st.subheader("Your Personal Library")
        for book in self.books:
            st.write(f"**{book['title']}** by {book['author']} ({book['genre']}) - {'Read' if book['read'] else 'Unread'}")
            if book["cover"]:
                cover_img = Image.open(book["cover"])
                st.image(cover_img, width=100)
            st.markdown("---")

    def run(self):
        # Set a creative background color
        st.markdown(
            """
            <style>
            body {
                background-color: #FFEBF0;
                color: #5A2D2D;
            }
            h1 {
                font-family: 'Courier New', Courier, monospace;
                color: #5A2D2D;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.title("My Personal Library")
        menu = ["Add Book", "View Library", "Exit"]
        choice = st.radio("Select an option", menu)

        if choice == "Add Book":
            self.add_book()
        elif choice == "View Library":
            self.display_books()
        elif choice == "Exit":
            st.write("Goodbye! Happy reading!")

if __name__ == "__main__":
    library = MyPersonalLibrary()
    library.run()