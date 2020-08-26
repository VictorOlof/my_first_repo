def main():
    """
    Determine distance between three points
    :return:
    """
    # initialize variables
    x, y, z = 2, 3, 4

    # Pythagoream theorem
    w_squared = (2 ** 2) + (3 ** 2) + (4 ** 2)

    # Square root gives distance
    w = w_squared ** .5

    # show the distance
    print(w)

if __name__ == '__main__':
    main()
