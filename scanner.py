from enum import IntEnum


class Token:
    """Class to handle tokens
    """

    def __init__(self, token_type, lexeme, line, literal):
        """initializes a new token object

        Args:
            token_type: int -> comes from the token type enum
            lexeme: str -> the raw character of the token
            line: int -> line the token sits in
            literal: int, str, float, None -> the literal that the token holds
        """
        self.token_type = token_type
        self.lexeme = lexeme
        self.line = line
        self.literal = literal

    def __str__(self) -> str:
        """string representaion of Token
        """
        return f"Token {{ token_type: {self.token_type}, lexeme: '{self.lexeme}', literal: {self.literal}, line: {self.line} }}"


class TokenType(IntEnum):

