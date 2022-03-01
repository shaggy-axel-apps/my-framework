import pprint as pp


def application(environ: dict, start_response) -> list[bytes]:
    """
    my simple `WSGI`-application:
    - `environ`: dict of env-vars
    - `start_response`: function for response
    """
    # передаем в ответ заголовки, статус ответа и content-type в headers
    start_response("200 OK", [("Content-Type", "text/html")])

    # можно просмотреть какие переменные передает gunicorn/uwsgi
    pp.pprint(environ, indent=4)

    # возвращаем body ответа
    return [b'Hello world from Simple WSGI-application']
