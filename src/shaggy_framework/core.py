from types import FunctionType


class NotFoundPage:
    def __call__(self, request):
        return "404 Not found", "Page not found"


class Application:
    def __init__(self, url_patterns: list):
        self.url_patterns = url_patterns
        self.headers = [("Content-Text", "file/html")]

    def __call__(self, environ: dict, start_response: FunctionType) -> list[bytes]:
        """
        `environ` - dictionary with environ variables of request
        `start_response` - response function for client request
        """
        path = environ.get("PATH_INFO")
        if not path.endswith("/"):
            path = f"{path}/"

        if path in self.url_patterns:
            view = self.url_patterns.get(path)
        else:
            view = NotFoundPage()
        request = dict()

        code, text = view(request)
        start_response(code, self.headers)
        return [text.encode("utf-8")]
