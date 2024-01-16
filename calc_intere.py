def calc_without_add(start, years, performance):
    for i in range(years):
        profit = start * performance
        start = start * (1 + performance)
        print(f"Year {i + 1}: {int(profit)}", end=" ")
        print(f"Total: {int(start)}")
    print(f"Total: {int(start)}")


calc_without_add(200000, 30, 0.036)


def calc_with_add(start, years, performance, add=0):
    for i in range(years):
        start += add
        profit = start * performance
        start = start * (1 + performance)
        print(f"Year {i + 1}: {int(profit)}", end=" ")
        print(f"Total: {int(start)}")
    print(f"Total: {int(start - (add * years))}")


# calc_with_add(10000, 40, 0.1, 24000)
