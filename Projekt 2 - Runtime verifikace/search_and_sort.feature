Feature: Items sorting and searching

	# 7
	Scenario Outline: Searching for item
		Given user is at homepage
		When user search "<item>"
		Then results page shows "<item>"

		Examples:
			| item |
			| Canon EOS 5D |
			| iPhone |
			| Samsung SyncMaster 941BW |
			| iMac |

	# 8
	Scenario Outline: User wants to view items in category
		Given user is at homepage
		When user clicks on "<category>"
		Then "<category>" page with "<items>" is shown

		Examples:
			| category | items |
			| Tablets | Samsung Galaxy Tab 10.1 |
			| Cameras | Canon EOS 5D |
			| Cameras | Nikon D300 |

	# 9
	Scenario: User wants to view items in empty category
		Given user is at homepage
		When user clicks on "Software"
		Then results page shows "There are no products to list in this category."

	# 10
	Scenario Outline: User wants to view subcategories
		Given user is at homepage
		When user select "<category>"
		Then drop-down menu containing "<subcategory>" is shown
		
		Examples:
		| category | subcategory |
		| Desktops | PC |
		| Desktops | Mac |
		| Components | Monitors |
		| Components | Printers |
		| Components | Scanners |

	# 11
	Scenario Outline: User wants to view items in subcategory
		Given user is at homepage
		And "Desktops" subcategory drop-down menu is shown
		When user clicks on "Mac"
		Then results page shows "<item>"

		Examples:
		| item |
		| iMac | 

	# 12
	Scenario: User wants to view items in empty subcategory
		Given user is at homepage
		And "Desktops" subcategory drop-down menu is shown
		When user clicks on "PC"
		Then results page shows "There are no items to list in this category."

	# 13
	Scenario Outline: User wants to view item detail
		Given user is at "<category>" category page
		When user clicks on "<item>"
		Then "<item>" detail page is shown

		Examples:
		| category | item |
		| Mac | iMac |
		| Cameras | Canon EOS 5D |
		| Tablets | Samsung Galaxy Tab 10.1 |