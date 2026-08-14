Feature: Costumer creates order

    # 1
	Scenario: Adding item to shopping cart
		Given user is on "<item>" detail page
		When user fills options on "<item>" detail page
        And user clicks on "Add to cart" button
		Then shopping cart contains "<item>"

        Examples:
        | item |
        | Canon EOS 5D |
		| iPhone |
		| Samsung SyncMaster 941BW |
		| iMac |

    # 2
    Scenario: Check shopping cart
        Given user is on homepage
        And "<item>" is in shopping cart
        When user clicks on "Shopping Cart"
        Then Shopping cart page containg "<item>" is shown

        Examples:
        | item |
        | Canon EOS 5D |
		| iPhone |
		| Samsung SyncMaster 941BW |
		| iMac |

    # 3
    Scenario: Change item quantity in shopping cart
        Given user is on shopping cart page
        And "iMac" is in shopping cart
        When user change quantity to "<number>" for "iMac" row
        And clicks on "Udpdate" button
        Then alert containing "Success: You have modified yor shopping cart!" is shown
        And "Quantity" for "iMac" row should be "<number>"
        And "Total price" for "iMac" row should be "Unit Price" * "<number>"

    # 4
    Scenario: Remove item from shopping cart
        Given user is on shopping cart page
        And "iMac" is in shopping cart
        When user clicks on "Remove" button for "iMac" row
        Then shopping cart does not contain "iMac"

    # 5
    Scenario: Continue to checkout
        Given user is on shopping cart page
        And "iMac" is in shopping cart
        And alert "Products marked with *** are not available in the desired quantity or not in stock!" isn't displayed
        When user clicks on "Checkout" button
        Then Checkout page is shown

    # 6
    Scenario: Continue to checkout with items out of stock or unavailable
        Given user is on shopping cart page
        And "<item>" is in shopping cart
        And alert "Products marked with *** are not available in the desired quantity or not in stock!" is displayed
        When user clicks on "Checkout" button
        Then Shopping cart is refreshed

        Examples:
        | item |
        | Canon EOS 5D |
		| iPhone |
		| Samsung SyncMaster 941BW |
		| iMac |

