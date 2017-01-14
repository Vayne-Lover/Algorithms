#!/usr/local/bin/python

def merge(a,b):
    result=[]
    new1=a[:]+[float('inf')]
    new2=b[:]+[float('inf')]
    i=0
    j=0
    for k in range(0,len(a)+len(b)):
      if new1[i]<=new2[j]:
        result.append(new1[i])
        i+=1
      else:
        result.append(new2[j])
        j+=1
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
