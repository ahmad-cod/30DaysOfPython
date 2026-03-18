# Exercises: Level 2

#     Use for loop to iterate from 0 to 100 and print the sum of all numbers.

sum = 0
for i in range(101):
  sum = sum + i
print(sum)

# The sum of all numbers is 5050.

#     Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

evens_sum = 0
odds_sum = 0

for i in range(101):
  if i % 2 == 0:
    evens_sum = evens_sum + i
  else:
    odds_sum = odds_sum + i

print(f"The sum of all evens is {evens_sum}. \nAnd the sum of all odds is {odds_sum}")

#     The sum of all evens is 2550. And the sum of all odds is 2500.

