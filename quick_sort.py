#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import random

def partition(A,p,r):
  x=A[r]
  i=p-1
  for j in range(p,r):
    if A[j]<=x:
      i+=1
      A[i],A[j]=A[j],A[i]
  A[i+1],A[r]=A[r],A[i+1]
  return i+1

def random_partition(A,p,r):
  i=random.randint(p,r)
  A[r],A[i]=A[i],A[r]
  return  partition(A,p,r)

def three_median_partition(A,p,r):
  (a,b,c)=[random.randint(p,r) for _ in range(3)]
  if a>=b:
    if c>=a:
      mid=a
    elif c>=b:
      mid=c
    else:
      mid=b
  else:
    if c>=b:
      mid=b
    elif c>=a:
      mid=c
    else:
      mid=a
  A[mid],A[r]=A[r],A[mid]
  return partition(A,p,r)

def quick_sort(A,p,r):
  if p<r:
    i=partition(A,p,r)
    quick_sort(A,p,i-1)
    quick_sort(A,i+1,r)

def random_quick_sort(A,p,r):
  if p<r:
    i=random_partition(A,p,r)
    random_quick_sort(A,p,i-1)
    random_quick_sort(A,i+1,r)

def three_median_quick_sort(A,p,r):
  if p<r:
    i=three_median_partition(A,p,r)
    three_median_quick_sort(A,p,i-1)
    three_median_quick_sort(A,i+1,r)

if __name__=='__main__':
  A=[2,4,6,3,8,7,9]
  B=[2,2,5,7,-2,7,-4,3,9.2]
  C=[]
  #quick_sort(A,0,len(A)-1)
  #quick_sort(B,0,len(B)-1)
  #quick_sort(C,0,len(C)-1)
  #random_quick_sort(A,0,len(A)-1)
  #random_quick_sort(B,0,len(B)-1)
  #random_quick_sort(C,0,len(C)-1)
  three_median_quick_sort(A,0,len(A)-1)
  three_median_quick_sort(B,0,len(B)-1)
  three_median_quick_sort(C,0,len(C)-1)
  print A
  print B
  print C
