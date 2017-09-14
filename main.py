from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    movie2 = get_random_movie()
    while movie==movie2:
        movie2=get_random_movie()        

    content += "<h1>Tomorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + movie2 + "</li>"
    content += "</ul>"
    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    # TODO: randomly choose one of the movies, and return it
    movielist=["The Big Lebowski", "Schindler's List","How to Lose a Guy in 10 Days"
    "The Ten Commandments", "Good Will Hunting", "What About Bob?", "Happy Gilmore",
    "Titanic","What's Eating Gilbert Grape?", "Lost in Translation", "The Lion King",
    "Beaches", "Frozen", "Babe", "Cat on a Hot Tin Roof", "The Seven Year Itch",
    "Lord of the Rings", "Star Trek: The Wrath of Khan", "Star Trek: Into Darkness",
    "The Help", "Charlie and the Chocolate Factory", "E.T.: The Extra-Terrestrial"]
    movie=random.choice(movielist)
    return movie


app.run()
