#!/usr/local/bin/python
def insertion_sort(a):
  for j in range(1,len(a)):
    i=j-1
    key=a[j] 
    while a[i]>key and i>0:
      a[i+1]=a[i]
      i=i-1
    a[i+1]=key
  print a
  return a
 
if __name__=='__main__':
  insertion_sort([1,3,2,6,8,9])
  insertion_sort([-1,-5,2,-5,7])
  insertion_sort([-0.1,3.2,-5,6,-4,7])
