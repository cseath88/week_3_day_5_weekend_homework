from flask import render_template, request, redirect
from app import app
from models.library import library, add_new_book, delete_book
from models.book import *


@app.route('/library')
def index():
    return render_template('index.jinja', title='Home', library=library)

@app.route('/book/<index>')
def individual_book(index):
    book = library[int(index) -1 ]
    return render_template('book.jinja', book = book, title = "Book Title")

@app.route('/library', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    newbook = Book(title=title, author=author, genre=genre)
    add_new_book(newbook)
    return redirect('/library')

@app.route('/library/delete/<name>', methods=['POST'])
def remove_book(name):
    delete_book(name)
    return redirect('/library')