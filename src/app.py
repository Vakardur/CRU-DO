from flask import Flask, render_template
import os
import database as db

#1. Setting template directory
#The template_dir variable is assigned the absolute path of the directory containing the current script (__file__).
#Then, it appends the subdirectories 'src' and 'templates' to the path, creating the path to the templates directory.

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir,'src', 'templates')

#2. Creating FLask App
#The Flask class is used to create a web application instance named app.
#The template_folder parameter is set to the previously defined template_dir, specifying the location of HTML template files.
app = Flask(__name__, template_folder = template_dir)


#3 Defining a Route
#This code defines a route for the root URL ("/"). When a user accesses the root URL, the home function is executed.
#The home function returns the result of the render_template function, which renders the 'index.html' template.
@app.route('/')
def home():

    return render_template('index.html')


#Start the Flask development Server
#Checks if the script is being run directly (if __name__ == '__main__':)
#and, if so, starts the Flask development server with debugging enabled on port 4000.

if __name__ == '__main__':
    app.run(debug=True, port=4000)