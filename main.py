# program to solve 8 queen puzzle using genetic algorithm
import random
import numpy as np

QUEEN = 8
lis=[]
fit=[]
#initializeing with random placing of queens
def init_board():
    arr = []
    for i in range(QUEEN):
        arr.append(random.randrange(1, 9))
    return arr


# this function will make 2D array of queen placed there , at place of queen we have placed '1'
def makeBoard(arr):
    matrix = np.zeros((8, 8))
    for i in range(QUEEN):
        matrix[-arr[i]][i] = 1
    return matrix



# def fitness(arr):
#     n = len(arr)
#     non_attacking = 0
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] == 1:
#                 for k in range(i+1, n):
#                     if arr[k][j] == 1: # Check column
#                         non_attacking += 1
#                         break
#                 for k in range(j+1, n):
#                     if arr[i][k] == 1: # Check row
#                         non_attacking += 1
#                         break
#                 for k in range(1, min(n-i, n-j)):
#                     if arr[i+k][j+k] == 1: # Check diagonal
#                         non_attacking += 1
#                         break
#                 for k in range(1, min(n-i, j+1)):
#                     if arr[i+k][j-k] == 1: # Check diagonal
#                         non_attacking += 1
#                         break
#     return n*(n-1)//2 - non_attacking
#



def fitness(arr):
    n = len(arr)
    non_attacking = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j] or abs(arr[i] - arr[j]) == j - i:
                non_attacking += 1
    return n * (n - 1) // 2 - non_attacking


# roulette wheel for selecting parents
def select_parent(population):
    total_fitness = sum([fitness(individual) for individual in population])

    r = random.uniform(0, total_fitness)
    current_fitness = 0
    for individual in population:
        current_fitness += fitness(individual)
        if current_fitness > r:
            return individual



#cross over function
def cross_over(arr):
    r1 = random.randint(1, 7)

    while r1 < len(arr[0]):
        arr[0][r1], arr[1][r1] = arr[1][r1], arr[0][r1]
        r1 = r1 + 1

    r = random.randint(1, 7)

    while r < len(arr[2]):
        arr[2][r], arr[3][r] = arr[3][r], arr[2][r]
        r = r + 1


    return arr


def mutation(arr):
    for i in range(4):
        arr[i][random.randint(1,7)]=random.randint(1,8)


    return arr

#the function in which we loop around mutation , crossover and rest of functionality
def working(arr_list):

    found=False

    for arr in arr_list:

        x=fitness(arr)
        fit.append(x)
        lis.append(arr)
        print(arr, " Fitness :", x)
        if x==28:
            print("Found ")
            print(arr)
            found=True
            return arr,found


    temp = []
    for i in range(4):
        temp.append(select_parent(arr_list))

    temp = (cross_over(temp))
    temp = (mutation(temp))
    print("\n")
    return temp, found





def main():



    arr1 = init_board()
    arr2 = init_board()
    arr3 = init_board()
    arr4 = init_board()

    print(arr1, '\n')
    matrix = makeBoard(arr1)
    arr_list = [arr1, arr2, arr3, arr4]

    for i in range(10):
        print("The Generation :", i)
        arr_list,check=(working(arr_list))
        if check==True:
            break


    if check==False:
        x=max(fit)
        ind=fit.index(x)
        print("The max fitness is :",x )
        print("The placing is :" ,lis[ind])



main()
