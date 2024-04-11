import matplotlib.pyplot as plt
from mpmath import *
from colorsys import hsv_to_rgb
# % matplotlib
# inline

# This script is a bit heavy and takes a while to run

pi = 3.1415926535898


def PerFract(x, t, m, M):
    x = x / t
    return m + (M - m) * (x - floor(x))


def color_clines(fz):  # this is the color function that replaces the
    # default  color function implemented in mpmath.cplot
    if isinf(fz):
        return 0, 0, 1.0  # hsv code
    if isnan(fz):
        return 0., 0., 0.5

    n = 15  # n is the number of rays drawn in a cycle

    h = (float(arg(fz)) + pi) / (2 * pi)  # hue
    h = (h - 0.5) % 1.0

    Phc = PerFract(h, 1.0 / n, 0.6, 1)  # set brightness between 0.6 and 1,
    # in order to avoid too dark colors
    modul = fabs(fz)
    Logm = log(modul)
    s = 0.9  # saturation

    Modc = PerFract(Logm, 2 * pi / n, 0.6, 1)
    v = Modc * Phc

    return hsv_to_rgb(h, s, v)


plt.rcParams['figure.figsize'] = 7, 11
cplot(zeta, re=[-6, 6], im=[-20, 20], color=color_clines, verbose=False, points=200000,
      file='19_Zeta_Bonus3_Riemann-Zeta-Func.png')
