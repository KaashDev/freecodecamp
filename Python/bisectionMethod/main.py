def square_root_bisection(square_target, tolerance=0.01, max_iterations = 100):

    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    low = 0
    high = max(1, square_target)
    iterations = 0
    while iterations < max_iterations:
        mid = (low+high)/2
        square = mid ** 2
        if abs(high-low) <= tolerance:
            print(f"The square root of {square_target} is approximately {mid}")
            return mid
        elif square < square_target:
            low = mid
            iterations += 1
        else:
            high = mid
            iterations +=1
    print(f"Failed to converge within {max_iterations} iterations")
    return None

print(square_root_bisection(0.001, 1e-7, 50))
