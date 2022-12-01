import random
import itertools

# Global constant for random event environments, add more events for higher probability of occurrence
ENVIRONMENTS = (("bat", "", "A weak bat flutters around you"),
                ("goblin", "", "A ferocious goblin sees you"),
                ("nothing", "", "There is nothing here"),
                ("nothing", "", "There is nothing here"))


def random_event(character):
    enemies_list = list(itertools.repeat(ENVIRONMENTS[0], character["level"] * 3))
    ridl_list = list(itertools.repeat(ENVIRONMENTS[1], character["level"] * 2))
    none_list = list(itertools.repeat(ENVIRONMENTS[2], character["level"] * 1))
    scaled_environment_list = list(itertools.chain.from_iterable([enemies_list, ridl_list, none_list]))
    print(scaled_environment_list)
    return random.choice(scaled_environment_list)


def cool_description(character):
    return random.choice([("", "", "The musty ground envelops you"), ("", "", "The dark air is suffocating"),
                          ("", "", "You can't see through this fog"), ("", "", "You smell rotting flesh")])


def wall(character):
    return ("wall", "%", "A wall towers over you")


def water(character):
    return ("water", "#", "A large body of water")