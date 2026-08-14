Feature: User registration

    # 14
    Scenario Outline: User wants to create account at checkout
        Given unregistered user is at "<item>" checkout page
        When "Register Account" option is sellected
        And "<required>" fields are filled
        And user clicks on "Continue" button
        Then alert with text "Success: Yout account has been created!" is shown

        Examples:
        | item |
        | Canon EOS 5D |
		| iPhone |
		| Samsung SyncMaster 941BW |
		| iMac |

        Examples:
        | required |
        | First Name |
        | Last Name |
        | E-Mail |
        | Address 1 |
        | City |
        | Country |
        | Region / State |
        | Password | 
        | Privacy Policy |

    # 15
    Scenario Outline: User wants to create account at checkout - missing required
        Given unregistered user is at "<item>" checkout page
        When "Register Account" option is sellected
        And any of "<required>" fields isn't filled
        And user clicks on "Continue" button
        Then alert for "<required>" field is shown

        Examples:
        | item |
        | Canon EOS 5D |
		| iPhone |
		| Samsung SyncMaster 941BW |
		| iMac |

        Examples:
        | required |
        | First Name |
        | Last Name |
        | E-Mail |
        | Address 1 |
        | City |
        | Country |
        | Region / State |
        | Password | 
        | Privacy Policy |

    # 16
    Scenario Outline: User won't fill all required fields in registration form
		Given unregistered user is on registration page
		When "<required>" field is empty
        Then alert for "<required>" field is shown

        Examples:
        | required |
        | First Name |
        | Last Name |
        | E-Mail |
        | Password |

    # 17
	Scenario Outline: User fills registration form
		Given unregistered user is on registration page
		When user inserts all "<required>" details
        And user clicks on "Continue" button
		Then results page shows "Your Account Has Been Created!" message

        Examples:
        | required |
        | First Name |
        | Last Name |
        | E-Mail |
        | Password |

    # 18
    Scenario: Registered user drop-down menu
        Given logged in user is at homepage
        When user clicks on "My Account"
        Then drop-down menu with following information is shown:
        | My Account |
        | Order History |
        | Transactions |
        | Downloads |
        | Logout |

    # 19
    Scenario: Registered user wants to display order history
        Given logged in user is at homepage
        When user clicks on "My Account"
        And user clicks on "Order History"
        Then order history page is shown
    
    # 20
    Scenario: View order history
        Given logged in user is at homepage
        And user ordered "<number>" times
        When user clicks on "My Account"
        And user clicks on "Order History"
        Then order history page with "<number>" orders is shown

