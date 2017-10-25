def top3(list2):
  list2.sort()

  for i in range(len(list2)-1,2,-1):
     print(list2[i])

if __name__ == "__main__":
    list1 = [34, 68, 454, 8, 4, 3437]
    top3(list1)

