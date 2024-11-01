import random
import time
import threading
import os

class AdvancedEmotionBot:
    def __init__(self, name, personality_traits=None, parents=None):
        self.name = name
        self.emotions = {
            "happiness": 0.5,
            "sadness": 0.5,
            "anger": 0.5,
            "fear": 0.5,
            "surprise": 0.5,
            "disgust": 0.5,
        }
        self.memory = []
        self.emotion_decay_rate = 0.1
        self.sensitivity = 0.5
        self.age = 0
        
        self.personality = personality_traits or {
            "optimism": 0.5,
            "neuroticism": 0.5,
            "agreeableness": 0.5,
        }

        self.partner = None
        self.love_interest = None
        self.attraction = {}
        self.children_count = 0 
        self.recent_interactions = []
        self.parents = parents 
        self.children = [] 
        

    def adjust_emotion(self, emotion, amount, duration=5, damping=0.2):
        """Adjusts the emotion of the bot by a certain amount for a specific duration, with damping to prevent sharp changes."""
        if emotion in self.emotions:
            adjusted_amount = amount * self.sensitivity
            
            self.emotions[emotion] += damping * (adjusted_amount - self.emotions[emotion])
            
            self.emotions[emotion] = max(0.0, min(1.0, self.emotions[emotion]))

            #print(f"{self.name} adjusted {emotion} by {adjusted_amount:.2f} with damping. New value: {self.emotions[emotion]:.2f}")
            self.record_event(emotion, adjusted_amount, duration)


    def cheat_on_partner(self, new_love):
        """Handles cheating scenario where a bot cheats on its current partner with another bot."""
        if self.partner:
            self.partner.adjust_emotion("happiness", -0.4)
            self.partner.adjust_emotion("anger", +0.5)
            self.adjust_emotion("suprise", +0.3)
            self.partner.recent_interactions.append(f"{self.name} cheated with {new_love.name}.")
        
            self.adjust_emotion("happiness", -0.2)
            self.adjust_emotion("sadness", +0.3)
            self.recent_interactions.append(f"Cheated on {self.partner.name} with {new_love.name}.")
        else:
            self.recent_interactions.append(f"Developed a new love interest in {new_love.name}.")
        
        self.love_interest = new_love
        new_love.consider_love_interest(self)



    def record_event(self, emotion, impact, duration):
        """Records an emotional event with a weighted impact based on its intensity."""
        weight = abs(impact) 
        self.memory.append({
            "emotion": emotion, 
            "impact": impact, 
            "end_time": time.time() + duration,
            "weight": weight 
        })
        self.memory = sorted(self.memory, key=lambda x: x["weight"], reverse=True)
        if len(self.memory) > 15:
            self.memory = sorted(self.memory, key=lambda x: x["weight"], reverse=True)[:15]


    def decay_emotions(self):
        """Decays emotions over time, and allows memories to influence emotions."""
        current_time = time.time()
        for emotion in self.emotions:
            self.emotions[emotion] *= (1 - self.emotion_decay_rate)
        
        for event in self.memory:
            time_remaining = event["end_time"] - current_time
            if time_remaining > 0:
                decay_factor = time_remaining / 10.0  
                impact = event["impact"] * event["weight"] * decay_factor
                self.emotions[event["emotion"]] += impact

            self.emotions[event["emotion"]] = max(0.0, min(1.0, self.emotions[event["emotion"]]))
        
        self.memory = [event for event in self.memory if event["end_time"] > current_time]



    def interact_with(self, other_bot):
        """Interacts with another bot, influencing attraction, emotions, partnership, and reproduction."""
        if other_bot.name not in self.attraction:
            self.attraction[other_bot.name] = 0.0

        if self.is_family(other_bot):
            self.interact_as_family(other_bot)
        else:
            if self.emotions["happiness"] > 0.4 or random.random() < 0.3:
                self.attraction[other_bot.name] += 0.1 * (1 + self.personality["agreeableness"])
                other_bot.receive_praise(self.name)
            elif self.emotions["anger"] > 0.4 or random.random() < 0.2: 
                self.attraction[other_bot.name] -= 0.1 * (1 + self.personality["neuroticism"])
                other_bot.receive_criticism(self.name)

            if self.attraction[other_bot.name] > 0.6 and self.love_interest is None:
                self.love_interest = other_bot
                self.recent_interactions.append(f"Developed a love interest in {other_bot.name}.")
                other_bot.consider_love_interest(self)
            elif self.attraction[other_bot.name] > 0.6 and self.love_interest is not None and self.love_interest != other_bot:
                if other_bot.love_interest == self:
                    self.cheat_on_partner(other_bot)

            if self.love_interest == other_bot and other_bot.love_interest == self and self.partner is None:
                self.partner = other_bot
                other_bot.partner = self
                self.recent_interactions.append(f"Partnered with {other_bot.name}.")
                other_bot.recent_interactions.append(f"Partnered with {self.name}.")

            if self.partner == other_bot and random.random() < 0.3: 
                self.reproduce(environment)


                    

    def receive_praise(self, from_bot):
        """Adjust emotions when receiving praise from another bot."""
        self.adjust_emotion("happiness", +0.2)
        self.adjust_emotion("sadness", -0.1)
        self.adjust_emotion("anger", -0.05) 
        self.adjust_emotion("suprise", +0.05)

    def receive_criticism(self, from_bot):
        """Adjust emotions when receiving criticism from another bot."""
        self.adjust_emotion("anger", +0.3 * (1 + self.personality["neuroticism"]))
        self.adjust_emotion("sadness", +0.2)
        self.adjust_emotion("happiness", -0.15)
        self.adjust_emotion("suprise", +0.1)

    def interact_as_family(self, other_bot):
        """Special interactions between family members."""
        if other_bot in self.children:
            self.give_parental_advice(other_bot)
        elif other_bot in (self.parents or []):
            self.seek_parental_support(other_bot)
        else:
            self.family_bonding(other_bot)

    def is_family(self, other_bot):
        """Checks if another bot is a family member (parent, child, or sibling)."""
        return other_bot in self.children or other_bot in (self.parents or []) or \
               (self.parents and other_bot.parents == self.parents)
    
    def give_parental_advice(self, child_bot):
        """Parent bot provides advice that influences both emotions and personality traits."""
        child_bot.adjust_emotion("happiness", +0.1)
        child_bot.personality["agreeableness"] += 0.01
        self.recent_interactions.append(f"Advised child {child_bot.name} on personality.")


    def seek_parental_support(self, parent_bot):
        """Child bot interacts with its parent for emotional support."""
        self.adjust_emotion("sadness", -0.3)
        self.adjust_emotion("happiness", +0.2)
        self.recent_interactions.append(f"Sought support from parent {parent_bot.name}.")
        parent_bot.recent_interactions.append(f"Provided support to child {self.name}.")

    def family_bonding(self, family_member):
        """Bots bond with their family members."""
        self.adjust_emotion("happiness", +0.2)
        self.adjust_emotion("sadness", +0.4)
        family_member.adjust_emotion("happiness", +0.2)
        self.recent_interactions.append(f"Bonded with family member {family_member.name}.")
        family_member.recent_interactions.append(f"Bonded with {self.name}.")

    def consider_love_interest(self, other_bot):
        if other_bot.name not in self.attraction:
            self.attraction[other_bot.name] = 0.0 
        if self.love_interest is None and self.attraction[other_bot.name] > 0.6:
            if other_bot.partner is None:
                self.love_interest = other_bot
                self.recent_interactions.append(f"Developed a love interest in {other_bot.name}.")
            else:
                self.adjust_emotion("anger", +0.3)
                self.adjust_emotion("sadness", +0.5)
                self.adjust_emotion("surprise", +0.2)
                self.adjust_emotion("sadness", +0.1)
                self.recent_interactions.append(f"{other_bot.name} already has a partner, causing emotional conflict.")

        elif self.love_interest == other_bot and other_bot.partner and other_bot.partner != self:
            self.adjust_emotion("anger", +0.5)
            self.adjust_emotion("sadness", +0.3)
            self.adjust_emotion("suprise", +0.1)
            self.adjust_emotion("disgust", +0.05)
            self.recent_interactions.append(f"Feeling rejected as {other_bot.name} is already partnered with {other_bot.partner.name}.")

    def get_status(self):
        """Returns a detailed status of the bot, including all emotion levels."""
        emotion_status = ', '.join([f"{emo.capitalize()}: {val:.2f}" for emo, val in self.emotions.items()])
        love_status = f"In love with {self.love_interest.name}" if self.love_interest else "Single"
        partner_status = f"Partnered with {self.partner.name}" if self.partner else "No partner"
        return f"{self.name} Emotional State -> {emotion_status}\n{love_status}, {partner_status}."

    def consider_partnership(self):
        """If mutual love interest exists, bots form a partnership."""
        if self.love_interest and self.love_interest.love_interest == self and not self.partner:
            self.partner = self.love_interest
            self.love_interest.partner = self
            self.recent_interactions.append(f"Partnered with {self.love_interest.name}.")

    def reproduce(self, environment):
        """Bots reproduce if partnered, creating a new bot with inherited personality."""
        if self.partner and self.children_count < 3 and random.random() < 0.3:
            new_name = f"Bot_{environment.bot_counter}"
            child_personality = {
                "optimism": (self.personality["optimism"] + self.partner.personality["optimism"]) / 2,
                "neuroticism": (self.personality["neuroticism"] + self.partner.personality["neuroticism"]) / 2,
                "agreeableness": (self.personality["agreeableness"] + self.partner.personality["agreeableness"]) / 2
            }
            child = AdvancedEmotionBot(new_name, child_personality, parents=(self, self.partner))
            environment.add_bot(child)
            self.children.append(child)
            self.partner.children.append(child)
            self.children_count += 1 
            self.recent_interactions.append(f"Reproduced with {self.partner.name}, creating {new_name}.")
            self.partner.recent_interactions.append(f"Reproduced with {self.name}, creating {new_name}.")



    def simulate_turn(self, environment):
            """Simulates one turn of the bot's life, including emotional decay and relationship impacts."""
            self.decay_emotions()

            if self.partner:
                self.partner.adjust_emotion("happiness", self.emotions["happiness"] * 0.1) 
                self.partner.adjust_emotion("sadness", self.emotions["sadness"] * 0.1)

            self.consider_partnership()
            self.reproduce(environment)
            self.age += 1



class BotEnvironment:
    def __init__(self, num_bots):
        self.bot_counter = 1
        self.bots = {}
        for i in range(num_bots):
            name = f"Bot_{i+1}"
            personality = {
                "optimism": random.uniform(0.2, 0.8),
                "neuroticism": random.uniform(0.2, 0.8),
                "agreeableness": random.uniform(0.2, 0.8)
            }
            bot = AdvancedEmotionBot(name, personality)
            self.bots[name] = bot

    def add_bot(self, bot):
        """Adds a new bot to the environment."""
        self.bots[bot.name] = bot
        print(f"New bot born!: {bot.name}")
        self.bot_counter += 1

    def simulate(self):
        """Simulates the environment with all bots, running indefinitely."""
        turn = 1
        threading.Thread(target=self.listen_for_input, daemon=True).start()
        try:
            while True:
                for bot in list(self.bots.values()):
                    other_bot = random.choice([b for b in self.bots.values() if b != bot])
                    bot.interact_with(other_bot)
                    bot.simulate_turn(self)

                self.bots = {name: bot for name, bot in self.bots.items() if bot.age < 1000}

                if turn % 10 == 0:
                    self.clear_console()
                    self.provide_overview()

                time.sleep(1)
                turn += 1
        except KeyboardInterrupt:
            print("Simulation stopped by user.")

    def listen_for_input(self):
        """Allows the user to check a bot's status during the simulation."""
        while True:
            user_input = input("Enter a bot name to check status or 'exit' to stop: ")
            if user_input.lower() == 'exit':
                print("Exiting simulation...")
                exit(0)
            status = self.get_bot_status(user_input)
            print(status)

    def provide_overview(self):
        """Provides a periodic overview of the environment."""
        num_bots = len(self.bots)
        average_age = sum(bot.age for bot in self.bots.values()) / num_bots if num_bots > 0 else 0
        num_partnerships = sum(1 for bot in self.bots.values() if bot.partner) // 2
        oldest_bot = max(self.bots.values(), key=lambda b: b.age, default=None)
        newest_bot = min(self.bots.values(), key=lambda b: b.age, default=None)

        print("\n--- Environment Overview ---")
        print(f"Total bots: {num_bots}")
        print(f"Average age of bots: {average_age:.2f}")
        print(f"Number of partnerships: {num_partnerships}")
        if oldest_bot:
            print(f"Oldest bot: {oldest_bot.name} (Age: {oldest_bot.age})")
        if newest_bot:
            print(f"Newest bot: {newest_bot.name} (Age: {newest_bot.age})")
        print("---------------------------\n")

    def get_bot_status(self, bot_name):
        """Returns the status of a specific bot."""
        if bot_name in self.bots:
            return self.bots[bot_name].get_status()
        return "Bot not found."

    def clear_console(self):
        """Clears the console."""
        os.system('cls' if os.name == 'nt' else 'clear')

environment = BotEnvironment(num_bots=5)
environment.simulate()