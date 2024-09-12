from base_api_requestor import Requestor

client = Requestor()
print(client.get('https://httpbin.org/anything').text)
print(client.get('https://httpbin.org/cookies/set?foo1=one&foo2=two').text)
print(client.get('https://httpbin.org/cookies/set?foo1=one_proxy&foo2=two_proxy', True).text)
print(client.get('https://httpbin.org/cookies', True).text)
print(client.get('https://httpbin.org/anything').text)
print(client.get('https://httpbin.org/anything', True).text)
print(client.get('https://httpbin.org/anything').text)
print(client.client.cookies)
