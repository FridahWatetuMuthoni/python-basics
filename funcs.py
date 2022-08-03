def formated_name(first,last,middle=""):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
        
    return full_name.title()


def location(city,country):
    location = f"{city}, {country}"
    return location.title()
