Feature: Calculadora
    Como: usuario
    Quiero: realizar operaciones de suma en la calculadora
    Para: verificar que los calculos sean correctos

  @calculadora
  Scenario Outline: Suma dos numeros
    Given ingreso el primer digito "<num1>"
    And ingreso el segundo digito "<num2>"
    When presiono el boton suma
    Then El resultado deberia ser "<result>"

    Examples: 
      | num1 | num2 | result |
      |    5 |    3 |      8 |
      |   10 |    7 |     17 |
      |    2 |   20 |     30 |
