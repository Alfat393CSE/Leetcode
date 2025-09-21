from sortedcontainers import SortedList

class MovieRentingSystem(object):

    def __init__(self, n, entries):
        # Map to store price for each (shop, movie)
        self.price = {}
        
        # Unrented movies for each movie: movie -> SortedList of (price, shop)
        self.available = {}
        
        # Rented movies: SortedList of (price, shop, movie)
        self.rented = SortedList()
        
        for shop, movie, p in entries:
            self.price[(shop, movie)] = p
            if movie not in self.available:
                self.available[movie] = SortedList()
            self.available[movie].add((p, shop))

    def search(self, movie):
        if movie not in self.available:
            return []
        # Return first 5 shop numbers of available movies
        return [shop for p, shop in self.available[movie][:5]]

    def rent(self, shop, movie):
        p = self.price[(shop, movie)]
        # Remove from available
        self.available[movie].remove((p, shop))
        # Add to rented
        self.rented.add((p, shop, movie))

    def drop(self, shop, movie):
        p = self.price[(shop, movie)]
        # Remove from rented
        self.rented.remove((p, shop, movie))
        # Add back to available
        self.available[movie].add((p, shop))

    def report(self):
        # Return first 5 rented movies as [shop, movie]
        return [[shop, movie] for p, shop, movie in self.rented[:5]]
