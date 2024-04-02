"""
  app.py - This file contains the main Flask application for adopting pets.
  
  The app allows users to browse and adopt pets such as dogs, cats, and rabbits through different routes.
  Routes include:
  - '/' : Displays the home page with links to different pet types.
  - '/animals/<string:pet_type>' : Displays a list of pets based on the given pet type.
  - '/animals/<string:pet_type>/<int:pet_id>' : Displays details about a specific pet based on its type and ID.
  
  The Flask server is run with debug mode enabled.
"""

from flask import Flask

from helper import pets

app = Flask(__name__)


@app.route('/')
def index():
  """
  This function displays the home page for adopting a pet.
  
  Returns:
      str: The HTML content for the home page with links to different pet types.
  """
  return '''
  <h1>Adopt a Pet<h1/>
  <p>Browse through the links below to find your new furry friend:<p/> 
<ul>
<li><a href='/animals/dogs'>Dogs</a></li> 
<li><a href='/animals/cats'>Cats </a> </li> 
<li><a href='/animals/rabbits'>Rabbits</a></li> 
</ul>

  '''


# Route to display the list of pets based on pet type
@app.route('/animals/<string:pet_type>')
def animals(pet_type):
  """
  This function displays a list of pets based on the given pet type.
  
  Args:
      pet_type (str): The type of pet for which the list is displayed.
      
  Returns:
      str: The HTML content for displaying the list of pets of the specified type.
  """
  html = f'<h1>List of {pet_type}<h1/>'
  html += '<ul>'
  for id, pet in enumerate(pets[pet_type]):
    html += f'<li><a href="/animals/{pet_type}/{id}">{pet["name"]}</a></li>'
  return html


# Route to display details about a specific pet
@app.route('/animals/<string:pet_type>/<int:pet_id>')
def pet(pet_id, pet_type):
  """
  This function displays details about a specific pet based on its type and ID.
  
  Args:
      pet_id (int): The ID of the specific pet.
      pet_type (str): The type of the pet.
      
  Returns:
      str: The HTML content for displaying the details of the specific pet.
  """
  list_pet_type = pets[pet_type]
  pet = list_pet_type[pet_id]
  return f'''
  <h1> {pet["name"]}</h1>

  <img src={pet["url"]} /> 

  <p>{pet["description"]}</p>

  <ul>
    <li>{pet["breed"]} </li>
    <li>{pet["age"]} </li>
  </ul>
  '''


# This line is important for starting the Flask server
app.run(debug=True, host="0.0.0.0")
