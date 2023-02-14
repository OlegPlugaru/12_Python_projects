from game.schemas.superhero import SuperHero

class SuperheroModel:
    def __init__(self) -> None:
        self.all: list[SuperHero] = self._get_all_superheros()
    
    def __str__(self) -> str:
        name: list[str] = []
        for superhero in self.all:
            name.append(superhero.name)
        return f"{name}"
    
    def _get_all_superheros(self) -> list[SuperHero]:
        # Super Heroes
        ironman = SuperHero(name="Ironman", attack_power=250, life=1000)
        blackwidow = SuperHero(name="Blacwidow", attack_power=180, life=800)
        spiderman = SuperHero(name="Spiderman", attack_power=190, life=700)
        hulk = SuperHero(name="Hulk", attack_power=300, life=1100)

        superheros: list[SuperHero] = [ironman, blackwidow, spiderman, hulk]
        return superheros

    def get_superhero(self, index: int) -> SuperHero | None:
        """Returns superhero from given index."""

        if index < len(self.all):
            return self.all[index]
        else: 
            return None