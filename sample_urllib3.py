# urllib3 is a powerful, user-friendly HTTP client for Python.
# To learn more about the package,
# visit https://urllib3.readthedocs.io/en/stable/reference/index.html
# if you are using Postman or Insomnia for APIs, you can use the services from httpbin.org
import urllib3
http = urllib3.PoolManager()

# httpbin.org is A simple HTTP Request & Response Service.
# POST
r = http.request(
     'POST',
     'http://httpbin.org/post',
     fields={'hello': 'world'})
print(r.data)
# GET - Read robots.txt of a website
r = http.request('GET', 'http://httpbin.org/robots.txt')
print(r.status)
print(r.data)