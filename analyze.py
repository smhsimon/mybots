import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
targetAngles = numpy.load("data/targetAngles.npy")

# matplotlib.pyplot.plot(backLegSensorValues, label = 'back', linewidth = .5)
# matplotlib.pyplot.plot(frontLegSensorValues, label = 'front')
# matplotlib.pyplot.legend()
matplotlib.pyplot.plot(targetAngles)
matplotlib.pyplot.show()


