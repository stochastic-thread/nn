def get_sentinel(nd):
  for a in nd:
    if nd[a]: return a
  return False

def setup(n):
  nums = dict()
  for i in range(int(n)):
    nums[i] = False if i in (0, 1) else True
  return nums

def primes(n):
  retval = []
  nums = setup(n)
  while True:
    s = get_sentinel(nums)
    retval.append(s)
    if s is False: return retval[0:len(retval)-1]
    else:
      for index in range(s, len(nums)):
        if index % s == 0:
          nums[index] = False

def main():
  n = input()
  print(primes(n))

if __name__ == "__main__":
  main()
