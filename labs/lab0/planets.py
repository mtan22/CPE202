# Given earth weight and planet, returns weight on provided planet
# If string does not match a planet, raise ValueError
def weight_on_planets(pounds: float, planet: str) -> float:

    if planet == 'Mars':
        marsWeight = pounds * 0.38
        return marsWeight

    elif planet == 'Jupiter':
        jupiterWeight = pounds * 2.34
        return jupiterWeight

    elif planet == 'Venus':
        venusWeight = pounds * 0.91
        return venusWeight

    else:
        raise ValueError


if __name__ == '__main__':  # pragma: no cover
    pounds = float(input("What do you weigh on earth? "))
    print("\nOn Mars you would weigh", weight_on_planets(pounds, 'Mars'), "pounds.\n" +
          "On Jupiter you would weigh", weight_on_planets(pounds, 'Jupiter'), "pounds.")
