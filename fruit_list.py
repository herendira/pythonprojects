
"""OBJECT ORIENTED PROGRAMING WITH DOT .metoth"""
def main():
    try:
    # Create and print a list named fruit.
      fruit_list = ["pear", "banana", "apple", "mango"]
      print(f"Original Fruit List: {fruit_list}")

      fruit_list.reverse()
      print(f"Reverse Fruit list: {fruit_list}")

      fruit_list.append("orange")
      print(f"Product adding to a Fruit list: {fruit_list}")

      fruit_list.remove("banana")
      print(f"Banana removed from the Fruit list: {fruit_list}")

      fruit_list.pop()
      print(f"List without the last elemnt from Fruit list: {fruit_list} ")

      fruit_list.sort()
      print(f"List sorted: {fruit_list} ")

      index = fruit_list.index("apple")
      fruit_list.insert(index, "cherry")
      print(f"List Fruit with cherry insted of apple: {fruit_list}")

      fruit_list.clear()
      print(f"Cleared Fruit List: {fruit_list} ")

    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")









if __name__ == "__main__":
    main()