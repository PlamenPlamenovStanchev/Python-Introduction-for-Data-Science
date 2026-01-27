countries = input().split(", ")
capitals = input().split(", ")
country_capitals = dict(zip(countries, capitals))
for country, capital in country_capitals.items():
    print(f"{country} -> {capital}")