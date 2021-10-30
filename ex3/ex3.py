#################################################################
# FILE : ex3.py
# WRITER : eyal , eyalmutzary , 206910432
# EXERCISE : intro2cs ex3 2021
# DESCRIPTION: All ex3 in one place.
# STUDENTS I DISCUSSED THE EXERCISE WITH:
# WEB PAGES I USED: Wikipedia
# NOTES: ...
#################################################################

def input_list():
    lst = []
    lst_sum = 0
    while True:
        num = input()
        if num == "":
            break
        else:
            lst.append(float(num))
    for number in lst:
        lst_sum += number
    lst.append(lst_sum)
    return lst


def inner_product(vec_1, vec_2):
    if len(vec_1) == 0 and len(vec_2) == 0:
        return 0
    if len(vec_1) != len(vec_2) or len(vec_1) == 0 or len(vec_2) == 0:
        return None
    vec_sum = 0
    for i in range(len(vec_1)):
        vec_sum += vec_1[i] * vec_2[i]
    return vec_sum


def sequence_monotonicity(sequence):
    seq_list = [True, True, True, True]
    if len(sequence) == 0 or len(sequence) == 1:
        return seq_list
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i-1]:
            seq_list[1], seq_list[3] = False, False
        elif sequence[i] > sequence[i-1]:
            seq_list[2], seq_list[3] = False, False
        elif sequence[i] < sequence[i-1]:
            seq_list[0], seq_list[1] = False, False
        else:
            seq_list = [False, False, False, False]
            break
    return seq_list


def check_possible_monotonicity(def_bool):
    if (def_bool[1] and (def_bool[2] or def_bool[3])) \
            or (def_bool[3] and (def_bool[0] or def_bool[1])):
        return False
    true_counter = 0
    for val in def_bool:
        if val:
            true_counter += 1
            if true_counter == 3:
                return False
    if true_counter == 1 and (def_bool[1] or def_bool[3]):
        return False
    return True


def monotonicity_inverse(def_bool):
    if not check_possible_monotonicity(def_bool):
        return None

    if def_bool[0] and def_bool[2]:
        return [1,1,1,1,1,1]
    elif def_bool[0] or def_bool[1]:
        if not def_bool[1]:
            return [1,1,2,3,4,4]
        return [1,2,3,4,5,6]
    elif def_bool[2] or def_bool[3]:
        if not def_bool[3]:
            return [6,5,5,4,4,3]
        return [6,5,4,3,2,1]
    else:
        return [1,0,-1,1,12,3]


def check_prime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True


def primes_for_asafi(n):
    primes_lst = []
    num = 2
    while len(primes_lst) < n:
        print(num)
        if check_prime(num):
            primes_lst.append(num)
        num += 1
    return primes_lst


def sum_of_vectors(vec_lst):
    if len(vec_lst) == 0:
        return None
    elif len(vec_lst[0]) == 0:
        return []
    new_vec = []
    for i in range(len(vec_lst[0])):
        new_vec.append(0)
        for vector in vec_lst:
            new_vec[i] += vector[i]
    return new_vec


def num_of_orthogonal(vectors):
    counter = 0
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            if inner_product(vectors[i], vectors[j]) == 0:
                counter += 1
    return counter

bool_def = [False, False, True, False]
print(monotonicity_inverse(bool_def))