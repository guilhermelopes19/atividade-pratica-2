programa {

  inclua biblioteca Matematica --> mat

  funcao inicio() {
    real grausF, grausC

    escreva("Digite uma temperatura F: ")
    leia(grausF)

    grausC = 5 * ((grausF - 32) / 9)

    escreva("A temperatura ", grausF, "F  igual a ", grausC, "C")
  }
}
