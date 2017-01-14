#!/usr/local/bin/python
from math import floor

def merge(a,p,q,r):
  if p==r
    return a
  else:
    new1=a[p:q+1]+[float('inf')]
    new2=a[q+1:r]+[float('inf')]
    i=0
    j=0
    result=[]
    for k in range(r-p+1):
      if new1[i]<=new2[j]:
        result.append(new1[i])
        i+=1
      else:
        result.append(new2[j])
        j+=1
    return result

def merge_sort(a,p,r):
  if  p<r:
    q=floor((p+r)/2)
    merge_sort(a,p,q)
    merge_sort(a,q+1,r)
    merge(a,p,q,r)


  
