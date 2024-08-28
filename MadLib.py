#MadLib.py
#Name: Josue Reza-Rivera
#Date:
#Assignment: Lab 1

def main():
  print("Madlib")
  #Ask user for words
  animal1 = input("Enter an animal")
  food1 = input("Enter a food")
  noun1 = input("Enter a noun")
  noun2 = input("Enter a noun")
  animal2 = input("Enter a animal")
  location1 = input("Enter a noun")
  #Print the story with the user supplied words.

  print("If you give a " + animal1 + "a dozen" + food1 + " he/she will ask for a " + noun1 + ".")
  print("When he/she is done, he/she will " + noun2 + "with their friend the " + animal2 + "until they both go to " + location1 + ".")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
