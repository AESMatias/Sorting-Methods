def insertion_sort(list):
  for i in range(1, len(list)):
    aux = list[i]
    j = i
    while (j>0 and aux<list[j-1]):
      list[j] = list[j-1]
      j -= 1
    list[j] = aux
return list
