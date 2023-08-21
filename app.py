from flask import Flask, render_template, request, redirect, url_for
from character import DnDCharacter # Import the DnDCharacter class from character.py


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', character=None)

@app.route('/create_character', methods=['GET', 'POST'])
def create_character():
    races = ["Elf", "Human", "Dwarf"]  # Add more race options as needed
    classes = ["Fighter", "Wizard", "Rogue"]  # Add more class options as needed

    if request.method == 'POST':
        name = request.form['name']
        race = request.form['race']
        character_class = request.form['character_class']
        character = DnDCharacter(name, race, character_class)
        return render_template('index.html', character=character)
        
    return render_template('create_character.html')

if __name__ == '__main__':
    app.run(debug=True)
