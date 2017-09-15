from cube import *

R = [13,10,12,14,2,4,16,19,17,15,22,24]
U = [1,9,10,2,5,6,4,17,18,3,13,14]
F = [9,3,4,10,13,15,12,22,21,11,8,6]

RIGHT = Rotation("R",R)
UP = Rotation("U", U)
FRONT = Rotation("F",F)

moves = ()
cube = {}
goal_cubies = {}

def createGoalCube(cube):
    #set the cube colour dictionary
    for i in range(1,25):
        if i/4.0 > 5:
            cube[i] = "g"
        elif i/4.0 > 4:
            cube[i] = "o"
        elif i/4.0 > 3:
            cube[i] = "y"
        elif i/4.0 > 2:
            cube[i] = "r"
        elif i/4.0 > 1:
            cube[i] = "w"
        else:
            cube[i] = "b"
    return cube

def createCubies(cube):
    cubies={}
    cubies.update({(0,1,-1):(cube[1], cube[5], cube[18])})
    cubies.update({(1, 1, 1): (cube[2], cube[14], cube[17])})
    cubies.update({(0, 1, 0): (cube[3], cube[6], cube[9])})
    cubies.update({(1, 1, 0) : (cube[4], cube[10], cube[13])})
    cubies.update({(0, 0, 0): (cube[21], cube[11], cube[8])})
    cubies.update({(1, 0, 0): (cube[22], cube[12], cube[15])})
    cubies.update({(0, 0, -1): (cube[23], cube[7], cube[20])})
    cubies.update({(1, 0, -1) : (cube[24], cube[16], cube[19])})
    return cubies

cube = createGoalCube(cube)
goal_cubies = createCubies(cube)
#for 1 rotation
new_cube = cube.copy()#copy.deepcopy(cube)
new_cube = FRONT.rotate(new_cube)
cubies1 = createCubies(new_cube)

#for 2 rotation
cube2 = cube.copy()
cube2 = RIGHT.rotate(cube2)
cube2 = UP.rotate(cube2)
cubies2 = createCubies(cube2)

#for 3 rotations
cube3 = cube.copy()
cube3 = RIGHT.rotate(cube3)
cube3 = UP.rotate(cube3)
cube3 = RIGHT.rotate(cube3)
cubies3 = createCubies(cube3)

#for 4 rotations
cube4 = cube.copy()
cube4 = RIGHT.rotate(cube4)
cube4 = UP.rotate(cube4)
cube4 = FRONT.rotate(cube4)
cube4 = RIGHT.rotate(cube4)
cubies4 = {}
cubies4.update({(0,1,-1) : (cube4[1], cube4[5], cube4[18])})
cubies4.update({(1, 1, 1) : (cube4[2], cube4[14], cube4[17])})
cubies4.update({(0, 1, 0) : (cube4[3], cube4[6], cube4[9])})
cubies4.update({(1, 1, 0) : (cube4[4], cube4[10], cube4[13])})
cubies4.update({(0, 0, 0) : (cube4[21], cube4[11], cube4[8])})
cubies4.update({(1, 0, 0) : (cube4[22], cube4[12], cube4[15])})
cubies4.update({(0, 0, -1) : (cube4[23], cube4[7], cube4[20])})
cubies4.update({(1, 0, -1) : (cube4[24], cube4[16], cube4[19])})

cube6 = cube.copy()
cube6 = RIGHT.rotate(cube6)
cube6 = UP.rotate(cube6)
cube6 = FRONT.rotate(cube6)
cube6 = UP.rotate(cube6)
cube6 = RIGHT.rotate(cube6)
cube6 = RIGHT.rotate(cube6)
cube6 = UP.rotate(cube6)
cube6 = UP.rotate(cube6)

cubies6 = {}
cubies6.update({(0,1,-1) : (cube6[1], cube6[5], cube6[18])})
cubies6.update({(1, 1, 1) : (cube6[2], cube6[14], cube6[17])})
cubies6.update({(0, 1, 0) : (cube6[3], cube6[6], cube6[9])})
cubies6.update({(1, 1, 0) : (cube6[4], cube6[10], cube6[13])})
cubies6.update({(0, 0, 0) : (cube6[21], cube6[11], cube6[8])})
cubies6.update({(1, 0, 0) : (cube6[22], cube6[12], cube6[15])})
cubies6.update({(0, 0, -1) : (cube6[23], cube6[7], cube6[20])})
cubies6.update({(1, 0, -1) : (cube6[24], cube6[16], cube6[19])})

cube7 = cube.copy()
cubeInput = list("bobowwwwrbrbyyyygogogrgr")
for i in range(len(cubeInput)):
    cube7[i+1] = cubeInput[i]
cubies7 = createCubies(cube7)


PROBLEMS = (
    #PROBLEM 1
    RubiksCube("START", 0, None,  new_cube, cube,  cubies1,goal_cubies, moves),
    RubiksCube("START", 0, None,  cube2, cube,  cubies2,goal_cubies, moves),
    RubiksCube("START", 0, None,  cube3, cube,  cubies3,goal_cubies, moves),
    RubiksCube("START", 0, None,  cube4, cube,  cubies4,goal_cubies, moves),
    RubiksCube("START", 0, None,  cube6, cube,  cubies6,goal_cubies, moves),
    RubiksCube("START", 0, None,  cube7, cube,  cubies6,goal_cubies, moves),
)
