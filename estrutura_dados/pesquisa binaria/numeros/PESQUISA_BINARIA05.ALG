Algoritmo "pesquisa_binaria01"
// console no meu pc nao esta amostrando o input
// em tela pequena, so em tela cheia.

Var
     vet:vetor[1..50] de inteiro

     i, ini, fim, meio, valor: inteiro

     achou: logico

Inicio
       para i de 1 ate 30 faca
            vet[i] <-  i * 2
                   Escreva(vet[i], " ")
       FimPara


       Escreva("digite um numero para iniciar : "," ")
       Leia(valor)
       EscrevaL( )
       EscrevaL( )

       
       

       ini <- 1
       fim <- 30
       achou <- falso

       Enquanto ini <= fim Faca
          EscrevaL( )
          EscrevaL("intervalo atual: " )
          EscrevaL( )
          
          Para i de ini ate fim Faca
            Escreva(vet[i], " " )
          FimPara
          EscrevaL( )
          
          meio <- (ini + fim) div 2
          EscrevaL( )
          EscrevaL("meio atual:",vet[meio])
          EscrevaL( )


          Se vet[meio] = valor Entao
             Escreva( )
             Escreva("achou na posiçao " , meio )
             EscrevaL( )
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