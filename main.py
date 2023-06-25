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
#estructura de control if ---------------------------------------
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
#-----------------------------------------------------
# estructura de control while ------------------------
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
#----------------------------------------------------
#usos generales -----------------------------------
def p_assignmentRule(p):
  '''
    assignmentRule : ID ASSIGNMENT number
                    | ID ASSIGNMENT ID
                    | ID ASSIGNMENT condition
                    | ID ASSIGNMENT TRUE
                    | ID ASSIGNMENT FALSE
                    | ID ASSIGNMENT creationTDA
                    | ID ASSIGNMENT operations
                    | ID ASSIGNMENT array
                    | ID ASSIGNMENT indexation
                    | ID ASSIGNMENT attribute
  '''
def p_bodyLine(p):
  '''
    bodyLine : assignmentRule
              | PRINT printBody 
              | nestedConditional
              | nestedWhile
              | functionCall
              | arrayConcat
              | RETURN arguments
              | PUTS printBody
              | method
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
              | method
              | functionCall
  '''

def p_argument(p):
  '''
    argument : ID
              | number
              | attribute
              | indexation
              | STRING
  '''

def p_arguments(p):
  '''
  arguments : argument
            | argument COMMA arguments
  '''
def p_method(p):
  '''
    method : ID DOT functionCall 
  '''
#------------------------------------------------------------  
#Parameters
def p_parameters(p):
  '''
    parameters : ID 
               | ID COMMA parameters 
  '''

def p_functionCall(p):
  '''
  functionCall : ID LPAREN arguments RPAREN
              | ID LPAREN RPAREN
  '''

#StructureData 
#STACK
def p_creationStack(p):
  '''
  creationStack : STACK DOT NEW
                | OPENBRACKET CLOSEDBRACKET
  '''


#linkedlist

def p_creationLinkedList(p):
  'creationLinkedList : LINKEDLIST DOT NEW'

def p_creationTDA(p):
  '''
    creationTDA : creationStack
                | creationLinkedList
                | creationHashmap

  '''

#Hashmap
def p_creationHashmap(p):
  '''creationHashmap : HASH DOT NEW
                    | LBRACE pairs RBRACE
                    | LBRACE RBRACE
  '''
def p_pair(p):
    '''pair : STRING COLON value'''

def p_pairs(p):
    '''pairs : pair
             | pair COMMA pairs''' 
    
def p_value(p):
    '''value : ID
             | STRING 
             | number
             | LBRACE pairs RBRACE
             | LBRACE RBRACE
    '''


#Operations
def p_arithmeticOperator(p):

  '''
    arithmeticOperator : PLUS
                        | MINUS
                        | POWER
                        | MULTIPLICATION 
                        | DIVISION
  '''
def p_attribute(p):
  '''
    attribute : ID DOT ID
  '''

def p_operationValue(p):
  '''
    operationValue : ID
                   | number
                   | attribute
                   | indexation
  '''
def p_operation(p):
  '''operation : operationValue arithmeticOperator operationValue
               | LPAREN operationValue arithmeticOperator operationValue RPAREN
  '''

def p_operations(p):
  '''
    operations : operation
               | operation arithmeticOperator operations
               | operation arithmeticOperator operationValue
               | operationValue arithmeticOperator operation
  '''
#DataTypes

#array----------------------------------------------
def p_array(p):
  '''array : OPENBRACKET element_list CLOSEDBRACKET
           | OPENBRACKET CLOSEDBRACKET'''

def p_element_list(p):
  '''element_list : conditionValue
                 | element_list COMMA conditionValue'''

def p_conditionValue(p):
  '''
    conditionValue : ID
                   | number
                   | indexation
                   | attribute
  '''
def p_arrayConcat(p):
  '''
  arrayConcat : ID ARRAYAPPEND ID
              | ID ARRAYAPPEND number
  '''

def p_indexation(p):
  '''
    indexation : ID OPENBRACKET element_list CLOSEDBRACKET
               | ID OPENBRACKET operation CLOSEDBRACKET
  '''
#----------------------------------------------

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
