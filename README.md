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

- [Mobile Homepage](/wireframes/Home-Mobile.png)
- [Tablet Homepage](/wireframes/Home-Tablet.png)
- [Desktop Homepage](/wireframes/Home-Desktop.png)

### Register

- [Mobile Register](/wireframes/Register-Mobile.png)
- [Tablet Register](/wireframes/Register-Tablet.png)
- [Desktop Register](/wireframes/Register-Desktop.png)

### Login

- [Mobile Login](/wireframes/Login-Mobile.png)
- [Tablet Login](/wireframes/Login-Tablet.png)
- [Desktop Login](/wireframes/Login-Desktop.png)

### Products

- [Mobile Products Page](/wireframes/Products-Mobile.png)
- [Tablet Products Page](/wireframes/Products-Tablet.png)
- [Desktop Products Page](/wireframes/Products-Desktop.png)

### Contact

- [Mobile Contact Page](/wireframes/Contact-Mobile.png)
- [Tablet Contact Page](/wireframes/Contact-Tablet.png)
- [Desktop Contact Page](/wireframes/Contact-Desktop.png)

### About

- [Mobile About Page](/wireframes/About-Mobile.png)
- [Tablet About Page](/wireframes/About-Tablet.png)
- [Desktop About Page](/wireframes/About-Desktop.png)

</details>

--

## Data Modelling

### Products

The standard inventory sold on this website is constructed with the following model:

| Key Name            | Database Key    | Field Validation                                     | Value Type                |
| ------------------- | --------------- | ---------------------------------------------------- | ------------------------- |
| Product Name        | name            | max_length=25                                        | CharField                 |
| Product Description | description     | ---                                                  | TextField                 |
| Product Price       | price           | max_digits=5, decimal_places=2, MinValueValidator(0) | DecimalField              |
| Quantity Available  | stock_available | MinValueValidator(0), MaxValueValidator(50)          | PositiveSmallIntegerField |

<!-- Further additions to this model will include a product image and if the product is part of the showcase set. -->
