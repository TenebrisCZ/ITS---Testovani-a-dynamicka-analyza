Feature: User creates order

    # 21
    Scenario: User displays checkout page
        Given user is at homepage
        And "<item>" is in shopping cart
        When user clicks on "Checkout" button
        Then "Checkout page" appears

    # 22
    Scenario Outline: User creates order
        Given unregistered user is at "Checkout page"
        When user fills all "<required>" fields
        And clicks on "Confirm Order" button
        Then page with "Your order has been placed!" appears

        Examples:
            | required |
            | First Name |
            | Last Name |
            | E-Mail |
            | Address 1 |
            | City |
            | Post Code |
            | Country |
            | Region / State |
