import random
import itertools

# Global constant for random event environments
ENVIRONMENTS = (("bat", "?", "A weak bat flutters around you"),
                ("goblin", "?", "A ferocious goblin sees you"),
                ("nothing", "?", "There is nothing here"))


def random_event(character):
    weak_enemies_list = list(itertools.repeat(ENVIRONMENTS[0], character["level"]))
    strong_enemies_list = list(itertools.repeat(ENVIRONMENTS[1], character["level"]))
    none_list = list(itertools.repeat(ENVIRONMENTS[2], 5))
    scaled_environment_list = list(itertools.chain.from_iterable([weak_enemies_list, strong_enemies_list, none_list]))
    # print(scaled_environment_list)
    return random.choice(scaled_environment_list)


def cool_description(_):
    return random.choice([("", "!", "The musty ground envelops you"), ("", "!", "The dark air is suffocating"),
                          ("", "!", "You can't see through this fog"), ("", "!", "You smell rotting flesh")])


def wall(_):
    return "wall", "%", "A wall towers over you"


def water(_):
    return "water", "#", "A large body of water"


def item(_):
    return "item", "@", "You see a item to help your adventures"


def final_boss(_):
    return "boss", "@", "The final boss is menacing"
