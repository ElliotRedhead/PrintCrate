# PrintCrate - Development Testing

## Automated Testing

### Django Unit Testing

#### Products Application

- The product model was tested upon creation to verify that the correct product name was returned. The test itself was validated by input of incorrect followed by correct test subjects, these returned a failed and passing test result as expected.
- Page loading of the standard list of all products is tested to verify the page loads with status code 200. The test was validated by input of combinations of incorrect URL and incorrect status code, the correct combination returns a passing test as expected.

## Manual Testing

### Project-Wide

- Page titles were found to be incorrectly handled upon utilising the Jinja {% include %} directive to incluide the head section in the base.html file.  
  Jinja variable blocks were found to not penetrate to the head section from a template extending the base.html file.  
  The corrective action was to pass the "page_title" variable as an argument from the rendering view.  
  This resolved the issue but was not possible for the login view as it is using one of Django's contrib packages, meaning it is not possible to access the view itself.  
  The extended corrective action to make the login page title function correctly was to pass the variable as an "extra_context" variable via the accounts/urls.py file, the view then passes this to the rendering HTML as expected.
