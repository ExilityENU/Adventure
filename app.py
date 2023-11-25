from flask import Flask, render_template, redirect, url_for, jsonify, request
from Game  import Adventure, game_state

app = Flask(__name__)

game = Adventure(game_state)
adventure_game = Adventure(game_state)
@app.route('/Game')
def index():
    room_info = adventure_game.get_current_room()
    return render_template('Game.html', room_info=room_info)

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
        # Perform any necessary setup for the game, such as creating a player object
        return redirect(url_for('/Game'))
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
    player_name = "Jedi Padawan"  # Replace with the actual player name or retrieve it from previous forms
    room_info = adventure_game.get_current_room()
    return render_template('Game.html', player_name=player_name, room_info=room_info)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)