class Country:
    def __init__(self, country: str, population: int, area: int) -> "Country":
        self.country = country
        self.population = population
        self.area = area

    def is_big(self) -> bool:
        if self.population > 20000000 and self.area > 3000000:
            status = True
        else:
            status = False
        return status
    
    def compare_pd(self, second: "Country") -> None:
        if (self.population / self.area) < (second.population / second.area):
            print(f" {self.country} has larger population density than {second.country}")
        else:
            print(f" {second.country} has larger population density than {self.country}")

australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
andorra.compare_pd(australia)
