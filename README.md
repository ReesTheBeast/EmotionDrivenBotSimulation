Advanced Emotion Bot Simulation
This project simulates a collection of AI bots with advanced emotional intelligence and relationships. Each bot has a variety of emotional states, personality traits, and the ability to form relationships, cheat, reproduce, and interact with others. The simulation runs continuously, showcasing the interactions between bots as they evolve over time.

Features
Emotions: Bots exhibit six primary emotions (happiness, sadness, anger, fear, surprise, and disgust) that can change based on interactions and events.
Personality Traits: Bots have traits such as optimism, neuroticism, and agreeableness that influence their behavior.
Relationships: Bots can develop romantic relationships, cheat on partners, and form familial bonds.
Reproduction: Bots can reproduce and create new bots with inherited personalities.
Memory System: Bots can recall past interactions and experiences, which influence their future decisions.
Simulated Environment: The bots live in an environment where they interact with each other, form relationships, and evolve over time.
Interactive Console: Users can check the status of any bot during the simulation and observe its emotional state, relationships, and age.
Requirements
Python 3.x
No additional libraries are required as the code utilizes Python's standard library.
Installation
Clone the repository:

git clone https://github.com/ReesTheBeast/EmotionDrivenBotSimulation.git
cd advanced-emotion-bot
Ensure you have Python 3 installed. You can verify this with:

python --version
Run the simulation:

python main.py
Usage
Start the simulation: Once you run the simulation, a set of bots will be created and interact with each other.
Check Bot Status: While the simulation is running, you can type a bot’s name to check its current emotional state, relationships, and other details.
Exit Simulation: To stop the simulation, type exit at the prompt.
Commands
Check status: Type the name of a bot to check its status.
Exit simulation: Type exit to stop the simulation.
Example:

Enter a bot name to check status or 'exit' to stop: Bot_1
Bot_1 Emotional State -> Happiness: 0.55, Sadness: 0.47, Anger: 0.40, Fear: 0.45, Surprise: 0.53, Disgust: 0.35
In love with Bot_2, Partnered with Bot_3.
Bot Interaction Logic
Emotion Adjustment: Bots can experience emotional changes based on interactions. For example:
Praise increases happiness.
Criticism increases anger and sadness.
Love and Relationships:
Bots develop romantic feelings based on attraction, influenced by personality traits.
Cheating, jealousy, and emotional conflict can arise if a bot's partner is unfaithful.
Bots can become parents and have children, with personality traits inherited from both parents.
Reproduction:
Bots can reproduce with their partners, creating new bots with combined personality traits. A bot can have up to 3 children.
Example Simulation Flow
Bots are created with random personality traits.
Each bot interacts with other bots. Emotions fluctuate based on the interaction type (praise, criticism, love, etc.).
Bots form relationships, develop love interests, and may cheat.
Over time, bots age, decay emotionally, and may reproduce if partnered.
The environment provides a periodic overview of the bots' ages, partnerships, and other stats.
Code Overview
The simulation is made up of two primary classes:

AdvancedEmotionBot
Represents an individual bot with emotions, relationships, memory, and personality traits. Key methods include:

adjust_emotion: Adjusts a bot's emotion based on interactions.
interact_with: Handles interaction between bots, including love, partnership, and emotional changes.
reproduce: Creates a new bot when two bots reproduce.
BotEnvironment
Represents the simulated environment where all bots exist. Key methods include:

simulate: Runs the simulation, including bot interactions and emotional decay.
add_bot: Adds a new bot to the environment.
provide_overview: Provides a periodic overview of the environment.
Customization
Number of Bots: You can customize the number of bots created when the environment is initialized by changing the num_bots parameter.
Bot Personalities: Personalities are generated randomly with traits of optimism, neuroticism, and agreeableness. You can modify the personality range or manually set personalities for specific bots.
License
This project is licensed under the MIT License

Acknowledgements
Thanks to the creators of the Python standard library, which powers much of this simulation.
Inspired by emotional AI research and relationship simulation systems.
