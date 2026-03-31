Algoritmo "SomadorNumerico"

Var
   Contador, N, S, maior : inteiro

Inicio
   Contador <- 1
   S <- 0

   Escreva("Digite o 1º valor => ")
   Leia(N)

   maior <- N
   S <- N
   Contador <- 2

   Enquanto (Contador <= 5) faca
      Escreva("Digite o ", Contador, "º valor => ")
      Leia(N)

      Se (N > maior) entao
         maior <- N
      FimSe

      S <- S + N
      Contador <- Contador + 1
   FimEnquanto

   Escreva("A soma de todos os valores foi ", S)
   Escreva("O maior valor digitado foi ", maior)

FimAlgoritmo
