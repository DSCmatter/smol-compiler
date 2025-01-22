### Overview
B2C Transpiler is a lightweight and minimalistic compiler designed to process a BASIC dialect using a clean and simple syntax for better readability and ease of use. The compiler is built using a three-stage architecture:

- Lexing: Tokenizes the input code, breaking it into meaningful elements.

- Parsing: Validates the syntax structure according to the rules of the BASIC dialect.

- Emitting: Generates C code output, ensuring compatibility with a widely-used language for practical deployment.

### Requirements

- Python 3.x
- GCC 

### Main code is located in:
``` /emitter```

### How to run it?

- ```python3 main.py hello.txt ``` -> in /parsing & /emitter 
- ```python3 main.py hello.txt && gcc out.c && ./a.out``` -> in /emitter 

### References:
[Lexical analysis](https://en.wikipedia.org/wiki/Lexical_analysis)

[Parsing](https://en.wikipedia.org/wiki/Parsing)

[@Austin Henley](https://austinhenley.com/blog/teenytinycompiler1.html)

[More stuff](https://craftinginterpreters.com/contents.html)
