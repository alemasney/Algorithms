#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # keep current index
  current_index = 0
  # keep highest index
  highest = 0
  # keep lowest index
  lowest = 0
  # loop through list
  for i in prices:
    print(i)



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))