import json
import logging

import allure
from allure_commons.types import AttachmentType
from requests import Response


def json_dumping(current_dict) -> str:
    return json.dumps(current_dict, indent=4, ensure_ascii=True)


def pretty_headers(headers):
    if headers:
        return json_dumping(dict(headers))
    else:
        return 'None'


def pretty_body(body: str):
    if body:
        try:
            return json_dumping(json.loads(body))
        except:
            return '\n'.join(list(filter(lambda x: bool(x.split()), body.split('\n'))))
    else:
        return 'None'


def request_attaching_and_logging(response: Response):
    url = response.request.url
    method = response.request.method
    request_body = pretty_body(response.request.body)
    request_headers = pretty_headers(response.request.headers)
    response_body = pretty_body(response.text)
    response_headers = pretty_headers(response.headers)

    allure.attach(body=f'REQUEST {method} {url}', name='Request general info', attachment_type=AttachmentType.TEXT,
                  extension='.txt')
    allure.attach(body=request_headers, name='Request headers', attachment_type=AttachmentType.JSON,
                  extension=json)
    allure.attach(body=request_body, name='Request body', attachment_type=AttachmentType.TEXT, extension='txt')
    allure.attach(body=response_headers, name='Response headers', attachment_type=AttachmentType.JSON,
                  extension=json)
    allure.attach(body=response_body, name='Response body', attachment_type=AttachmentType.TEXT, extension='txt')

    logging.info(f'\n\nREQUEST {method} {url}\n'
                 f'\nREQUEST HEADERS: \n{request_headers}\n'
                 f'\nREQUEST BODY: \n{request_body}\n'
                 f'\nRESPONSE STATUS CODE {response.status_code}\n'
                 f'\nRESPONSE HEADERS: \n{response_headers}\n'
                 f'\nRESPONSE BODY: \n{response_body}\n')
