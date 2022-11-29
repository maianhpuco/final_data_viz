i = 0
while i < n - 1:
  j = i + 1
  while j < n - 1:
    if a[i] > a[j]:
      swap(a[i], a[j])
    j += 1
  i += 1
