import sys
variables = {"args":sys.argv}
macros = {}

class token:
    tkn_type:int
    tkn_value:str

def make_token(tknt,tknv):
    newtoken=token()
    newtoken.tkn_type=tknt
    newtoken.tkn_value=tknv
    return newtoken

keywords = ["say","let","macro","dict","set","call","end","+","-","*","/","%","int","str","ask","get","get_elem","exec","goif","eval","print"]

def tokenize(file:str):
    tokens=[]
    token_asm=""

    for i in file:
        if i == " " or i == "'" or i == "\"":
            if token_asm != "":tokens.append(token_asm)
            token_asm=""
            tokens.append(i)
        else:token_asm+=i
    if token_asm != "":tokens.append(token_asm)

    tokens_clone=tokens
    tokens=[]
    token_asm=""
    mode=None

    for i in tokens_clone:
        if mode == "DQUOTE":
            if i == "\"":
                mode=None
                tokens.append(make_token("string",token_asm))
                token_asm=""
            else:token_asm+=i
        elif mode == "QUOTE":
            if i == "'":
                mode=None
                tokens.append(make_token("string",token_asm.replace(r"\n","\n")))
                token_asm=""
            else:token_asm+=i
        elif i in keywords:
            tokens.append(make_token("keyword",i))
        elif i == "\"":mode="DQUOTE"
        elif i == "'":mode="QUOTE"
        elif i != " ":
            try:
                tokens.append(make_token("number",int(i)))
            except:
                tokens.append(make_token("identifier",i))


    return tokens

stack=[]

def run(tokens:list):
    global stack

    def push(value):
        stack.append(value)

    def pop():
        return stack.pop()

    counter = 0
    
    def get_next(num:int):
        if counter+num < len(tokens):
            return tokens[counter+num]
        else:return None

    while counter < len(tokens):
        current = tokens[counter]

        if current.tkn_type == "keyword":
            if current.tkn_value=="say":
                print(stack[-1],end="")
            elif current.tkn_value=="+":
                push(stack[-2]+stack[-1])
            elif current.tkn_value=="-":
                push(stack[-2]-stack[-1])
            elif current.tkn_value=="*":
                push(stack[-2]*stack[-1])
            elif current.tkn_value=="/":
                push(stack[-2]/stack[-1])
            elif current.tkn_value=="%":
                push(stack[-2]%stack[-1])
            elif current.tkn_value=="int":push(int(stack[-1]))
            elif current.tkn_value=="str":push(str(stack[-1]))
            elif current.tkn_value=="let":variables.update({stack[-1]:stack[-2]})

            elif current.tkn_value=="ask":variables.update({stack[-1]:input()})

            elif current.tkn_value=="get_elem":push(stack[-2][stack[-1]])

            elif current.tkn_value=="get":push(variables[stack[-2]].get(stack[-1]))

            elif current.tkn_value=="dict":variables.update({stack[-1]:{}})

            elif current.tkn_value=="set":
                variables[stack[-3]].update({stack[-2]:stack[-1]})

            elif current.tkn_value=="exec":run(tokenize(stack[-1]))

            elif current.tkn_value=="print":print(stack[-1])

            elif current.tkn_value=="goif":
                if stack[-1] == True:
                    counter=stack[-3]
                    continue
                else:
                    counter=stack[-2]
                    continue

            elif current.tkn_value=="eval":
                push(eval(" ".join([str(stack[-3]), str(stack[-1]), str(stack[-2])])))

            else:print("Not implemented yet : ",current.tkn_value)
        elif current.tkn_type == "number":
            push(current.tkn_value)
        elif current.tkn_type == "string":
            push(current.tkn_value)
        elif current.tkn_type == "identifier":
            push(variables.get(current.tkn_value))

        counter+=1
