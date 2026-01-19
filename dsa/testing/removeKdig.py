


def removeKdigits(s: str, k: int) -> str:
  stack = []

  for digit in s:
      while stack and k > 0 and stack[-1] > digit:
          stack.pop()
          k -= 1
      stack.append(digit)

  # Remove remaining digits from the end
  while k > 0:
      stack.pop()
      k -= 1

  # Remove leading zeros
  result = ''.join(stack).lstrip('0')

  return result if result else "0"

print(removeKdigits(s="4325043", k=3))