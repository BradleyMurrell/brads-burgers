# ***Brad's Burgers***

## Description

For my project, I have created an ordering system for a burger restaurant called ***Brad's Burgers***.

The idea of the ordering system is that when the customer arrives to the restaurant, they will make their order on a terminal.

The customer will first see the home screen which will prompt them to ***Place Order***.

After ***Place Order*** has been selected, the screen will show a list of categories to choose from, ***Burger***, ***Meal***, ***Sides*** and ***Drinks***.

After selecting a category, the customer will have a choice of selecting from a list of the chosen category.

If ***Meal*** was chosen, the customer will get to choose from the three ***Burger***, ***Sides*** and ***Drinks*** categories.

In the ***Burger*** category, the customer will get to make their own burger by selecting from a number of sub-categories, ***Bun***, ***Meat***, ***Salad***, ***Dressing*** and ***Extra***.

The customer may choose one option from the ***Bun*** and ***Meat*** category, but may choose more than one from ***Salad***, ***Dressing*** and ***Extra*** categories at an extra price for each additional extra.

When the customer has finished with their order, they will see a table on the order page what they have ordered and the total cost.

When they are happy with the order, the customer can select the ***Finish Order*** button which will dirict them to a final page displaying their order number.

The restaurant will then be able to see the orders that have been made along side the order number.

When the order is complete, the restaurant can mark the order as complete.


------
## Wireframe

<img src="assets/images/Wireframe.png">

------
* **Update:** Due to time constraint, I have removed the ***Meals*** section and will add to future features.
* **Update:** Due to time constraint, I have removed the ability to create a burger. Instead I have added a ***Burger*** category. I will add the ability to create a burger to future features.

------
## Features
### Existing Features
* Customer can order their meal by selecting from a number of categories
* ~~Customer can customize their burger by selecting what they want on it from a number of sub-categories~~
* Customer can view what they have ordered with the price of each item and a total price before finishing their order
* Customer will be given an order number after finishing their order
* Restaurant can view what orders have been made along side the order number
* Restaurant can mark which orders have been completed

### Future Features
* Customer can make a payment with debit/credit card after completing order
* Customer can register their details and order/pay online
* Customer can have the option for home delivery
* Restaurant can show what items are out of stock
* Customer can customize their burger by selecting what they want on it from a number of sub-categories


------

<img src="assets/images/index.png"></img>
<img src="assets/images/order.png"></img>
<img src="assets/images/burger.png"></img>
<img src="assets/images/salad.png"></img>
<img src="assets/images/drink.png"></img>

------
## Testing
Testing was done through every step of the project. I did not do a final testing done due to not being able to complete the project on time

------
## Bugs
* Could not get the total cost to appear correctly in the order list
## Fixed Bugs
* script.js would not work. Line 2 was missing parenthesis
* Could not get item name and price to display in order list. In burger.html, line 13, 14, had to change `class` to `id`

------
## Deployment
This project was deployed using Heroku
* Steps for deployment
  * Create a Heroku app
  * Change ***DEBUG*** in ***settings.py*** to ***False***
  * Link the Heroku app to the repository
  * Click on deploy


------
## Credits
* Simen Daehlin (mentor) for help and advice
* Code Institute for the deployment instructions

------