from easygui import *



def sportsType():
    image = "sports-smart-analysis.png"
    msg = "Please Choose the Sport ?"
    choices = ["Football","Tennis" ]
    reply = buttonbox(msg, image=image, choices=choices)
    print(reply)
    print(type(reply))
    return reply
    
def informationForm(msg,fieldNames):

    title = "Sports Smart Analysis"
  
    fieldValues = []  # we start with blanks for the values
    fieldValues = multenterbox(msg,title, fieldNames)
    print(fieldValues)
    print(type(fieldValues))
    #make sure that none of the fields was left blank
    while 1:
        if fieldValues == None: break
        errmsg = ""
        if (isinstance(fieldValues, int)):
             return fieldValues
             break

        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
        if errmsg == "":
            return fieldValues
            break # no problems found
        errmsg = msg + "\n" + errmsg
        fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
    
       
            



def askUser(Content):
    msg = Content
    title = "Please Confirm"
    F = ynbox(msg,title)

    print(F)
    return F

