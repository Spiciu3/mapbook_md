
users: list = [
    {"name": "Kasia", "location": "Warszawa", "posts": 3},
    {"name": "Basia", "location": "Kraków", "posts": 5},
    {"name": "Asia", "location": "Wrocław", "posts": 7},
]

for user in users:
    print(f"Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów ")
