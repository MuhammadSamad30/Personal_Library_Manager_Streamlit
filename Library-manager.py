import streamlit as st
import json
import os

data_file = 'library.txt'


def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []


def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file)


def main():
    st.title('📚 Personal Library Manager')

    data = load_data()

    menu = ['Add a book', 'Remove a book', 'Search for a book',
            'Display all books', 'Display statistics']
    st.sidebar.markdown('👨‍💻 **Muhammad Samad**')
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Add a book':
        st.subheader('Add a New Book')
        title = st.text_input('Title')
        author = st.text_input('Author')
        year = st.text_input('Year')
        genre = st.text_input('Genre')
        read = st.checkbox('Have you read the book?')
        if st.button('Add Book'):
            new_book = {'title': title, 'author': author,
                        'year': year, 'genre': genre, 'read': read}
            data.append(new_book)
            save_data(data)
            st.success(f'Book "{title}" added successfully!')

    elif choice == 'Remove a book':
        st.subheader('Remove a Book')
        titles = [book['title'] for book in data]
        title = st.selectbox('Select a book to remove', titles)
        if st.button('Remove Book'):
            data = [book for book in data if book['title'] != title]
            save_data(data)
            st.success(f'Book "{title}" removed successfully!')

    elif choice == 'Search for a book':
        st.subheader('Search for a Book')
        title = st.text_input('Enter book title')
        if st.button('Search'):
            found = next(
                (book for book in data if book['title'].lower() == title.lower()), None)
            if found:
                st.json(found)
            else:
                st.error(f'Book "{title}" not found!')

    elif choice == 'Display all books':
        st.subheader('All Books')
        if data:
            for book in data:
                st.markdown(
                    f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
        else:
            st.info('No books found!')

    elif choice == 'Display statistics':
        st.subheader('Library Statistics')
        total_books = len(data)
        total_read = len([book for book in data if book['read']])
        percentage_read = (total_read / total_books) * \
            100 if total_books > 0 else 0
        st.write(f'Total books: {total_books}')
        st.write(f'Percentage read: {percentage_read:.2f}%')


if __name__ == '__main__':
    main()

# created by Muhammad Samad
st.markdown('---')
st.markdown('👨‍💻 **Created by Muhammad Samad**')
