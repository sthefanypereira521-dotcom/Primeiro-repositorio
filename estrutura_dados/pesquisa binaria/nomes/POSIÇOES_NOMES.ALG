Algoritmo "posiçoes_nomes"

Var
     nomes:vetor[1..7] de caractere
     nome:caractere
     esquerda, direita, meio:inteiro
     rodada:inteiro
     i:inteiro
     encontrado:logico
Inicio
      nomes[1] <- "ana"
      nomes[2] <- "bernado"
      nomes[3] <- "bruno"
      nomes[4] <- "carla"
      nomes[5] <- "daniel"
      nomes[6] <- "emilie"
      nomes[7] <- "sofie"

      Escreva("digite um nome para buscar: ")
      Leia(nome)
      escreval()

      esquerda <- 1
      direita <- 7
      encontrado <- falso

      enquanto (esquerda <= direita) faca
         Escreva("Rodada",rodada,".")



         escreval()
         escreva("intervalo atual: ")
         para i de esquerda ate direita faca
            escreva(nomes[i], " ")
         fimpara
         escreval()


         meio <-(esquerda + direita) div 2
         meio <- (esquerda + direita) div 2
         Escreva("meio atual: ", nomes[meio])
         escreval()
         
         
         escreval()
         se(nomes[meio] = nome)entao
            encontrado <- verdadeiro
            escreva("nome encontrado ")
            escreval()
            esquerda <- direita + 1
         senao
            se(nomes[meio] < nome)entao
               Escreval(nomes[meio], " < ",nome, ",buscando a direita..")
               esquerda <- meio + 1
            senao
               escreval(nomes[meio]," > ",nome, ",buscando a esquerda...")
               direita <- meio - 1
            fimse
         fimse
         

         rodada <- rodada + 1

      fimenquanto

      se(encontrado = falso)entao
         Escreval("nome nao encontrado")
      fimse

Fimalgoritmo