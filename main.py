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
    instruction : conditional
  '''
def p_conditional(p):
  '''
    conditional : IF condition instructionBody END
                | IF condition instructionBody conditionalElsif END
                | IF condition instructionBody ELSE instructionBody END
                | IF condition instructionBody conditionalElsif ELSE instructionBody END
  '''
def p_elsif(p):
  '''
  elsif : ELSIF condition instructionBody 
  '''
def p_nestedConditional(p):
  '''
    nestedConditional : conditional
                      | conditional nestedConditional
  '''

def p_conditionalElsif(p):
  '''
  conditionalElsif : elsif 
                  | elsif  conditionalElsif
  '''


def p_instructionLoop(p):
  '''
    instruction : whileLoop 
  '''

def p_whileLoop(P):
  '''
  whileLoop : WHILE condition instructionBody END
  '''

def p_nestedWhile(p):
  '''
    nestedWhile : whileLoop
                | whileLoop nestedWhile
  '''


def p_bodyLine(p):
  '''
    bodyLine : ID ASSIGNMENT number
                    | ID ASSIGNMENT STRING
                    | PRINT printBody 
                    | nestedConditional
                    | nestedWhile
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

def p_operation(p):
  '''
    operations : number arithmaticOperator number
  '''
#DataTypes

def p_conditionValue(p):
  '''
    conditionValue : ID
                   | number
  '''

def p_condition(p):
  '''
    condition : conditionValue comparator conditionValue
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
