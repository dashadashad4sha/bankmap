import re

i = 1


def extract_street_name(address):
    pattern = r"\bул\.\s*(\S+)"
    match = re.search(pattern, address)
    if match:
        n = "Банкомат на ул. " + match.group(1)
        if n[-1] == ',':
            n = n[0:-1:1]
        return n
    return "Банкомат"



