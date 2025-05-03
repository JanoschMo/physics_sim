import pygame as pg
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
g = 9.81
l1 = 0.4
m = 1

red = pg.Color((51, 204, 51))
green = pg.Color((0, 0, 255))


def step(t, r):
    x1, x2 = r
    return np.array([x2, -(g/l1) * np.sin(x1)])


def translateAngleToKartesian(phi):
    x, y = WIDTH / 2, HEIGHT / 2
    x1 = np.sin(phi[0])*l1*1000 + x
    y1 = np.cos(phi[0])*l1*1000 + y
    return (x, y), (x1, y1)


# This module is to numerically simulate a pendulum.
# The physical background is that:
# F = m * a,
WIDTH, HEIGHT = 1200, 1200


if __name__ == "__main__":

    # calculate
    time = np.arange(0, 120, 1/100)
    init_r = [np.radians(179), 0]
    solution = odeint(step, init_r, time, tfirst=True)

    # plot position in time domain
    # plt.figure()
    # plt.plot(time, solution.T[0])
    # plt.show()

    # calc energy over time
    E_pot = (l1 - np.cos(solution.T[0]) * l1) * m * g
    E_kin = np.square(solution.T[1] * l1) * 1/2 * m
    E = E_pot + E_kin
    print("Energy : {:.3e} +- {:.3e}, max {:.3e}, min {:.3e}".format(
        np.mean(E), np.std(E), np.max(E), np.min(E)))
    # plt.figure()
    # plt.plot(time, E, time, E_pot, time, E_kin)
    # plt.show()

    # render the scene
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    for sol in solution:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        start, end = translateAngleToKartesian(sol)
        screen.fill("black")
        pg.draw.line(screen, red, start, end, width=3)
        pg.draw.circle(screen, green, (WIDTH / 2, HEIGHT / 2), 10)
        pg.draw.circle(screen, green, end, 10)
        pg.display.flip()
        clock.tick(100)
