from django.test import TestCase, Client


class AboutViewTest(TestCase, Client):
    """Test if 'about us' view is displayed."""

    def client_setup(self):
        """Create client to conduct unit tests. """
        self.client = Client()

    def test_about_us_page_responds_with_url_call(self):
        """Test if a view is loaded upon calling the About URL.

        The test passes with 200 (success),
        test fails if other status codes e.g. 404 (not found) are returned.
        """
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_about_us_correct_template_rendered_with_call(self):
        """Test if correct templates are rendered upon calling About URL."""
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "about.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertTemplateUsed(response, "components/footer.html")
        self.assertTemplateUsed(response, "components/navbar.html")
        self.assertTemplateUsed(response, "layout/head.html")
        self.assertTemplateUsed(response, "layout/scripts.html")
