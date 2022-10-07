from flask import Flask

app = Flask(__name__)

from flask import Flask


app = Flask(__name__)


@app.get("/")
def pokemon_list():
    return "Bulbasaur, charmander, pikachu, eevee, diglett"


@app.get("/bulbasaur")
def bulbasaur_data():
    return "This is bulbasaur, a generation 1 pokemon who looks like a tiny dinosaur"


@app.get("/charmander")
def charmander_data():
    return "This is charmander, a generation 1 pokemon who looks like a tiny reptile"


@app.get("/pikachu")
def pikachu_data():
    return "This is pikachu, a generation 1 pokemon who looks like a tiny rodent"


@app.get("/eevee")
def eevee_data():
    return "This is eevee, a generation 1 pokemon who looks like a tiny fox"


@app.get("/diglett")
def diglett_data():
    return "This is diglett, a generation 1 pokemon who looks like a tiny mole"


if __name__ == "__main__":
    app.run()
from flask import Flask


app = Flask(__name__)


pokemon_creatures = {
    "bulbasaur": "dinosaur",
    "charmander": "reptile",
    "pikachu": "rodent",
    "eevee": "fox",
    "diglett": "mole",
}


@app.get("/")
def pokemon_list():
    return "Bulbasaur, charmander, pikachu, eevee, diglett"


@app.get("/<pokemon_name>")
def pokemon_data(pokemon_name):
    creature = pokemon_creatures.get(pokemon_name)
    return f"This is {pokemon_name}, a generation 1 pokemon who looks like a tiny {creature}"


if __name__ == "__main__":
    app.run()