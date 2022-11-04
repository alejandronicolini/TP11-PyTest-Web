@FeatureNuevoRegistro
Feature: Registro de cuenta de usuario

  Background:
    Given el usuario esta en la home page de automationtesting.in
    Given clic on My Account Menu2


# (1. Registration-Sign-in)
  # 1) Open the browser
  # 2) Enter the URL “http://practice.automationtesting.in/”
  # 3) Click on My Account Menu
  # 4) Enter registered Email Address in Email-Address textbox
  # 5) Enter your own password in password textbox
  # 6) Click on Register button
  # 7) User will be registered successfully and will be navigated to the Home page
  @RegistroExitoso
  Scenario Outline: Registro Exitoso de usuario nuevo
    Given enter Email <email> in Email-Address textbox
    Given enter password <password> in password textbox
    When click on Register button
    Then user will be registered successfully message
    Then will be navigated to the Home page
    Examples:
      | email                          | password              |
      | alejandronicolini201@ymail.com | AleNicoliniN1N125-5-- |


  # (2. Registration with invalid data)
    # 1) Open the browser
    # 2) Enter the URL “http://practice.automationtesting.in/”
    # 3) Click on My Account Menu
    # 4.1) Enter invalid Email Address in Email-Address textbox
    # 4.2) Enter empty Email Address in Email-Address textbox
    # 4.3) Enter valid Email Address in Email-Address textbox
    # 4.4) Enter empty Email Address in Email-Address textbox
    # 5.1) Enter your own password in password textbox
    # 5.2) Enter your own password in password textbox
    # 5.3) Enter empty password in password textbox
    # 5.4) Enter empty password in password textbox
    # 6) Click on Register button
    # 7.1) Registration must fail with a warning message(ie You must enter a valid email address)
    # 7.2) Registration must fail with a warning message(ie please provide valid email address)
    # 7.3) Registration must fail with a warning message(ie please enter an account password)
    # 7.4) Registration must fail with a warning message(ie please provide valid email address)
  @RegistroFallido
  Scenario Outline: Registro de Usuario Fallido con Mensaje de Error
    Given enter Email <email> in Email-Address textbox
    Given enter password <password> in password textbox
    When click on Register button
    Then Registration must fail with a warning message  <mensaje>

    Examples:
      | email               | password          | mensaje                                      |
      | florencia@gmail     | Florencia123456-- | Error: Please provide a valid email address. |
      |                     | Florencia123456-- | Error: Please provide a valid email address. |
      | florencia@gmail.com |                   | Error: Please enter an account password.     |
      |                     |                   | Error: Please provide a valid email address. |

