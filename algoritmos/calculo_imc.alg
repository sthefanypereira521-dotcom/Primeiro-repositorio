algoritmo "calculoIMC"
var 
      M, A , IMC : Real 
inicio 
            Escreva ("massa (kg)  : " ) 
            Leia (M)
            Escreva ("altura (m)  : " ) 
            Leia (A)
            IMC <- M / ( A ^ 2 )
            Escreva ("IMC:   " ,  IMC:  )
            Se (IMC >= 18.5 ) e ( IMC < 25) Entao 
                  Escreva (" estou na faixa de peso ideal " )
            senao 
                  Escreva (" nao estou na faixa de peso ideal ")
            FimSe
   fimalgoritmo
