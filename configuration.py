def get_tags():
    #todo - read these tags from cloud and return as list
    
    with open("tags.txt") as file:
        for i in file:
            x = i.split(', ')
    return x


def get_addresses():
    #todo read the ip addresses from cloud and return as list 
    with open("ipaddress.txt") as file:
        for i in file:
            x = i.split(', ')
    print(x)
    return x

