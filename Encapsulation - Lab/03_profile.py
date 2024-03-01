class Profile:
    def __init__(self, username, password) -> None:
        self.__username = None
        self.__password = None
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_length_valid = len(value) >= 8
        is_upper_case_presented = any(c.isupper() for c in value)
        is_digit_presented = any(c.isdigit() for c in value)

        if not (is_length_valid and is_upper_case_presented and is_digit_presented):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
