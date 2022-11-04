@FeatureLogin
Feature: Login de usuario

  Background:
    Given el usuario esta en la home page de practice.automationtesting.in
    Given clic on My Account Menu


# (1. Log-in with valid username and password)
  # 1) Open the browser
  # 2) Enter the URL “http://practice.automationtesting.in/”
  # 3) Click on My Account Menu
  # 4) Enter registered username in username textbox
  # 5) Enter password in password textbox
  # 6) Click on login button
  # 7) User must successfully login to the web page
  @LoginExitoso
  Scenario: 1. Log-in with valid username and password
    Given enter username alejandronicolini10@ymail.com in username textbox1
    Given enter password Ale1234567-- in password textbox login1
    When click on login button
    Then user must successfully login to the web page, message: Hello alejandronicolini10


# (2-3-4-5. Log-in with incorrect username and incorrect password.)
  # 1) Open the browser
  # 2) Enter the URL “http://practice.automationtesting.in/”
  # 3) Click on My Account Menu
  # 4) Enter incorrect username in username textbox
  # 5) Enter incorrect password in password textbox.
  # 6) Click on login button
  # 7) Proper error must be displayed(ie Invalid username) and prompt to enter login again
  @LoginFallido
  Scenario Outline: 2-3-4-5. Log-in Fallido
    Given enter username <username> in username textbox
    Given enter password <password> in password textbox login
    When click on login button
    Then Proper error must be displayed <message> and prompt to enter login again
    Examples:
      | username                    | password   | message                                                                                                                           |
      | alejandro                   | 12345      | Error: the username alejandro is not registered on this site. If you are unsure of your username, try your email address instead. |
      | alejandronicolini@ymail.com |            | Error: Password is required.                                                                                                      |
      |                             | Ale123456- | Error: Username is required.                                                                                                      |
      |                             |            | Error: Username is required.                                                                                                      |


# (6. Log-in -Password should be masked)
  # 1) Open the browser
  # 2) Enter the URL “http://practice.automationtesting.in/”
  # 3) Click on My Account Menu
  # 4) Enter the password field with some characters.
  # 5) The password field should display the characters in asterisks or bullets such that the password is not visible on the screen
  @PassMasked
  Scenario: 6. Log-in -Password should be masked
    When enter the password field with some characters.
    When the password field should display the characters in asterisks