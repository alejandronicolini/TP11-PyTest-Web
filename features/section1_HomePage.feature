@FeatureHomePage
Feature: Seccion Home Page

  Background:
    Given el usuario esta en la home page de practice.automationtesting
    Given clic on Shop Menu
    When click on Home menu button


# (1. Home Page with three Sliders only)
  # 1) Open the browser
  # 2) Enter the URL “http://practice.automationtesting.in/”
  # 3) Click on Shop Menu
  # 4) Now click on Home menu button
  # 5) Test whether the Home page has Three Sliders only
  # 6) The Home page must contains only three sliders
  Scenario: 1. Home Page with three Sliders only
    Then the Home page has Three Sliders only


# (2. Home page with three Arrivals only)
  # 1) Open the browser
  # 2) Enter the URL “http://practice.automationtesting.in/”
  # 3) Click on Shop Menu
  # 4) Now click on Home menu button
  # 5) Test whether the Home page has Three Arrivals only
  # 6) The Home page must contains only three Arrivals
  Scenario: 2. Home page with three Arrivals only
    Then the Home page has Three Arrivals only


# (3. Home page - Images in Arrivals should navigate)
  # 1) Open the browser
  # 2) Enter the URL “http://practice.automationtesting.in/”
  # 3) Click on Shop Menu
  # 4) Now click on Home menu button
  # 5) Test whether the Home page has Three Arrivals only
  # 6) The Home page must contains only three Arrivals
  # 7) Now click the image in the Arrivals
  # 8) Test whether it is navigating to next page where the user can add that book into his basket.
  # 9) Image should be clickable and should navigate to next page where user can add that book to his basket
  Scenario: 3. Home page - Images in Arrivals should navigate
    Then the Home page has Three Arrivals only
    Then click the image in the Arrivals
    Then navigating to next page where the user can add that book into his basket


# (4. Home page - Arrivals-Images-Description)
  # 1) Open the browser
  # 2) Enter the URL “http://practice.automationtesting.in/”
  # 3) Click on Shop Menu
  # 4) Now click on Home menu button
  # 5) Test whether the Home page has Three Arrivals only
  # 6) The Home page must contains only three Arrivals
  # 7) Now click the image in the Arrivals
  # 8) Test whether it is navigating to next page where the user can add that book into his basket.
  # 9) Image should be clickable and should navigate to next page where user can add that book to his basket
  # 10) Click on Description tab for the book you clicked on.
  # 11) There should be a description regarding that book the user clicked on
  Scenario: 4. Home page - Arrivals-Images-Description
    Then the Home page has Three Arrivals only
    Then click the image in the Arrivals
    Then navigating to next page where the user can add that book into his basket
    Then click on Description tab for the book you clicked on
    Then there should be a description regarding that book the user clicked on


# (5. Home page - Arrivals-Images-Reviews)
  # 1) Open the browser
  # 2) Enter the URL “http://practice.automationtesting.in/”
  # 3) Click on Shop Menu
  # 4) Now click on Home menu button
  # 5) Test whether the Home page has Three Arrivals only
  # 6) The Home page must contains only three Arrivals
  # 7) Now click the image in the Arrivals
  # 8) Test whether it is navigating to next page where the user can add that book into his basket.
  # 9) Image should be clickable and should navigate to next page where user can add that book to his basket
  # 10) Now click on Reviews tab for the book you clicked on
  # 11) There should be a Reviews regarding that book the user clicked on
  Scenario: 5. Home page - Arrivals-Images-Reviews
    Then the Home page has Three Arrivals only
    Then click the image in the Arrivals
    Then navigating to next page where the user can add that book into his basket
    Then click on Reviews tab for the book you clicked on
    Then there should be a Reviews regarding that book the user clicked on