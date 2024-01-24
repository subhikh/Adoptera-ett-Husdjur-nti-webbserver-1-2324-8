from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return '''
  <h1>Adopt a pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
      <li><a href="/animals/dogs">Dogs</a></li>
      <li><a href="/animals/cats">Cats</a></li>
      <li><a href="/animals/kaniner">Kaniner</a></li>
  </ul>
'''


@app.route('/animals/pet_type')
def animals(pet_type):
# Viktigt: Denna kodrad ska alltid placeras längst ner i filen.
# Detta för att säkerställa en korrekt uppstart av servern.

app.run(debug=True, host="0.0.0.0")
