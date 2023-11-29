from flask import Flask, render_template, session

from Game import *

app = Flask(__name__)

# Route for displaying the main game page
@app.route('/Game')
def index():
	room_info = adventure_game.get_current_room()
	# passing the room information to the template
	return render_template('Game.html', room_info=room_info)


# Route for handling movement within the game
@app.route('/move', methods=['POST'])
def move():
	direction = request.form['direction']
	if adventure_game.move(direction):
		return redirect(url_for('index'))
	else:
		return jsonify({'error': 'Invalid direction'})


@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
		# Handle form submission and start the game
		player_name = request.form['name']
		session['player_name'] = player_name  # Store player name in session
		session['current_section'] = 'temple_entrance'  # Set the starting section
		return redirect(url_for('Game'))
	return render_template('main.html')


@app.route('/Game', methods=['GET', 'POST'])
def game():
	if request.method == 'POST':
		# Check if 'direction' is in the form data
		if 'direction' in request.form:
			direction = request.form['direction']
			if adventure_game.move(direction):
				return redirect(url_for('game'))
			else:
				return jsonify({'error': 'Invalid direction'})
	player_name = "Jedi Padawan"
	room_info = adventure_game.get_current_room()
	return render_template('Game.html', player_name=player_name, room_info=room_info)


@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		# Check if 'direction' is in the form data
		if 'direction' in request.form:
			direction = request.form['direction']
			if adventure_game.move(direction):
				return redirect(url_for('register'))
			else:
				return jsonify({'error': 'Invalid direction'})
	return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		# Check if 'direction' is in the form data
		if 'direction' in request.form:
			direction = request.form['direction']
			if adventure_game.move(direction):
				return redirect(url_for('main'))
			else:
				return jsonify({'error': 'Invalid direction'})
	return render_template('login.html')


if __name__ == '__main__':
	app.run(host="0.0.0.0", port="8080", debug=True)
