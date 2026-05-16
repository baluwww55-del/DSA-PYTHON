# Power Set using Bit Manipulation

def print_power_set(s):
    n = len(s)
    p_size = 1 << n   # 2^n subsets

    # Loop through all numbers from 0 to 2^n - 1
    for i in range(p_size):
        # Check each bit position
        for j in range(n):
            if (i & (1 << j)) != 0:
                print(s[j], end="")
        print()   # Move to next line after each subset


# Driver Code
s = "abc"
print_power_set(s)