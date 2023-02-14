from typing import Final
from random import randint

from .models.superheros import SuperheroModel
from .models.villains import VillainModel
from .schemas.player import Player
from .schemas.game_state import GameState
from .schemas.superhero import SuperHero
from .schemas.villain import Villain
from .schemas.life import Life

class Game:
    def __init__(self, player: Player) -> None:
        self.player = player
        self.state = GameState.INITIALIZING
        self.superheros = SuperheroModel
        self.villains = VillainModel
    
    def __repr__(self) -> str:
        return "<class 'Game'>"
    
    def __str__(self) -> str:
        return (f"Player: {self.player},\nState: {self.state},\nSuperheros: {self.superheros},\n"
               f"Villains: {self.villains}"
               )

    # -------------------------------------- Main Logic ------------------------------------

    def attack(self) -> None:
        """Start the attack"""
        self.state = GameState.IN_PROGRESS
        print("Starting attack...")
        print(self.state)
        
        # Attack
        for attack_num in range(3):
            # each iteration get a new hero & villain
            hero_index = randint(0, 3)
            villain_index = randint(0, 2)

            current_superhero = self.superheros.get_superhero(hero_index)
            current_villain = self.villains.get_villain(villain_index)

            if current_superhero and current_villain:
                self.__do_attack(attack_num, current_superhero, current_villain)
            else:
                print("Error! No superheros or villains to fight.")

    def __do_attack(self, attack_num: int, superhero: SuperHero, villain: Villain) -> None:
        """Simulate the actual attack"""

        # Set life
        Life.inc_hero_life(superhero.life)
        Life.inc_villain_life(villain.life)

        print(
            f"Attack: {attack_num + 1} => {superhero.name} is going to fight with {villain.name}."
        )

        # Actual attack
        Life.dec_hero_life(villain.attack_power)
        Life.dec_villain_life(superhero.attack_power)

    #------------------------------------ Final Game Status --------------------------------------

    def win_or_loose(self) -> None:
        """Determine if Avengers won or lost"""

        # declare helper messages
        WIN_MSG: Final[str] = "You succesfully saved Zortan!!!"
        LOST_MSG: Final[str] = "Thanos killed Avengers and captured Zortan!!!"

        # Print a nice separating line
        print("=" * 58)

        # Win or Loose
        if Life.hero_life >= Life.villain_life:
            print(WIN_MSG)
        else:
            print(LOST_MSG)

