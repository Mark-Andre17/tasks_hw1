import math
from itertools import product, combinations


def domain_name(url):
    return url.split('www.')[-1].split('//')[-1].split('.')[0]


def int32_to_ip(int32):
    str_32 = f'{int32:b}'.rjust(32, '0')
    return '.'.join([str(int(str_32[idx:idx + 8], 2)) for idx in range(0, len(str_32), 8)])


def zeros(n):
    return zeros(n // 5) + n // 5 if n else 0


def bananas(s) -> set:
    result = set()
    word = 'banana'
    options = (x for x in product((' ', '-'), repeat=len(s)) if x.count('-') == (len(s) - len(word)))
    for var in options:
        new_str = ''.join(a if b == ' ' else b for b, a in zip(var, s))
        if new_str.replace('-', '') == word:
            result.add(new_str)
    return result


def bananas_2(s) -> set:
    result = set()
    word = 'banana'
    for combo in combinations(range(len(s)), len(s) - len(word)):
        list_s = list(s)
        for index in combo:
            list_s[index] = '-'
        option = ''.join(list_s)
        if option.replace('-', '') == word:
            result.add(option)
    return result


def count_find_num(primesL: list, limit: int):
    counter = 0
    largest_num = 0
    for a in range(2, limit + 1):
        divisor = 2
        new_list = []
        while divisor ** 2 <= a:
            if a % divisor == 0:
                a //= divisor
                new_list.append(divisor)
            else:
                divisor += 1
        if a != 1:
            new_list.append(a)
        if set(new_list) == set(primesL):
            counter += 1
            largest_num = math.prod(new_list)
    if counter != 0:
        return [counter, largest_num]
    else:
        return []


if __name__ == '__main__':
    print(domain_name('http://google.co.jp'))
    print(int32_to_ip(2154959208))
    print(zeros(1000))
    print(bananas('bbananana'))
    print(bananas_2('bbananana'))
    print(count_find_num([2, 3, 5], 200))
