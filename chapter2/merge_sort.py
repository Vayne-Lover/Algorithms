#!/usr/local/bin/python

def merge(a,b):
    result=[]
    i=0
    j=0
    while i<len(a) and j<len(b):       
      if a[i]<=b[j]:
        result.append(a[i])
        i+=1
      else:
        result.append(b[j])
        j+=1
    result+=a[i:]
    result+=b[j:]
    return result

def merge_sort(a):
  if  len(a)<=1:
    return a
  else:
    mid=len(a)/2
    left=merge_sort(a[:mid])
    right=merge_sort(a[mid:])
    return merge(left,right)

if __name__=='__main__':
    t1=[15,4,8,2,3,6,12,24]
    t2=[-2,1,-9.3,5.8,9,10,7]
    t3=[]
    print merge_sort(t1)
    print t1
    print merge_sort(t2)
    print t2
    print merge_sort(t3)
    print t3
