import random
import itertools

# Global constant for random event environments
ENVIRONMENTS = (("a weak enemy","",""), ("a strong enemy","",""), ("nothing","",""))


def random_event(character):
    enemies_list = list(itertools.repeat(ENVIRONMENTS[0], character["level"] * 3))
    ridl_list = list(itertools.repeat(ENVIRONMENTS[1], character["level"] * 2))
    none_list = list(itertools.repeat(ENVIRONMENTS[2], character["level"] * 1))
    scaled_environment_list = list(itertools.chain.from_iterable([enemies_list, ridl_list, none_list]))
    # print(scaled_environment_list)
    return random.choice(scaled_environment_list)


def cool_description(character):
    return random.choice([("the musty ground envelops you", "", ""), ("the dark air is suffocating", "", ""),
                          ("you can't see through this fog", "", ""), ("You smell rotting flesh", "", "")])


def wall(character):
    return ("wall", "%", "A wall")


def water(character):
    return ("water", "#", "A puddle of water")