from pyparsing import CaselessKeyword, Word, alphas, alphanums, delimitedList, Suppress, Optional, Group, ParseException, Literal

def build_sql_parser():
    SELECT = CaselessKeyword("select")
    INSERT = CaselessKeyword("insert")
    INTO = CaselessKeyword("into")
    VALUES = CaselessKeyword("values")
    DELETE = CaselessKeyword("delete")
    FROM = CaselessKeyword("from")
    WHERE = CaselessKeyword("where")
    
    identifier = Word(alphas, alphanums + "_").setName("identifier")
    columnName = delimitedList(identifier)
    tableName = identifier
    value = Word(alphanums + "_'\"-") 
    valueList = Group(delimitedList(value))
    
    selectStmt = (
        SELECT + columnName("columns") + 
        FROM + tableName("table") + 
        Optional(WHERE + identifier + Literal("=") + value)("where") + 
        Optional(";")
    )
    
    insertStmt = (
        INSERT + INTO + tableName("table") + 
        Optional("(" + columnName("columns") + ")") +
        VALUES + "(" + valueList("values") + ")" + 
        Optional(";")
    )
    
    deleteStmt = (
        DELETE + FROM + tableName("table") + 
        Optional(WHERE + identifier + Literal("=") + value)("where") + 
        Optional(";")
    )
    
    sqlParser = selectStmt | insertStmt | deleteStmt
    
    return sqlParser

sql_parser = build_sql_parser()

def check_sql_syntax(sql: str) -> bool:
    try:
        result = sql_parser.parseString(sql, parseAll=True)
        # print("Syntax is correct. Detected:", result)
        return True
    except ParseException as pe:
        # print("Incorrect syntax:")
        # print(pe.explain())
        return False

# print("\n--- TEST SELECT ---")
# print(check_sql_syntax("SELECT id, name FROM users WHERE id=1;"))    # True
# print(check_sql_syntax("SELECT FROM users;"))                        # False             

# print("\n--- TEST INSERT ---")
# print(check_sql_syntax("INSERT INTO customers VALUES (1, 'John');"))             # True
# print(check_sql_syntax("INSERT INTO orders (id, product) VALUES (101, 'X');"))   # True
# print(check_sql_syntax("INSERT INTO VALUES (1,2);"))                             # False

# print("\n--- TEST DELETE ---")
# print(check_sql_syntax("DELETE FROM logs WHERE date='2023-01-01';"))   # True
# print(check_sql_syntax("DELETE FROM products;"))                       # True           
# print(check_sql_syntax("DELETE products WHERE id=5;"))                 # False       