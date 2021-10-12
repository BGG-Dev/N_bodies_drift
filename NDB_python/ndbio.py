import csv
from os import close
from ndb import Vector, Body, Universe


class VectorIO:

    @staticmethod
    def read_vector(row: list[str], n: int, offset: int) -> Vector:
        """Reads vector from given row with given offset.

        Args:
            row (list[str]): row to read from.
            n (int): vector dimension.
            offset (int): offset, sets start position to read from.

        Returns:
            Vector: Vector instance with data from row.

        """
        coords = [float(row[i]) for i in range(offset, offset + n)]
        return Vector(coords)


class BodyIO:

    @staticmethod
    def read_body(row: list[str], n: int) -> Body:
        """Reads body from given row.

        Args:
            row (list[str]): row to read from.
            n (int): dimension of vectors.

        Returns:
            Body: Body instance with data from row.

        """
        # Reading data
        position = VectorIO.read_vector(row, n, 0)
        speed = VectorIO.read_vector(row, n, n)
        mass = float(row[-1])

        # Returning result
        return Body(position, speed, mass)

    @staticmethod
    def write_body(body: Body, writer: csv.writer) -> None:
        """Writes given body by using given writer.

        Args:
            body (Body): Body instance to write.
            writer (csv.writer): Writer instance to write body.

        """
        position_coords = list(body.Position.Coords)
        speed_coords = list(body.Speed.Coords)
        body_row = list(position_coords + speed_coords)
        body_row.append(body.Mass)
        writer.writerow(body_row)


class UniverseIO:

    @staticmethod
    def read_universe(fileName: str) -> Universe:
        """Reads universe from given file.

        Args:
            fileName (str): path to file to read from.

        Returns:
            Universe: Universe instance with data from file.

        """
        # Reading from file
        with open(fileName, 'r') as file:

            # Creating reader
            reader = csv.reader(file)

            # Reading columns
            info = [float(i) for i in next(reader)]

            # Calculating dimension
            n = int(info[3])

            # Reading data
            bodies = list()
            for row in reader:
                bodies.append(BodyIO.read_body(row, n))

        # Finish
        file.close()

        # Returning result
        return Universe(bodies, info[0], info[1], info[2])

    @staticmethod
    def write_universe(fileName: str, universe: Universe) -> None:
        """Writes given universe to file.

        Args:
            fileName (str): path to write in.
            universe (Universe): Universe instance to write.

        """
        # Writing to file
        with open(fileName, 'w') as file:

            # Creating writer
            writer = csv.writer(file)

            # Writting info
            writer.writerow([universe.DT, universe.G, universe.Epsilon, universe.N])            

            # Writting bodies
            for currentBody in universe.Bodies:
                BodyIO.write_body(currentBody, writer)

        # Finish
        file.close()
