#!/usr/local/bin/python
def insertion_sort(a):
  for j in range(1,len(a)):
    i=j-1
    key=a[i] 
    while a[i]>key and i>0:
      a[i+1]=a[i]
      i=i-1
    a[i+1]=key
  return a

