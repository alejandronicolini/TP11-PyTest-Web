Feature:Login SauceDemo

@example
  Scenario Outline: El usuario se loguea correctamente
    Given Se encuentra en la pagina de Login
    When Ingresa el usuario con <username>
    And Ingresa la password con <password>
    And Clic en el boton login
    Then Aparece el home correctamente
    Examples:
      | username      | password     |
      | standard_user | secret_sauce |


  Scenario Outline: Login Invalido
    Given Se encuentra en la pagina de Login
    When Ingresa el usuario con <username>
    And Ingresa la password con <password>
    And Clic en el boton login
    Then Aparece el mensaje <errorMensaje>
    Examples:
      | username      | password | errorMensaje                                                              |
      | qwert         | 1234     | Epic sadface: Username and password do not match any user in this service |
      | standard_user |          | Epic sadface: Password is required                                        |
      |               | 1234     | Epic sadface: Username is required                                        |
      |               |          | Epic sadface: Username is required                                        |

