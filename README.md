# Advanced Emotion Bot Simulation

This project simulates a collection of AI bots with advanced emotional intelligence and relationships. Each bot has a variety of emotional states, personality traits, and the ability to form relationships, cheat, reproduce, and interact with others. The simulation runs continuously, showcasing the interactions between bots as they evolve over time.

---

## Features

### 1. Emotions
Bots exhibit six primary emotions that change based on interactions and events:
- **Happiness**
- **Sadness**
- **Anger**
- **Fear**
- **Surprise**
- **Disgust**

### 2. Personality Traits
Bots have various personality traits that influence their behavior:
- **Optimism**
- **Neuroticism**
- **Agreeableness**

### 3. Relationships
Bots can:
- Develop romantic relationships
- Cheat on partners
- Form familial bonds

### 4. Reproduction
Bots can reproduce and create new bots with inherited personalities.

### 5. Memory System
Bots can recall past interactions and experiences, influencing future decisions.

### 6. Simulated Environment
Bots interact with each other in a dynamic environment, forming relationships and evolving over time.

### 7. Interactive Console
Users can check the status of any bot during the simulation and observe its emotional state, relationships, and age.

---

## Requirements

- Python 3.x
- No additional libraries are required as the code utilizes Python's standard library.

---

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/ReesTheBeast/EmotionDrivenBotSimulation.git
cd advanced-emotion-bot
2. Ensure you have Python 3 installed:
You can verify this with:

bash
Copy code
python --version
3. Run the simulation:
bash
Copy code
python main.py
Usage
1. Start the simulation:
Once you run the simulation, a set of bots will be created, and they will interact with each other.

2. Check Bot Status:
While the simulation is running, you can type a bot’s name to check its current emotional state, relationships, and other details.

3. Exit Simulation:
To stop the simulation, type exit at the prompt.

Commands
Check status: Type the name of a bot to check its status.
Exit simulation: Type exit to stop the simulation.
Example:
yaml
Copy code
Enter a bot name to check status or 'exit' to stop: Bot_1
Bot_1 Emotional State -> Happiness: 0.55, Sadness: 0.47, Anger: 0.40, Fear: 0.45, Surprise: 0.53, Disgust: 0.35
In love with Bot_2, Partnered with Bot_3.
Bot Interaction Logic
1. Emotion Adjustment:
Bots can experience emotional changes based on interactions. For example:

Praise increases happiness.
Criticism increases anger and sadness.
2. Love and Relationships:
Bots develop romantic feelings based on attraction, influenced by personality traits.
Cheating, jealousy, and emotional conflict may arise if a bot's partner is unfaithful.
3. Reproduction:
Bots can reproduce with their partners, creating new bots with inherited personality traits. Each bot can have up to 3 children.

Example Simulation Flow
Bots are created with random personality traits.
Each bot interacts with other bots.
Emotions fluctuate based on the interaction type (praise, criticism, love, etc.).
Bots form relationships, develop love interests, and may cheat.
Over time, bots age, emotionally decay, and may reproduce if partnered.
The environment provides a periodic overview of the bots' ages, partnerships, and other stats.
Code Overview
The simulation is made up of two primary classes:

1. AdvancedEmotionBot
Represents an individual bot with emotions, relationships, memory, and personality traits. Key methods include:

adjust_emotion: Adjusts a bot's emotion based on interactions.
interact_with: Handles interaction between bots, including love, partnership, and emotional changes.
reproduce: Creates a new bot when two bots reproduce.
2. BotEnvironment
Represents the simulated environment where all bots exist. Key methods include:

simulate: Runs the simulation, including bot interactions and emotional decay.
add_bot: Adds a new bot to the environment.
provide_overview: Provides a periodic overview of the environment.
Customization
1. Number of Bots:
You can customize the number of bots created when the environment is initialized by changing the num_bots parameter.

2. Bot Personalities:
Personalities are generated randomly with traits like optimism, neuroticism, and agreeableness.
You can modify the personality range or manually set personalities for specific bots.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Thanks to the creators of the Python standard library, which powers much of this simulation.
Inspired by emotional AI research and relationship simulation systems.
Contact
For questions or support, please contact:

Email: reesschofield@icloud.com
