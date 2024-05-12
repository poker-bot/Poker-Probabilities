# poker_simulator.py
# Aidan Nachi
# 2024.5.12
# 
# This File defines a get_data function that gets data from a 
# Monte Carlo Simulation of Poker games. The specific data that
# is returned is different pocket hand combinations, whether they're
# suited, connected, or a pair, and win percentages with different numers
# of other players playing they're hand (1-8). Monte Carlo methods, or Monte
# Carlo experiments, are a broad class of computational algorithms that rely on
# repeated random sampling to obtain numerical results. The underlying concept
# is to use randomness to solve problems that might be deterministic in principle.
# In this program randomness is used in different cards on the board and different opponent
# hands for each hand combination that is simulated to give us data on the win percentages of 
# different pocket hands. 


from poker_monte_carlo import Poker_monte_carlo


def get_data():
    """ Get data from a Monte Carlo Simulation for pocket hands in poker. """

    simulation = Poker_monte_carlo()
    simulation.pocket_hand_analysis()


def main():
    """ Demonstrate get_data functionality. """

    get_data()


if __name__ == '__main__':
    main()

