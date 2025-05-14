python src/lexer/lexer.py -f test/main.gt -o test/output/token_output.json
python src/lexer/lexer.py -f test/main.gt
python src/parser/parser.py -f test/output/token_output.json -o test/output/ast_output.json
python src/parser/parser.py -f test/output/token_output.json