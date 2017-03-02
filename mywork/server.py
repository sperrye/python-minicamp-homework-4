from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('database.db')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/movie', methods = ['POST'])
def addmovie():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    try:
        title = request.form['title']
        year = request.form['year']
        rating = request.form['rating']
        summary = request.form['summary']
        cursor.execute('INSERT INTO movies (title, year, rating, summary) VALUES (?,?,?,?)', (title,year,rating,summary))
        connection.commit()
        message = 'Movie successfully added'
    except:
        connection.rollback()
        message = 'There was a problem adding the movie to the database'
    finally:
        return render_template('movielist.html', message = message)
        connection.close()

@app.route('/movies')
def showmovies():
    return render_template('addnew.html')
    #this route will return the JSON for all movies in your database

@app.route('/search')
def search():
    return render_template('home.html')

app.run(debug = True)
