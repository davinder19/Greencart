import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # import for BY using css Selector
from selenium.webdriver.support import expected_conditions  # import for expected conditions
from selenium.webdriver.support.wait import WebDriverWait  # import and use for Explicit wait

list1 =[]  # declare empty list here to add the select fruit name which are added i cart.
list2 =[]  # declare empty list here to add the select fruit name which are added i cart.
davinder = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
davinder.get("https://rahulshettyacademy.com/seleniumPractise/#/")
davinder.maximize_window() # maximize method maximize your window
# find using ID USERNAME #ID NAME

davinder.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4) # sleep method used to sleep the execution. here we put wait or sleep up-to 4 second
# next wen create a xpath than check the length of display products and assign into variable
count = len(davinder.find_elements_by_xpath("//div[@class='products']/div"))
print("item select counting is =", count)
# here we use thw (assert) to check the condition
assert count == 3

# find the selected item add button class and add those items to cart
# select button and add to assign to variable
buttons = davinder.find_elements_by_xpath("//div[@class='product-action']/button")
btnlength = len(buttons) # check the button length and assign to variable
print("button length is =", btnlength)  # print the button length

# here using for loop to click add cart button to add the all items to cart

for button in buttons:
      # here next line we traverse child to parents use parent ::
      # //div[@class='product-action']/button/parent::div/parent::div/h4
      # coz we want trevarse from button so don't need to use driver. find element controll will start from begining
      # so we start from button coz we trevarse from button
      # xpath from "//div[@class='product-action']/button" already save in button so we used only left part here to find h4
      # print(button.find_element_by_xpath("parent::div/parent::div/h4").text) # it will print fruit name
      list1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)  # add the fruits name to the empty list
      button.click()
print(list1)
# print(len(buttons)," button are clicked")

davinder.find_element_by_css_selector("img[alt='Cart']").click()
davinder.find_element_by_xpath("//button[contains(text(), 'PROCEED TO CHECKOUT')]").click()
# Explicit wait
# Explicit wait used when you want to wait only for specific condition, object or page etc
# for eg we want wait only before apply promo code apply all other code execute but wait only before promo-code line
wait = WebDriverWait(davinder, 5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
veggies = davinder.find_elements_by_css_selector("p.product-name") # get fruit name when check out
for veg in veggies:
      list2.append(veg.text)
print(list2)
# assert method to compare two list item same means page one select fruit and 2nd page are same
# assert list1 == list2
davinder.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

davinder.find_element_by_css_selector(".promoBtn").click()
davinder.implicitly_wait(5)
# wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR, "span.promoInfo"))
promoText = davinder.find_element_by_css_selector("span.promoInfo").text
print(promoText)
# get all the total amount of each items
amounts = davinder.find_elements_by_xpath("//tr/td[5]/p")
sum = 0  # sum variable use to add the all items amount
# amount text get the each total amount but text is string so INT use to convert string into Int value
for amount in amounts:
      amount = int(amount.text)
      sum = sum + amount

print("Sum of Amount is =", sum)
totalAmount = davinder.find_element_by_class_name("totAmt")
totalAmount = int(totalAmount.text)
print("Total Amount is= ", totalAmount)
difference = sum-totalAmount

print("Difference between sum of amount and totalAmount is =", difference)
# get the total items add it cart
totalItems = davinder.find_elements_by_xpath("//tr/td[3]/p")
countItems = 0
for item in totalItems:
      item = int(item.text)
      countItems = countItems + item # count the total Items add in cart
print("Total Items added=", countItems)
totalAfterDiscount = davinder.find_element_by_class_name("discountAmt") # get final amount after discount
totalAfterDiscount = totalAfterDiscount.text
totalDiscount = 0
totalSave = 0
print("Your Total Amount After Discount =", totalAfterDiscount)
totalSave = float(totalAmount) - float(totalAfterDiscount) # convert value in float
totalDiscount = totalSave / totalAmount * 100  # use formula to get discount percentage
print("Total discount you got =", round(totalDiscount, 1),"%")
print("Your total save today purchase is =", "$", round(totalSave, 2))
# use assert to check items in cart count is same  ==
assert  count == countItems
# use assert to check sum of amount and totalAmount is  ==
assert  sum == totalAmount

