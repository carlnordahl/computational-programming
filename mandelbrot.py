import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision = 2, floatmode='fixed')

def complexmat(N, z0, z1):
    # skapar en N x N-matris med komplexa tal a + bi
    # där re(z0) <= a <= re(z1) och im(z1) <= b <= im(z0)
    # (jämnt fördelade i matrisen)
 
    xs = np.linspace(z0.real, z1.real, num = N)  # realdelar
    ys = np.linspace(z0.imag, z1.imag, num = N)  # imaginärdelar
 
    # skapa två matriser med real- respektive imaginärdelar
    [X, Y] = np.meshgrid(xs, ys)
 
    # matrisen X innehåller resultatets realdelar
    # matrisen Y innehåller resultatets imaginärdelar
 
    return X + Y * 1j    # Vi multiplicerar Y med 1j, då Y är imaginärdelen.

def converge(c):
    # Kollar hur många upprepningar av serien som krävs för att värdet ska
    # divergera. z divergerar om |z| > 2
    iterations = 0

    z0 = c
    
    for k in range(100):
        iterations += 1
        c = c**2 + z0
        if abs(c) > 2:
            break

    return iterations

# Vektoriserad version av converge
vConverge = np.vectorize(converge)

m = complexmat(1000, -2+1j, 1 - 1j)

v = vConverge(m)

plt.imshow(v, aspect = 2/3, cmap = plt.get_cmap('plasma'))
plt.show()
plt.imsave('mandelbrot.png', v)

m1 = complexmat(200, -0.7 + 0.7j, -0.5 + 0.6j)
v1 = vConverge(m1)

plt.imshow(v1, aspect = 1/2, cmap = plt.get_cmap('Spectral'))
plt.show()

m2 = complexmat(200, -1.4 + 0.48j, -1.1 + 0.24j)
v2 = vConverge(m2)

plt.imshow(v2, aspect = 4/5, cmap = plt.get_cmap('cubehelix'))
plt.show()
