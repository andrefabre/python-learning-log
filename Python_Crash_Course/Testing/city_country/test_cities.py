from city_functions import city_country

def test_city_country():
    """Do names like Santiago, Chile work?"""
    city_country_name = city_country("Santiago", "Chile")
    assert city_country_name == "Santiago, Chile"

def test_city_country_population():
    """Do names like Santiago, Chile, Population xxxxxx work?"""
    city_country_name = city_country("Santiago", "Chile", 5000000)
    assert city_country_name == "Santiago, Chile - population 5000000"