i = 0
while i < n:
  j = i + 1
  while j < n:
    if a[i] > a[j]:
      swap(a[i], a[j])
    j += 1
  i += 1
