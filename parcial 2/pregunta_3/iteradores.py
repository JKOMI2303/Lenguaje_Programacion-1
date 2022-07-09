def ins(e, ls):
    yield [e, *ls]
    if ls:
        for i in ins(e, ls[1:]):
            yield [ls[0], *i]

def misterio(ls):
    acc=[]
    if ls:
        for m in misterio(ls[1:]): 
            for i in ins(ls[0], m):
                if i not in acc: ## Se usa la lista aculador para ir añadiendo todas las cadenas y en el caso e una repetida no sera analizada por paratizado y se descarta
                    acc.append(i)
                    yield i
                else:
                    pass
    else:
        yield []

def bienParentizadas(n):
    parentesis='('*n+')'*n
    stack=[]
    for m in misterio(parentesis):
        for x in range(len(m)+1):

            if(x==len(m)):
                cadena="".join(m)
                yield cadena
                break
            if(m[x]=="("):
                stack.append(m[x])
            elif(m[x]==")"):
                if(len(stack)==0):
                    break
                else:
                    stack.pop()

for k in bienParentizadas(3):
    print(k)


##En este caso bienParentizado aprovecha los iteradores ins y misterios ya que estos retornan todas las posibles permutaciones de una lista o una cadena de String luego parentizado filtra esa cadena y comprueba si esta bien.
            
