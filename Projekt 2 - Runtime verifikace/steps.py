from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@given(u'Logged in user has administrator role')
def step_impl(context):
    context.driver.get("{}/administration".format(context.BASE_URL))
    context.driver.find_element(By.ID, "input-username").send_keys("user")
    context.driver.find_element(By.ID, "input-password").send_keys("bitnami")
    context.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']").click()


@given(u'administrator is at "Dashboard" page')
def step_impl(context):
    context.driver.get('{}/administration/index.php?route=common/dashboard'.format(context.BASE_URL))


@when(u'administrator clicks on "View more..." at "Total orders" tab')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div[1]/div/div[3]/a").click()


@then(u'"Order List" is shown')
def step_impl(context):
    assert context.driver.find_element(By.ID, "order")


@given(u'administrator is at order list page')
def step_impl(context):
    context.driver.get('{}/administration/index.php?route=sale/order'.format(context.BASE_URL))


@given(u'"<order>" is in order list')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='form-order']/div[1]/table/tbody/tr[1]/td[2]").text == "15"

@when(u'administrator clicks on "View" button in "Action" row')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='form-order']/div[1]/table/tbody/tr[1]/td[9]/a").click()


@then(u'detail page for "<order>" is shown')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[1]/div[1]/text()") == " Order (#15)"


@given(u'administrator is at navigation tab at "Dashboard" page')
def step_impl(context):
    context.driver.get('{}/administration/index.php?route=common/dashboard'.format(context.BASE_URL))


@when(u'administrator clicks on "Catalog"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='menu-catalog']/a").click()


@when(u'selects "Categories"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='collapse-1']/li[1]/a").click()


@then(u'"Category list" page is shown')
def step_impl(context):
    context.driver.get("{}/administration/index.php?route=catalog/category".format(context.BASE_URL))


@given(u'administrator is at category list page')
def step_impl(context):
    context.driver.get("{}/administration/index.php?route=catalog/category".format(context.BASE_URL))

@when(u'administrator clicks on "Add New"')
def step_impl(context):
    context.find_element(By.XPATH, "//*[@id='content']/div[1]/div/div/a").click()


@then(u'"Add category" page with form is shown')
def step_impl(context):
    context.driver.get("{}/administration/index.php?route=catalog/category|form".format(context.BASE_URL))


@when(u'user clicks on "Checkout" button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='top']/div/div[2]/ul/li[5]/a").click()


@then(u'"Checkout page" appears')
def step_impl(context):
    context.driver.get("{}//en-gb?route=checkout/cart".format(context.BASE_URL))


@given(u'unregistered user is at "Checkout page"')
def step_impl(context):
    context.driver.get("{}//en-gb?route=checkout/cart".format(context.BASE_URL))


@given(u'unregistered user is at "Canon EOS 5D" checkout page')
def step_impl(context):
    context.driver.get("{}/en-gb?route=checkout/checkout".format(context.BASE_URL))
    context.driver.find_element(By.XPATH, "//*[@id='checkout-confirm']/div[1]/table/tbody/tr/td[1]/a").text == "Canon EOS 5D"


@given(u'unregistered user is at "iPhone" checkout page')
def step_impl(context):
    context.driver.get("{}/en-gb?route=checkout/checkout".format(context.BASE_URL))
    context.driver.find_element(By.XPATH, "//*[@id='checkout-confirm']/div[1]/table/tbody/tr/td[1]/a").text == "iPhone"


@given(u'unregistered user is at "Samsung SyncMaster 941BW" checkout page')
def step_impl(context):
    context.driver.get("{}/en-gb?route=checkout/checkout".format(context.BASE_URL))
    context.driver.find_element(By.XPATH, "//*[@id='checkout-confirm']/div[1]/table/tbody/tr/td[1]/a").text == "Samsung SyncMaster 941BW"


@given(u'unregistered user is at "iMac" checkout page')
def step_impl(context):
    context.driver.get("{}/en-gb?route=checkout/checkout".format(context.BASE_URL))
    context.driver.find_element(By.XPATH, "//*[@id='checkout-confirm']/div[1]/table/tbody/tr/td[1]/a").text == "iMac"


@given(u'unregistered user is at "<item>" checkout page')
def step_impl(context):
    context.driver.get("{}/en-gb?route=checkout/checkout".format(context.BASE_URL))


@when(u'"First Name" fields are filled')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("Karel")


@when(u'"Last Name" fields are filled')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("Novak")


@when(u'"E-Mail" fields are filled')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("example@email.cz")


@when(u'"Address 1" fields are filled')
def step_impl(context):
    context.driver.find_element(By.ID, "input-shipping-address-1").send_keys("Hrbitovni 11")


@when(u'"City" fields are filled')
def step_impl(context):
    context.driver.find_element(By.ID, "input-shipping-city").send_keys("Praha")


@when(u'"Country" fields are filled')
def step_impl(context):
    select = Select(context.driver.find_element(By.ID, "input-shipping-country"))
    select.select_by_value('244')


@when(u'"Region / State" fields are filled')
def step_impl(context):
    select = Select(context.driver.find_element(By.ID, 'input-shipping-zone'))
    select.select_by_value('3513')


@when(u'"Password" fields are filled')
def step_impl(context):
    context.driver.find_element(By.ID, "input-password").send_keys("Heslo13.")


@when(u'"Privacy Policy" fields are filled')
def step_impl(context):
    select = Select(context.driver.find_element(By.ID, 'input-register-agree'))
    select.select_by_value('1')


@when(u'any of "<required>" fields isn\'t filled')
def step_impl(context):
    context.driver.find_element(By.ID, "input-shipping-postcode").send_keys("")


@when(u'any of "First Name" fields isn\'t filled')
def step_impl(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("")


@when(u'any of "Last Name" fields isn\'t filled')
def step_impl(context):
    context.driver.find_element(By.ID, "input-lastname").send_keys("")


@when(u'any of "E-Mail" fields isn\'t filled')
def step_impl(context):
    context.driver.find_element(By.ID, "input-email").send_keys("")


@when(u'user search "Canon EOS 5D"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='search']/input").send_keys("Canon EOS 5D")
    context.driver.find_element(By.XPATH, "//*[@id='search']/button").click()


@then(u'results page shows "Canon EOS 5D"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='product-list']/div/form/div/div[2]/div[1]/h4/a").text == "Canon EOS 5D"


@when(u'user search "iPhone"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='search']/input").send_keys("iPhone")
    context.driver.find_element(By.XPATH, "//*[@id='search']/button").click()


@then(u'results page shows "iPhone"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='product-list']/div/form/div/div[2]/div[1]/h4/a").text == "iPhone"
    

@when(u'user search "Samsung SyncMaster 941BW"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='search']/input").send_keys("Samsung SyncMaster 941BW")
    context.driver.find_element(By.XPATH, "//*[@id='search']/button").click()


@then(u'results page shows "Samsung SyncMaster 941BW"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='product-list']/div/form/div/div[2]/div[1]/h4/a").text == "Samsung SyncMaster 941BW"


@when(u'user search "iMac"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='search']/input").send_keys("iMac")
    context.driver.find_element(By.XPATH, "//*[@id='search']/button").click()


@then(u'results page shows "iMac"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='product-list']/div/form/div/div[2]/div[1]/h4/a").text == "iMac"


@when(u'user clicks on "Tablets"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='narbar-menu']/ul/li[4]/a").click()


@then(u'"Tablets" page with "Samsung Galaxy Tab 10.1" is shown')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='product-list']/div/form/div/div[2]/div[1]/h4/a").text == "Samsung Galaxy Tab 10.1"


@when(u'user clicks on "Cameras"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='narbar-menu']/ul/li[7]/a").click()


@then(u'"Cameras" page with "Canon EOS 5D" is shown')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='product-list']/div[1]/form/div/div[2]/div[1]/h4/a").text == "Canon EOS 5D"


@then(u'"Cameras" page with "Nikon D300" is shown')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='product-list']/div[2]/form/div/div[2]/div[1]/h4/a").text == "Nikon D300"


@when(u'user clicks on "Software"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='narbar-menu']/ul/li[5]/a").click()


@then(u'results page shows "There are no products to list in this category."')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id'content']/p").text == "There are no products to list in this category."
    

@when(u'user select "Desktops"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='narbar-menu']/ul/li[1]/a").click()


@then(u'drop-down menu containing "PC" is shown')
def step_impl(context):  
    context.driver.find_element(By.XPATH, "//*[@id='narbar-menu']/ul/li[1]/div/div/ul/li[1]/a")


@then(u'drop-down menu containing "Mac" is shown')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='narbar-menu']/ul/li[1]/div/div/ul/li[2]/a")


@when(u'user select "Components"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='narbar-menu']/ul/li[3]/a").click()


@when(u'user clicks on "Mac"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='narbar-menu']/ul/li[1]/div/div/ul/li[2]/a").click()


@when(u'user clicks on "PC"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='narbar-menu']/ul/li[1]/div/div/ul/li[1]/a").click()


@given(u'user is at "Mac" category page')
def step_impl(context):  
    context.driver.get('{}/en-gb/catalog/desktops/mac'.format(context.BASE_URL))


@when(u'user clicks on "iMac"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='product-list']/div/form/div/div[2]/div[1]/h4/a").click()


@then(u'"iMac" detail page is shown')
def step_impl(context):
    context.driver.get('{}/en-gb/catalog/desktops/mac/imac'.format(context.BASE_URL))


@given(u'user is at "Cameras" category page')
def step_impl(context):
    context.driver.get('{}/en-gb/catalog?path=33'.format(context.BASE_URL))


@when(u'user clicks on "Canon EOS 5D"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='product-list']/div[1]/form/div/div[2]/div[1]/h4/a").click()


@then(u'"Canon EOS 5D" detail page is shown')
def step_impl(context):
    context.driver.get('{}/en-gb/product/canon-eos-5d?path=33'.format(context.BASE_URL))   


@given(u'user is at "Tablets" category page')
def step_impl(context):
    context.driver.get('{}/en-gb/catalog/tablet'.format(context.BASE_URL))


@when(u'user clicks on "Samsung Galaxy Tab 10.1"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='product-list']/div/form/div/div[1]/a/img").click()


@then(u'"Samsung Galaxy Tab 10.1" detail page is shown')
def step_impl(context):
    context.driver.get('{}/en-gb/product/tablet/samsung-galaxy-tab-10-1'.format(context.BASE_URL))


@given(u'user is at "Canon EOS 5D" detail page')
def step_impl(context):
    context.driver.get('{}/en-gb/product/canon-eos-5d?path=33'.format(context.BASE_URL))


@when(u'user fills options on "Canon EOS 5D" detail page')
def step_impl(context):
    select = Select(context.driver.find_element(By.ID, 'input-option-226'))
    select.select_by_value('15')


@when(u'user clicks on "Add to cart" button')
def step_impl(context):
    context.driver.find_element(By.ID, 'button-cart')


@then(u'shopping cart contains "Canon EOS 5D"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='header-cart']/div/button").click()
    context.driver.find_element(By.XPATH, "//*[@id='header-cart']/div/ul/li/table/tbody/tr/td[2]/a").text == "Canon EOS 5D"


@given(u'user is at "iPhone" detail page')
def step_impl(context):
    context.driver.get('{}/en-gb/product/smartphone/iphone'.format(context.BASE_URL))


@when(u'user fills options on "iPhone" detail page')
def step_impl(context):
    context.driver.find_element(By.ID, "input-quantity").send_keys("1")


@then(u'shopping cart contains "iPhone"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='header-cart']/div/button").click()
    context.driver.find_element(By.XPATH, "//*[@id='header-cart']/div/ul/li/table/tbody/tr/td[2]/a").text == "iPhone"


@then(u'Checkout page is shown')
def step_impl(context):
    context.driver.get("{}/en-gb/?route=checkout/checkout".format(context.BASE_URL))


@given(u'alert "Products marked with *** are not available in the desired quantity or not in stock!" is displayed')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='checkout-cart']/div[1]")