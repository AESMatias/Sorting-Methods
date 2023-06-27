def selection_sort(list):
  for i in range(len(list)-1):
  position = i
    for j in range(pos+1, len(list)):
      if (list[pos] > list[j]):
        position = j
    aux = list[position]
    list[position] = list[i]
    list[i] = aux
return list
