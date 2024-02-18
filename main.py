# Change Case to Lower
def chg2lower(text):
  return text.lower()


def chg2upper(text):
  return text.upper()


def chg2title(text):
  return text.title()


def chg2cap(text):
  return text.capitalize()


def split_and_join(text):
  text = text.split(" ")
  text = "-".join(text)
  return text


def reverser(text):
  return text[::-1]


def swapecase(text):
  return text.swapcase()


def remove_spaces(text):
  return text.replace(" ", "")


if __name__ == '__main__':
  # importing the required modules
  text = input("Enter a string: ")
  print(chg2lower(text))
  print(chg2upper(text))
  print(chg2title(text))
  print(chg2cap(text))
  print(split_and_join(text))
  print(reverser(text))
  print(swapecase(text))
  print(remove_spaces(text))
