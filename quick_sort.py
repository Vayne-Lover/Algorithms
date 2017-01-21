#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def partition(A,p,r):
  x=A[r]
  i=p-1
  for j in range(p,r):
    if A[j]<=x:
      i+=1
      A[i],A[j]=A[j],A[i]
  A[i+1],A[r]=A[r],A[i+1]
  return i+1

def quick_sort(A,p,r):
  if p<r:
    i=partition(A,p,r)
    quick_sort(A,p,i-1)
    quick_sort(A,i+1,r)

if __name__=='__main__':
  A=[2,4,6,3,8,7,9]
  quick_sort(A,0,len(A)-1)
  print A
