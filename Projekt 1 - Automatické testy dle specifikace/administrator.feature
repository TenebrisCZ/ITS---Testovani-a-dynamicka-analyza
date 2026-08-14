Feature: Administration of items, customers and orders

    Background: 
        Given Logged in user has administrator role

    # 23
    Scenario: View orders
        Given administrator is at "Dashboard" page
        When administrator clicks on "View more..." at "Total orders" tab
        Then "Order List" is shown

    # 24
    Scenario: Display order details
        Given administrator is at order list page
        And "<order>" is in order list
        When administrator clicks on "View" button in "Action" row
        Then detail page for "<order>" is shown

    # 25
    Scenario: Edit order
        Given administrator is at "<order>" detail page
        And all "<required>" fields are filled
        When administrator edits "<required>" field
        And clicks on "Confirm" button
        Then alert with "Success: You have modified orders!" is shown
        And "<required>" field is changed

        Examples:
            | required |
            | Customer |
            | Shopping Address |
            | Shipping Method |
            | Payment Method |
            | Product |

    # 26
    Scenario: Delete order
        Given administrator is at order list page
        And "<order>" is in order list
        When administrator select "<order>"
        And clicks on "Delete" button
        Then "<order>" is not in order list

    # 27
    Scenario: Create order - show form
        Given administrator is at order list page
        When administrator clicks on "Add new" button
        Then page with form for creating order is shown

    # 28
    Scenario: Create order 
        Given administrator is at page with form for creating "<order>"
        When administrator fills all "<required>" field
        And clicks on "Confirm" button
        Then alert with "Success: You have modified orders!" is shown
        And "<order>" appears in order list

        Examples:
            | required |
            | Customer |
            | Shopping Address |
            | Shipping Method |
            | Payment Method |
            | Product |

    # 29
    Scenario: View customers
        Given administrator is at "Dashboard" page
        And "<user>" account exists
        When administrator clicks on "View more..." at "Total customers" tab
        Then customer list includes "<user>"

    # 30
    Scenario: View customer detail page
        Given administrator is at customer list page
        And "<user>" is in customer list
        When administrator clicks on "Edit" button
        Then form for editing "<user>" is shown

    # 31
    Scenario: Add customer - form
        Given administrator is at customer list page
        When administrator clicks on "Add new" button
        Then page with form for adding customer is shown

    #32
    Scenario: Add customer
        Given administrator is at page with form for creating "<user>" account
        When administrator fills all "<required>" field
        And clicks on "Save" button
        Then alert with "Success: You have modified customers!" is shown
        And "<user>" appears in customer list

        Examples:
            | required |
            | First Name |
            | Last Name |
            | E-Mail |
            | Password |
            | Confirm |

    # 33
    Scenario: Delete customer
        Given administrator is at customer list page
        And "<user>" is in order list
        When administrator select "<user>"
        And clicks on "Delete" button
        Then "<user>" is not in customer list

    # 34
    Scenario: Edit customer detail
        Given administrator is at "<user>" edit page at "General" tab
        When administrator changes "<field>"
        And all "<required>" fields are filled
        And administrator clicks on "Save" button
        Then success alert is shown
        And "<field>" is changed

        Examples:
            | required |
            | First Name |
            | Last Name |
            | E-Mail |
            | Password |
            | Confirm |

        Examples:
            | fields |
            | First Name |
            | Last Name |
            | E-Mail |
            | Password |
            | Confirm |
            | Store |
            | Customer Group |
            | Newsletter |
            | Status |
            | Safe |

    # 35
    Scenario: Add customer address - form
        Given administrator is at "<user>" edit page at "Addresses" tab
        When administrator clicks on "Add Address" button
        Then page with form for creating address is shown

    # 36
    Scenario: Add customer address
        Given administrator is at page with form for creating "<address>"
        When administrator fills all "<required>" fields
        And clicks on "Save" button
        Then alert with "Succes: You have modified customers!" is shown

        Examples:
            | required |
            | First Name |
            | Last Name |
            | Address 1 |
            | City |
            | Country |
            | Region / State |

    # 37
    Scenario: View categories
        Given administrator is at navigation tab at "Dashboard" page
        When administrator clicks on "Catalog"
        And selects "Categories"
        Then "Category list" page is shown

    # 38
    Scenario: Add category - form
        Given administrator is at category list page
        When administrator clicks on "Add New"
        Then "Add category" page with form is shown

    # 39
    Scenario: Add category
        Given administrator is at "Add category" page
        When administrator fills "<required>" fields for "<category>"
        And clicks on "Save" button
        Then alert with "Success: You have modified categories!" is shown
        And "<category>" is added to category list

    Examples:
        | required |
        | Category Name |
        | Meta Tag Title |
        | Keyword |

    # 40
    Scenario: Remove category
        Given administrator is at category list page
        When administrator selects "<category>"
        And clicks on "Delete"
        Then "<category>" is not in category list

    # 41
    Scenario: Edit category
        Given administrator is at "Edit Category" page
        When administrator changes "<field>"
        And all "<required>" fields are filled
        And administrator clicks on "Save" button
        Then alert with "Success: You have modified categories!" is shown
        And "<field>" is changed

        Examples:
            | field |
            | Category Name |
            | Description |
            | Mega Tag Title |
            | Keyword |
            | Layout Override |

        Examples: 
            | required |
            | Category Name |
            | Meta Tag Title |
            | Keyword |
        
    # 42
    Scenario: View products
        Given administrator is at navigation tab at "Dashboard" page
        When administrator clicks on "Catalog"
        And selects "Products"
        Then "Product List" page is shown

    # 43
    Scenario: Add product - form
        Given administrator is at product list page
        When administrator clicks on "Add New"
        Then "Add Product" page with form is shown

    # 44
    Scenario: Add product
        Given administrator is at "Add product" page
        When administrator fills "<required>" fields for "<product>"
        And clicks on "Save" button
        Then alert with "Success: You have modified products!" is shown
        And "<product>" is added to product list

        Examples:
            | required |
            | Product Name |
            | Model |
            | Meta Tag Title |
            | Keyword |

    # 45
    Scenario: Remove product
        Given administrator is at product list page
        When administrator selects "<product>"
        And clicks on "Delete"
        Then "<product>" is not in product list

    # 46
    Scenario: Edit product 
        Given administrator is at "Edit product" page
        When administrator changes "<field>"
        And all "<required>" fields are filled
        And administrator clicks on "Save" button
        Then alert with "Success: You have modified products!" is shown
        And "<field>" is changed

        Examples:
            | field |
            | Product Name |
            | Description |
            | Model |
            | Meta Tag Title |
            | Product Tags |
            | Keyword |
            | EAN |
            | Price |
            | Location |

        Examples: 
            | required |
            | Product Name |
            | Model |
            | Meta Tag Title |
            | Keyword |