#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
'''
can eat 0,1,2,3 at a time
how many ways could he eat jar with n cookies
make function eating_cookies
funciton counts number of possible ways he can eat all of the cookies in jar.
ex. jar of cookies with 3 cookies. --> 4 possible ways for him to eat all
1. eat one cookie 3 times
2. eat 1 cooke, then eat 2
3. eat 2 cookies, then eat 1
4. eat 3 cookies all at once
so eating_cookes(3) == 4

base case: n <= 0 cookies
'''
def eating_cookies(n, cache=None):
    if n == 0:
      return 1
    if n == 1:
      return 1
    if n == 2:
      return 2
    if n >= 1000:
      print(f"Cookie monster has died, to many cookies where consumed")

    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
print(eating_cookies(1001))
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
