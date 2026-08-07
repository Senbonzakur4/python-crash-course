# 11.1(b) City Country

from city_country import format_city_country

def test_city_country_format():
    """Test the format_city_country function."""
    formatted_city = format_city_country('santiago', 'chile')
    assert formatted_city == 'Santiago, Chile'