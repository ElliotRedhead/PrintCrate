# PrintCrate

A full ecommerce website built in Django for purchasing of 3D-printed models.

The target market is primarily customers that require designed pieces to fulfil niche requirements, products that may not be available as lone pieces elsewhere (e.g. spare parts) or customisation of existing model dimensions to suit their purpose (e.g. clean attachment to desks of various thicknesses without screw-fixtures).

The webshop boasts a modern and intuitive shopping experience, providing customers with options to purchase from standard stock items or request commissions.

[![Build Status](https://travis-ci.org/ElliotRedhead/PrintCrate.svg?branch=master)](https://travis-ci.org/ElliotRedhead/PrintCrate)

---

## User Experience

### Target Audience

- Potential buyers of the existing standard product range.
- People with product requirements that require specific customisation.
- People searching for 3D-printed products.

## User Stories

### User Story Scope

Key objectives/requirements for site users.

1. As a new user: I want to create an account.
2. As a returning user: I want to login to my existing account.
3. As a user browsing products: I want to navigate products effectively.
4. As a user interested in a particular product: I want to expand details of a specific product to view a description.
5. As a user interested in the background of the company: I want to read more about the business.
6. As a user purchasing a product: I want to add a product to my cart.
7. As a user purchasing a product: I want to know if there is sufficient stock available for my order.
8. As a user purchasing a product: I want to view the products currently in my cart.
9. As a user reviewing my cart: I want to alter quantities of products in my cart.
10. As a returning user: I want to be able to update my account details if required.
11. As a satisfied customer: I want to be able to share PrintCrate on social networks.
12. As a customer requesting a non-standard model: I want to upload an image file for the company to review, with a message and contact details.

---

## Design & Styling

### Colour Palette

This colour palette was formed upon project inception and used to drive UI decisions within the project, adjustments may be made to this as project development progresses.

![#fcfcfc](https://placehold.it/15/fcfcfc/000000?text=+) `#fcfcfc`  
![#9ec3d6](https://placehold.it/15/9ec3d6/000000?text=+) `#9ec3d6`  
![#93ba7e](https://placehold.it/15/93ba7e/000000?text=+) `#93ba7e`  
![#2f4677](https://placehold.it/15/2f4677/000000?text=+) `#2f4677`  
![#8e638a](https://placehold.it/15/8e638a/000000?text=+) `#8e638a`

### Wireframes

<details>
<summary> Project Inception Wireframes </summary>

Project inception wireframes were created to provide guidance from the initial planning stages with a mobile-first development perspective and were used as the starting point for page layouts.

### Homepage

- [Mobile Homepage](/wireframes/home-mobile.png)
- [Tablet Homepage](/wireframes/home-tablet.png)
- [Desktop Homepage](/wireframes/home-desktop.png)

### Register Page

- [Mobile Register](/wireframes/register-mobile.png)
- [Tablet Register](/wireframes/register-tablet.png)
- [Desktop Register](/wireframes/register-desktop.png)

### Login Page

- [Mobile Login](/wireframes/login-mobile.png)
- [Tablet Login](/wireframes/login-tablet.png)
- [Desktop Login](/wireframes/login-desktop.png)

### Products Page

- [Mobile Products Page](/wireframes/products-mobile.png)
- [Tablet Products Page](/wireframes/products-tablet.png)
- [Desktop Products Page](/wireframes/products-desktop.png)

### Contact Page

- [Mobile Contact Page](/wireframes/contact-mobile.png)
- [Tablet Contact Page](/wireframes/contact-tablet.png)
- [Desktop Contact Page](/wireframes/contact-desktop.png)

### About Page

- [Mobile About Page](/wireframes/about-mobile.png)
- [Tablet About Page](/wireframes/about-tablet.png)
- [Desktop About Page](/wireframes/about-desktop.png)

</details>

--

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

### Contact

The contact page provides a form for users to send their message directly to the PrintCrate owners.  
The recipient email address is kept hidden in this way and prevents bot scraping of that information.

### Frequently Asked Questions

The FAQ page answers some common questions that are raised concerning logistics of the business, product material details and other services provided by PrintCrate.

### Register Account

### Login

### Logout

### Cart

### Checkout

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
