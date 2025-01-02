# Sahad Rafiuzzaman
# Date: 12/28/2024


# Sum
# Python has lots of built-in functions to help us work with numbers.
# One of them helps us calculate the sum (the total). e.g.

student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores)
print(total_score)

# But how does sum() work behind the scenes?
sum = 0
for score in student_scores:
    sum += score
print(sum)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")
