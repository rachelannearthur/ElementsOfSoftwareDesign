def qsort1 (a, lo, hi):
  if (lo >= hi):
    print(a)

  pivot = a[lo]
  m = lo
  for i in range (lo, hi + 1):
    if (a[i] < pivot):
      n = m + 1
      a[n], a[i] = a[i], a[n]
  
  a[lo], a[n] = a[n], a[lo]

  qsort1 (a, lo, m - 1)
  qsort1 (a, m + 1, hi)


def main():

  a = [2, 6, 4, 3, 5]

  qsort1(a, 0, 4)

main()
