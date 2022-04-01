import numpy
from scipy import stats 

speed = [80, 70, 50 ,30, 30, 50, 50, 50]
x = numpy.mean(speed)
y = numpy.median(speed)
z = stats.mode(speed)
a = numpy.std(speed)
b = numpy.var(speed)
c = numpy.percentile(speed, 75)

print (x)
print (y)
print (z)
print (a)
print(b)
print(c)