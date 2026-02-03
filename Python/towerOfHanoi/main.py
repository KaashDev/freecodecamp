def hanoi_solver(n):

    A = list(range(n, 0, -1))
    B = []
    C = []

    result = ""
    result += f"{A} {B} {C}\n"

    def han(n, source, dest, aux):
        nonlocal result

        if n == 1:
            dest.append(source.pop())
            result += f"{A} {B} {C}\n"
            return

        han(n-1, source, aux, dest)
        dest.append(source.pop())
        result += f"{A} {B} {C}\n"
        han(n-1, aux, dest, source)

    han(n, A, C, B)

    return result.rstrip()


if __name__ == "__main__":
    print(hanoi_solver(3))