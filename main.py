import random


class Hero:
	def __init__(self, nick, power):
		self.nick = nick
		self.power = power

	@classmethod
	def get_rage_mode(cls, nick, power):
		return cls(nick, power + 100)


class Game:
	reserve_players = [
		('Galat',50),
		('МС Пох',125),
		('Jubilee',5),
		('SODA Luv',75)
	]
	def __init__(self, heroes):
		self.heroes = heroes

	def show_top_rating(self):
		self.heroes.sort(key=lambda x: x.power,reverse=True)
		print('\nРейтинг: ')
		for count, hero in enumerate(self.heroes):
			print(f'#{count + 1} - {hero.nick}')

	def start_versus(self, first_player, second_player):
		print('Сравнение реперов: ')
		first_player = list(filter(lambda x: x.nick == first_player, self.heroes))[0]
		second_player = list(filter(lambda x: x.nick == second_player, self.heroes))[0]

		template_print = lambda first,second,label: f'{label} - {first} vs {second}\n'
		print(template_print(first_player.nick, second_player.nick, 'Имена'))
		print(template_print(first_player.power, second_player.power, 'Сила'))

		print(f'Победил - {first_player.nick}') if first_player.power > second_player.power else print(f'Победил - {second_player.nick}')

	def create_pairs(self):
		if int(len(self.heroes) / 2) % 2 != 0:
			self.heroes.append(Hero(*random.choice(self.reserve_players))) if random.randint(1,2) == 1 else self.heroes.append(Hero.get_rage_mode(*random.choice(self.reserve_players)))

		random.shuffle(self.heroes)

		first_team = self.heroes[:int(len(self.heroes) / 2) + 1]
		second_team = self.heroes[int(len(self.heroes) / 2):]

		for first, second in zip(first_team, second_team):
			first_player = first.nick 
			second_player = second.nick 

			print(f'{first_player} vs {second_player}')
			self.start_versus(first_player,second_player)


hero_l = [Hero.get_rage_mode('Oxxxymiron',120),Hero.get_rage_mode('Rickey F',20),Hero('MAYOT',250)]
game = Game(hero_l)
game.create_pairs()
game.show_top_rating()
