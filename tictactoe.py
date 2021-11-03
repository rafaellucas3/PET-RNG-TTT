import numpy as np
from random import randint
import sys

pets = {
    'none'         : {'name': 'None',     'icon': 'assets/pets/png/none.png',     'hp': 0, 'res': 0, 'attack_damage': 0, 'attack_type': '', 'attack_pattern': [[0,0,0],[0,0,0],[0,0,0]], 'ability': ''},
    'koala'        : {'name': 'Koala',    'icon': 'assets/pets/png/koala.png',    'hp': 3, 'res': 2, 'attack_damage': -1, 'attack_type': 'r1+', 'attack_pattern': [[0,0,0],[0,0,0],[0,0,0]], 'ability': 'Heals one HP in one random space in + direction.'},
    'panda'        : {'name': 'Panda',    'icon': 'assets/pets/png/panda.png',    'hp': 2, 'res': 2, 'attack_damage': 0, 'attack_type': 'pat', 'attack_pattern': [[0,1,0],[1,0,1],[0,1,0]], 'ability': 'Deals one damage in + direction.'},
    'tiger'        : {'name': 'Tiger',    'icon': 'assets/pets/png/tiger.png',    'hp': 2, 'res': 2, 'attack_damage': 0, 'attack_type': 'pat', 'attack_pattern': [[1,0,1],[0,0,0],[1,0,1]], 'ability': 'Deals one damage in x direction.'},
    'snake'        : {'name': 'Snake',    'icon': 'assets/pets/png/snake.png',    'hp': 1, 'res': 2, 'attack_damage': 0, 'attack_type': 'r1+', 'attack_pattern': [[0,0,0],[0,0,0],[0,0,0]], 'ability': 'Deals one damage in one random + direction and inflicts poison.'},
    'capybara'     : {'name': 'Capybara', 'icon': 'assets/pets/png/capybara.png', 'hp': 1, 'res': 3, 'attack_damage': 0, 'attack_type': '', 'attack_pattern': [[0,0,0],[0,0,0],[0,0,0]], 'ability': 'It is immune for 2 turns.'},
    'bunny'        : {'name': 'Bunny',    'icon': 'assets/pets/png/bunny.png',    'hp': 1, 'res': 1, 'attack_damage': 0, 'attack_type': '', 'attack_pattern': [[0,0,0],[0,0,0],[0,0,0]], 'ability': 'No special ability.'},
    'monkey'       : {'name': 'Monkey',   'icon': 'assets/pets/png/monkey.png',   'hp': 2, 'res': 2, 'attack_damage': 0, 'attack_type': '', 'attack_pattern': [[0,0,0],[0,0,0],[0,0,0]], 'ability': 'When hurt, moves one space to a random + direction if empty.'},
    'pig'          : {'name': 'Pig',      'icon': 'assets/pets/png/pig.png',      'hp': 2, 'res': 1, 'attack_damage': 0, 'attack_type': '', 'attack_pattern': [[0,0,0],[0,0,0],[0,0,0]], 'ability': 'No special ability.'},
    'leo'          : {'name': 'Leo',      'icon': 'assets/pets/png/leo.png',      'hp': 3, 'res': 3, 'attack_damage': 0, 'attack_type': 'pat', 'attack_pattern': [[1,1,1],[1,0,1],[1,1,1]], 'ability': 'Deals one damage in all directions.'},
}

BOARD_SIZE = 3

class Game():
    def __init__(self):
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE))
        self.p1_choices = np.zeros((BOARD_SIZE, BOARD_SIZE))
        self.p2_choices = np.zeros((BOARD_SIZE, BOARD_SIZE))

        self.remaining_empty_spaces = self.count_empty_spaces()
        #Generates a numpy array of empty pets.
        self.battlefield = np.array([Pet(pets['none'], 0) for _ in range(BOARD_SIZE**2)]).reshape((BOARD_SIZE, BOARD_SIZE))

    def count_empty_spaces(self):
        return BOARD_SIZE**2 - np.count_nonzero(self.board)

    def update_empty_spaces(self):
        self.remaining_empty_spaces = self.count_empty_spaces()

    def valid_move_check(self, i, j):
        if self.board[i][j] == 0:
            return True
        else:
            return False
    
    def make_choice(self, player, pos):
        i = pos[0]
        j = pos[1]
        if (player == 1 and self.valid_move_check(i,j)):
            self.board[i][j] = 1
            self.p1_choices[i][j] = 1
            self.update_empty_spaces()
        elif (player == 2 and self.valid_move_check(i,j)):
            self.board[i][j] = 2
            self.p2_choices[i][j] = 1
            self.update_empty_spaces()
        else:
            print("Invalid Move.")
    
    def make_random_move(self, player):
        i = randint(0, BOARD_SIZE-1)
        j = randint(0, BOARD_SIZE-1)
        self.make_choice(player, [i,j])
    
    def make_guided_random_move(self, player):
        empty_spaces = np.where(self.board == 0)
        list_of_coordinates = list(zip(empty_spaces[0], empty_spaces[1]))
        size_list_of_coordinates = len(list_of_coordinates)
        random_guess = randint(0, size_list_of_coordinates-1)
        choice = list_of_coordinates[random_guess]
        self.make_choice(player, choice)
    
    def check_win_choices(self, choices):
        vertical_sum = choices.sum(axis=0)
        horizontal_sum = choices.sum(axis=1)
        diagonal_sum = choices.diagonal().sum()
        antidiagonal_sum = np.fliplr(choices).diagonal().sum()
        
        if BOARD_SIZE in vertical_sum:
            return True
        elif BOARD_SIZE in horizontal_sum:
            return True
        elif diagonal_sum == BOARD_SIZE:
            return True
        elif antidiagonal_sum == BOARD_SIZE:
            return True
        else:
            return False 

    def check_win(self):
        if tictac.check_win_choices(tictac.p1_choices):
            sys.exit("Player 1 wins.")
        elif tictac.check_win_choices(tictac.p2_choices):
            sys.exit("Player 2 wins.")
        elif tictac.check_draw():
            sys.exit("It's a draw.")
        else:
            print("No one wins, continue.")
    
    def check_draw(self):
        if self.remaining_empty_spaces <= 0:
            return True
        else:
            return False

    def print_board(self):
        print(self.board)

    #A game starts with a Draw -> Summon -> Battle
    # Game loop: P1 Draw -> P1 Summon -> Battle -> P2 Draw -> P2 Summon -> Battle
    def main():
        #while (win condition):

        pass

    def draw_phase():
        pass

    def summon_phase():
        pass

    def battle_phase():
        pass

class Pet():
    def __init__(self, pet: dict, player: int):
        self.owner = player
        self.name = pet['name']
        self.icon = pet['icon']
        self.total_hp = pet['hp']
        self.res_cost = pet['res']
        self.ability = pet['ability']
        self.attack_damage = pet['attack_damage']
        self.attack_pattern = pet['attack_pattern']

        self.current_hp = self.total_hp
        self.poisoned = False
        self.imune = False

    @property
    def is_alive(self):
        if self.current_hp <= 0:
            return False
        else:
            return True

    @property
    def is_hurt(self):
        if self.current_hp < self.total_hp:
            return True
        else:
            return False
    
    def __repr__(self):
        #set output of print
        return repr(f'P{self.owner} {self.name} [{self.current_hp}]')
    
    def take_damage(self, damage):
        self.current_hp -= damage
        print(f'{self.name} took {damage} point of damage.')
        self.check_alive()

class Empty(Pet):
    def __init__(self):
        super().__init__()
        self.attack_damage = 0
        self.attack_pattern = [[False, False, False], [False, False, False], [False, False, False]]

class Panda(Pet):
    def __init__(self):
        super().__init__()
        self.attack_damage = 1
        self.attack_pattern = [[False, True, False], [True, False, True], [False, True, False]]

class Player():
    def __init__(self, board_size, name):
        self.user = name
        self.choices = np.zeros((board_size, board_size))
        self.hand = []
    
    def draw_hand():
        pass
    
if __name__ == "__main__":
    tictac = Game()
    tictac.print_board()

    for _ in range(15):
        tictac.make_guided_random_move(1)
        tictac.print_board()
        print(tictac.battlefield)
        tictac.check_win()
        tictac.make_guided_random_move(2)
        tictac.print_board()
        tictac.check_win()
