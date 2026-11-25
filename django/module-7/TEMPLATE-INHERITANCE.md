# Template Inheritance in Django

`base.html` holds the HTML shared by every page. Each page uses `base.html` and fills in the parts that are different.

| Code | Simple meaning | Where to use it |
|---|---|---|
| `base.html` | The common design for all pages. | Create it inside `templates/`. Put the shared navbar, footer, CSS, and scripts here. |
| `{% extends 'base.html' %}` | “Use the common design.” | At the top of each page, such as `about.html` and `contact.html`. |
| `{% block title %}...{% endblock %}` | Sets the browser-tab title. | Define the space in `base.html`; fill it in each page. |
| `{% block page_header %}...{% endblock %}` | Shows the page heading or homepage carousel. | Define the space in `base.html`; put “About Us” in `about.html` and the carousel in `index.html`. |
| `{% block content %}...{% endblock %}` | Shows the page's main content. | Define the space in `base.html`; put the contact form in `contact.html`, for example. |
| `{% endblock %}` | Marks where a block finishes. | After the HTML belonging to each block. |
| `{% url 'about' %}` | Finds the About page's URL by its route name. | In links, such as the navbar link in `base.html`. |
| `{% if request.path == '/about/' %}` | Checks whether About is the current page. | In the shared navbar in `base.html`, to highlight About. |

**Remember:** `base.html` provides the spaces; each page fills those spaces with its own HTML.
