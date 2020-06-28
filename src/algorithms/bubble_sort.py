def bubble_sort(s: str):
    str_len = len(s)
    for _ in range(str_len - 1):
        for i in range(str_len - 1):
            if s[i] > s[i + 1]:
                max_val = s[i]
                s[i] = s[i + 1]
                s[i + 1] = max_val
    return s


def selection_sort(s: str):
    len_s = len(s)
    for j in range(len_s):
        temp_val = s[j]
        min_val = s[j]
        swap_indx = j
        for i in range(j, len_s):
            if min_val > s[i]:
                min_val = s[i]
                swap_indx = i

        s[j] = min_val
        s[swap_indx] = temp_val
    return s


def insertion_sort(s):
    indx_curr = 1
    while indx_curr < len(s):
        curr_num = s[indx_curr]
        prev_num = s[indx_curr - 1]
        if curr_num < prev_num:
            s[indx_curr] = prev_num
            s[indx_curr - 1] = curr_num
            indx_curr -= 1
            if indx_curr == 0:
                indx_curr += 2
        else:
            indx_curr += 1

    return s


def test():
    print(insertion_sort([99, 2, 0, 44, 5, 3, 63, 87, 283, 4]))
