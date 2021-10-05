"""
  Students  |  Grades  |  Letters
------------|----------|----------
  George    |  46      |  F
  Michell   |  80      |  B
  Josh      |  12      |  F
  Chloe     |  68      |  D
  Stanley   |  99      |  A
  Annie     |  100     |  A+
"""

gradeToTest = 55

if gradeToTest == 100:
    print("A+")
elif gradeToTest > 89:
    print("A")
elif gradeToTest > 79:
    print("B")
elif gradeToTest > 69:
    print("C")
elif gradeToTest > 49:
    print("D")
else:
    print("F")
