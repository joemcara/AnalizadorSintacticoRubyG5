from lexico import tokens
import ply.yacc as yacc

#Intructions

def p_instruction(p):
  'instruction : instructionBody'

def p_instructionFunction(p):
  '''
  instruction : DEF ID LPAREN parameters RPAREN instructionBody END
              | DEF ID LPAREN RPAREN END
  '''

def p_instructionConditional(p):
  '''  
    instruction : IF condition 
  '''

def p_instructionLoop(p):
  '''
    instruction : WHILE condition instructionBody END
  '''
def p_bodyLine(p):
  '''
    bodyLine : ID ASSIGNMENT number
                    | ID ASSIGNMENT STRING
                    | PRINT printBody  
  '''
def p_instructionBody(p):
  '''
    instructionBody : bodyLine
                    | bodyLine instructionBody 
  '''

def p_printBody(p):
  '''
  printBody : ID 
              | TRUE  
              | FALSE 
              | dataType
              | condition
  '''
#Parameters
def p_parameters(p):
  '''
    parameters : ID 
               | ID COMMA ID 
  '''

#StructureData


#Operations
def p_arithmeticOperator(p):

  '''
    arithmaticOperator : PLUS
                        | MINUS
                        | POWER
                        | MULTIPLICATION 
                        | DIVISION
  '''

def p_operations(p):
  '''
    operations : dataType arithmaticOperator dataType
  '''
#DataTypes

def p_condition(p):
  '''
    condition : number comparator number
  '''

def p_comparator(p):
  '''
    comparator : GREATERTHAN
               | LESSTHAN
               | EQUALS
               | GREATEROREQUALS
               | LESSOREQUALS
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
