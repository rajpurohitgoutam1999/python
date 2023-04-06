import numpy as np

a = np.array([[1, 2],
			[3, 4]])

b = np.array([[5, 6],
			[7, 8]])

# vertical stacking
print("Vertical stacking:\n", np.vstack((a, b)))

# horizontal stacking
print("\nHorizontal stacking:\n", np.hstack((a, b)))

c = [5, 6]

# stacking columns
print("\nColumn stacking:\n", np.column_stack((a, c)))

# concatenation method
print("\nConcatenating to 2nd axis:\n", np.concatenate((a, b), 1))



import numpy as np

a = np.array([[1, 3, 5, 7, 9, 11],
			[2, 4, 6, 8, 10, 12]])

# horizontal splitting
print("Splitting along horizontal axis into 2 parts:\n", np.hsplit(a, 2))

# vertical splitting
print("\nSplitting along vertical axis into 2 parts:\n", np.vsplit(a, 2))



import numpy as np

a = np.array([1.0, 2.0, 3.0])

# Example 1
b = 2.0
print(a * b)

# Example 2
c = [2.0, 2.0, 2.0]
print(a * c)



import numpy as np

a = np.array([0.0, 10.0, 20.0, 30.0])
b = np.array([0.0, 1.0, 2.0])

print(a[:, np.newaxis] + b)

import numpy as np

# creating a date
today = np.datetime64('2017-02-12')
print("Date is:", today)
print("Year is:", np.datetime64(today, 'Y'))

# creating array of dates in a month
dates = np.arange('2017-02', '2017-03', dtype='datetime64[D]')
print("\nDates of February, 2017:\n", dates)
print("Today is February:", today in dates)

# arithmetic operation on dates
dur = np.datetime64('2017-05-22') - np.datetime64('2016-05-22')
print("\nNo. of days:", dur)
print("No. of weeks:", np.timedelta64(dur, 'W'))

# sorting dates
a = np.array(['2017-02-12', '2016-10-13', '2019-05-22'], dtype='datetime64')
print("\nDates in sorted order:", np.sort(a))



import numpy as np

A = np.array([[6, 1, 1],
			[4, -2, 5],
			[2, 8, 7]])

print("Rank of A:", np.linalg.matrix_rank(A))

print("\nTrace of A:", np.trace(A))

print("\nDeterminant of A:", np.linalg.det(A))

print("\nInverse of A:\n", np.linalg.inv(A))

print("\nMatrix A raised to power 3:\n", np.linalg.matrix_power(A, 3))


import numpy as np

# coefficients
a = np.array([[1, 2], [3, 4]])
# constants
b = np.array([8, 18])

print("Solution of linear equations:", np.linalg.solve(a, b))


import numpy as np
import matplotlib.pyplot as plt

# x co-ordinates
x = np.arange(0, 9)
A = np.array([x, np.ones(9)])

# linearly generated sequence
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
# obtaining the parameters of regression line
w = np.linalg.lstsq(A.T, y)[0]

# plotting the line
line = w[0]*x + w[1] # regression line
plt.plot(x, line, 'r-')
plt.plot(x, y, 'o')
plt.show()

