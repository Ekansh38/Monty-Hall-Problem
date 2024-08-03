import random


class Door:
    def __init__(self):
        self.isOpen = False
        self.has_prize = False
        self.picked = False

    def open(self):
        self.isOpen = True

    def give_prize(self):
        self.has_prize = True


games = 100000
switch_wins = 0
stay_wins = 0
num_doors = 3


for _ in range(games):
    doors = []
    for _ in range(num_doors):
        doors.append(Door())

    prize_door = random.choice(doors)
    prize_door.give_prize()

    first_pick = random.choice(doors)
    first_pick.picked = True

    can_open = []

    for door in doors:
        if not door.picked and not door.has_prize:
            can_open.append(door)

    opened = 0
    for door in can_open:
        if not door.has_prize:
            door.open()
            opened += 1
            if len(doors) - 2 == opened:
                break

    new_pick = random.choice(doors)
    for door in doors:
        if not door.isOpen and not door.picked:
            new_pick = door
            break

    if new_pick.has_prize:
        switch_wins += 1


for _ in range(games):
    doors = []
    for _ in range(num_doors):
        doors.append(Door())

    prize_door = random.choice(doors)
    prize_door.give_prize()

    first_pick = random.choice(doors)
    first_pick.picked = True

    if first_pick.has_prize:
        stay_wins += 1


print("Switch Rate: ", switch_wins / games * 100)
print("Stay Rate: ", stay_wins / games * 100)
