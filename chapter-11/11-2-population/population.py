# 11.2(a) Population

def format_city_country(city, country, population=''):
    """Return a neatly formatted string of the form
       'City, Country - Population: xxx'."""
    if population:
        return f"{city.title()}, {country.title()} - Population: {population}"
    else:
        return f"{city.title()}, {country.title()}"