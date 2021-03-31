class Error(Exception):
    pass


class DownloadError(Error):
    pass


class PaymentGatewayError(Error):
    def __init__(self, code, message):
        self.code = code
        self.message = message


class Refused(PaymentGatewayError):
    pass


class Stolen(PaymentGatewayError):
    pass