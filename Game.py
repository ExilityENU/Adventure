from flask import Flask

app = Flask(__name__)

class Adventure:
    def __init__(self, game_state):
        # This is the setup when you create a new Adventure.
        # We'll use the game_state to know where the player is and what's happening.
        self.game_state = game_state
        self.current_room = game_state['current_room']

    def move(self, direction):
        # Move the player to a new room.
        # If the direction is legit (in the options for the current room), we'll update the current room.
        # Returns True if the move is valid, False if it's not.
        if direction in self.game_state['rooms'][self.current_room]['options']:
            self.current_room = direction
            return True
        else:
            return False

    def get_current_room(self):
        # Just a way to get info about the current room.
        return self.game_state['rooms'][self.current_room]


# Define static GIF
static_gif_url = 'static/star-wars-the-old-republic.gif'

# Initialize a variable to store the current image URL
current_image_url = static_gif_url

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
            'options': ['knowledge', 'combat'],
        },
        'knowledge': {
            'text': 'You enter a vast chamber filled with holographic archives. A wise old Jedi Guardian appears before you. "Choose a path to enlightenment," he says. Options:',
            'options': ['study ancient texts (Wisdom)', 'meditate on the Force (Mastery)']
        },
        'combat': {
            'text': 'A training ground with remote droids awaits. A battle-hardened Jedi Sentinel oversees the challenge. "Show your skill in combat," she commands. Options:',
            'options': ['engage in a swift and aggressive attack (Agility)', 'focus on defense and counterattacks (Resilience)']
        },
        'explore_forest': {
            'text': 'You decide to explore the forest surrounding the temple. The dense vegetation hides mysteries and potential dangers. Choose your next move:',
            'options': ['insight', 'harmony']
        },
        'engage in a swift and aggressive attack (Agility)': {
            'text': 'You unleash a flurry of swift and aggressive attacks, overpowering your opponents with speed and precision. Your agility in combat is unmatched. Choose your next move:',
            'options': ['utilize strategic agility (Agile Strikes)', 'proceed to the next chapter']
        },
        'utilize strategic agility (Agile Strikes)': {
            'text': 'You harness your agility strategically, striking with precision and evading enemy attacks. Your combat style becomes a dance of calculated moves. Choose your next move:',
            'options': ['return to temple entrance', 'proceed to the next chapter']
        },
        'focus on defense and counterattacks (Resilience)': {
            'text': 'You adopt a defensive stance, patiently waiting for your opponents to strike. Your resilience allows you to counterattack with precision. Choose your next move:',
            'options': ['employ resilient counterattacks (Counterstrike)', 'proceed to the next chapter']
        },
        'employ resilient counterattacks (Counterstrike)': {
            'text': 'Your defensive strategy pays off as you counterattack with resilience, turning your opponents\' moves against them. Your combat prowess is undeniable. Choose your next move:',
            'options': ['return to temple entrance', 'proceed to the next chapter']
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
                'explore dissonant tones to understand the nature of the Dark Side (Discord)',
                'immerse yourself in the music to find inner peace (Serenity)',
                'engage in a rhythmic dance to connect with the Force (Dance of the Force)']
        },
        'compose a melody that resonates with the Light Side (Harmony)': {
            'text': 'You focus your energy on composing a melody that reflects the harmonious essence of the Light Side. The room is filled with a soothing aura. Choose your next move:',
            'options': ['apply harmonious melodies in combat', 'proceed to the next chapter']
        },
        'apply harmonious melodies in combat': {
            'text': 'Empowered by the harmonious melodies you composed, you return to the training ground. The battle-hardened Jedi Sentinel observes your every move. Options:',
            'options': ['utilize rhythmic precision (Harmonic Strikes)', 'proceed to the next chapter']
        },
        'explore dissonant tones to understand the nature of the Dark Side (Discord)': {
            'text': 'You delve into the exploration of dissonant tones, seeking to understand the chaotic nature of the Dark Side. The room resonates with discordant energies. Choose your next move:',
            'options': ['apply discordant tones in combat', 'proceed to the next chapter']
        },
        'apply discordant tones in combat': {
            'text': 'Infused with the chaotic energy of discordant tones, you return to the training ground. The battle-hardened Jedi Sentinel observes your every move. Options:',
            'options': ['unleash chaotic power (Discordant Strikes)', 'proceed to the next chapter']
        },
        'immerse yourself in the music to find inner peace (Serenity)': {
            'text': 'You immerse yourself in the calming music, finding inner peace and serenity. The energies of the Force flow harmoniously through you. Choose your next move:',
            'options': ['apply serenity in decision-making', 'proceed to the next chapter']
        },
        'apply serenity in decision-making': {
            'text': 'Guided by the inner peace you found, you navigate the challenges with a serene mind. Your decisions become centered and balanced. Choose your next move:',
            'options': ['return to temple entrance', 'proceed to the next chapter']
        },
        'engage in a rhythmic dance to connect with the Force (Dance of the Force)': {
            'text': 'You engage in a rhythmic dance, synchronizing your movements with the flowing energies of the Force. The room pulses with a vibrant connection. Choose your next move:',
            'options': ['apply dance-inspired agility in combat', 'proceed to the next chapter']
        },
        'apply dance-inspired agility in combat': {
            'text': 'Infused with the agility inspired by your rhythmic dance, you return to the training ground. The battle-hardened Jedi Sentinel observes your every move. Options:',
            'options': ['utilize dance-inspired agility (Dance of Strikes)', 'proceed to the next chapter']
        },
        'study ancient texts (Wisdom)': {
            'text': 'You dedicate yourself to the study of ancient texts, delving into the wisdom of the Jedi. The knowledge you gain will shape your understanding of the Force. Choose your next move:',
            'options': ['apply wisdom in combat', 'continue exploring the temple']
        },
        'apply wisdom in combat': {
            'text': 'Armed with newfound wisdom, you return to the training ground. The battle-hardened Jedi Sentinel observes your every move. Options:',
            'options': ['utilize strategic wisdom (Tactician)', 'employ ancient techniques (Wisdom in Combat)']
        },
        'employ ancient techniques (Wisdom in Combat)': {
            'text': 'You tap into the ancient techniques passed down through generations. Your combat style becomes a dance of traditional and strategic moves. Choose your next move:',
            'options': ['return to temple entrance', 'proceed to the next chapter']
        },
        'utilize strategic wisdom (Tactician)': {
            'text': 'You strategically apply wisdom to your combat techniques, analyzing and outsmarting your opponents. The Jedi Sentinel nods in approval. Choose your next move:',
            'options': ['return to temple entrance', 'proceed to the next chapter']
        },
        'meditate on the Force (Mastery)': {
            'text': 'You choose to meditate on the Force, seeking mastery over its energies. Your connection deepens, opening new pathways to understanding. Choose your next move:',
            'options': ['apply mastery in combat', 'continue exploring the temple']
        },
        'apply mastery in combat': {
            'text': 'Embracing your mastery of the Force, you return to the training ground. The battle-hardened Jedi Sentinel observes your every move. Options:',
            'options': ['unleash controlled power (Masterful Strikes)', 'weave the Force into defense (Force Shield)']
        },
        'unleash controlled power (Masterful Strikes)': {
            'text': 'You unleash a torrent of controlled power, overwhelming your opponents with precise and devastating strikes. Your mastery is unmatched. Choose your next move:',
            'options': ['return to temple entrance', 'proceed to the next chapter']
        },
        'weave the Force into defense (Force Shield)': {
            'text': 'You weave the Force into a formidable shield, deflecting attacks with ease. Your defensive prowess is unmatched. Choose your next move:',
            'options': ['return to temple entrance', 'proceed to the next chapter']
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
            'text': 'The holographic transmission reveals a Republic commander pleading for Jedi assistance. The Sith Empires forces are overwhelming. Options:',
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
        'lead the Vanguard Assault': {
            'text': 'You take charge of the Vanguard Assault, leading Republic forces against the Sith. The battle is intense, and you find yourself face to face with a formidable Sith Lord. Choose your next move:',
            'options': ['strike the boss down with a barrage of blows', 'seek a diplomatic resolution']
        },
        'strike the boss down with a barrage of blows': {
            'text': 'You engage the Sith Lord in a fierce duel, unleashing a barrage of powerful blows. The battle is intense, but your skill and determination prevail. The Sith Lord falls defeated. Choose your next move:',
            'options': ['go to Galactic Space Station']
        },
        'seek a diplomatic resolution': {
            'text': 'You attempt to find a diplomatic resolution with the Sith Lord, hoping to end the conflict without further bloodshed. The Sith Lord seems open to negotiation. Choose your next move:',
            'options': ['convince the Sith Lord to retreat', 'engage in a duel for honor']
        },
        'convince the Sith Lord to retreat': {
            'text': 'Your diplomatic efforts succeed, and the Sith Lord agrees to retreat, bringing an unexpected end to the battle. The Republic forces secure the frontlines. Choose your next move:',
            'options': ['go to Galactic Space Station']
        },
        'engage in a duel for honor': {
            'text': 'Despite your attempts at negotiation, the Sith Lord challenges you to a duel for honor. The battle is fierce, and the outcome uncertain. Choose your next move:',
            'options': ['embrace the Dark Side to ensure victory', 'fight with honor and integrity']
        },
        'embrace the Dark Side to ensure victory': {
            'text': 'In a moment of desperation, you embrace the Dark Side to ensure victory. The power surges through you, but at a cost. Choose your next move:',
            'options': ['wrestle control back from the Dark Side', 'embrace the Dark Side completely']
        },
        'wrestle control back from the Dark Side': {
            'text': 'You struggle against the influence of the Dark Side, fighting to regain control. Your inner strength prevails, and you emerge from the battle with a newfound understanding. Choose your next move:',
            'options': ['go to Galactic Space Station']
        },
        'embrace the Dark Side completely': {
            'text': 'You fully embrace the Dark Side, succumbing to its temptations. The power consumes you, and your actions become twisted by the darkness. Choose your next move:',
            'options': ['proclaim loyalty to the Sith', 'seek redemption and return to the Light']
        },
        'proclaim loyalty to the Sith': {
            'text': 'You proclaim loyalty to the Sith, aligning yourself with the dark forces. Your destiny takes a dark turn, and the galaxy awaits the consequences of your choice. Congratulations! Your journey as a Dark Side Force user continues.',
            'options': ['go to Galactic Space Station']
        },
        'seek redemption and return to the Light': {
            'text': 'In a moment of clarity, you reject the Dark Side and seek redemption. The Light welcomes you back, and you vow to use your strength for the greater good. Choose your next move:',
            'options': ['go to Galactic Space Station']
        },
        'infiltrate Behind Enemy Lines': {
            'text': 'You choose to infiltrate Behind Enemy Lines, seeking to disrupt the Sith war efforts. As you navigate through enemy territory, you encounter a powerful Sith assassin. Choose your next move:',
            'options': ['engage in a stealthy confrontation', 'confront the assassin directly']
        },
        'engage in a stealthy confrontation': {
            'text': 'You use stealth to confront the Sith assassin, moving silently through the shadows. A tense battle ensues, with each move calculated for maximum efficiency. Choose your next move:',
            'options': ['utilize guerrilla tactics (Stealth Strikes)', 'proceed to the next chapter']
        },
        'utilize guerrilla tactics (Stealth Strikes)': {
            'text': 'You employ guerrilla tactics, striking from the shadows with deadly precision. The Sith assassin is caught off guard, and you emerge victorious. Choose your next move:',
            'options': ['go to Galactic Space Station']
        },
        'confront the assassin directly': {
            'text': 'You choose to confront the Sith assassin directly, engaging in a head-on confrontation. The battle is fierce, with lightsabers clashing in a display of raw power. Choose your next move:',
            'options': ['overwhelm the assassin with aggressive attacks', 'defend and wait for an opening']
        },
        'overwhelm the assassin with aggressive attacks': {
            'text': 'You unleash a barrage of aggressive attacks, overwhelming the Sith assassin with sheer force. The battle is intense, but your aggression proves to be too much for the assassin. Choose your next move:',
            'options': ['go to Galactic Space Station']
        },
        'defend and wait for an opening': {
            'text': 'You adopt a defensive stance, patiently waiting for an opening in the Sith assassin\'s attacks. Your resilience pays off as you find the perfect moment to strike. Choose your next move:',
            'options': ['deliver a decisive counterattack', 'proceed to the next chapter']
        },
        'deliver a decisive counterattack': {
            'text': 'Your patience pays off as you deliver a decisive counterattack, defeating the Sith assassin with precision. The path is now clear for further infiltration. Choose your next move:',
            'options': ['go to Galactic Space Station']
        },
        'go to Galactic Space Station': {
            'text': 'You decide to head to the Galactic Space Station, a hub of activity and a nexus for various paths in the galaxy. As you arrive, new opportunities and challenges present themselves. Choose your next move:',
            'options': ['return to the start page', 'head to Hoth']
        },
        'head to Hoth': {
            'text': 'You decide to head to the icy planet of Hoth, where new adventures and trials await. As you embark on this journey, the story takes a temporary pause. TO BE CONTINUED...',
            'options': ['return to the start page']
        },
        'return to the start page': {
            'text': 'As the echoes of your dark choice reverberate through the Force, you find yourself back at the start page, standing before the ancient temple of Morai on the remote planet of Tython. A chilling wind rustles the leaves as you enter the forest, guided only by the Force. Choose a direction:',
            'options': ['enter_temple', 'explore_forest']
        }
    }
}