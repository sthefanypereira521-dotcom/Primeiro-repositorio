Algoritmo "Fatorial"

Var
   C, N, F : inteiro

Inicio
      Escreva ( "Digite um numero : " )
      Leia(N)
      C <- N
      F <- 1
      Repita
            F <- F * C 
            C <- C - 1
         Ate (C < 1)
         Escreva ( " o valor do Fatorial de  "  ,  N ,  " e igual  a "  ,  F )
FimAlgoritmo
