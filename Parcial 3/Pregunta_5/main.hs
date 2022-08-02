foldr :: (a -> b -> b) -> b -> [a] -> b
foldr _ e []        = e
foldr f e (x:xs)    = f x $ foldr f e xs

const :: a -> b -> a
const x _ = x

what :: a -> ([b] -> [(a, b)]) -> [b] -> [(a, b)]
what _ _ []     = []
what x f (y:ys) = (x, y) : f ys

--a) 
misteriosa :: ???
misteriosa = foldr what (const [])

gen :: Int -> [Int]
gen n = n : gen (n + 1)

--a.i) orden de evaluacion normal Respuesta
 misteriosa "abc" (gen 1)
=
foldr what (const []) "abc" (gen 1)
=
what "a" $ foldr what (const []) "bc" (gen 1)
=
what "a" $ foldr what (const []) "bc" (1 : gen 2)
=
("a", 1) : $ foldr what (const []) "bc" (gen 2)
=
("a", 1) : what "b" $ foldr what (const []) "c" (gen 2)
=
("a", 1) : what "b" $ foldr what (const []) "c" (2 : gen 3)
=
("a", 1) : ("b", 2) : $ foldr what (const []) "c" (gen 3)
=
("a", 1) : ("b", 2) : what "c" $ foldr what (const []) "" (gen 3)
=
("a", 1) : ("b", 2) : what "c" $ foldr what (const []) "" (3 : gen 4)
=
("a", 1) : ("b", 2) : ("c", 3) $ foldr what (const []) "" (gen 4)
=
("a", 1) : ("b", 2) : ("c", 3) : (const []) (gen 4)
=
("a", 1) : ("b", 2) : ("c", 3) : []
=
("a", 1) : ("b", 2) : ("c", 3) : []
=
("a", 1) : ("b", 2) : [("c", 3)]
=
("a", 1) : [("b", 2), ("c", 3)]
=
[("a", 1), ("b", 2), ("c", 3)]

-- ii) Orde de evaluacion aplicativo Respuesta
misteriosa "abc" (gen 1)
=
misteriosa "abc" (1 : gen 2)
=
misteriosa "abc" (1 : 2 : gen 3)
=
misteriosa "abc" (1 : 2 : 3 : gen 4)
=
misteriosa "abc" (1 : 2 : 3 : 4 : gen 5)
=
misteriosa "abc" (1 : 2 : 3 : 4 : 6 : gen 6)
.
.
.
--Evaluacion recursiva infinita de gen

--5 b) 
data Arbol a = Hoja | Rama a (Arbol a) (Arbol a)

--Su función debe cumplir con la siguiente firma:
foldA :: (a -> b -> b -> b) -> b -> Arbol a -> b

--5 b) Respuesta:

foldA :: (a -> b -> b -> b) -> b -> Arbol a -> b
foldA _ i Hoja = i 
foldA f i (Rama value left right) = f value (foldA f i left) (foldA f i right)


--5 c)

whatTF :: a
    -> (Arbol b -> Arbol (a, b))
    -> (Arbol b -> Arbol (a, b))
    -> Arbol b
    -> Arbol (a, b)
whatTF _ _ _  Hoja          = Hoja
whatTF x f g (Rama y i d)   = Rama (x, y) (f i) (g d)

sospechosa :: ???
sospechosa = foldA whatTF (const Hoja)

genA :: Int -> Arbol Int
genA n = Rama n (genA (n + 1)) (genA (n * 2))

arbolito :: Arbol Char
arbolito = Rama 'a' (Rama 'b' Hoja (Rama 'c' Hoja Hoja)) Hoja

-- i) Orden de evaluacion Normal Respuesta:

sospechosa arbolito (genA 1)
=
foldA whatTF (const Hoja) arbolito (genA 1)
=
foldA whatTF (const Hoja) (Rama 'a' 
                                (Rama 'b' 
                                       Hoja 
                                       (Rama 'c' Hoja Hoja)
                                ) 
                                Hoja
                          ) (genA 1)
=
whatTF 'a' (foldA whatTF (const Hoja) (Rama 'b'
                                             Hoja
                                             (Rama 'c' 
                                                    Hoja 
                                                    Hoja
                                             )
                                       )
            ) 
            (foldA whatTF (const Hoja) Hoja) 
            (genA 1)
= -- Evaluamos (genA 1)
whatTF 'a' (foldA whatTF (const Hoja) (Rama 'b'                     
                                            Hoja                    
                                            (Rama 'c' Hoja Hoja)    
                                      )                             
           (foldA whatTF (const Hoja) Hoja)                     
           (Rama 1                                                
                (genA (1 + 1))                               
                (genA (1 * 2))                                      
           )
= -- Evaluamos whatTF 'a' f g (Rama y i d) -:

--Rama ( x , y)

Rama ('a', 1) 
     ((foldA whatTF (const Hoja) (Rama 'b'                         
                                        Hoja                       
                                        (Rama 'c' Hoja Hoja)       
                                 )                                  
      )                                                            
      (genA (1 + 1))                                              
     ) 
     ((foldA whatTF (const Hoja) Hoja)                            
      (genA (1 * 2))                                             
     )
= -- Evaluamos el foldA que se encuentra más arriba
Rama ('a', 1) 
     (whatTF 'b' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)) (genA (1 + 1))) 
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
= -- Evaluamos (genA (1+1))

Rama ('a', 1) 
     (whatTF 'b' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)) (Rama 2 
                                                                                                         (genA (2 + 1))     ----i
                                                                                                         (genA (2 * 2))     ----d
                                                                                                   )
     )                                                                                           
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))
=
-- Evaluamos whatTF 'b' ---:
Rama ('a', 1) 
     (Rama ('b', 2)
           ((foldA whatTF (const Hoja) Hoja)                (genA (2 + 1)))
           (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)  (genA (2 * 2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos el foldA que se encuentra más arriba

Rama ('a', 1) 
     (Rama ('b', 2)
           ((const Hoja) (genA (2 + 1)))
           (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)  (genA (2 * 2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos (const Hoja) (genA (2 + 1))

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja
           (foldA whatTF (const Hoja) (Rama 'c' Hoja Hoja)  (genA (2 * 2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos foldA de más arriba

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja
           (whatTF 'c' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) Hoja) (genA (2 * 2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos (genA (2 * 2))

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           (whatTF 'c' (foldA whatTF (const Hoja) Hoja) (foldA whatTF (const Hoja) Hoja) (Rama 4
                                                                                               (genA(4+1))      
                                                                                               (genA(4*2))      
                                                                                          ) 
           )
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos whatTF 'c' ....

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                ((foldA whatTF (const Hoja) Hoja) (genA(4+1)))
                ((foldA whatTF (const Hoja) Hoja) (genA(4*2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos foldA de más arriba

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                ((const Hoja) (genA(4+1)))
                ((foldA whatTF (const Hoja) Hoja) (genA(4*2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= --- Evaluamos (const Hoja) (genA(4+1))

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                Hoja
                ((foldA whatTF (const Hoja) Hoja) (genA(4*2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos foldA de más arriba

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                Hoja
                ((const Hoja) (genA(4*2)))
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= --- Evaluamos (const Hoja) (genA(4*2))

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                Hoja
                Hoja
     )
     ((foldA whatTF (const Hoja) Hoja) (genA (1 * 2)))

= -- Evaluamos foldA de más arriba

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                Hoja
                Hoja
     )
     ((const Hoja) (genA (1 * 2)))

= -- Evaluamos (const Hoja) (genA (1 * 2))

Rama ('a', 1) 
     (Rama ('b', 2)
           Hoja 
           Rama ('c', 4)
                Hoja
                Hoja
     )
     Hoja

--- ii) Orden de evaluación Aplicativo Respuesta:
 

sospechosa arbolito (genA 1)
=
sospechosa arbolito Rama 1 
                         (genA (2)) 
                         (genA (2))
=
sospechosa arbolito Rama 1 
                         (Rama 2 (genA (3)) (genA (4))) 
                         (genA (2))
=
sospechosa arbolito Rama 1 
                         (Rama 2 (genA (3)) (genA (4))) 
                         (Rama 2 (genA (3)) (genA (4))) 
=
sospechosa arbolito Rama 1 
                         (Rama 2 
                               (genA (3)) 
                               (genA (4))
                         ) 
                         (Rama 2 
                               (genA (3)) 
                               (genA (4))
                         ) 
=
sospechosa arbolito Rama 1 
                         (Rama 2 
                               (Rama 3 (genA (4)) (genA (6))) 
                               (genA (4))
                         ) 
                         (Rama 2 
                               (genA (3)) 
                               (genA (4))
                         ) 
=
sospechosa arbolito Rama 1 
                         (Rama 2 
                               (Rama 3 (genA (4)) (genA (6))) 
                               (Rama 3 (genA (4)) (genA (6))) 
                         ) 
                         (Rama 2 
                               (genA (3)) 
                               (genA (4))
                         ) 
.
.
.
--Evaluacion recursiva infinita de genA. 
