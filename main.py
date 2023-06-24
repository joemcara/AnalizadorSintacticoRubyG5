from lexico import tokens
import ply.yacc as yacc

#Intructions

def p_instruction(p):
  'instruction : PRINT printBody'

def p_instructionFunction(p):
  '''
  instruction : DEF ID LPAREN parameters RPAREN END
              | DEF ID LPAREN RPAREN END
  '''

def p_printBody(p):
  '''
  printBody : ID 
              | TRUE  
              | FALSE 
              | dataType
              | condition
  '''

def p_instructionConditional(p):
  '''  
    instruction : IF condition 
  '''
def p_instructionLoop(p):
  '''
    instruction : WHILE condition END
  '''
#Parameters
def p_parameters(p):
  '''
    parameters : ID 
               | ID COMMA ID 
  '''

#StructureData


#Operations
def p_operationsArithmetic(p):

  '''
    arithmetic : PLUS
              | MINUS
              | POWER
              | MULTIPLICATION 
              | DIVISION
  '''

def p_operations(p):
  '''
    operations : dataType arithmetic dataType
               | arithmetic dataType 
  '''
#DataTypes

def p_condition(p):
  '''
    condition : TRUE
               | FALSE
               | number GREATEROREQUALS number
  '''

def p_number(p):
    '''
      number : FLOAT
             | INTEGER
    '''

def p_dataType(p):
  '''
  dataType : STRING
           | number
  '''

def p_error(p):
  if p:
    print("Error de sintaxis en token:", p.type)
    #sintactico.errok()
  else:
    print("Syntax error at EOF")


sintactico = yacc.yacc()

while True:
  try:
    s = input('ruby > ')
  except EOFError:
    break
  if not s: continue
  result = sintactico.parse(s)
  if result != None: print(result)
