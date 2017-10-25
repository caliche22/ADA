from sys import stdin
# Carlos Arboleda - ADA - Camilo Rocha 
# Potentiometers.py hecho en clase 
# Se utilizo la clase segmentation tree para poder hacer las operaciones y luego ir partiendo de a dos en dos y luego devolverme operando para arriba 
# Se discutio con la clase y fue hecho en clase 
class segtree(object):

  def __init__(self,a):
    """create an empty segment tree"""
    self.__a = list(a)
    self.__s = [ None for i in range(len(a)<<2) ]
    self.__build_tree(0,0,len(a))

  def __len__(self):
    """return the length of the collection of values"""
    return len(self.__a)

  def __str__(self):
    """return the string representation of the segment tree"""
    return str(self.__s)
  
  def __left(self,i):
    """return the index of the left child of i"""
    return 1+(i<<1)

  def __right(self,i):
    """return the index of the left child of i"""
    return (1+i)<<1

  def __build_tree(self,i,low,hi):
    """store the sum of __a[low..hi) in __s[i]"""
    ans = None
    if low+1==hi:
      ans = self.__s[i] = self.__a[low]
    else:
      mid = low+((hi-low)>>1)
      ans = self.__s[i] = self.__build_tree(self.__left(i),low,mid) \
                          + self.__build_tree(self.__right(i),mid,hi)
    return ans

  def query_range(self,i,j):
    """return the sum in the range [i..j)"""
    assert 0 <= i <= j <= len(self)
    ans = self.__query_aux(0,0,len(self),i,j)
    return ans

  def __query_aux(self,i,low,hi,start,end):
    """return the sum in the intersection of and  __a[low..hi) and __a[start..end)""" 
    ans = None
    if hi<=start or end<=low: ans = 0
    elif start<=low and hi<=end: ans = self.__s[i]
    else:
      mid = low+((hi-low)>>1)
      ans = self.__query_aux(self.__left(i),low,mid,start,end) \
            + self.__query_aux(self.__right(i),mid,hi,start,end)
    return ans

  def updateValue(self,i,x):
    """update the value of the i-th element to be x"""
    assert 0 <= i < len(self)
    self.__update_aux(0,0,len(self),i,x)

  def __update_aux(self,i,low,hi,j,x):
    assert low<=j<hi
    ans = None
    if low+1==hi: ans = self.__a[j] = self.__s[i] = x
    else:
      mid = low+((hi-low)>>1)
      if j<mid: ans = self.__s[i] = self.__update_aux(self.__left(i),low,mid,j,x) + self.__s[self.__right(i)]
      else: ans = self.__s[i] = self.__s[self.__left(i)] + self.__update_aux(self.__right(i),mid,hi,j,x)
    return ans



def main():
  caso=0
  k=int(stdin.readline())
  #print(type(k))
  while k!=0:
    listap=[]
    for i in range(k):
      n=int(stdin.readline())
      listap.append(n)
    st=segtree(listap) ## se crea el arbol de segmento
    accion=stdin.readline()
    caso+=1
    print("Case "+str(caso)+":")
    while accion[0]!='E': ## solucion del profesor para no buscar END si no algo que empiece por E
      letra=accion.split()[0]
      x,y=[int (x) for x in accion.split()[1:]] # letra x y 
      #print(letra,x,y,"sirve")
      if letra=="M":
        print(st.query_range(x-1,y))
        #pass
      elif letra=="S":
        st.updateValue(x-1,y)
      accion=stdin.readline()
    k=int(stdin.readline())
    if k==0:
      print(end="")
    else:
      print()
main()












