#numpy for 3d array

from search import *

class RubiksCube(StateSpace):
#           top
#        +-------+
#        | 1   2 |
#        | 3   4 |
# +------+-------+-------+-------+
# | 5  6 | 9  10 | 13 14 | 17 18 |
# | 7  8 | 11 12 | 15 16 | 19 20 |
# +------+-------+-------+-------+
#        | 21 22 |
#        | 23 24 |
#        +-------+
#          bottom

    def __init__(self, action, gval, parent, currCube, goalCube, cubies, goal_cubies, moves):
        StateSpace.__init__(self, action, gval, parent)
        self.currCube = currCube
        self.goalCube = goalCube
        self.goal_cubies = goal_cubies
        self.cubies = cubies
        self.gval = gval
        self.moves = moves # list of moves made to reach this point

    def successors(self):
        successors = []
        transition_cost = 1
        for rotation in (RIGHT,FRONT,UP):
            new_cube = rotation.rotate(self.currCube)
            new_cubies = self.update_cubies(new_cube, self.cubies)
            new_moves = self.moves + (rotation.name,)
            new_state = RubiksCube(action=rotation.name, gval=self.gval + transition_cost, parent=self, currCube=new_cube, goalCube=self.goalCube, cubies=new_cubies, goal_cubies=self.goal_cubies, moves=new_moves)
            successors.append(new_state)
        return successors

    def update_cubies(self, cube, cubies):
        copy_cubies = cubies
        copy_cubies.update({(0,1,-1) : (cube[1], cube[5], cube[18])})
        copy_cubies.update({(1, 1, 1) : (cube[2], cube[14], cube[17])})
        copy_cubies.update({(0, 1, 0) : (cube[3], cube[6], cube[9])})
        copy_cubies.update({(1, 1, 0) : (cube[4], cube[10], cube[13])})
        copy_cubies.update({(0, 0, 0) : (cube[21], cube[11], cube[8])})
        copy_cubies.update({(1, 0, 0) : (cube[22], cube[12], cube[15])})
        copy_cubies.update({(0, 0, -1) : (cube[23], cube[7], cube[20])})
        copy_cubies.update({(1, 0, -1) : (cube[24], cube[16], cube[19])})
        return copy_cubies

    def hashable_state(self):
        return frozenset(self.currCube.items())

    def state_string(self):
        return (str(self.moves)+ "\n  "+self.currCube[1]+self.currCube[2]+"\n  "+
            self.currCube[3]+self.currCube[4]+"\n"+
            self.currCube[5]+self.currCube[6]+self.currCube[9]+self.currCube[10]+self.currCube[13]+
            self.currCube[14]+self.currCube[17]+self.currCube[18]+"\n"+self.currCube[7]+
            self.currCube[8]+self.currCube[11]+self.currCube[12]+self.currCube[15]+self.currCube[16]+
            self.currCube[19]+self.currCube[20]+"\n  "+self.currCube[21]+self.currCube[22]+"\n  "+
            self.currCube[23]+self.currCube[24])

    def print_state(self):
        print("ACTION was "+ self.action)
        print(self.state_string())

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

    '''
    Assuming python dictionaries compare dicts both vals and keys this way, as stated on Stack overflow
    '''
def rubiks_goal_state(state):

    for key in state.goalCube:
        if state.goalCube[key] != state.currCube[key]:
            return False
    return True

class Rotation():

    def __init__(self, name, cycle, numOfQuarterTurns=1):
        self.name = name
        self.cycle = cycle
        self.numOfQuarterTurns = numOfQuarterTurns

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return self.__str__()
    '''
    @return dictionary representation of cube
    '''
    def rotate(self, cube):
        shift = 3
        if(self.numOfQuarterTurns==2):
            shift = 6
        temp = {}
        temp_cube = cube.copy()
        #hold the vals
        for i in self.cycle:
            temp[i] = cube[i]

        for i in range(len(self.cycle)):
            temp_cube[self.cycle[(i+shift)%len(self.cycle)]] = temp[self.cycle[i]]
        return temp_cube


# rotations all use the concept of cycle permutation, eg of part of an L cycle(5,6,8,7)
R = [13,10,12,14,2,4,16,19,17,15,22,24]
U = [1,9,10,2,5,6,4,17,18,3,13,14]
F = [9,3,4,10,13,15,12,22,21,11,8,6]


RIGHT = Rotation("R",R)
UP = Rotation("U", U)
FRONT = Rotation("F",F)


