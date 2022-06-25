def repToDecimal(value, base):
  value = value[::-1]
  temp = 1
  result = 0
  for x in value:
      if (x.isdigit()):
          result += temp * int(x)
      else:
          x = x.upper()
          result += temp * (ord(x) - ord('A') + 10)
      temp *= base
  return result

def main():
  value = input("Enter a value: ")
  base = int(input("Enter a base for the value: "))
  print("Function returned", repToDecimal(value, base))
  print(repToDecimal("10", 8))
  print(repToDecimal("5", 16))
  print(repToDecimal("10", 2))
  print(repToDecimal("a", 8))
