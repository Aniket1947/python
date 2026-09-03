# Input string for demonstration
original_string = "Python_Code"
print(f"Original String: {original_string}\n")


# def reverse_string(n):
#     reverseString=n[::-1]
#     return reverseString

# print(f"Reverse String using slicing:{reverse_string(original_string)}")


# # --- Method 2: Using a Loop (Iterative Approach) ---
# def reserve_string(n):
#     reserve=""
#     for char in n:
#         reserve=char + reserve
#     return reserve
# print(f"Using a loop:{reverse_string(original_string)}")

# --- Method 3: Using Recursion ---
def reverse_with_recursion(s):
    if len(s) <= 1:
        return s
    print(s[:])
    return reverse_with_recursion(s[1:]) + s[0]
print(f"Reversed (Recursion): {reverse_with_recursion(original_string)}")