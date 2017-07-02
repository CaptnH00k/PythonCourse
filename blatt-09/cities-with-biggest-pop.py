import heapq


class CitiesWithLargestPopulation:
    def __init__(self, file, k):
        self.file = file
        self.k = k
        self.queue = []
        self.read_cities_and_insert_into_queue()

    def read_cities_and_insert_into_queue(self):
        with open(self.file, "r") as fh:
            for line in fh:
                [population, city_name] = self.parse_line(line)
                heapq.heappush(self.queue, (population, city_name))

    @staticmethod
    def parse_line(line):
        """
        >>> tline = "testCity\ttestCountry\t420\t63.99722\t10.21828"
        >>> c = CitiesWithLargestPopulation.parse_line(tline)
        [420, "testCity"]
        """
        print(line)
        splitted_line = line.split("\t")
        return (int(splitted_line[2]), splitted_line[0])

    def get_cities(self, k):
        return heapq.nlargest(
            k,
            self.queue,
        )


if __name__ == "__main__":
    print("[i] Reading file...")
    c = CitiesWithLargestPopulation("./cities.txt", 10)
    print("[i] Outputting cities")
    for [pop, city_name] in c.get_cities(10):
        print(pop, city_name)
    print("---------------------")
    for [pop, city_name] in c.get_cities(20):
        print(pop, city_name)
