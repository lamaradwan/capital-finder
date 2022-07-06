from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        print(url_components)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        print(dic)
        result = []
        if 'country' in dic:
            country = dic['country']
            url = 'https://restcountries.com/v3.1/name/'
            r = requests.get(url + country)
            data = r.json()
            print(data)
            for word_data in data:
                capital = f"The capital of {country} is {word_data['capital'][0]}"
                result.append(capital)

            message = str(result)
        elif 'capital' in dic:
            capital = dic['capital']
            url ='https://restcountries.com/v3.1/capital/'
            r = requests.get(url+capital)
            data = r.json()
            print(data)
            for capi in data:
                country = f"{capital} is the capital of {capi['name']['common']}"
                result.append(country)
            message = str(result)
        else:
            message = "Please provide me with a word"


        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())

        return
