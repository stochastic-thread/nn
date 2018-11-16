
def get_sentinel(nd):
  for a in nd:
    if nd[a] == True:
      return a
  return False

def setup(n):
  nums = dict()
  for i in range(int(n)):
    if i == 0: nums[i] = False
    elif i == 1: nums[i] = False
    else: nums[i] = True
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
