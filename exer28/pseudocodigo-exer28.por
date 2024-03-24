programa {

  inclua biblioteca Matematica --> mat

  funcao inicio() {
    real a, b, c

    escreva("Digite o coeficiente a: ")
    leia(a)

    se(a == 0) {
      escreva("O coeficiente a deve ser maior que 0!")
    } senao {
      escreva("Digite o coeficiente b: ")
      leia(b)

      escreva("Digite o coeficiente c: ")
      leia(c)

      real delta = mat.potencia(b, 2) - 4 * a * c

      se(delta > 0) {
        real x1 = (b + mat.raiz(delta, 2)) / (2 * a)
        real x2 = (b - mat.raiz(delta, 2)) / (2 * a)

        escreva("x1 = ", x1, "\n")
        escreva("x2 = ", x2)
      } senao se(delta == 0) {
        real x = (b) / (2 * a)

        escreva("x = ", x)
      } senao {
        escreva("Delta menor que 0!")
      }
    }
  }
}
