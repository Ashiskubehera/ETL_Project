import re

#API URL
API_url = 'https://api.coincap.io/v2/assets'

#Database Credential
db_username = '*************'
db_password = *************
db_host = '*************'
db_port = *************
db_name = '*************'


#Regular Expression used
def identify_user_input(user_input):
    id_pattern = re.compile(r'id (\w+)', re.I)
    symbol_pattern = re.compile(r'symbol (\w+)', re.I)
    name_pattern = re.compile(r'name (\w+)', re.I)
    rank_pattern = re.compile(r'rank (\d+)', re.I)
    price_pattern = re.compile(r'price (>|<|=)?\s*(\d+)', re.I)

    # User requarement
    id_match = id_pattern.search(user_input)
    symbol_match = symbol_pattern.search(user_input)
    name_match = name_pattern.search(user_input)
    rank_match = rank_pattern.search(user_input)
    price_match = price_pattern.search(user_input)

    if id_match:
        Id = id_match.group(1)
        return f"id==\"{Id}\""
    elif symbol_match:
        symbol = symbol_match.group(1)
        return f"symbol==\"{symbol}\""
    elif name_match:
        name = name_match.group(1)
        return f"name==\"{name}\""
    elif rank_match:
        rank = rank_match.group(1)
        return f"rank=={rank}"
    elif price_match:
        operator = price_match.group(1) or "=="
        amount = price_match.group(2)
        return f"price_Rupee{operator}{amount}"
    else:
        print("Sorry, I couldn't understand the user's request.")
        return f"id==\"Rupee\""