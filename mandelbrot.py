import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
from numba import jit


@jit 
def mandelbrot( xmin,
                xmax,
                width,
                ymin,
                ymax,
                height,
                max_iterations = 256
                ):
    def check_mandelbrot(c, max_iterations):
        z = c
        for i in range(max_iterations):
            if abs(z) > 2:
                return i
            z = z*z + c
        return 0

    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    mandolin = np.empty((height, width))
    for m in range(len(x)):
        for n in range(len(y)):
            mandolin[n][m] = check_mandelbrot((x[m] + 1j*y[n]), max_iterations)
    return mandolin

@jit
def mandelbrot_center(  center_x = -0.5,
                        center_y = 0,
                        zoom = 1,
                        width = 6,
                        height = 6,
                        dpi = 227,
                        max_iterations = 256
                        ):

    def check_mandelbrot(c, max_iterations):
            z = c
            for i in range(max_iterations):
                if abs(z) > 2:
                    return i
                z = z*z + c
            return 0

    xmin = center_x - 1.5/zoom
    xmax = center_x + 1.5/zoom
    ymin = center_y - 1.5/zoom
    ymax = center_y + 1.5/zoom

    x = np.linspace(xmin, xmax, width * dpi)
    y = np.linspace(ymin, ymax, height * dpi)
    mandolin = np.empty((height * dpi, width * dpi))

    for m in range(len(x)):
        if m % 100 == 0:
            print(m)
        for n in range(len(y)):
            mandolin[n][m] = check_mandelbrot((x[m] + 1j*y[n]), max_iterations)
    return mandolin

@jit
def julia(xmin, xmax, width, ymin, ymax, height, c, max_iterations):

    def check_julia(z, c, max_iterations):
        for i in range(max_iterations):
            if abs(z) > 2:
                return i
            z = z*z + c

    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    jules = np.empty((height, width))
    for m in range(len(x)):
        for n in range(len(y)):
            jules[n][m] = check_julia((x[m] + 1j*y[n]), c, max_iterations)
    return jules




# jules = julia(-1.2, 1.2, 1600, -1.2, 1.2, 1600, (0.28 + 0.008j), 1024)
# mandolin = mandelbrot(-2, 1, 1600, -1.5, 1.5, 1600, 2048)

mandolin = mandelbrot_center(center_x = 0.28, center_y = 0.008, zoom = 256, width=50, height=50, max_iterations=1024)

np.savetxt("mandolin_rlly_big", mandolin)

length = len(mandolin)
halfsies = length//2
quarters = length//4
image_top = Image.fromarray(mandolin[0:halfsies])
image_bot = Image.fromarray(mandolin[halfsies:])

# image1 = Image.fromarray(mandolin[0:quarters])
# image2 = Image.fromarray(mandolin[quarters:2*quarters])
# image3 = Image.fromarray(mandolin[2*quarters:3*quarters])
# image4 = Image.fromarray(mandolin[3*quarters:])

# quartered = Image.new("F", (length, length))
# quartered.paste(image1, (0,0))
# quartered.paste(image2, (0, quarters))
# quartered.paste(image3, (0, 2*quarters))
# quartered.paste(image4, (0, 3*quarters))
# quartered.show()

stitched = Image.new("F", (length, length))
stitched.paste(image_top, (0,0))
stitched.paste(image_bot, (0, halfsies))
stitched.show()
