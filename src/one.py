import pygame as pg
import numpy as np
from scipy.integrate import solve_ivp, odeint
import matplotlib.pyplot as plt
g = 9.81
l1 = 0.4


def step(t, r):
    omega, theta = r
    return np.array([-g / l1 * np.sin(theta), omega])


def translateAngleToKartesian(phi):
    x, y = WIDTH / 2, HEIGHT / 2
    x1 = np.sin(phi[1]) + x
    y1 = np.cos(phi[0]) + y
    return (x, y), (x1, y1)


# This module is to numerically simulate a pendulum.
# The physical background is that:
# F = m * a,
WIDTH, HEIGHT = 1200, 1200


if __name__ == "__main__":
    # pg.init()
    # screen = pg.display.set_mode((WIDTH, HEIGHT))
    # clock = pg.time.Clock()
    running = True

    # calculate
    time = np.linspace(0, 30, 10000)
    init_r = [0, np.radians(179)]

    solution = odeint(step, init_r, time, tfirst=True)
    print(solution.shape)
    plt.figure()
    plt.plot(time, solution.T[1])
    plt.show()

 #   while running:
 #       for event in pg.event.get():
 #           if event.type == pg.QUIT:
 #               running = False

 #       phi1 = solve_ivp(step, (0.0, 0.1), phi1)

 #       start, end = translateAngleToKartesian(phi1)
 #       pg.draw.line(screen, pg.color.g, start, end, width=3)
 #       screen.fill("black")
 #       pg.display.flip()

# pg.quit()
