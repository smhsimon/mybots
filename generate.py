import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
length = 1
width = 1
height = 1

x = 0
y = 0
z = .5

a = 0
b = 0
c = .5

for i in range (5):
    for j in range (5):
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[i, j, c + k] , size=[length * ((.9) ** k), width * ((.9) ** k), height * ((.9) ** k)])

#pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])
#pyrosim.Send_Cube(name="Box2", pos=[a, b, c] , size=[length, width, height])
pyrosim.End()