import heapq

class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.food_to_info = {}  # maps food -> (cuisine, rating)
        self.cuisine_to_heap = {}  # maps cuisine -> max-heap of (-rating, food)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_info[food] = (cuisine, rating)
            if cuisine not in self.cuisine_to_heap:
                self.cuisine_to_heap[cuisine] = []
            # Use negative rating for max-heap
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        cuisine, oldRating = self.food_to_info[food]
        self.food_to_info[food] = (cuisine, newRating)
        # Push the new rating into the heap
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisine_to_heap[cuisine]
        while True:
            # Get the current highest-rated food
            rating, food = heap[0]
            # If the rating in heap matches the actual rating, return the food
            if -rating == self.food_to_info[food][1]:
                return food
            # Otherwise, remove outdated entry
            heapq.heappop(heap)
foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
ratings = [9, 12, 8, 15, 14, 7]

foodRatings = FoodRatings(foods, cuisines, ratings)

print(foodRatings.highestRated("korean"))   # "kimchi"
print(foodRatings.highestRated("japanese")) # "ramen"
foodRatings.changeRating("sushi", 16)
print(foodRatings.highestRated("japanese")) # "sushi"
foodRatings.changeRating("ramen", 16)
print(foodRatings.highestRated("japanese")) # "ramen"
