import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as img

def check_mandelbrot(c, max_iterations):
    z = c
    for i in range(max_iterations):
        if abs(z) > 2:
            return i
        z = z*z + c
    return 0

def check_julia(z, c, max_iterations):
    for i in range(max_iterations):
        if abs(z) > 20:
            return i
        z = z*z + c

def mandelbrot(xmin, xmax, width, ymin, ymax, height, max_iterations):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    mandolin = np.empty((height, width))
    for m in range(len(x)):
        for n in range(len(y)):
            mandolin[n][m] = check_mandelbrot((x[m] + 1j*y[n]), max_iterations)
    return mandolin

def julia(xmin, xmax, width, ymin, ymax, height, c, max_iterations):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    jules = np.empty((height, width))
    for m in range(len(x)):
        for n in range(len(y)):
            jules[n][m] = check_julia((x[m] + 1j*y[n]), c, max_iterations)
    return jules

mandolin = mandelbrot(-2.1, 1.1, 2560, -1, 1, 1600, 256)

#mandolin = mandelbrot(-1.8, -1.7, 75, -0.025, 0.025, 150, 64)

#jules = julia(-2, 2, 100, -2, 2, 200, (-0.52 + 0.57j), 256)

#mandolin = mandelbrot(-2, 2, 800, -2, 2, 800, 256)
#plt.imshow(mandolin, cmap='hot', interpolation='Gaussian')
np.savetxt('mandolin_2560x1600.txt', mandolin)
set_image = img.fromarray(mandolin)
set_image.show()
#plt.show()
    