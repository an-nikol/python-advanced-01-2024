import re
from pyisemail import is_email


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class ValidSymbolsCheck(Exception):
    pass


class EmailDoesNotExist(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "org", "net")
MIN_NAME_CHARS = 4

pattern = r"[^@]+@[^@]+\.[^@]+"  # it has exactly one @ sign and atleast one . in the part after the @

email = input()
while email != "End":
    if len(email.split("@")[0]) <= MIN_NAME_CHARS:
        raise NameTooShortError("Name must be more than 4 characters")

    elif "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    elif email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: .{', '.join(VALID_DOMAINS)}")
    elif not re.match(pattern, email):
        raise ValidSymbolsCheck
    elif not is_email(email, check_dns=True):
        raise EmailDoesNotExist("The email does not exist.")

    print("Email is valid.")
    email = input()
