import timeit

N = 100000000

def while_loop():
    i = 0
    while i < N:
        i += 1


def for_loop_pure():
    for i in range(N):
        pass


def for_loop_with_increment():
    for i in range(N):
        i += 1


def for_loop_with_test():
    for i in range(N):
        if i < N: pass


def for_loop_with_increment_and_test():
    for i in range(N):
        if i < N: pass
        i += 1


def main():
    print('while loop\t\t', timeit.timeit(while_loop, number=1))
    print('for pure\t\t', timeit.timeit(for_loop_pure, number=1))
    print('for inc\t\t\t', timeit.timeit(for_loop_with_increment, number=1))
    print('for test\t\t', timeit.timeit(for_loop_with_test, number=1))
    print('for inc+test\t', timeit.timeit(for_loop_with_increment_and_test, number=1))


if __name__ == '__main__':
    main()