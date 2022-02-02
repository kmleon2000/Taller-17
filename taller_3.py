def factorial(n):
  """ Recursive method to get factorial number
  >>> factorial(5)
  120

  >>> factorial(9)
  362880

  >>> factorial(16)
  20922789888000
  """
  return n if n == 1 else n * factorial(n - 1)
  