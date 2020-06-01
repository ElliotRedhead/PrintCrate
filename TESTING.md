# PrintCrate - Development Testing

## Note to Assessors

Superuser access to the PostgreSQL database is granted to the following account for ease of your testing purposes.  
Username: CodeInstitute  
Password: PrintCI2020  
These credentials have only been made available for assessment purposes of this educational project, and would not be shared in a production environment.  
If assessing using a new database: a minimum of three showcase products must be added in order to view the product showcase section on the homepage.

## Automated Testing

Automated testing is conducted to support manual testing during development as required, the intent is not to achieve 100% coverage with automated testing alone as this would delay rather than aid project development.

### Python Unit Testing

_NB: The Heroku hobby-tier does not give permissions to allow creation of databases that are required for python automated testing. In order to run the unit testing I temporarily commented out the postgres credentials for this project to test against the default sqlite database._

Unit tests can be found in the "tests.py" files of applicable applications within the repository.

### Travis CI Testing

- Travis testing was reporting failing tests when attempting to test the products view, this was found to be due to the disabling of AWS services to prevent exceeding free account limits. Testing was passed during development by only applying custom storages if a "DEPLOY" variable was present in the os environment. This bug will be re-tested upon deployment to ensure it was handled correctly.

## Manual Testing

Manual testing was conducted with each feature/iteration, the development server was accessed on a second monitor as changes were made to view in realtime what the impact of changes were.  
Following user stories and attempting to anticipate unexpected traversal of the site has resulted in a more robust final product despite the greater time required to achieve this.  
The project was also shared with friends with the objective of breaking the site in any way that they could, this encouraged defensive design regarding multiple users conducting transactions that affect product availability and better stock control. This also encouraged greater thought of how users may navigate the site in random ways and manipulation of URLs.

### Project-Wide

- Page titles were found to be incorrectly handled upon utilising the Jinja {% include %} directive to incluide the head section in the base.html file.  
  Jinja variable blocks were found to not penetrate to the head section from a template extending the base.html file.  
  The corrective action was to pass the "page_title" variable as an argument from the rendering view.  
  This resolved the issue but was not possible for the login view as it is using one of Django's contrib packages, meaning it is not possible to access the view itself.  
  The extended corrective action to make the login page title function correctly was to pass the variable as an "extra_context" variable via the accounts/urls.py file, the view then passes this to the rendering HTML as expected.

- Simulation of poor network conditions for mobiles revealed excessively long load times for the homepage jumbotron background image.  
  The jumbotron background was deemed too resource intensive for mobile network usage, and the applied solution is to subsitute the jumbotron background image at lower resolutions via CSS media queries. The applied solution was successful in reducing network load with negligible impact to end-user aesthetics.

- Product pagination is implemented to prevent long loading times (negating the requirement for a loading progress indicator also) as the product database could expand greatly in the future.
  The same process is applied to viewing products that have been filtered by the search function. However, both pagination and the search function are dependent upon URL manipulation.  
   With initial implementation of pagination a conflict was raised with the search feature as the URL queries were being overwritten.  
   The solution was conditional URL manipulation managed by [custom javascript](static/js/custom.js), which preserves both additions.

#### Database Integrity

- Removal of products from the database with those products in the user's cart resulted in a server error (500) as the cart context file was seeking a non-existing item.  
  This bug was fixed by removing the item from the user's cart if it did not exist in the product database, see [the contexts file, cart_contents function](cart\contexts.py).

- Preservation of a user's previous orders is important to manage sales metrics and for both business and customer traceability following a purchase.  
  Initial handling of product deletion was to prevent deletion if orders of those items had been placed in the past. However, over time this would result in a bloated library of redundant products if items were discontinued over time.  
  The solution was to add another field to all products, "active_product" with default value of True.  
  The products list is filtered to show only active products and any inactive products in user carts are removed.  
  This allows the site owner to toggle visibility of items that may be out of stock for longer periods of time without deleting valuable order information.

- Upon deployment of PrintCrate to Heroku a server error occured, caused by the selection of random showcase products for the homepage showcase products display.  
  As there were less than three showcase products in the PostgreSQL database, sampling of three distinct objects with that filter was impossible and so caused an error.  
  The implemented solution was to only sample if there are more than three showcase products in the database, select all if there are only three showcase products and only display the product showcase section if products are passed from the view.
