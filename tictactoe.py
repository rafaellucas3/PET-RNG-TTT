import numpy as np
from random import randint
import sys

pets = {
    'none'         : {'name': 'None',     'icon': 'assets/pets/png/none.png',     'hp': 0, 'res': 0, 'ability': ''},
    'koala'        : {'name': 'Koala',    'icon': 'assets/pets/png/koala.png',    'hp': 3, 'res': 2, 'ability': 'Heals one HP in one random space in + direction.'},
    'panda'        : {'name': 'Panda',    'icon': 'assets/pets/png/panda.png',    'hp': 2, 'res': 2, 'ability': 'Deals one damage in + direction.'},
    'tiger'        : {'name': 'Tiger',    'icon': 'assets/pets/png/tiger.png',    'hp': 2, 'res': 2, 'ability': 'Deals one damage in x direction.'},
    'snake'        : {'name': 'Snake',    'icon': 'assets/pets/png/snake.png',    'hp': 1, 'res': 2, 'ability': 'Deals one damage in one random + direction and inflicts poison.'},
    'capybara'     : {'name': 'Capybara', 'icon': 'assets/pets/png/capybara.png', 'hp': 1, 'res': 3, 'ability': 'It is immune for 2 turns.'},
    'bunny'        : {'name': 'Bunny',    'icon': 'assets/pets/png/bunny.png',    'hp': 1, 'res': 1, 'ability': 'No special ability.'},
    'monkey'       : {'name': 'Monkey',   'icon': 'assets/pets/png/monkey.png',   'hp': 2, 'res': 2, 'ability': 'When hurt, moves one space to a random + direction if empty.'},
    'pig'          : {'name': 'Pig',      'icon': 'assets/pets/png/pig.png',      'hp': 2, 'res': 1, 'ability': 'No special ability.'},
    'leo'          : {'name': 'Leo',      'icon': 'assets/pets/png/leo.png',      'hp': 3, 'res': 3, 'ability': 'Deals one damage in all directions.'},
}

class Game():
    def __init__(self):
        self.board_size = 3
        self.board = np.zeros((self.board_size, self.board_size))
        self.p1_choices = np.zeros((self.board_size, self.board_size))
        self.p2_choices = np.zeros((self.board_size, self.board_size))

        self.remaining_empty_spaces = self.count_empty_spaces()
        #Generates a numpy array of empty pets.
        self.battlefield = np.array([Pet(pets['none'], 0) for _ in range(self.board_size**2)]).reshape((self.board_size,self.board_size))

    def count_empty_spaces(self):
        return self.board.size - np.count_nonzero(self.board)

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
        i = randint(0, self.board_size-1)
        j = randint(0, self.board_size-1)
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
        
        if self.board_size in vertical_sum:
            return True
        elif self.board_size in horizontal_sum:
            return True
        elif diagonal_sum == self.board_size:
            return True
        elif antidiagonal_sum == self.board_size:
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

class Pet():
    def __init__(self, pet: dict, player: int):
        self.name = pet['name']
        self.icon = pet['icon']
        self.total_hp = pet['hp']
        self.res_cost = pet['res']
        self.ability = pet['ability']
        self.owner = player

        self.current_hp = self.total_hp
        self.poisoned = False
        self.is_alive = True
    
    def __repr__(self):
        #set output of print
        return repr(f'P{self.owner} {self.name} [{self.current_hp}]')
    
    def take_damage(self, damage):
        self.current_hp -= damage
        print(f'{self.name} took {damage} point of damage.')
        self.check_alive()

    def check_alive(self):
        if self.current_hp <= 0:
            self.is_alive = False
        else:
            self.is_alive = True

class Player():
    def __init__(self):
        self.hand = []
    
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
