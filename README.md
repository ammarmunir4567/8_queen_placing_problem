8 Queen Puzzle Solver Using Genetic Algorithm
This project aims to solve the 8 Queen Puzzle using the genetic algorithm. The 8 Queen Puzzle is a classic problem in which eight queens are placed on an 8x8 chessboard in such a way that no two queens threaten each other. In other words, no two queens should be placed on the same row, column, or diagonal.

Requirements
Python 3
NumPy
How to Use
Clone the repository or download the source code.
Install the required packages (NumPy) using the command: pip install numpy.
Run the main.py file.
Implementation
The program starts by randomly initializing the placement of the queens on the chessboard. The positions of the queens are represented as an array of length 8, where each element represents the position of the queen in the corresponding row.

The fitness() function calculates the fitness score of a given placement of queens. It counts the number of non-attacking queen pairs and returns the difference between the total number of pairs and the number of non-attacking pairs.

The select_parent() function selects two parents from the population using the roulette wheel selection method. The probability of selecting an individual for reproduction is proportional to its fitness score.

The cross_over() function performs a crossover operation between two parents to produce two offspring. The crossover point is chosen randomly, and the elements after the crossover point are swapped between the two parents.

The mutation() function randomly changes the position of a queen in a placement with a certain probability.

The working() function loops through the population, calculating the fitness scores and storing them. It selects two parents, performs crossover and mutation operations, and adds the resulting offspring to the population. If a placement with a fitness score of 28 (i.e., a solution) is found, the function returns the placement and terminates.

The main() function initializes the population with four random placements and runs the working() function for a fixed number of generations (10 in this case). If a solution is found, the program terminates, and the solution is printed. Otherwise, the placement with the highest fitness score is printed as the best placement found.

References
Goldberg, D. E. (1989). Genetic Algorithms in Search, Optimization, and Machine Learning. Addison-Wesley.
