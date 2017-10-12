def findMaxMin(args):
  if min(args) == max(args):
    return [min(args)]
  else:
    return [min(args),max(args)]

print(findMaxMin([1, 2, 3, 4]))