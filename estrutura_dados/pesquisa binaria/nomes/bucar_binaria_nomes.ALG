Algoritmo "pesquisa_nomes"

Var
     nomes:vetor[1..7] de caractere
     nome:caractere
     esquerda, direita, meio:inteiro
     encontrado:logico
Inicio
      nomes[1] <- "ana"
      nomes[2] <- "bruno"
      nomes[3] <- "carla"
      nomes[4] <- "carlos"
      nomes[5] <- "daniel"
      nomes[6] <- "emilie"
      nomes[7] <- "sofie"

      Escreva("digite um nome para buscar: ")
      Leia(nome)
      
      esquerda <- 1
      direita <- 7
      encontrado <- falso
      
      enquanto (esquerda <= direita) faca
         meio <-(esquerda + direita) div 2
         
         se(nomes[meio] = nome)entao
            encontrado <- verdadeiro
            escreva("nome encontrado na posiçao: ",meio)
            esquerda <- direita + 1
         senao
            se(nomes[meio] < nome)entao
               esquerda <- meio + 1
            senao
               direita <- meio - 1
            fimse
         fimse
      fimenquanto
            
      se(encontrado = falso)entao
         Escreva("nome nao encontrado")
      fimse

Fimalgoritmo