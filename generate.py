import pyrosim.pyrosim as pyrosim

def CreateWorld():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[3, 2, 0.5] , size=[1, 1, 1])
    pyrosim.End()

def CreateRobot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5] , size=[1, 1, 1])
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.5,0,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5] , size=[1, 1, 1])
    
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-.5,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5] , size=[1, 1, 1])
    pyrosim.End()

CreateWorld()
CreateRobot()
# pyrosim.Start_SDF("world.sdf")
# length = 1
# width = 1
# height = 1

# x = 0
# y = 0
# z = .5

# a = 0
# b = 0
# c = .5

# # for i in range (5):
# #     for j in range (5):
# #         for k in range(10):
# #             pyrosim.Send_Cube(name="Box", pos=[i, j, c + k] , size=[length * ((.9) ** k), width * ((.9) ** k), height * ((.9) ** k)])

# pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])
# #pyrosim.Send_Cube(name="Box2", pos=[a, b, c] , size=[length, width, height])
# pyrosim.End()