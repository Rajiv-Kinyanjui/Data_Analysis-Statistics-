# import numpy
# from scipy import stats 

# speed = [80, 70, 50 ,30, 30, 50, 50, 50]
# x = numpy.mean(speed)
# y = numpy.median(speed)
# z = stats.mode(speed)
# a = numpy.std(speed)
# b = numpy.var(speed)
# c = numpy.percentile(speed, 75)

# print (x)
# print (y)
# print (z)
# print (a)
# print(b)
# print(c)

# import numpy
# import matplotlib.pyplot as plt

# x = numpy.random.normal(5,1, 1000)
# y = numpy.random.normal(10,2, 1000)

# #print (x)
# plt.scatter(x,y)
# plt.show()

from scipy import stats
import matplotlib.pyplot as plt

x = [5,7,8,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,11,86,103,87,94,78,77,85]

# plt.scatter(x,y)
# plt.show()
slope, intercept, r, p, std_err = stats.linregress(x,y)
print(r)
# print(slope)
def myfunc(x):
    return slope*x+intercept

model = list(map(myfunc,x))
plt.scatter(x,y)
plt.plot(x,model)
plt.show()
