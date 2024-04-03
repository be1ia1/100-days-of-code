



person1, person2 = get_person(randint(len(data))), get_person(randint(len(data)))

from game_data import data

print(data[2])
print(data[1])

print(data[2]["follower_count"] > data[1]["follower_count"])

answer = {
        ['A']: person1["follower_count"] > person2["follower_count"],
        ['B']: person2["follower_count"] > person1["follower_count"]
    }