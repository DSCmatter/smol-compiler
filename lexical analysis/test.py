from lex import * 

def main():
    source = "IF+-123 foo*THEN/"
    lexer = Lexer(source)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()

main()

# If this runs successfully and shows output like: 
# TokenType.IF
# TokenType.PLUS
# TokenType.MINUS
# TokenType.NUMBER
# TokenType.IDENT
# TokenType.ASTERISK
# TokenType.THEN
# TokenType.SLASH
# TokenType.NEWLINE

# then lexer can correctly identify every token that the language needs.