from search import *
from cube import *
import math
import copy
from test_problems import PROBLEMS, createGoalCube, createCubies


def manhattan_dist(state):

    distance = 0
    max_dist = 0
    goal = state.goalCube
    coordinates = [(0, 1, -1), (1, 1, 1), (0, 1, 0), (1, 1, 0), (0, 0, 0), (1, 0, 0), (0, 0, -1), (1, 0, -1)]

    for i in coordinates:
        for j in coordinates:
            #if cubie is in the goal state return 0
            if(state.goal_cubies[i] == state.cubies[j]):
                goal_x = i[0]
                goal_y = i[1]
                goal_z = i[2]
                cur_x = j[0]
                cur_y = j[1]
                cur_z = j[2]

                distance = abs(goal_x - cur_x) + abs(goal_y - cur_y) + abs(goal_z - cur_z)

                max_dist += distance
                break

    return float(max_dist*0.25)

def fval_function(sN, weight):
#IMPLEMENT
    """
    Provide a custom formula for f-value computation for Anytime Weighted A star.
    Returns the fval of the state contained in the sNode.

    @param sNode sN: A search node (containing a SnowballState)
    @param float weight: Weight given by Anytime Weighted A star
    @rtype: float
    """

    #Many searches will explore nodes (or states) that are ordered by their f-value.
    #For UCS, the fvalue is the same as the gval of the state. For best-first search, the fvalue is the hval of the state.
    #You can use this function to create an alternate f-value for states; this must be a function of the state and the weight.
    #The function must return a numeric f-value.
    #The value will determine your state's position on the Frontier list during a 'custom' search.
    #You must initialize your search engine object as a 'custom' search engine if you supply a custom fval function.

    value = 0
    value += sN.gval + (weight * sN.hval)
    return value

def anytime_weighted_astar(initial_state, heur_fn, weight=1., timebound = 10):
#IMPLEMENT
    '''Provides an implementation of anytime weighted a-star, as described in the HW1 handout'''
    '''INPUT: a snowball state that represents the start state and a timebound (number of seconds)'''
    '''OUTPUT: A goal state (if a goal is found), else False'''
    time = os.times()[0]
    endTime = timebound + os.times()[0]


    wrapped_fval_function = (lambda sN : fval_function(sN, weight))
    se = SearchEngine('custom','full')
    se.init_search(initial_state, rubiks_goal_state, heur_fn, wrapped_fval_function)

    costbound = (float('inf'), float('inf'), float('inf'))
    result = se.search(timebound, costbound)
    bestResult = result

    while time < endTime :
        if(result == False):
            return bestResult
        if (costbound[0] > se.cost):
            bestResult = result
            costbound = (se.cost,se.cost,se.cost)
        time = os.times()[0]
        new_timebound = endTime - time
        result = se.search(new_timebound, costbound)


    return result



if __name__ == "__main__":
    ida_star = False
    moves = ()
    print("[Welcome to the rubiks solver]")

    sc = input("Would you like to enter your own cube? [y/q] (entering anything else will run premade test cases)")

    while sc!='q':
        if sc=='y':
            print("""
                     top
                     blue
                   +-------+
                   | 1   2 |
             white | 3   4 | yellow  orange
            +------+-------+-------+-------+
            | 5  6 | 9  10 | 13 14 | 17 18 |
            | 7  8 | 11 12 | 15 16 | 19 20 |
            +------+-------+-------+-------+
                   | 21 22 |
                   | 23 24 |
                   +-------+
                    bottom 
                     green

    When entering the colour string orient the cube 
    so that the side with the ***most red pieces*** is in the middle 
    facing towards you.

                    """)
            sc = input("Please enter cube string of length 24 eg bobowwwwrbrbyyyygogogrgr or byygwgwborrywbbyrogowogr [string/q]:")
            while len(sc)!=24:
                if(sc=='q'):
                    break
                sc = input("Please enter cube string of length 24 [string/q]: ")
                if(len(sc)==24):
                    break
            if(sc=='q'):
                continue
            input_cube = {}
            goal_cube = {}
            cubeInput = list(sc)
            #cube is not 0 indexed
            for i in range(len(cubeInput)):
                input_cube[i+1] = cubeInput[i]

            goal_cube = createGoalCube(goal_cube)
            goal_cubies = createCubies(goal_cube)

            input_cubies = createCubies(input_cube)


            s0 = (RubiksCube("START", 0, None, input_cube, goal_cube, input_cubies, goal_cubies, moves),)

        else:
            ida_star = True
            s0 = PROBLEMS

        solved = 0; unsolved = []; counter = 0; percent = 0; timebound = 2; #2 second time limit for each problem

        print("*************************************")
        print("Running IDA-star")

        for i in range(len(s0)): #note that there are 20 problems in the set that has been provided.  We just run through 10 here for illustration.

            print("*************************************")
            print("PROBLEM {}".format(i))

            se = SearchEngine('astar', 'full')
            se.init_search(s0[i], goal_fn=rubiks_goal_state, heur_fn=manhattan_dist)
            #final = se.search(timebound=120)
            #final = iterative_deepening_astar(s0, heur_fn=manhattan_dist, max_depth=13)
            #final = se.iterative_deepening_astar(s0, goal_cube=rubiks_goal_state, depth=13, heur_fn=manhattan_dist)
            #final = anytime_weighted_astar(s0, heur_fn=manhattan_dist, weight=1, timebound=14)
            final = se.iterative_deepening_astar(max_depth=42)
            if final:
                final.print_path()
                finalSolution = ""
                solution = list(final.moves)
                i = 0
                # converting (FFF) to F' and FF to F2
                while i < len(solution):
                    count = 0;
                    for j in range(i+1,len(solution)):
                        if(j>i+2):
                            break
                        if(solution[i] == solution[j]):
                            count+=1
                        else:
                            break
                    if count == 2:
                        count+=1
                        finalSolution+= solution[i]+"' "
                    elif count == 1 :
                        finalSolution+= solution[i]+"2 "
                        count+=1
                    else:
                        finalSolution+= solution[i]+" "
                        count+=1
                    i+=(count)
                print("Final Solution: ", finalSolution)
                solved += 1
            else:
                unsolved.append(i)
            counter += 1

        if counter > 0:
            percent = (solved/counter)*100

        print("*************************************")
        print("{} of {} problems ({} %) solved.".format(solved, counter, percent, timebound))
        print("Problems that remain unsolved in the set are Problems: {}".format(unsolved))
        print("*************************************")
        sc = input("Would you like to enter your own cube? [y/q] (entering anything else will run premade test cases)")
