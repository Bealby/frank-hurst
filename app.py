# Imports

import os
from flask import Flask, render_template, request, url_for
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


# Function to load 'Home' page as default

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


# Function to load 'About'

@app.route('/about')
def about():
    return render_template("about.html")


# Function to load 'Books'

@app.route('/books')
def books():
    return render_template("books.html")


# Function to load 'Book1 - The Postmistress of Nong Khai'
@app.route('/book1')
def book1():
    return render_template("book1.html")


# Function to load 'Book2 - The Chiang Mai Assignment'
@app.route('/book2')
def book2():
    return render_template("book2.html")


# Function to load 'Book3 - Mekong Dragon'
@app.route('/book3')
def book3():
    return render_template("book3.html")


# Function to load 'Book3 - The Peccavi Plot'
@app.route('/book4')
def book4():
    return render_template("book4.html")


# Function to load 'Gallery'

@app.route('/gallery')
def gallery():
    return render_template("gallery.html")


# Function to load 'Gallery'

@app.route('/galleryTemples')
def galleryTemples():
    return render_template("gallery-temples.html")


# Function to load 'News'

@app.route('/news')
def news():
    return render_template("news.html")


# Function to load 'Contact'

@app.route('/contact')
def contact():
    return render_template("contact.html")


# IP and PORT
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
