from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    sol = []
    i = 1

    while i <= n:
        if i % 15 == 0:
            sol.append('FizzBuzz')
        elif i % 3 == 0:
            sol.append('Fizz')
        elif i % 5 == 0:
            sol.append('Buzz')
        else:
            sol.append(i)

        i += 1
        
    return sol

