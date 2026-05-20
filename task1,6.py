import datetime

def merge_lists(web_order: list, app_order: list) -> list:
    result = []

    numweb = 0
    numapp = 0

    while numweb < len(web_order) and numapp < len(app_order):
        if web_order[numweb] <= app_order[numapp]:
            result.append(web_order[numweb])
            numweb += 1
        
        else: 
            result.append(app_order[numapp])
            numapp += 1
 
    while numweb < len(web_order):
        result.append(web_order[numweb])
        numweb += 1 

    while numapp < len(app_order):
        result.append(app_order[numapp])
        numapp += 1 
    return result

web_order = [
    "10:00",
    "10:30",
    "12:15"
]
app_order = [
    "10:05",
    "10:40",
    "12:00"
]

merged = merge_lists(web_order, app_order)

print(merged)

            
