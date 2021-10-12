import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
from ndb import Universe


# Fixing random state for reproducibility
np.random.seed(random.randint(1, 2 ** 32 - 123))

# Scale constant
SCALE = 1


class Graphics:

    def __init__(self, universe: Universe):

        # Initialize canvas
        self._fig = plt.figure(figsize=(10, 10))
        self._ax = self._fig.add_axes([0, 0, 1, 1], frameon=False)
        self._ax.set_xlim(-20, 20), self._ax.set_xticks([])
        self._ax.set_ylim(-20, 20), self._ax.set_yticks([])

        # Create start dots
        self._universe = universe
        self._dots = np.zeros(len(self._universe.Bodies), dtype=[('position', float, (2,)),
                                                                 ('size',
                                                                  float),
                                                                 ('color',    float, (4,))])
        # Setting dots params
        for i in range(len(self._universe.Bodies)):
            self._dots['size'][i] = self._universe.Bodies[i].Mass * SCALE
            self._dots['color'][i] = np.random.uniform(0, 1, 4)
        self._get_coords_from_universe()

        # Creating scatter
        self._scat = self._ax.scatter(self._dots['position'][:, 0], self._dots['position'][:, 1],
                                      s=self._dots['size'], lw=10, edgecolors=self._dots['color'],
                                      facecolors=self._dots['color'])

    def run(self):
        animation = FuncAnimation(self._fig, self._update, interval=1)
        plt.show()

    def _update(self, i):

        # Printing current state
        print("\nIteration " + str(i) + ":\n\n" + str(self._universe))

        # Updating universe
        self._universe.update()

        # Updating animation
        self._get_coords_from_universe()
        self._scat.set_offsets(self._dots['position'])

    def _get_coords_from_universe(self):
        #temp = np.ndarray((len(self._universe.Bodies), 2), dtype = float)
        for i in range(len(self._universe.Bodies)):
            self._dots['position'][i][0] = self._universe.Bodies[i].Position.Coords[0]
            self._dots['position'][i][1] = self._universe.Bodies[i].Position.Coords[1]
