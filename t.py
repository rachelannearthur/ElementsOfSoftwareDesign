def compute_series(v, k, p):
  total = v
  lines_code = v // (k ** p)
  while (lines_code > 0):
    total += lines_code
    p += 1
    lines_code = v // (k**p)
    print(total)


def main():


  compute_series(54, 9, 1)

main()

