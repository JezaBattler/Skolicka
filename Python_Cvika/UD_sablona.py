class Prvek:
    def __init__(self, x, dalsi):
        self.x = x
        self.dalsi = dalsi

def VytiskniLSS( p ):
    print( "LSS:", end=" " )
    while p!=None:
        print( p.x, end=" " )
        p = p.dalsi
    print(".")

def NactiLSS():
    """cte cisla z radku, dokud nenacte prazdny radek"""
    prvni = None
    posledni = None
    r = input()
    while r!="":
        radek = r.split()
        if len(radek)==0: # protoze ten test r!="" v RCDX neukoncil cyklus!
            break
        for s in radek:
            p = Prvek(int(s),None)
            if prvni==None:
                prvni = p
            else:
                posledni.dalsi = p
            posledni = p
        r = input()
    return prvni

#################################################

def UnionDestruct(a,b):
    """ destruktivni sjednoceni dvou usporadanych seznamu
    * nevytvari zadne nove prvky, vysledny seznam bude poskladany z prvku puvodnich seznamu,
    * vysledek je MNOZINA, takze se hodnoty neopakuji """
    prvni = None
    posledni = None

    while a != None or b != None:
        if a is not None and (b is None or a.x < b.x):
            temp = a
            a = a.dalsi
        elif b is not None and (a is None or b.x < a.x):
            temp = b
            b = b.dalsi
        else:  
            temp = a
            a = a.dalsi
            b = b.dalsi
        if prvni == None:
            prvni = temp
            posledni = prvni
        elif posledni.x != temp.x:
            posledni.dalsi = temp
            posledni = temp
        posledni.dalsi = None
        

        

    # sem doplnte kod funkce, dalsi casti zdrojoveho kodu NEMENTE
    # ....................................................
    # ....................................................
    # ....................................................
    # ....................................................
    # ....................................................
    # ....................................................
    # ....................................................
    # ....................................................
    # ....................................................

    return prvni

#################################################

VytiskniLSS( UnionDestruct( NactiLSS(), NactiLSS() ) )
