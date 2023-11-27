import random

class Perfume:
    def __init__(self, name, brand, notes, category):
        self.attributes = {
            'name': name,
            'brand': brand,
            'notes': notes,
            'category': category
        }
class Recommendation:
    def __init__(self, perfumes_list):
        self.perfumes = self.load_perfumes(perfumes_list)

    def load_perfumes(self, perfumes_list):
        perfumes = []
        with open(perfumes_list, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                name, brand, notes, category = data[0], data[1], data[2:-1], data[-1]
                perfumes.append(Perfume(name, brand, notes, category))
        return perfumes

    def get_user_brand(self):
        available_brands = ["Le Labo", "Valentino", "Yves Saint Laurent", "Byredo", "Gucci"]
        print("Available Perfume Brands:", ", ".join(available_brands))

        while True:
            try:
                user_brand = input("Enter your favorite perfume brand: ").lower()
                if user_brand in map(str.lower, available_brands):
                    return user_brand
                else:
                    raise ValueError("Invalid brand. Please choose from the available brands.")
            except ValueError as e:
                print(e)

    def get_user_input(self):
        print("Let's pick out your next fragrance!")

        user_brand = self.get_user_brand()

        while True:
            try:
                # User input stored in lists
                notes = input("Enter your preferred fragrance notes separated by a comma: ").split(", ")
                if notes:
                    return [note.lower() for note in notes]
                else:
                    raise ValueError("Notes cannot be empty. Please enter at least one note.")
            except ValueError as e:
                print(e)

    def recommend_perfume(self, user_notes):
        # Updated recommendation algorithm based on shared notes
        recommended_perfumes = [perfume for perfume in self.perfumes
                                if len(set(user_notes) & set(map(str.lower, perfume.attributes['notes']))) >= 2]

        if not recommended_perfumes:
            print("Sorry, no matching perfumes found.")
        else:
            print("\nRecommended Perfumes:")
            for perfume in recommended_perfumes:
                print(f"{perfume.attributes['name']} by {perfume.attributes['brand']} - Notes: {', '.join(perfume.attributes['notes'])} - Category: {perfume.attributes['category']}")

if __name__ == "__main__":
    recommendation_system = Recommendation('perfumes_list.txt')
    user_notes = recommendation_system.get_user_input()
    recommendation_system.recommend_perfume(user_notes)
