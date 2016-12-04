__author__ = 'Vili Volcini'

#library for complex numbers
import cmath
import numpy
import math



#Discrete Fourier Transform (slow version)
class DFT_Transform:

    def __init__(self, samplesSize):
        self.samplesSize = samplesSize

    def Transform(self, vector):

        if len(vector) != self.samplesSize:
            raise Exception("vector size is not equal to sampleSize defined in DFT_Transform")

        N = len(vector)

        self.result = []

        for k in range(0, N):

            sum = 0

            for n, val in enumerate(vector):

                sum += cmath.exp(-2 * 1j * math.pi * n * (k /N))


                pass

            #this sum is from dot product
            self.result += [sum]

        return self.result


#NOT SURE HOW GOOD IT WORKS
simpleSin = [math.sin(1.52*x) for x in range(0, 64)]

print(simpleSin)

t = DFT_Transform(64)

r = t.Transform(simpleSin)

print(r)