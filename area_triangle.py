# !/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Jan. 19, 2022
# This program calculates the area of a triangle.

def calc_area(base, height):
  # calculate area using the base and height
  area = (base*height)/2
  # Display the area to the user.
  print("The area is {0} cm2".format(area))

def main():
  # This function gets the base from the user.
  base_from_user_string = input("Enter the base of the triangle(cm): ")
  try:
    # convert the base from the user from string to float
    base_from_user_float = float(base_from_user_string)
    # get the height from the user.
    height_from_user_string = input("Enter the height of a triangle(cm): ")
    try:
      # convert the height from the user from string to int
      height_from_user_float = float(height_from_user_string)
      if base_from_user_float > 0 and height_from_user_float > 0:
        # call function
        calc_area(base_from_user_float, height_from_user_float)
      else:
        print("Base and height must be greater than 0.")
    except Exception:
      print("{} is not a number. Enter a number.".format(height_from_user_string))
  except Exception:
    print("{} is not a number. Enter a number".format(base_from_user_string))


if __name__ ==  "__main__":
  main()




