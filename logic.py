'''This program is designed to calculate how many years until the user celebrates a centenary birthday'''
current_year = int(input("Enter current year:\n"))
birth_year = int(input("Enter your year of birth:\n"))
centenary = 100 - current_year - birth_year
# logical error in line 4 because of calculation order missing brackets that calculate the user age seperately.
print(f"WOW!You are {centenary} years away from your centenary birthday!")