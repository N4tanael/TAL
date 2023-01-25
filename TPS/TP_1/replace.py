def replaceTokens(Entities):

    replacements = {"ORGANIZATION": "ORG",
                    "PERSON": "PERS",
                    "LOCATION": "LOC",
                    "DATE": "MISC",
                    "TIME": "MISC",
                    "MONEY": "MISC",
                    "PERCENT": "MISC",
                    "FACILITY": "ORG",
                    "GPE": "LOC"}
    
    for replacement in replacements:
        Entities = Entities.replace(replacement,replacements[replacement])
        

    return Entities

