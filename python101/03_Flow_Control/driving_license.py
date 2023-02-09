"""
Loui wants to drive a car and wants to know if he can 
apply for a driving license or not.
"""

age: int = 13

# ---------------------------------------------------
# If / Else Statement
# ---------------------------------------------------

if age < 16:
    print('You are NOT eligible for a Licence')
else: 
    print('You are legible for a License')

# ---------------------------------------------------
# After a couple of years
# ---------------------------------------------------

age = 19

if age < 16:
    print('You are NOT eligible for a Licence')
else:
    print('You are eligible for a License')

# ----------------------------------------------------
# Alternative Implementation - Without 'Else' block
# ----------------------------------------------------

if age < 16:
    print('You are NOT eligible for a License')

print('You are eligible for a License')

# ------------------------------------------------------
# After too many years
# ------------------------------------------------------

age = 100

if age < 16:
    print('You are NOT eligible for a license')
elif age >= 100:
    print('You are too old to get a License')
else:
    print('You are eligible for a license')