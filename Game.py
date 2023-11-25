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
    'intro': 'You find yourself in the midst of the Old Republic era, a time of galactic strife and political turmoil. The Sith Empire and the Galactic Republic are locked in a relentless conflict, and you, a young Force-sensitive individual, stand at the crossroads of destiny. As a member of an ancient order known as the Sentinels of the Eternal Flame, you possess a unique ability to influence the outcome of this eternal war.',
    'current_room': 'temple_entrance',
    'rooms': {
        'temple_entrance': {
            'text': 'You stand before the ancient temple of Morai on the remote planet of Tython. A chilling wind rustles the leaves as you enter the forest, guided only by the Force. Choose a direction:',
            'options': ['enter_temple', 'explore_forest']
        },
        'enter_temple': {
            'text': 'The grand entrance looms ahead. Massive stone doors engraved with the symbols of the Force beckon you. As you approach, you sense a disturbance in the Force. Your journey begins. Choose your next move:',
            'options': ['knowledge', 'combat']
        },
        'knowledge': {
            'text': 'You enter a vast chamber filled with holographic archives. A wise old Jedi Guardian appears before you. "Choose a path to enlightenment," he says. Options:',
            'options': ['study ancient texts (Wisdom)', 'meditate on the Force (Mastery)']
        },
        'combat': {
            'text': 'A training ground with remote droids awaits. A battle-hardened Jedi Sentinel oversees the challenge. "Show your skill in combat," she commands. Options:',
            'options': ['engage in a swift and aggressive attack (Agility)',
                        'focus on defense and counterattacks (Resilience)']
        },
        'explore_forest': {
            'text': 'You decide to explore the forest surrounding the temple. The dense vegetation hides mysteries and potential dangers. Choose your next move:',
            'options': ['insight', 'harmony']
        },
        'insight': {
            'text': 'As you progress deeper into the grove, you find yourself in a chamber shrouded in mystical energy. A holographic projection of a venerable Jedi Consular appears. "The path to true understanding requires insight," she advises. Options:',
            'options': ['commune with the Force to glimpse the future (Foresight)',
                        'engage in philosophical contemplation to understand the present (Reflection)']
        },
        'commune with the Force to glimpse the future (Foresight)': {
            'text': 'You open yourself to the Force, allowing its currents to guide you through glimpses of possible futures. The visions reveal potential paths, both light and dark. Choose your next move:',
            'options': ['apply foresight in decision-making', 'proceed to the next chapter']
        },
        'apply foresight in decision-making': {
            'text': 'Armed with foresight, you navigate the challenges with a heightened sense of awareness. Your decisions become calculated and precise. Choose your next move:',
            'options': ['return to temple entrance', 'proceed to the next chapter']
        },
        'engage in philosophical contemplation to understand the present (Reflection)': {
            'text': 'You delve into deep contemplation, seeking a profound understanding of the present moment. Your connection to the Force deepens. Choose your next move:',
            'options': ['apply reflection in decision-making', 'proceed to the next chapter']
        },
        'apply reflection in decision-making': {
            'text': 'With a clearer understanding of the present, your decision-making becomes grounded and wise. Your choices are influenced by a deep sense of purpose. Choose your next move:',
            'options': ['return to temple entrance', 'proceed to the next chapter']
        },
        'harmony': {
            'text': 'An ethereal room filled with calming energies presents itself. A Force-sensitive musician awaits, surrounded by harmonic resonance. "Balance is the key to harmony," she whispers. Options:',
            'options': ['compose a melody that resonates with the Light Side (Harmony)',
                        'explore dissonant tones to understand the nature of the Dark Side (Discord)']
        },
        'study ancient texts (Wisdom)': {
            'text': 'You dedicate yourself to the study of ancient texts, delving into the wisdom of the Jedi. The knowledge you gain will shape your understanding of the Force. Choose your next move:',
            'options': ['apply wisdom in combat', 'continue exploring the temple']
        },
        'apply wisdom in combat': {
            'text': 'Armed with newfound wisdom, you return to the training ground. The battle-hardened Jedi Sentinel observes your every move. Options:',
            'options': ['utilize strategic wisdom (Tactician)', 'employ ancient techniques (Wisdom in Combat)']
        },
        'meditate on the Force (Mastery)': {
            'text': 'You choose to meditate on the Force, seeking mastery over its energies. Your connection deepens, opening new pathways to understanding. Choose your next move:',
            'options': ['apply mastery in combat', 'continue exploring the temple']
        },
        'apply mastery in combat': {
            'text': 'Embracing your mastery of the Force, you return to the training ground. The battle-hardened Jedi Sentinel observes your every move. Options:',
            'options': ['unleash controlled power (Masterful Strikes)', 'weave the Force into defense (Force Shield)']
        },
        'return to temple entrance': {
            'text': 'You decide to return to the temple entrance, reflecting on your journey and preparing for what lies ahead. As you arrive, the path splits once more. Choose your next move:',
            'options': ['knowledge', 'combat']
        },
        'continue exploring the temple': {
            'text': 'You choose to explore more of the temple, seeking hidden knowledge and connections to the Force. As you move forward, the path splits. Choose your next move:',
            'options': ['wisdom', 'mastery']
        },
        'wisdom': {
            'text': 'A hidden chamber reveals itself, filled with ancient scrolls and artifacts. The echoes of wise Jedi resonate within. Choose your next move:',
            'options': ['apply wisdom in combat', 'proceed to the next chapter']
        },
        'mastery': {
            'text': 'You discover a secluded training area, untouched by time. The aura of mastery lingers in the air. Choose your next move:',
            'options': ['apply mastery in combat', 'proceed to the next chapter']
        },
        'proceed to the next chapter': {
            'text': 'Having completed your trials, the Force guides you to a holographic communicator. A desperate message from the frontlines of the war reaches you. Choose your next move:',
            'options': ['answer Republics call', 'embrace Darkened Whispers']
        },
        'answer Republics call': {
            'text': 'The holographic transmission reveals a Republic commander pleading for Jedi assistance. The Sith Empire\'s forces are overwhelming. Options:',
            'options': ['rush to the frontlines (Valor)', 'delve into strategic planning (Tactician)']
        },
        'embrace Darkened Whispers': {
            'text': 'A mysterious figure in Sith robes appears, tempting you with promises of power and revenge. The Dark Side calls to you. Options:',
            'options': ['succumb to the Dark Side (Power)', 'resist the allure (Purity)']
        },
        'rush to the frontlines (Valor)': {
            'text': 'You heed the Republics call and rush to the frontlines. The battlefield is chaotic, and the fate of the galaxy hangs in the balance. Choose your next move:',
            'options': ['lead the Vanguard Assault', 'infiltrate Behind Enemy Lines']
        },
        'delve into strategic planning (Tactician)': {
            'text': 'You choose to focus on strategic planning and tactics to aid the Republic. Your decisions will influence the flow of the battle. Choose your next move:',
            'options': ['lead the Vanguard Assault', 'infiltrate Behind Enemy Lines']
        },
        'succumb to the Dark Side (Power)': {
            'text': 'You embrace the Dark Side, seeking power at any cost. The dark energies flow through you, empowering your every move. Choose your next move:',
            'options': ['lead the Vanguard Assault', 'infiltrate Behind Enemy Lines']
        },
        'resist the allure (Purity)': {
            'text': 'You resist the allure of the Dark Side, remaining true to the Light. Your inner strength bolsters your resolve. Choose your next move:',
            'options': ['lead the Vanguard Assault', 'infiltrate Behind Enemy Lines']
        },
    }
}