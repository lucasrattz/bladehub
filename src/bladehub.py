import buildings
import demons
import ghosts
import leviathans
import people
import streets
import cults
import scores
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

@app.route('/api/<type>', methods=['GET'])
def generate(type):
    if(request.method != 'GET'):
        response = jsonify({'error': 'Invalid request method'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    if type == 'common_person':
        common_person = people.Person("common")
        description = common_person.describe()

    if type == 'rare_person':
        rare_person = people.Person("rare")
        description = rare_person.describe()

    if type == 'street':
        random_street = streets.Street()
        description = random_street.describe()

    if type == 'common_building':
        common_building = buildings.Building("common")
        description = common_building.describe()

    if type == 'rare_building':
        rare_building = buildings.Building("rare")
        description = rare_building.describe()

    if type == 'demon':
        random_demon = demons.Demon()
        description = random_demon.describe()

    if type == 'ghost':
        random_ghost = ghosts.Ghost()
        description = random_ghost.describe()

    if type == 'cult':
        random_cult = cults.Cult()
        description = random_cult.describe()

    if type == 'score':
        random_score = scores.Score()
        description = random_score.describe()

    if type == 'banal_leviathan':
        random_leviathan = leviathans.Leviathan("banal")
        description = random_leviathan.describe()

    if type == 'surreal_leviathan':
        random_leviathan = leviathans.Leviathan("surreal")
        description = random_leviathan.describe()

    if type == 'leviathan_spawn':
        random_spawn = leviathans.LeviathanSpawn()
        description = random_spawn.describe()

    if 'description' in locals(): 
        response = jsonify({'description': description})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    
    else:
        response = jsonify({'error': 'Invalid type'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

if __name__ == "__main__":
    from waitress import serve
    print("API running on port 2774")
    serve(app, host="0.0.0.0", port=2774)