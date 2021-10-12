import copy
import math


# Zero constant
ZERO = 0


class Vector:

    def __init__(self, coords: list[float]):
        """Vector constructor.

        Args:
            coords (list): start vector coords.

        """
        # Setting variables
        self._coords = copy.deepcopy(coords)
        self._n = len(self._coords)

        # Calculating module
        temp = 0
        for i in range(self._n):
            temp += (self._coords[i] ** 2)
        self._module = math.sqrt(temp)

    @property
    def Coords(self):
        """Vector read-only property.

        Returns:
            list: Vector coords.

        """
        return self._coords

    @property
    def N(self) -> int:
        """Vector read-only property.

        Returns:
            int: Vector dimension.

        """
        return self._n

    @property
    def Module(self) -> float:
        """Vector read-only property.

        Returns:
            float/double/real/int: vector's module.

        """
        return self._module

    def __add__(self, other):
        """Add override method for Vector type.

        Args:
            other (Vector): Vector to add.

        Returns:
            Vector: operation result.

        """
        # Creating list to store coords sum
        sum_coords = list()

        # Cycle
        for i in range(self._n):
            temp = self._coords[i] + other._coords[i]
            sum_coords.append(temp)

        # Returning result
        return Vector(sum_coords)

    def __sub__(self, other):
        """Sub override method for Vector type.

        Args:
            other (Vector): Vector to subtract.

        Returns:
            Vector: operation result.

        """
        # Creating list to store coords sum
        sub_coords = list()

        # Cycle
        for i in range(self._n):
            temp = self._coords[i] - other._coords[i]
            sub_coords.append(temp)

        # Returning result
        return Vector(sub_coords)

    def __eq__(self, other) -> bool:
        """Equals override method for Vector type.

        Args:
            other (Vector): Vector to compare with.

        Returns:
            bool: Sign of equality.

        """
        if self._coords == other._coords:
            return True
        return False

    def __str__(self) -> str:
        """Str override method for Vector type.

        Returns:
            string: string, represents Vector instance.

        """
        return str("Vector instance at: " + str(id(self)) + "\n" +
                   "    Coords:" + str(self._coords) + "\n" +
                   "    Dimension:" + str(self._n) + "\n" +
                   "    Module:" + str(self._module))

    def multiply_on_scalar(self, k: float):
        """Returns result of multiplying current vector on given number.

        Args:
            k (float/double/int): multiplier.

        Returns:
            Vector: operation result. 

        """
        return Vector([currentCoord * k for currentCoord in self._coords])

    def normalize(self):
        """Normalize vector instance.

        Returns:
            Vector: Vector instance with module 1, which corresponds to self.

        """
        try:
            return self.multiply_on_scalar(1 / self._module)
        except ZeroDivisionError:
            return self  # in case of zero vector return itself


class Body:

    def __init__(self, position: Vector, speed: Vector, mass: float):
        """Body constructor.

        Args:
            position (Vector): represents start body's position.
            speed (Vector): represents start body's speed.
            mass (float/real/double/int): represents body's mass.

        """
        self._position = copy.deepcopy(position)
        self._speed = copy.deepcopy(speed)
        self._mass = mass

    @property
    def Position(self) -> Vector:
        """Body read-only property.

        Returns:
            Vector: Vector instance, represents body's position.

        """
        return self._position

    @property
    def Speed(self) -> Vector:
        """Body read-only property.

        Returns:
            Vector: Vector instance, represents body's speed.

        """
        return self._speed

    @property
    def Mass(self) -> float:
        """Body read-only property.

        Returns:
            double/real/float/int: body's mass.

        """
        return self._mass

    def __str__(self) -> str:
        """Str override method for body type.

        Returns:
            string: string, represents Body instance.

        """
        return str("Body instance at: " + str(id(self)) + "\n" +
                   "-----\nPosition:\n" + str(self._position) +
                   "\n-----\nSpeed:\n" + str(self._speed) +
                   "\n-----\nMass: " + str(self._mass))

    def move_by_force(self, force: Vector, dt: float) -> None:
        """Changes speed and position by applying force during dt

        Args:
            force (Vector): force, applyied to body.
            dt (float/int/real/double): time span, during which force affects body.

        """
        # Changing speed
        self._speed = self._speed + force.multiply_on_scalar(dt / self._mass)

        # Changing position
        self._position = self._position + self._speed.multiply_on_scalar(dt)


class Universe:

    def __init__(self, bodies: list[Body], dt = 1.0, G = 6.67e-11, epsilon = 1e-5):
        """Universe constructor

        Args:
            bodies (list[Body]): list of bodies.
            dt (float): universe tick duration.
            G (float): gravity constant.
            epsilon (float): zero barier value.

        """
        self._bodies = copy.deepcopy(bodies)
        self._dt = dt
        self._G = G
        self._epsilon = epsilon

    @property
    def Bodies(self) -> list[Body]:
        """Universe read-only property.

        Returns:
            list[Body]: bodies in universe.

        """
        return self._bodies

    @property
    def N(self) -> int:
        """Universe read-only property.

        Returns:
            int: universe dimension.

        """
        return self.Bodies[0].Position.N

    @property
    def DT(self) -> float:
        """Universe read-only property.

        Returns:
            float: universe tick duration.

        """        
        return self._dt

    @property
    def G(self) -> float:
        """Universe read-only property.

        Returns:
            float: gravity constant.
        """        
        return self._G

    @property
    def Epsilon(self) -> float:
        """Universe read-only property.

        Returns:
            float: zero barier value.
        """        
        return self._epsilon

    def __str__(self) -> str:
        """Str override method for Universe type.

        Returns:
            string: string, represents Universe instance.

        """
        return ("Universe instance at: " + str(id(self)) + "\ndt: " + str(self._dt) + "; G: " + str(self._G) + "; Epsilon: " + str(self._epsilon) + "\n\n-------------------------c\n\n" +
                "\n\n--------------------------c\n\n".join([str(currentBody) for currentBody in self._bodies]))

    def update(self) -> None:
        """
        Main universe method, runs one existence iteration.
        """
        # Calculating result force for each body
        forces = list()
        for currentBody in self._bodies:
            forces.append(self._calc_result_force_on(currentBody))

        # Moving bodies
        for i in range(len(self._bodies)):
            self._bodies[i].move_by_force(forces[i], self._dt)

    def _calc_result_force_on(self, body: Body) -> Vector:
        """Calculates result force for given body.

        Args:
            body (Body): body to calculate result force for.

        Returns:
            Vector: result force for given body.

        """
        # Creating vector to store result force
        result = Vector([0.0 for i in range(self.N)])

        # Creating copy of bodies list without given body
        newBodies = list(copy.copy(self._bodies))
        for currentBody in newBodies:
            if currentBody.Position == body.Position:
                newBodies.remove(currentBody)
                break

        # Adding forces
        for currentBody in newBodies:
            result += self._calc_force_between(body, currentBody)

        # Returning result
        return result

    def _calc_force_between(self, startBody: Body, endBody: Body) -> Vector:
        """Calculates force between 2 given bodies

        Args:
            startBody (Body): body - vector start.
            endBody (Body): body - vector end.

        Returns:
            Vector: force between startBody and endBody.

        """
        # Calculating vector start -> end
        direction = endBody.Position - startBody.Position

        # Getting module of force
        gTilde = self._G / ((direction.Module) ** 2)
        if gTilde < self._epsilon:
            gTilde = ZERO
        module = gTilde * startBody.Mass * endBody.Mass 

        # Returning result
        return (direction.normalize()).multiply_on_scalar(module)
