from ndb import Vector, Body, Universe
from ndbio import VectorIO, BodyIO, UniverseIO
from graphics import Graphics


def vector_creation_test():
    print("\n\nVector creation test\n:")
    v = Vector([3, 4])
    print(v)


def vector_multiplication_on_scalar_test():
    print("\n\nVector multiplication on scalar test:\n")
    v = Vector([1, 1])
    result = v.multiply_on_scalar(10)
    if result.Coords[0] == 10 and result.Coords[1] == 10:
        print("Passed")
    else:
        print("Failed")


def vector_normalization_test():
    print("\n\nVector normalization test:\n")
    v = Vector([34, 78, 1])
    result = v.normalize()
    if result.Module == 1:
        print("Passed")
    else:
        print("Failed")


def vector_sum_test():
    print("\n\nVector sum test:\n")
    a = Vector([1, 2])
    b = Vector([1, 0])
    c = a + b
    if c.Coords[0] == 2 and c.Coords[1] == 2:
        print("Passed")
    else:
        print("Failed")


def vector_sub_test():
    print("\n\nVector sub test:\n")
    a = Vector([1, 2])
    b = Vector([1, 0])
    c = a - b
    if c.Coords[0] == 0 and c.Coords[1] == 2:
        print("Passed")
    else:
        print("Failed")


def body_move_test():
    print("\n\nBody move test:\n")
    b = Body(Vector([-1, 2, 3]), Vector([5, -6, 1]), 34)
    print("Original body: " + str(b))
    b.move_by_force(Vector([9, 8, 7]), 0.34)
    print("Final body: " + str(b))


def universe_calc_force_between_test():
    print("\n\nUniverse force between 2 bodies test:\n")
    bodyStart = Body(Vector([2, 1]), Vector([0, 0]), 1.5)
    bodyEnd = Body(Vector([5, 3]), Vector([0, 0]), 7.3)
    u = Universe(bodies = [bodyStart, bodyEnd], G = 0.1)

    print("m1m2:")
    print(u._calc_force_between(u.Bodies[0], u.Bodies[1]))

    print("\nm2m1:")
    print(u._calc_force_between(u.Bodies[1], u.Bodies[0]))


def universe_calc_force_on_test():
    print("\n\nResult force calculation test:\n")
    b1 = Body(Vector([2, 1]), Vector([0, 0]), 1.5)
    b2 = Body(Vector([5, 3]), Vector([0, 0]), 7.3)
    b3 = Body(Vector([3, -2]), Vector([0, 0]), 5.8)
    u = Universe(bodies = [b1, b2, b3], G = 0.1)

    print("Result on m3:")
    print(u._calc_result_force_on(u.Bodies[2]))


def universe_update_test():
    u = UniverseIO.read_universe("test.csv")

    i = 0
    while(True):
        if input("\n\n\nTo exit, enter e: ") == 'e':
            exit()
        u.update()
        print("\nIteration " + str(i) + ":\n\n" + str(u))
        i += 1


def read_and_write_test():
    result = UniverseIO.read_universe("test.csv")
    print(result)
    UniverseIO.write_universe("writetest.csv", result)


def basic_tests():
    vector_creation_test()
    print("")
    vector_sum_test()
    print("")
    vector_sub_test()
    print("")
    vector_multiplication_on_scalar_test()
    print("")
    vector_normalization_test()
    print("")
    read_and_write_test()


def force_test():
    universe_calc_force_between_test()
    print("\n\n")
    universe_calc_force_on_test()


def graphics_test():
    u = UniverseIO.read_universe("test.csv")
    g = Graphics(u)
    g.run()


def main():
    #basic_tests()
    #force_test()
    #universe_update_test()
    graphics_test()


if __name__ == "__main__":
    main()
