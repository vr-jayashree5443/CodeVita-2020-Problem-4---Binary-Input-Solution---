#!/usr/bin/env python
# coding: utf-8

# In[2]:


def calculate_distance(binary_string, A, B):
    if not all(bit in '01' for bit in binary_string):
        return "INVALID"
    count_01 = binary_string.count("01")
    count_10 = binary_string.count("10")
    cost_original = count_01 * A + count_10 * B

    rearranged_string = min(binary_string.count("0"), binary_string.count("1")) * "01"

    cost_rearranged = rearranged_string.count("01") * A + rearranged_string.count("10") * B

    distance = abs(cost_original - cost_rearranged)

    return distance


def main():
    T = int(input("Enter the number of test cases: "))
    distances = []
    for _ in range(T):
        binary_string = input().strip()
        A, B = map(int, input().split())
        result = calculate_distance(binary_string, A, B)
        distances.append(result)

    for distance in distances:
        print(distance)


if __name__ == "__main__":
    main()

