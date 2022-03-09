def app(environ: dict, start_response) -> list[bytes]:
    """ my wsgi application """
    if environ["REQUEST_METHOD"] == "GET":
        return []
