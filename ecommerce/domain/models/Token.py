from ecommerce.domain.value_objects.TokenValue import TokenValue


class Token:
    def __init__(self, token_value: TokenValue):
        self.token_value = token_value

    def is_expired(self):
        return self.token_value.is_expired()

    def get_value(self):
        return self.token_value.get_value()