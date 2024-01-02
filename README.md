1. **Function `calculate_distance`:**
   - The function takes three parameters: `binary_string`, `A`, and `B`.
   - It first checks if the `binary_string` contains only '0' and '1'. If not, it returns "INVALID".
   - It then calculates the cost of the original string (`cost_original`) based on the occurrences of "01" and "10" using the given values of `A` and `B`.
   - The function then creates a rearranged string (`rearranged_string`) with the minimum number of occurrences of "01" or "10", whichever is smaller.
   - It calculates the cost of the rearranged string (`cost_rearranged`) using the same logic as for the original string.
   - The distance between the original and rearranged strings is calculated as the absolute difference between their costs.

2. **Main Function:**
   - The main function starts by taking input for the number of test cases (`T`).
   - It iterates through each test case, taking input for the binary string, `A`, and `B`.
   - It calls the `calculate_distance` function for each test case and stores the results in a list (`distances`).

3. **Printing Results:**
   - Finally, the main function prints the distances for each test case.

### Example:

Let's take the first example provided:
- `T = 2`
- Test Case 1:
   - Binary string: `0100`
   - `A = 3`, `B = 2`
   - The cost of the original string is calculated: `count_01 * A + count_10 * B = 1 * 3 + 0 * 2 = 3`
   - The rearranged string with minimum occurrences is `1000`.
   - The cost of the rearranged string is calculated: `count_01 * A + count_10 * B = 0 * 3 + 1 * 2 = 2`
   - The distance is calculated as `|3 - 2| = 1`.
- Test Case 2:
   - Binary string: `000`
   - `A = 4`, `B = 5`
   - The cost of the original string is calculated: `count_01 * A + count_10 * B = 0 * 4 + 0 * 5 = 0`
   - The rearranged string is the same as the original as it already has the minimum cost.
   - The cost of the rearranged string is `0`.
   - The distance is `0`.
- The output will be `1 0` for these test cases.

The second example with an invalid input will return "INVALID" because the binary string contains a character other than '0' and '1'.

**TEST CASE 1**

![T1](https://github.com/vr-jayashree5443/CodeVita-2020-Problem-4---Binary-Input-Solution---/assets/128161257/c53276e5-dcc3-4fcd-b04e-dbe97f1f3692)

**TEST CASE 2**

![image](https://github.com/vr-jayashree5443/CodeVita-2020-Problem-4---Binary-Input-Solution---/assets/128161257/6c7c4eef-3745-4099-8aad-4c218cddf435)

