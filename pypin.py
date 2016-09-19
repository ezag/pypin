from __future__ import print_function

from urllib import urlencode
from urllib2 import urlopen
from urlparse import parse_qs
import json
import os.path
import sys

ACCESS_TOKEN_PATH = '.pypin-access-token'

def cache_access_token(access_token):
    with open(ACCESS_TOKEN_PATH, 'w') as f:
        f.write(access_token)


def request_access_token():
    oauth_url = '{}?{}'.format(
        'https://api.pinterest.com/oauth/',
        urlencode(dict(
            client_id=4779055074072594921,
            redirect_uri='https://developers.pinterest.com/tools/api-explorer/',
            scope=','.join(['read_public', 'write_public']),
            response_type='token',
        ))
    )
    redirect_url = raw_input(
        "- Go to following URL in your browser: \n\n{}\n\n"
        "- Confirm permissions\n"
        "- You'll be redirected to another page - put its URL below:\n\n"
        "> ".format(oauth_url))
    access_token = parse_qs(redirect_url.split('?')[1])['access_token'][0]
    cache_access_token(access_token)
    return access_token


def get_access_token():
    if os.path.exists(ACCESS_TOKEN_PATH):
        with open(ACCESS_TOKEN_PATH) as f:
            access_token = f.readline()
    else:
        access_token = request_access_token()
    return access_token


def post_pin(access_token, board, note, link, image_url):
    response = urlopen(
        'https://api.pinterest.com/v1/pins/',
        data=urlencode(dict(
            access_token=access_token,
            board=board,
            note=note,
            link=link,
            image_url=image_url,
        )))
    response_data = json.load(response)
    return response_data


if __name__ == '__main__':
    board, note, link, image_url = sys.argv[1:]
    access_token = get_access_token()
    response = post_pin(access_token, board, note, link, image_url)
    print(json.dumps(response, indent=2))
