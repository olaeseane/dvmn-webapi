import os
import requests
import argparse

from requests.exceptions import HTTPError
from dotenv import load_dotenv


def shorten_link(token, link):
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    payload = {
        "long_url": link
    }
    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()


def count_clicks(token, bitlink_id):
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_id}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='CLI for URL shortener using bit.ly'
    )
    parser.add_argument('url', help='long URL or short bitlink')
    args = parser.parse_args()

    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')

    link = args.url

    if not link.startswith('bit.ly'):
        try:
            bitlink = shorten_link(bitly_token, link)
        except HTTPError as http_err:
            print(f'HTTP error occurred:\n{http_err}')
        except Exception as err:
            print(f'Other error occurred:\n{err}')
        else:
            print('Битлинк', bitlink['link'])
    else:
        try:
            bitlink_clicks = count_clicks(bitly_token, link)
        except HTTPError as http_err:
            print(f'HTTP error occurred:\n{http_err}')
        except Exception as err:
            print(f'Other error occurred:\n{err}')
        else:
            print(
                f'По вашей ссылке прошли {bitlink_clicks["total_clicks"]} раз')
