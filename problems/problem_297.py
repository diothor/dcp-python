def lazy_bartender_drinks(preferences: dict) -> int:
    min_drinks = find_min_subset_of_drinks(preferences, set())
    return len(min_drinks)


def find_min_subset_of_drinks(preferences: dict, drinks_for_all: set) -> set:
    if not preferences:
        # if there are no more preferences, stop recursion
        return drinks_for_all

    current_drinks = set(preferences.popitem()[1])
    options = []
    if current_drinks & drinks_for_all:
        # if a person has in his preferences drink, which is already in our set, just simply go for another person
        options.append(find_min_subset_of_drinks(preferences, drinks_for_all))
    else:
        # if a person does not have any drink in our set, create all possible versions of drinks_for_all set and go for another person
        for drink in current_drinks:
            drinks_for_all_copy = drinks_for_all.copy()
            drinks_for_all_copy.add(drink)
            options.append(find_min_subset_of_drinks(preferences.copy(), drinks_for_all_copy))
    # from all options get first set with the lowest number of drinks
    return min(options, key=lambda d: len(d))


test_preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
assert lazy_bartender_drinks(test_preferences) == 2

test_preferences_2 = {
    0: [3, 7, 5, 2, 9],
    1: [5],
    2: [2, 3],
    3: [4],
    4: [3, 4, 5, 7]
}
assert lazy_bartender_drinks(test_preferences_2) == 3
