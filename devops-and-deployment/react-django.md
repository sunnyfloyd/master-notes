# React and Django (Architecture and Deployment)

## Sources

- [Making React and Django play well together](https://fractalideas.com/blog/making-react-and-django-play-well-together/)

## Frontend and Backend Architectures

There are 4 main architectures that can be applied to separete frontend and backend:

1. Running the frontend and the backend on distinct origins (frontend: app.example.com. tha makes cross-origin API requests to api.example.com). Most Single-Page Apps (SPA) use this architecture.

2. Making the backend serve static files for the frontend. This is Django’s default behavior in development: `runserver` serves static assets with a WSGI middleware provided by the staticfiles app. WhiteNoise provides a production-ready implementation of that behavior.

3. Making the frontend proxy API requests to the backend. Traditional production deployments of Django use this architecture. With Apache and mod_wsgi, Apache serves static files and proxies other requests to mod_wsgi. With nginx and a WSGI server such as gunicorn, uWSGI, or waitress, nginx serves static files and proxies other requests to the application server.

4. Dispatching frontend and backend requests with a reverse proxy. This setup is less common. It happens when a CDN (e.g. CloudFront) serves static assets from an object storage (e.g. S3) and forwards other requests to an application server. For practical purposes, it doesn’t matter very much how static files are served, so options 3 and 4 are equivalent.

- 1 - is called a **single page app model** and 2, 3, 4 are called **hybrid app models**.

- The “single page app” model requires setting up CORS because the frontend and the backend run on separate domains. This is easily achieved with [django-cors-headers](https://github.com/adamchainz/django-cors-headers) and the following settings::

```python
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = ['https://app.example.com']
```

- It’s hard to quantify how client-side rendering affects search ranking compared to traditional server-side rendering but it’s almost certainly a loss. Experiments show that the crawl frequency is lower. Regular HTML pages are a safer bet for the time being when SEO is a concern.

## Authentication

- There are two mainstream mechanisms for authenticating users: **cookies** and **JWTs**.

- By default, Django’s user authentication system relies on cookie-based sessions.

- Since JWTs are managed at the application level, each application must implement storage, expiry and renewal of JWTs. This is a significant, security-sensitive responsibility.
