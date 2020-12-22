#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

numbers = []
answer = 0

def digit_fifth_powers(integer):
    sum = 0
    for i in str(integer):
        sum += pow(int(i), 5)
    if sum == integer:
        numbers.append(integer)

for k in range(2,1000000):
    digit_fifth_powers(k)

for j in numbers:
    answer += j

print(answer)