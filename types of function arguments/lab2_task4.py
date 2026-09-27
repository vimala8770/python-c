def build_profile(**details):
    print("----- PROFILE CARD -----")
    
    for key, value in details.items():
        print(key.capitalize() + ":", value)
    
    print("------------------------")


# First profile
build_profile(
    name="alekhya",
    age=19,
    city="vizianagaram",
    hobby="Coding"
)

print()

# Second profile
build_profile(
    name="vimala",
    age=18,
    city="kakinada",
    hobby="Reading",
    course="B.Tech"
)
output:
----- PROFILE CARD -----
Name: alekhya
Age: 19
City: vizianagaram
Hobby: Coding
------------------------

----- PROFILE CARD -----
Name: vimala
Age: 18
City: kakinada
Hobby: Reading
Course: B.Tech
------------------------
