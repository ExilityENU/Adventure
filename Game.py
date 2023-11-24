from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

class Adventure:
    def __init__(self, game_state):
        self.game_state = game_state
        self.current_room = game_state['current_room']

    def move(self, direction):
        if direction in self.game_state['rooms'][self.current_room]['options']:
            self.current_room = direction
            return True
        else:
            return False

    def get_current_room(self):
        return self.game_state['rooms'][self.current_room]

# Define the initial game state
game_state = {
    'current_room': 'home',
    'rooms': {
        'home': {
            'text': 'You are at home. Choose a direction:',
            'options': ['forest', 'mountain']
        },
        'forest': {
            'text': 'You entered the forest. Choose a direction:',
            'options': ['home', 'cave']
        },
        'cave': {
            'text': 'You found a dark cave. Choose a direction:',
            'options': ['forest']
        },
        'mountain': {
            'text': 'You are climbing the mountain. Choose a direction:',
            'options': ['home']
        }
    }
}