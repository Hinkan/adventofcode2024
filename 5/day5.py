class value_rules():
    """docstring for ClassName."""
    def __init__(self, value, forbidden):
        self.value=value
        self.forbidden=[forbidden]
    
    def get_value(self):
        return self.value
    def get_forbidden(self):
        return self.forbidden

    



def read_instructions(filename):
    f=open(filename)
    empty_reached=False
    rules=[]
    instructions=[]
    for line in f:
        if line =="\n":
            empty_reached=True
            continue
        if empty_reached==False:
            rules.append(line[:-1])
        else:

            instructions.append(line[:-1].split(','))
    return rules, instructions

def prepare_rules_lists(rules):
    #reduced_instructions=list(set(instrctions)).sort()
    #forbiddens=[]
    dictlist=[]#dict={value:right column, forbiddens=[list of let values]}
    for rule in rules:
        values=[x.get_value() for x in dictlist]
        split=rule.split('|')
        if split[0] not in values:
            dictlist.append(value_rules(split[0], split[1]))
        else:
            dictlist[values.index(split[0])].forbidden.append(split[1])
    return dictlist

def check_violation(dictlist, instrcutionline):
    values_before=[instrcutionline[0]]
    values_w_rules=[x.get_value() for x in dictlist]
    for instruction in instrcutionline[1:]:
        for val in values_before:
            if instruction in values_w_rules:
                if val in dictlist[values_w_rules.index(instruction)].get_forbidden():
                    return True
        values_before.append(instruction)
    return False

def switch_violators(dictlist, instrcutionline):
    corrected=instrcutionline.copy()
    values_before=[instrcutionline[0]]
    values_w_rules=[x.get_value() for x in dictlist]
    for idx,instruction in enumerate(instrcutionline[1:]):
        for val in values_before:
            if instruction in values_w_rules:
                if val in dictlist[values_w_rules.index(instruction)].get_forbidden():
                    value1=instruction
                    value2=val
                    corrected[corrected.index(value1)], corrected[corrected.index(value2)]=corrected[corrected.index(value2)], corrected[corrected.index(value1)]
                    corrected=switch_violators(dictlist, corrected)
                    
        values_before.append(instruction)
    return corrected
        



if __name__=='__main__':
    rules, instructions=read_instructions("day5.txt")
    dictlist=prepare_rules_lists(rules)
    invalid_instructions=[]
    pagesum=0

    for dict in dictlist:
        print(f'{dict.get_value()}\t{dict.get_forbidden()}')
    
    for instruction in instructions:
        if check_violation(dictlist, instruction):

            print(f'{instruction} is forbidden')
            invalid_instructions.append(instruction)
            
        else:
            print(f'{instruction} is allowed')
            middleindex=int(len(instruction)/2)
            pagesum+=int(instruction[middleindex])
    print(pagesum)
    corrected=[]
    for tocorrect in invalid_instructions:
        corrected.append(switch_violators(dictlist, tocorrect))
        print(tocorrect)
    pagesum=0
    for instruction in corrected:
        if check_violation(dictlist, instruction):

            print(f'{instruction} is forbidden')
            invalid_instructions.append(instruction)
            
        else:
            print(f'{instruction} is allowed')
            middleindex=int(len(instruction)/2)
            pagesum+=int(instruction[middleindex])
    print(pagesum)