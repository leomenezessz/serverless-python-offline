import debugpy


class debug(object):
    def __init__(self, debug=False, host="0.0.0.0", port=5890):
        self.debug = debug
        self.host = host
        self.port = port

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            if self.debug and not debugpy.is_client_connected():
                debugpy.listen((self.host, self.port))
                debugpy.wait_for_client()
                return function(*args, **kwargs)
            return function(*args, **kwargs)

        return wrapper
