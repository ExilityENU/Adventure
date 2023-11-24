from flask import Flask, render_template, redirect, url_for, jsonify, request
from Game  import Adventure, game_state

app = Flask(__name__)

game = Adventure(game_state)
adventure_game = Adventure(game_state)

@app.route("/")
def hello():
    return "Hello Traveller!"

@app.route('/Game')
def index():
    room_info = adventure_game.get_current_room()
    return render_template('main.html', room_info=room_info)

@app.route('/move', methods=['POST'])
def move():
    direction = request.form['direction']
    if adventure_game.move(direction):
        return redirect(url_for('index'))
    else:
        return jsonify({'error': 'Invalid direction'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)