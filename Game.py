from flask import url_for, request, redirect, jsonify


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
			'options': ['Enter Temple', 'Explore Forest'],
			'image': 'jeditemple.jpg'
		},
		'Enter Temple': {
			'text': 'The grand entrance looms ahead. Massive stone doors engraved with the symbols of the Force beckon you. As you approach, you sense a disturbance in the Force. Your journey begins. Choose your next move:',
			'options': ['knowledge', 'combat'],
			'image': 'jeditemple.jpg'
		},
		'knowledge': {
			'text': 'You enter a vast chamber filled with holographic archives. A wise old Jedi Guardian appears before you. "Choose a path to enlightenment," he says. Options:',
			'options': ['study ancient texts (Wisdom)', 'meditate on the Force (Mastery)'],
			'image': 'Firefly LIB.jpg'
		},
		'combat': {
			'text': 'A training ground with remote droids awaits. A battle-hardened Jedi Sentinel oversees the challenge. "Show your skill in combat," she commands. Options:',
			'options': ['engage in a swift and aggressive attack (Agility)',
						'focus on defense and counterattacks (Resilience)'],
			'image': 'Tythonian_War_Droid.jpg'
		},
		'Explore Forest': {
			'text': 'You decide to explore the forest surrounding the temple. The dense vegetation hides mysteries and potential dangers. Choose your next move:',
			'options': ['insight', 'harmony'],
			'image': 'Firefly_forest.jpg'
		},
		'engage in a swift and aggressive attack (Agility)': {
			'text': 'You unleash a flurry of swift and aggressive attacks, overpowering your opponents with speed and precision. Your agility in combat is unmatched. Choose your next move:',
			'options': ['utilize strategic agility (Agile Strikes)', 'proceed to the next chapter'],
			'image': 'JediShadow.jpg'
		},
		'utilize strategic agility (Agile Strikes)': {
			'text': 'You harness your agility strategically, striking with precision and evading enemy attacks. Your combat style becomes a dance of calculated moves. Choose your next move:',
			'options': ['return to temple entrance', 'proceed to the next chapter'],
			'image': 'jedivsSith.jpg'
		},
		'focus on defense and counterattacks (Resilience)': {
			'text': 'You adopt a defensive stance, patiently waiting for your opponents to strike. Your resilience allows you to counterattack with precision. Choose your next move:',
			'options': ['employ resilient counterattacks (Counterstrike)', 'proceed to the next chapter'],
			'image': 'Aura.jpg'
		},
		'employ resilient counterattacks (Counterstrike)': {
			'text': 'Your defensive strategy pays off as you counterattack with resilience, turning your opponents moves against them. Your combat prowess is undeniable. Choose your next move:',
			'options': ['return to temple entrance', 'proceed to the next chapter'],
			'image': 'swtor-blade.jpg'
		},
		'insight': {
			'text': 'As you progress deeper into the grove, you find yourself in a chamber shrouded in mystical energy. A holographic projection of a venerable Jedi Consular appears. "The path to true understanding requires insight," she advises. Options:',
			'options': ['commune with the Force to glimpse the future (Foresight)',
						'engage in philosophical contemplation to understand the present (Reflection)'],
			'image': 'Satele_hologram.jpg'
		},
		'commune with the Force to glimpse the future (Foresight)': {
			'text': 'You open yourself to the Force, allowing its currents to guide you through glimpses of possible futures. The visions reveal potential paths, both light and dark. Choose your next move:',
			'options': ['apply foresight in decision-making', 'proceed to the next chapter'],
			'image': 'future.jpg'
		},
		'apply foresight in decision-making': {
			'text': 'Armed with foresight, you navigate the challenges with a heightened sense of awareness. Your decisions become calculated and precise. Choose your next move:',
			'options': ['return to temple entrance', 'proceed to the next chapter'],
			'image': 'swtor__jedi_meditation.jpg'
		},
		'engage in philosophical contemplation to understand the present (Reflection)': {
			'text': 'You delve into deep contemplation, seeking a profound understanding of the present moment. Your connection to the Force deepens. Choose your next move:',
			'options': ['apply reflection in decision-making', 'proceed to the next chapter'],
			'image': 'meditation.jpg'
		},
		'apply reflection in decision-making': {
			'text': 'With a clearer understanding of the present, your decision-making becomes grounded and wise. Your choices are influenced by a deep sense of purpose. Choose your next move:',
			'options': ['return to temple entrance', 'proceed to the next chapter'],
			'image': 'Firefly_Jedi.jpg'
		},
		'harmony': {
			'text': 'An ethereal room filled with calming energies presents itself. A Force-sensitive musician awaits, surrounded by harmonic resonance. "Balance is the key to harmony," she whispers. Options:',
			'options': ['compose a melody that resonates with the Light Side (Harmony)',
						'explore dissonant tones to understand the nature of the Dark Side (Discord)',
						'immerse yourself in the music to find inner peace (Serenity)',
						'engage in a rhythmic dance to connect with the Force (Dance of the Force)'],
			'image': 'Firefly_Jedi.jpg'
		},
		'compose a melody that resonates with the Light Side (Harmony)': {
			'text': 'You focus your energy on composing a melody that reflects the harmonious essence of the Light Side. The room is filled with a soothing aura. Choose your next move:',
			'options': ['apply harmonious melodies in combat', 'proceed to the next chapter'],
			'image': 'Firefly_Jedi.jpg'
		},
		'apply harmonious melodies in combat': {
			'text': 'Empowered by the harmonious melodies you composed, you return to the training ground. The battle-hardened Jedi Sentinel observes your every move. Options:',
			'options': ['utilize rhythmic precision (Harmonic Strikes)', 'proceed to the next chapter'],
			'image': 'Training.jpg'
		},
		'explore dissonant tones to understand the nature of the Dark Side (Discord)': {
			'text': 'You delve into the exploration of dissonant tones, seeking to understand the chaotic nature of the Dark Side. The room resonates with discordant energies. Choose your next move:',
			'options': ['apply discordant tones in combat', 'proceed to the next chapter'],
			'image': 'dark side.jpg'
		},
		'apply discordant tones in combat': {
			'text': 'Infused with the chaotic energy of discordant tones, you return to the training ground. The battle-hardened Jedi Sentinel observes your every move. Options:',
			'options': ['unleash chaotic power (Discordant Strikes)', 'proceed to the next chapter'],
			'image': 'Training.jpg'
		},
		'immerse yourself in the music to find inner peace (Serenity)': {
			'text': 'You immerse yourself in the calming music, finding inner peace and serenity. The energies of the Force flow harmoniously through you. Choose your next move:',
			'options': ['apply serenity in decision-making', 'proceed to the next chapter'],
			'image': 'Jedi study.jpg'
		},
		'apply serenity in decision-making': {
			'text': 'Guided by the inner peace you found, you navigate the challenges with a serene mind. Your decisions become centered and balanced. Choose your next move:',
			'options': ['return to temple entrance', 'proceed to the next chapter'],
			'image': 'light.jpg'
		},
		'engage in a rhythmic dance to connect with the Force (Dance of the Force)': {
			'text': 'You engage in a rhythmic dance, synchronizing your movements with the flowing energies of the Force. The room pulses with a vibrant connection. Choose your next move:',
			'options': ['apply dance-inspired agility in combat', 'proceed to the next chapter'],
			'image': 'maxresdefault.jpg'
		},
		'apply dance-inspired agility in combat': {
			'text': 'Infused with the agility inspired by your rhythmic dance, you return to the training ground. The battle-hardened Jedi Sentinel observes your every move. Options:',
			'options': ['utilize dance-inspired agility (Dance of Strikes)', 'proceed to the next chapter'],
			'image': 'Training.jpg'
		},
		'study ancient texts (Wisdom)': {
			'text': 'You dedicate yourself to the study of ancient texts, delving into the wisdom of the Jedi. The knowledge you gain will shape your understanding of the Force. Choose your next move:',
			'options': ['apply wisdom in combat', 'continue exploring the temple'],
			'image': 'Jedi study.jpg'
		},
		'apply wisdom in combat': {
			'text': 'Armed with newfound wisdom, you return to the training ground. The battle-hardened Jedi Sentinel observes your every move. Options:',
			'options': ['utilize strategic wisdom (Tactician)', 'employ ancient techniques (Wisdom in Combat)'],
			'image': 'Training.jpg'
		},
		'employ ancient techniques (Wisdom in Combat)': {
			'text': 'You tap into the ancient techniques passed down through generations. Your combat style becomes a dance of traditional and strategic moves. Choose your next move:',
			'options': ['return to temple entrance', 'proceed to the next chapter'],
			'image': 'swtor-blade.jpg'
		},
		'utilize strategic wisdom (Tactician)': {
			'text': 'You strategically apply wisdom to your combat techniques, analyzing and outsmarting your opponents. The Jedi Sentinel nods in approval. Choose your next move:',
			'options': ['return to temple entrance', 'proceed to the next chapter'],
			'image': 'Training.jpg'
		},
		'meditate on the Force (Mastery)': {
			'text': 'You choose to meditate on the Force, seeking mastery over its energies. Your connection deepens, opening new pathways to understanding. Choose your next move:',
			'options': ['apply mastery in combat', 'continue exploring the temple'],
			'image': 'Firefly_Jedi.jpg'
		},
		'apply mastery in combat': {
			'text': 'Embracing your mastery of the Force, you return to the training ground. The battle-hardened Jedi Sentinel observes your every move. Options:',
			'options': ['unleash controlled power (Masterful Strikes)', 'weave the Force into defense (Force Shield)'],
			'image': 'Training.jpg'
		},
		'unleash controlled power (Masterful Strikes)': {
			'text': 'You unleash a torrent of controlled power, overwhelming your opponents with precise and devastating strikes. Your mastery is unmatched. Choose your next move:',
			'options': ['return to temple entrance', 'proceed to the next chapter'],
			'image': 'master.jpg'
		},
		'weave the Force into defense (Force Shield)': {
			'text': 'You weave the Force into a formidable shield, deflecting attacks with ease. Your defensive prowess is unmatched. Choose your next move:',
			'options': ['return to temple entrance', 'proceed to the next chapter'],
			'image': 'jedi-knight-guardian-defense.jpg'
		},
		'return to temple entrance': {
			'text': 'You decide to return to the temple entrance, reflecting on your journey and preparing for what lies ahead. As you arrive, the path splits once more. Choose your next move:',
			'options': ['knowledge', 'combat'],
			'image': 'jeditemple.jpg'
		},
		'continue exploring the temple': {
			'text': 'You choose to explore more of the temple, seeking hidden knowledge and connections to the Force. As you move forward, the path splits. Choose your next move:',
			'options': ['wisdom', 'mastery'],
			'image': 'jeditemple.jpg'
		},
		'wisdom': {
			'text': 'A hidden chamber reveals itself, filled with ancient scrolls and artifacts. The echoes of wise Jedi resonate within. Choose your next move:',
			'options': ['apply wisdom in combat', 'proceed to the next chapter'],
			'image': 'Firefly  Jedi Temple LIB.jpg'
		},
		'mastery': {
			'text': 'You discover a secluded training area, untouched by time. The aura of mastery lingers in the air. Choose your next move:',
			'options': ['apply mastery in combat', 'proceed to the next chapter'],
			'image': 'JediShadow.jpg'
		},
		'proceed to the next chapter': {
			'text': 'Having completed your trials, the Force guides you to a holographic communicator. A desperate message from the frontlines of the war reaches you. Choose your next move:',
			'options': ['answer Republics call', 'embrace Darkened Whispers'],
			'image': 'Jedi holo.jpg'
		},
		'answer Republics call': {
			'text': 'The holographic transmission reveals a Republic commander pleading for Jedi assistance. The Sith Empires forces are overwhelming. Options:',
			'options': ['rush to the frontlines (Valor)', 'delve into strategic planning (Tactician)'],
			'image': 'Jedi holo.jpg'
		},
		'embrace Darkened Whispers': {
			'text': 'A mysterious figure in Sith robes appears, tempting you with promises of power and revenge. The Dark Side calls to you. Options:',
			'options': ['succumb to the Dark Side (Power)', 'resist the allure (Purity)'],
			'image': 'dark aura.jpg'
		},
		'rush to the frontlines (Valor)': {
			'text': 'You heed the Republics call and rush to the frontlines. The battlefield is chaotic, and the fate of the galaxy hangs in the balance. Choose your next move:',
			'options': ['lead the Vanguard Assault', 'infiltrate Behind Enemy Lines'],
			'image': 'SWTOR_War.jpg'
		},
		'delve into strategic planning (Tactician)': {
			'text': 'You choose to focus on strategic planning and tactics to aid the Republic. Your decisions will influence the flow of the battle. Choose your next move:',
			'options': ['lead the Vanguard Assault', 'infiltrate Behind Enemy Lines'],
			'image': 'stratagy.jpg'
		},
		'succumb to the Dark Side (Power)': {
			'text': 'You embrace the Dark Side, seeking power at any cost. The dark energies flow through you, empowering your every move. Choose your next move:',
			'options': ['lead the Vanguard Assault', 'infiltrate Behind Enemy Lines'],
			'image': 'dark aura.jpg'
		},
		'resist the allure (Purity)': {
			'text': 'You resist the allure of the Dark Side, remaining true to the Light. Your inner strength bolsters your resolve. Choose your next move:',
			'options': ['lead the Vanguard Assault', 'infiltrate Behind Enemy Lines'],
			'image': 'Aura.jpg'
		},
		'lead the Vanguard Assault': {
			'text': 'You take charge of the Vanguard Assault, leading Republic forces against the Sith. The battle is intense, and you find yourself face to face with a formidable Sith Lord. Choose your next move:',
			'options': ['strike the boss down with a barrage of blows', 'seek a diplomatic resolution'],
			'image': 'SWTOR_War.jpg'
		},
		'strike the boss down with a barrage of blows': {
			'text': 'You engage the Sith Lord in a fierce duel, unleashing a barrage of powerful blows. The battle is intense, but your skill and determination prevail. The Sith Lord falls defeated. Choose your next move:',
			'options': ['go to Galactic Space Station'],
			'image': 'spaceStation.jpg', 'image': 'jedivsSith.jpg'
		},
		'seek a diplomatic resolution': {
			'text': 'You attempt to find a diplomatic resolution with the Sith Lord, hoping to end the conflict without further bloodshed. The Sith Lord seems open to negotiation. Choose your next move:',
			'options': ['convince the Sith Lord to retreat', 'engage in a duel for honor'],
			'image': 'jks.jpg'
		},
		'convince the Sith Lord to retreat': {
			'text': 'Your diplomatic efforts succeed, and the Sith Lord agrees to retreat, bringing an unexpected end to the battle. The Republic forces secure the frontlines. Choose your next move:',
			'options': ['go to Galactic Space Station'],
			'image': 'spaceStation.jpg'
		},
		'engage in a duel for honor': {
			'text': 'Despite your attempts at negotiation, the Sith Lord challenges you to a duel for honor. The battle is fierce, and the outcome uncertain. Choose your next move:',
			'options': ['embrace the Dark Side to ensure victory', 'fight with honor and integrity'],
			'image': 'jedivsSith.jpg'
		},

		'embrace the Dark Side to ensure victory': {
			'text': 'In a moment of desperation, you embrace the Dark Side to ensure victory. The power surges through you, but at a cost. Choose your next move:',
			'options': ['wrestle control back from the Dark Side', 'embrace the Dark Side completely'],
			'image': 'dark aura.jpg'
		},
		'fight with honor and integrity': {
			'text': 'You choose to face the Sith Lord in a duel with honor and integrity. The clash of lightsabers echoes through the chamber as you and your opponent engage in a battle of skill and determination. Your commitment to the Light Side strengthens your resolve and is enough to deal a massive blow and defeat the Sith. Choose your next move:',
			'options': ['go to Galactic Space Station'],
			'image': 'jedivsSith.jpg'
		},
		'wrestle control back from the Dark Side': {
			'text': 'You struggle against the influence of the Dark Side, fighting to regain control. Your inner strength prevails, and you emerge from the battle with a newfound understanding. Choose your next move:',
			'options': ['go to Galactic Space Station'],
			'image': 'spaceStation.jpg'
		},
		'embrace the Dark Side completely': {
			'text': 'You fully embrace the Dark Side, succumbing to its temptations. The power consumes you, and your actions become twisted by the darkness. Choose your next move:',
			'options': ['proclaim loyalty to the Sith', 'seek redemption and return to the Light'],
			'image': 'ds.jpg'
		},
		'proclaim loyalty to the Sith': {
			'text': 'You proclaim loyalty to the Sith, aligning yourself with the dark forces. Your destiny takes a dark turn, and the galaxy awaits the consequences of your choice. Congratulations! Your journey as a Dark Side Force user continues.',
			'options': ['go to Galactic Space Station'],
			'image': '', 'image': 'spaceStation.jpg'
		},
		'seek redemption and return to the Light': {
			'text': 'In a moment of clarity, you reject the Dark Side and seek redemption. The Light welcomes you back, and you vow to use your strength for the greater good. Choose your next move:',
			'options': ['go to Galactic Space Station'],
			'image': 'Aura.jpg ', 'image': 'spaceStation.jpg'
		},
		'infiltrate Behind Enemy Lines': {
			'text': 'You choose to infiltrate Behind Enemy Lines, seeking to disrupt the Sith war efforts. As you navigate through enemy territory, you encounter a powerful Sith assassin. Choose your next move:',
			'options': ['engage in a stealthy confrontation', 'confront the assassin directly'],
			'image': 'swtor-onslaught-1_feature.jpg'
		},
		'engage in a stealthy confrontation': {
			'text': 'You use stealth to confront the Sith assassin, moving silently through the shadows. A tense battle ensues, with each move calculated for maximum efficiency. Choose your next move:',
			'options': ['utilize guerrilla tactics (Stealth Strikes)', 'proceed to the next chapter'],
			'image': 'jedi-consular.jpg'
		},
		'utilize guerrilla tactics (Stealth Strikes)': {
			'text': 'You employ guerrilla tactics, striking from the shadows with deadly precision. The Sith assassin is caught off guard, and you emerge victorious. Choose your next move:',
			'options': ['go to Galactic Space Station'],
			'image': 'trooper.jpg'
		},
		'confront the assassin directly': {
			'text': 'You choose to confront the Sith assassin directly, engaging in a head-on confrontation. The battle is fierce, with lightsabers clashing in a display of raw power. Choose your next move:',
			'options': ['overwhelm the assassin with aggressive attacks', 'defend and wait for an opening'],
			'image': 'stand.jpg'
		},
		'overwhelm the assassin with aggressive attacks': {
			'text': 'You unleash a barrage of aggressive attacks, overwhelming the Sith assassin with sheer force. The battle is intense, but your aggression proves to be too much for the assassin. Choose your next move:',
			'options': ['go to Galactic Space Station'],
			'image': 'jedivsSith.jpg'
		},
		'defend and wait for an opening': {
			'text': 'You adopt a defensive stance, patiently waiting for an opening in the Sith assassins attacks. Your resilience pays off as you find the perfect moment to strike. Choose your next move:',
			'options': ['deliver a decisive counterattack', 'proceed to the next chapter'],
			'image': 'swtor-onslaught-1_feature.jpg'
		},
		'deliver a decisive counterattack': {
			'text': 'Your patience pays off as you deliver a decisive counterattack, defeating the Sith assassin with precision. The path is now clear for further infiltration. Choose your next move:',
			'options': ['go to Galactic Space Station'],
			'image': 'spaceStation.jpg', 'image': 'jedivsSith.jpg'
		},
		'go to Galactic Space Station': {
			'text': 'You decide to head to the Galactic Space Station, a hub of activity and a nexus for various paths in the galaxy. As you arrive, new opportunities and challenges present themselves. Choose your next move:',
			'options': ['return to the start page', 'head to Hoth'],
			'image': 'spaceStation.jpg'
		},
		'return to the start page': {
			'text': 'As the echoes of your dark choice reverberate through the Force, you find yourself back at the start page, standing before the ancient temple of Morai on the remote planet of Tython. A chilling wind rustles the leaves as you enter the forest, guided only by the Force. Choose a direction:',
			'options': ['Enter Temple', 'Explore Forest'],
			'image': 'jeditemple.jpg'
		},
		'head to Hoth': {
			'text': 'You decide to head to the icy planet of Hoth, a battleground in the ongoing war between the Sith Empire and the Galactic Republic. As you arrive, you find yourself in the midst of a specific battle, the Battle of Hoth, where the fate of the galaxy hangs in the balance. The freezing winds and vast snowy landscapes set the stage for an epic conflict. Choose your next move:',
			'options': ['join the Republic defense (Fortress)'],
			'image': 'Aurek_Base.jpg'
		},
		'join the Republic defense (Fortress)': {
			'text': 'You choose to join the Republic forces in defending their stronghold against the relentless assault of the Sith Empire. The chilling winds carry the sounds of blaster fire and lightsaber clashes. Choose your next move:',
			'options': ['hold the frontlines with valor (Valor)', 'coordinate strategic defenses (Tactician)'],
			'image': 'Aurek_Base.jpg'
		},
		'hold the frontlines with valor (Valor)': {
			'text': 'With unwavering courage, you hold the frontlines against the Sith onslaught. Blaster bolts and lightsabers clash in a symphony of war. Choose your next move:',
			'options': ['engage the Sith in a duel of might (Mighty Duel)',
						'call for reinforcements (Strategic Reinforcement)'],
			'image': 'battle.jpg'
		},
		'coordinate strategic defenses (Tactician)': {
			'text': 'You take on the role of a tactician, coordinating the Republics defenses with strategic brilliance. The battlefield becomes a chessboard of war. Choose your next move:',
			'options': ['utilize defensive emplacements (Fortified Defense)',
						'execute a counteroffensive strategy (Counterstrike)'],
			'image': 'trooper.jpg'
		},
		'engage the Sith in a duel of might (Mighty Duel)': {
			'text': 'You engage in a duel of might with the Sith, lightsabers clashing in a display of raw power. The outcome of this individual battle could sway the tide of the larger conflict. Choose your next move:',
			'options': ['overpower the Sith with sheer strength (Brute Force)',
						'utilize finesse and technique (Precision Strikes)'],
			'image': 'battle.jpg'
		},
		'call for reinforcements (Strategic Reinforcement)': {
			'text': 'Recognizing the need for additional support, you call for reinforcements to bolster the Republic defense. The battle takes a strategic turn with the arrival of fresh troops. Choose your next move:',
			'options': ['lead the reinforced charge (Counteroffensive)'],
			'image': 'swtor-troopers.jpg'
		},
		'utilize defensive emplacements (Fortified Defense)': {
			'text': 'You strategically deploy defensive emplacements, creating a formidable barrier against the Sith advance. The Republic stronghold becomes a fortress that is challenging to breach. Choose your next move:',
			'options': ['execute a counteroffensive strategy (Counterstrike)'],
			'image': 'SWTOR_War.jpg'
		},
		'execute a counteroffensive strategy (Counterstrike)': {
			'text': 'With a counteroffensive strategy, you lead the Republic forces in a determined push against the Sith. The tide of battle begins to shift in favor of the Republic. Choose your next move:',
			'options': ['coordinate with Republic forces for a strategic encirclement (Encirclement)'],
			'image': 'obi_wan.jpg'
		},
		'overpower the Sith with sheer strength (Brute Force)': {
			'text': 'You overpower the Sith with sheer strength, dominating the individual duel. The defeated Sith forces retreat, demoralized by your display of power. Choose your next move:',
			'options': ['pursue the retreating Sith for a decisive victory (Pursuit)',
						'consolidate gains and prepare for the next assault (Preparation)'],
			'image': 'jedivsSith.jpg'
		},
		'utilize finesse and technique (Precision Strikes)': {
			'text': 'With finesse and technique, you outmaneuver the Sith in the individual duel. The Sith forces are left in disarray, opening opportunities for the Republic. Choose your next move:',
			'options': ['consolidate gains and fortify positions (Secure Advantage)'],
			'image': 'swtor-onslaught-1_feature.jpg'
		},
		'pursue the retreating Sith for a decisive victory (Pursuit)': {
			'text': 'You choose to pursue the retreating Sith, determined to achieve a decisive victory. The chase is intense, and the Sith forces are on the brink of collapse. Choose your next move:',
			'options': ['launch a swift and aggressive assault (Swift Assault)',
						'coordinate with Republic forces for a strategic encirclement (Encirclement)'],
			'image': 'swtor-onslaught-1_feature.jpg'
		},
		'launch a swift and aggressive assault (Swift Assault)': {
			'text': 'You launch a swift and aggressive assault, catching the retreating Sith forces off guard. The battlefield becomes chaotic as your lightsaber cuts through enemy ranks. Choose your next move:',
			'options': ['regroup with Republic forces to assess the situation (Regroup)'],
			'image': 'trooper.jpg'
		},
		'coordinate with Republic forces for a strategic encirclement (Encirclement)': {
			'text': 'You coordinate with Republic forces to execute a strategic encirclement of the retreating Sith. The Sith find themselves surrounded and overwhelmed. Choose your next move:',
			'options': ['press the advantage for a swift victory (Advantage Press)',
						'allow the Sith a chance to surrender (Surrender Offer)'],
			'image': 'swtor-troopers.jpg'
		},
		'regroup with Republic forces to assess the situation (Regroup)': {
			'text': 'You regroup with Republic forces to assess the situation. The battlefield is in flux, and a strategic decision must be made. Choose your next move:',
			'options': ['allow the Sith a chance to surrender (Surrender Offer)'],
			'image': 'alliance.jpg'
		},
		'press the advantage for a swift victory (Advantage Press)': {
			'text': 'You press the advantage, aiming for a swift and decisive victory over the surrounded Sith forces. The Republic gains momentum, and victory seems within reach. Choose your next move:',
			'options': ['consolidate gains and fortify positions (Secure Advantage)'],
			'image': 'chase.jpg'
		},
		'allow the Sith a chance to surrender (Surrender Offer)': {
			'text': 'Despite having the advantage, you offer the retreating Sith forces a chance to surrender. The battlefield falls silent as you await their response. Choose your next move:',
			'options': ['accept the Siths surrender and seek a diplomatic resolution (Diplomatic Resolution)'],
			'image': 'jks.jpg'
		},
		'lead the reinforced charge (Counteroffensive)': {
			'text': 'You take command of the reinforced charge, leading Republic forces in a counteroffensive against the Sith. The battlefield dynamic shifts in your favor. Choose your next move:',
			'options': ['launch a targeted strike on Sith command posts (Command Post Strike)',
						'coordinate with allied Jedi for a synchronized assault (Jedi Alliance)'],
			'image': 'trooper.jpg'
		},
		'launch a targeted strike on Sith command posts (Command Post Strike)': {
			'text': 'You decide to launch a targeted strike on Sith command posts, disrupting their coordination and weakening their strategic position. The Republic gains a tactical advantage. Choose your next move:',
			'options': ['consolidate gains and fortify positions (Secure Advantage)'],
			'image': 'Aurek_Base.jpg'
		},
		'coordinate with allied Jedi for a synchronized assault (Jedi Alliance)': {
			'text': 'You coordinate with allied Jedi, forming a powerful alliance to synchronize your assault on the Sith. The combined strength of the Jedi forces creates a formidable front. Choose your next move:',
			'options': ['launch a decisive assault on Sith strongholds (Decisive Assault)'],
			'image': 'alliance.jpg'
		},
		'launch a decisive assault on Sith strongholds (Decisive Assault)': {
			'text': 'With the Jedi Alliance, you launch a decisive assault on Sith strongholds, aiming to break their defenses and secure a significant victory. The battle reaches a critical point. Choose your next move:',
			'options': ['consolidate gains and fortify positions (Secure Advantage)'],
			'image': 'trooper.jpg'
		},
		'accept the Siths surrender and seek a diplomatic resolution (Diplomatic Resolution)': {
			'text': 'The Sith, recognizing the futility of continued resistance, offer their surrender. Choosing the path of diplomacy, you accept their surrender and seek a peaceful resolution. Choose your next move:',
			'options': ['consolidate gains and fortify positions (Secure Advantage)'],
			'image': 'stratagy.jpg'
		},
		'pursue the retreating Sith for a decisive victory (Chase Down)': {
			'text': 'You choose to pursue the retreating Sith, determined to achieve a decisive victory. The chase is intense, and the Sith forces are on the brink of collapse. Choose your next move:',
			'options': ['consolidate gains and fortify positions (Secure Advantage)'],
			'image': 'chase.jpg'
		},
		'consolidate gains and fortify positions (Secure Advantage)': {
			'text': 'You decide to consolidate gains and fortify positions, securing the advantage gained in the battle. As the Sith retreat, you receive new orders from the Republic command. Choose your next move:',
			'options': ['return to the Galactic Space Station (Again)', ],
			'image': 'spaceStation.jpg'
		},
		'return to the Galactic Space Station (Again)': {
			'text': 'Congratulations! You have successfully navigated the challenges of the Old Republic era, making pivotal decisions that shaped the course of the galaxy. The Force is strong with you. Thank you for playing!',
			'image': 'star-wars-the-old-republic.gif'
		},
	}

}
game = Adventure(game_state)
adventure_game = Adventure(game_state)


def game(username):
	if request.method == 'POST':
		if 'direction' in request.form:
			direction = request.form['direction']
			if adventure_game.move(player, direction):
				return redirect(url_for('game', username=username))
			else:
				return jsonify({'error': 'Invalid direction'})
		elif 'save_game' in request.form:
			save_game()
			return jsonify({'message': 'Game saved successfully'})
