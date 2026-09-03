# # Print "VAISHNAVI" using star patterns

# for i in range(7):  # 0 to 6 rows
#     # V
#     for j in range(7):
#         if (j == 0 and i < 6) or (j == 6 and i < 6) or (i == 6 and j == 3):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print(" ", end=" ")

#     # A
#     for j in range(7):
#         if ((j == 0 and i != 0) or (j == 6 and i != 0) or (i == 0 and j != 0 and j != 6) or (i == 3)):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print(" ", end=" ")

#     # I
#     for j in range(7):
#         if (j == 3) or (i == 0) or (i == 6):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print(" ", end=" ")

#     # S
#     for j in range(7):
#         if (i == 0 or i == 3 or i == 6) or (j == 0 and i < 3) or (j == 6 and i > 3):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print(" ", end=" ")

#     # H
#     for j in range(7):
#         if (j == 0 or j == 6 or i == 3):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print(" ", end=" ")

#     # N
#     for j in range(7):
#         if (j == 0 or j == 6 or i == j):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print(" ", end=" ")

#     # A
#     for j in range(7):
#         if ((j == 0 and i != 0) or (j == 6 and i != 0) or (i == 0 and j != 0 and j != 6) or (i == 3)):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print(" ", end=" ")

#     # V
#     for j in range(7):
#         if (j == 0 and i < 6) or (j == 6 and i < 6) or (i == 6 and j == 3):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print(" ", end=" ")

#     # I
#     for j in range(7):
#         if (j == 3) or (i == 0) or (i == 6):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()  # Move to next line


# Print "ANIKET" using star patterns

for i in range(7):  # Rows 0–6
    # A
    for j in range(7):
        if ((j == 0 and i != 0) or (j == 6 and i != 0) or (i == 0 and j != 0 and j != 6) or (i == 3)):
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end=" ")

    # N
    for j in range(7):
        if (j == 0 or j == 6 or i == j):
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end=" ")

    # I
    for j in range(7):
        if (j == 3) or (i == 0) or (i == 6):
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end=" ")

    # K
    for j in range(7):
        if (j == 0) or (i + j == 3) or (i - j == 3):
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end=" ")

    # E
    for j in range(7):
        if (j == 0) or (i == 0) or (i == 3) or (i == 6):
            print("*", end="")
        else:
            print(" ", end="")
    print(" ", end=" ")

    # T
    for j in range(7):
        if (i == 0) or (j == 3):
            print("*", end="")
        else:
            print(" ", end="")
    print()  # Move to next line
