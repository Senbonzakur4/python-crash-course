# 11.2(b) Population

from population import format_city_country

def test_city_country_format():
    """Test the format_city_country function."""
    formatted_city = format_city_country('santiago', 'chile', 5_000_000)
    assert formatted_city == 'Santiago, Chile - Population: 5000000'