Algoritmo "pesquisa_binaria01"

Var
     vet:vetor[1..25] de inteiro

     i, ini, fim, meio, valor: inteiro

     achou: logico

Inicio
       para i de 1 ate 25 faca
            vet[i] <-  i * 3
                   EscrevaL(vet[i])
       FimPara

       Escreva("digite um numero: ")
       Leia(valor)

       ini <- 1
       fim <- 50
       achou <- falso

       Enquanto ini <= fim Faca
          meio <- (ini + fim) div 2

          Se vet[meio] = valor Entao
             Escreva("achou na posiçao " , meio )
             achou <- verdadeiro
             ini <- fim + 1

          Senao
             Se valor < vet[meio] Entao
                fim <- meio - 1

             Senao
                ini <- meio + 1
             FimSe
          FimSe
       FimEnquanto

       Se achou = falso Entao
          Escreva("numero nao encontrado... " )
       FimSe
Fimalgoritmo