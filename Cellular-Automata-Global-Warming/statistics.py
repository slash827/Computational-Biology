from world import update_all, game
from board import BOARD_SIZE
import matplotlib.pyplot as plt

AMOUNT_OF_DAYS = 61


def average_pollution():
    avg_pollution = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            current_cell = game.board.get_cell(i, j)
            avg_pollution += current_cell[3]

    avg_pollution /= BOARD_SIZE ** 2
    return avg_pollution


def average_temperature():
    avg_temperature = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            current_cell = game.board.get_cell(i, j)
            avg_temperature += current_cell[1]

    avg_temperature /= BOARD_SIZE ** 2
    return avg_temperature


def amount_of_ice():
    total_ice = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            current_cell = game.board.get_cell(i, j)
            if current_cell[0] == 1.0:
                total_ice += 1
    return total_ice


def plot_ice_each_day():
    ice_per_generation = []
    for day in range(AMOUNT_OF_DAYS):
        total_ice = amount_of_ice()
        ice_per_generation.append(total_ice)
        update_all()

    plt.scatter(range(AMOUNT_OF_DAYS), ice_per_generation)
    plt.xlabel("Days")
    plt.ylabel("Ice amount")
    plt.title("Ice amount each day")
    plt.show()


def plot_temperature_each_day():
    temp_per_generation = []
    for day in range(AMOUNT_OF_DAYS):
        avg_temp = average_temperature()
        temp_per_generation.append(avg_temp)
        update_all()

    plt.scatter(range(AMOUNT_OF_DAYS), temp_per_generation)
    plt.xlabel("Days")
    plt.ylabel("Average temperature")
    plt.title("Average temperature each day")
    plt.show()


def plot_temperature_pollution():
    temp_per_generation = []
    pollution_per_generation = []
    for day in range(AMOUNT_OF_DAYS):
        avg_temperature = average_temperature()
        temp_per_generation.append(avg_temperature)

        avg_pollution = average_pollution()
        pollution_per_generation.append(avg_pollution)
        update_all()

    plt.scatter(pollution_per_generation, temp_per_generation)
    plt.xlabel("Average pollution")
    plt.ylabel("Average temperature")
    plt.title("Pollution Vs Temperature")
    plt.show()


def plot_ice_pollution():
    ice_per_generation = []
    pollution_per_generation = []
    for day in range(AMOUNT_OF_DAYS):
        total_ice = amount_of_ice()
        ice_per_generation.append(total_ice)

        avg_pollution = average_pollution()
        pollution_per_generation.append(avg_pollution)
        update_all()

    plt.scatter(pollution_per_generation, ice_per_generation)
    plt.xlabel("Average pollution")
    plt.ylabel("Amount of ice")
    plt.title("Pollution Vs Ice")
    plt.show()


def main():
    plot_ice_pollution()


if __name__ == '__main__':
    main()
