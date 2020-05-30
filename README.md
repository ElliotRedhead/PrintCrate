# PrintCrate

A full ecommerce website built in Django for purchasing of 3D-printed models.

The target market is primarily customers that require designed pieces to fulfil niche requirements, products that may not be available as lone pieces elsewhere (e.g. spare parts) or customisation of existing model dimensions to suit their purpose (e.g. clean attachment to desks of various thicknesses without screw-fixtures).

The webshop boasts a modern and intuitive shopping experience, providing customers with options to purchase from standard stock items or request commissions via contacting the site owner.

[![Build Status](https://travis-ci.org/ElliotRedhead/PrintCrate.svg?branch=master)](https://travis-ci.org/ElliotRedhead/PrintCrate)

---

## User Experience

### Target Audience

- Potential buyers of the existing standard product range.
- People with product requirements that require specific customisation.
- People searching for 3D-printed products.

### User Stories

#### Customer Stories

Key objectives/requirements for site users.

1. As a new user: I want to create an account.
2. As a returning user: I want to login to my existing account.
3. As a user browsing products: I want to navigate standard products.
4. As a user interested in a particular product: I want to expand details of a specific product to view a description.
5. As a user interested in the background of the company: I want to read more about the business.
6. As a user purchasing a product: I want to add a product to my cart.
7. As a user purchasing a product: I want to know if there is sufficient stock available for my order.
8. As a user purchasing a product: I want to view the products currently in my cart.
9. As a user reviewing my cart: I want to alter quantities of products in my cart.
10. As a user reviewing my cart: I want to remove a product from my cart.
11. As a user finalising a purchase: I want to provide shipping information and pay for my purchase.
12. As a user with finalised purchases: I want to view all of my ordered products.
13. As a returning user: I want to be able to update my account details if required.
14. As a satisfied customer: I want to be able to share PrintCrate on social networks.
15. As a development-inclined visitor: I want to view the site's GitHub repository.
16. As a customer requesting a non-standard model or with an additional query: I want to contact the site owner.

#### Customer Story Fulfilment

1. From any page of the PrintCrate site: selection of the "Register" button in the navigation bar loads a registration page. The registration page displays a form with validation. If the form is populated with invalid values the registration is rejected upon submission with an error message detailing why registration has failed. Upon population of the form with valid values the browser redirects away from the register page with a success feedback message displayed.
2. From a logged-out state, access to the "Profile" or "Checkout" pages is restricted. The login feature is accessed by selecting "Login" from the navigation bar, which loads the login page. The login page displays a form with validation. If the form is populated with invalid values the login is rejected upon submission with an error message detailing why login has failed. Upon login success the user is redirected to their account page with new navigation options and success modal indicating the updated user state.
3. From the site homepage, selection of the "Browse Products" button in the jumbotron or from the navigation bar loads a page of all products sold by PrintCrate. If the number of items exceeds 15 the products are split across multiple pages (pagination) to account for load times, especially if hundreds of items become available in the future.
4. Having located the product I am interested in, either by finding it as a showcase product on the homepage, in a mix of all products, or as a result of the search function: selecting either the "Product Details" button or the product's image redirects to display a more detailed view of the target product. The notable addition of the product detail page is the description and ability to add a product to a cart.
5. Selecting the "About Us" button from the jumbotron on the homepage or selecting the "About" navigation bar icon redirects to display a short description of PrintCrate and an accordion display of frequently asked questions.
6. Having located a desired product and accessing the product details display of said product, either iterating the quantity or manually typing the quantity before selecting the "Add" button results in addition of the desired quantity of that product to the cart. Form validation prevents entering a quantity less than zero, non-integers or a number exceeding the quantity of that item in stock. Upon selecting the "add" button, a redirect occurs to view the current cart contents.
7. Upon locating a desired product and selecting the "Product Details" button or the product image to acces the product details: the available quantity of the desired product can be viewed as part of the product information. If a customer wants to place an order in excess of the quantity available they can contact the store owner via the "Contact Us" form as detailed in the "About" page.
8. The current cart contents can be accessed at any time by selecting the cart icon from the navigation bar. If the cart is empty: a modal is displayed to let the user know that the cart is empty and redirects them to view all of the PrintCrate products with a prompt to add products to the cart. If there are items in the cart: the cart contents are displayed with product names, prices and quantities with the total price of all products.
9. When viewing the cart contents with items occupying the cart: the quantity input field is pre-populated with the current quantity of the specific item in their cart. This field can be selected and overwritten by using the selector iteration arrows or by manually typing the desired value. The maximum number this field allows is the available quantity of the product and the lowest number this can be changed to is 0. Upon changing the number from the original cart quantity: an "Amend" button is displayed for the user to confirm their change, upon selecting this button the page is refreshed with their new quantity and total price.
10. Upon viewing an occupied cart contents page: the user can remove an item by either decreasing the quantity to zero and confirming the removal by selecting the "Amend" button or selecting the red cross displayed to the left of any item and confirming removal by selection of the "Remove" button in the triggered modal. In either method, the user stages the removal by either setting the quantity equal to zero or clicking the red cross icon and then must confirm the deletion by selecting "Amend" or selecting "Remove" in the modal, this is designed to minimise instances of customers accidentally removing items from their cart.
11. From the cart contents page, selection of the "Checkout" button redirects to display a shipping information form if the user is logged in. If the user is not logged in they are required to create an account or login to continue with their transaction. The shipping information form is displayed with every transaction as the user may wish to send their purchase to a new address. Upon submission of valid details for the shipping information form: a payment information page is displayed, this reminds the user of the total price of their transaction and allows for entry of payment credentials. Submission of invalid credentials returns an error message for the invalid field, submission of valid credentials results in display of a successful payment modal and redirect to display the user's purchased products and order status.
12. A logged-in user with past orders can view their purchased products by selecting "Profile" from the navigation bar. The user is redirected, with their purchased products displayed in a table, detailing the product name, quantity, total price, purchase date and order status.
13. A logged-in user can select "Profile" from the navigation bar to view their purchased products and option to update their account details. Population of the "New Email Address" and "New Password" fields with valid data redirects the user to Login with their updated password. Submission of invalid credentials yields an error message detailing the failed test.
14. The user can select one of the social media icons in the footer to open a new browser tab and share a link to the website on that respective site. Alternatively, selection of the hyperlink icon copies the page URL to the user's clipboard with a success modal detailing this for custom sharing options for the user.
15. Selection of the GitHub icon in the footer opens the GitHub repository of this site in a new browser tab.
16. Selection of the "Contact Us" button from the navigation bar redirects the user to display a contact form. Population of this form followed by submission via selecting the "Send" button directs the user to a message success page for user feedback.

## Design & Styling

### Colour Palette

This colour palette was formed upon project inception and used to drive UI decisions within the project, adjustments may be made to this as project development progresses.

# Detail colour scheme here.

### Wireframes

<details>
<summary> Project Inception Wireframes (Click to View) </summary>

Project inception wireframes were created to provide guidance from the initial planning stages with a mobile-first development perspective and were used as the starting point for page layouts.

#### Homepage

- [Mobile Homepage](/wireframes/home-mobile.png)
- [Tablet Homepage](/wireframes/home-tablet.png)
- [Desktop Homepage](/wireframes/home-desktop.png)

#### Register Page

- [Mobile Register](/wireframes/register-mobile.png)
- [Tablet Register](/wireframes/register-tablet.png)
- [Desktop Register](/wireframes/register-desktop.png)

#### Login Page

- [Mobile Login](/wireframes/login-mobile.png)
- [Tablet Login](/wireframes/login-tablet.png)
- [Desktop Login](/wireframes/login-desktop.png)

#### Products Page

- [Mobile Products Page](/wireframes/products-mobile.png)
- [Tablet Products Page](/wireframes/products-tablet.png)
- [Desktop Products Page](/wireframes/products-desktop.png)

#### Contact Page

- [Mobile Contact Page](/wireframes/contact-mobile.png)
- [Tablet Contact Page](/wireframes/contact-tablet.png)
- [Desktop Contact Page](/wireframes/contact-desktop.png)

#### About Page

- [Mobile About Page](/wireframes/about-mobile.png)
- [Tablet About Page](/wireframes/about-tablet.png)
- [Desktop About Page](/wireframes/about-desktop.png)

</details>

<details>
<summary> Project Evolution Wireframes (Click to View) </summary>

As the project progressed, wireframes were created to guide towards a final project layout and better reflect the project evolution.

#### Homepage

- [Mobile Home Page](/wireframes/home-mobile-v2.png)
- [Tablet Home Page](/wireframes/home-tablet-v2.png)
- [Desktop Home Page](/wireframes/home-desktop-v2.png)

#### Register Page

- [Mobile Register Page](/wireframes/register-mobile-v2.png)
- [Tablet Register Page](/wireframes/register-tablet-v2.png)
- [Desktop Register Page](/wireframes/register-Desktop-v2.png)

#### Login Page

- [Mobile Login Page](/wireframes/login-mobile-v2.png)
- [Tablet Login Page](/wireframes/login-tablet-v2.png)
- [Desktop Login Page](/wireframes/login-desktop-v2.png)

#### Products List Page

- [Mobile Products List Page](/wireframes/products-mobile-v2.png)
- [Tablet Products List Page](/wireframes/products-tablet-v2.png)
- [Desktop Products List Page](/wireframes/products-desktop-v2.png)

#### Product Detail Page

- [Mobile Product Detail Page](/wireframes/productdetail-mobile-v2.png)
- [Tablet Product Detail Page](/wireframes/productdetail-tablet-v2.png)
- [Desktop Product Detail Page](/wireframes/productdetail-desktop-v2.png)

#### Contact Page

- [Mobile Contact Page](/wireframes/contact-mobile-v2.png)
- [Tablet Contact Page](/wireframes/contact-tablet-v2.png)
- [Desktop Contact Page](/wireframes/contact-desktop-v2.png)

#### About Page

- [Mobile About Page](/wireframes/about-mobile-v2.png)
- [Tablet About Page](/wireframes/about-tablet-v2.png)
- [Desktop About Page](/wireframes/about-desktop-v2.png)

#### Cart Page

- [Mobile Cart Page](/wireframes/cart-mobile-v2.png)
- [Tablet Cart Page](/wireframes/cart-tablet-v2.png)
- [Desktop Cart Page](/wireframes/cart-desktop-v2.png)

#### Checkout (Shipping) Page

- [Mobile Shipping Page](/wireframes/shipping-mobile-v2.png)
- [Tablet Shipping Page](/wireframes/shipping-tablet-v2.png)
- [Desktop Shipping Page](/wireframes/shipping-desktop-v2.png)

#### Checkout (Payment) Page

- [Mobile Payment Page](/wireframes/payment-mobile-v2.png)
- [Tablet Payment Page](/wireframes/payment-tablet-v2.png)
- [Desktop Payment Page](/wireframes/payment-desktop-v2.png)

#### Error404 Page

- [Mobile 404 Page](/wireframes/error404-mobile-v2.png)
- [Tablet 404 Page](/wireframes/error404-tablet-v2.png)
- [Desktop 404 Page](/wireframes/error404-desktop-v2.png)

#### Error500 Page

- [Mobile 500 Page](/wireframes/error500-mobile-v2.png)
- [Tablet 500 Page](/wireframes/error500-tablet-v2.png)
- [Desktop 500 Page](/wireframes/error500-desktop-v2.png)

</details>

## Page Features

### Home

The homepage serves as the main landing page for site visitors.  
The user is directed to browse products or learn more about PrintCrate, with a selection of products showcased as examples for the user.

### Products List

Cards displaying the products available at PrintCrate provide an overview of standard stock, giving a summary of each product available at a glance.  
Users can access more details about each product by using the "Product Details" button of their selected product.

### Product Details

Individual product detail pages include information such as the product name, image, description, price and quantity available.  
The option to add a product to the user's cart is given here.

### About PrintCrate

The about page gives a brief summary of what PrintCrate is and the main offering to the customer.
Some common questions concerning logistics of the business, product material details and other services provided by PrintCrate are also answered.

### Contact

The contact page provides a form for users to send their message directly to the PrintCrate owners.  
The recipient email address is kept hidden in this way and prevents bot scraping of that information.

### Register Account

A user who is not logged in can access the Register page from the navigation bar, they are then prompted for username, email, password and a confirmation of the chosen password in order to create an account.  
If the user already owns an account, there is a prompt to login instead below the registration form.

### Login

The login page prompts the user for their existing username and password to access their account.  
If the user does not already own an account, a prompt below the login form can be clicked to redirect to the registration form.

### Logout

A logged in user can logout via the navigation bar link, this clears all session data. Any items in their cart and not checked out at that time are cleared to prevent shared accounts detailing incomplete orders to other users.

### Cart

The cart provides a list of all products in the user's cart with the current total price of all items in the cart.  
The user has the ability to update the quantities of products in their cart, and the total price is updated when those changes are submitted.

### Checkout

The checkout feature allows users to submit their shipping address and conduct payment through Stripe processing.

## Data Modelling

### User Model

The User model for this project is part of the Django defaults "django.contrib.auth.models".

### Products Model

The standard inventory sold on this website is constructed with the following model:

| Key Name            | Database Key     | Field Validation                                     | Value Type                |
| ------------------- | ---------------- | ---------------------------------------------------- | ------------------------- |
| Product Name        | name             | max_length=25                                        | CharField                 |
| Product Image       | product_image    | blank=True                                           | ImageField                |
| Product Description | description      | max_length=150                                       | TextField                 |
| Product Price       | price            | max_digits=5, decimal_places=2, MinValueValidator(0) | DecimalField              |
| Quantity Available  | stock_available  | MinValueValidator(0), MaxValueValidator(50)          | PositiveSmallIntegerField |
| Showcase Product    | showcase_product | default=False                                        | Boolean                   |

### Shipping Information Model

This model stores the shipping information for an order placed by a user.

| Key Name               | Database Key           | Field Validation                     | Value Type      |
| ---------------------- | ---------------------- | ------------------------------------ | --------------- |
| Customer               | customer               | on_delete=models.CASCADE             | ForeignKey User |
| Customer Full Name     | full_name              | max_length=100, blank=False          | CharField       |
| Primary Address Line   | primary_address_line   | max_length=50, blank=False           | CharField       |
| Secondary Address Line | secondary_address_line | max_length=50, blank=True, null=True | CharField       |
| Town/City              | town_or_city           | max_length=50, blank=False           | CharField       |
| County                 | county                 | max_length=50, blank=False           | CharField       |
| Postcode               | postcode               | max_length=20, blank=False           | CharField       |
| Country                | country                | max_length=50,blank=False            | CharField       |
| Phone Number           | phone_number           | max_length=20, blank=False           | CharField       |

### Order Detail Model

This model stores the details of an order made by a customer.

| Key Name    | Database Key | Field Validation                        | Value Type                  |
| ----------- | ------------ | --------------------------------------- | --------------------------- |
| Shipping    | shipping     | null=False, on_delete=models.CASCADE    | ForeignKey CustomerShipping |
| Product     | product      | null=False, on_delete=models.CASCADE    | ForeignKey Product          |
| Quantity    | quantity     | blank=False                             | IntegerField                |
| Total Price | total        | default=datetime.date.today, blank=True | DateField                   |

## Testing

Testing details can be viewed in the [TESTING.md](/TESTING.md) file.

## Deployment

### Prerequisites

- An Integrated Development Environment (IDE) e.g. [Visual Studio Code](https://code.visualstudio.com/)
- [Python 3](https://www.python.org/downloads/)
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

Accounts for the following (some environmental variables are required from these.):

- [Stripe](https://dashboard.stripe.com/register)
- [AWS](https://aws.amazon.com/) and [an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
- [Gmail](https://www.google.com/gmail/)

### Running this project in a local environment

1. Save a copy of this github repository with the Git clone function in your terminal:

   ```
   git clone https://github.com/ElliotRedhead/PrintCrate
   ```

2. In your IDE, navigate to the location that you saved the repository to.

3. Create a virtual environment to load the project's required packages into. Enter the command:

   ```terminal
   py .venv venv
   ```

   _NB: Please refer to documentation for the specific syntax required for your OS, `py` may require replacement with `python3` or `python`_

4. Activate the virtual environment:

   ```terminal
   source venv/Scripts/activate
   ```

   _NB: This command will vary based on your OS, see [Virtual Environment documentation](https://docs.python.org/3/library/venv.html) for help._

5. If required, update the Package Installer for Python (PIP):

   ```terminal
   pip install --upgrade pip.
   ```

6. Install all required project packages:

   ```terminal
   pip install -r requirements.txt.
   ```

7. Setting environment variables:  
    Create a file in the root of the project named "env.py", copy the code block below and populate with your details:

   ```python
   import os
   os.environ.setdefault("AWS_ACCESS_KEY_ID", "<Your AWS Access Key>")
   os.environ.setdefault("AWS_SECRET_ACCESS_KEY","<Your AWS Secret Access Key>")
   os.environ.setdefault("DATABASE_URL", "<Your PostgreSQL Database URL>")
   os.environ.setdefault("EMAIL_HOST", "<Your SMTP Enabled Gmail Address>")
   os.environ.setdefault("HOST_PASS", "<Your SMTP Enabled Gmail Password>")
   os.environ.setdefault("EMAIL_RECIPIENT", "<Email Address to Send Contact Form Messages to>")
   os.environ.setdefault("STRIPE_PUBLISHABLE", "<Your Stripe Publishable Key>")
   os.environ.setdefault("STRIPE_SECRET", "<Your Stripe Secret Key>")
   os.environ.setdefault("DJANGO_SECRET", "<Your Stripe Secret Key>")
   os.environ.setdefault("DEPLOY", "True")
   ```

   See [this page](https://kinsta.com/knowledgebase/free-smtp-server/) for instructions to enable SMTP with Gmail.

8. Make and migrate models to create your database structures:

   ```terminal
   py manage.py makemigrations
   py manage.py migrate
   ```

9. Create a superuser to access admin features:

   ```terminal
   py manage.py createsuperuser
   ```

10. Add your development IP to the ALLOWED_HOSTS variable list in settings.py.

11. Run the project on a local server:

    ```terminal
    py manage.py runserver
    ```

12. Add new products to the database by accessing the URL provided in the terminal and adding "/admin", logging in with your superuser credentials and accessing the Products table.

---

### Deployment of this project to Heroku

Steps to deploy PrintCrate to Heroku:

1. Create a requirements.txt file populated by required python modules:

   ```terminal
   pip freeze > requirements.txt
   ```

   _NB: Please refer to documentation for the specific syntax required for your OS, `pip` may require replacement with `pip3`._

2. Create a Procfile:

   ```terminal
   echo web: py app.py > Procfile.
   ```

   _NB: Please refer to documentation for the specific syntax required for your OS, `py` may require replacement with `python3` or `python`_

3. Add requirements.txt and Procfile to git tracking, committing their addition and pushing those changes.

4. Open [https://dashboard.heroku.com/apps](Heroku) in your browser, signing in/creating an account as required.  
   Create an application by selecting the "New" button on the dashboard. Create a name for the application with an appropriate region.

5. Open the dashboard of the new application on Heroku, select the "Deployment" tab and select GitHub from the Deployment Method selection.

6. Search for the correct GitHub repository from the list of your existing repositories and select the correct repository.

7. Within the application dashboard, select the "Settings" tab then "Reveal Config Vars".

   Populate the config variables table with the following:

   | Key                   | Value                                              |
   | --------------------- | -------------------------------------------------- |
   | DJANGO_SECRET         | `<Your Django Secret Key>`                         |
   | AWS_ACCESS_KEY_ID     | `<Your AWS Access Key>`                            |
   | AWS_SECRET_ACCESS_KEY | `<Your AWS Secret Access Key>`                     |
   | DATABASE_URL          | `<Your PostgreSQL Database URL>`                   |
   | EMAIL_HOST            | `<Your SMTP Enabled Gmail Address>`                |
   | HOST_PASS             | `<Your SMTP Enabled Gmail Password>`               |
   | EMAIL_RECIPIENT       | `<Email Address to Send Contact Form Messages to>` |
   | STRIPE_PUBLISHABLE    | `<Your Stripe Publishable Key>`                    |
   | STRIPE_SECRET         | `<Your Stripe Secret Key>`                         |
   | DEPLOY                | `True`                                             |

8. Ensure you are using the postgreSQL database by either creating an env file as instructed in "Running this project in a local environment.7" or stipulating the postgreSQL URL in settings.py.

9. Make migrations and migrate the database models to the postgreSQL database:

   ```terminal
   py manage.py makemigrations
   py manage.py migrate
   ```

10. In the Heroku app dashboard, select the "Deploy" tab. Scroll down to "Manual Deploy", select the master branch and select "Deploy Branch".

11. The build progress can be monitored in the log for the Heroku application, upon build completion, select the "Open App" button to view the deployed application.
