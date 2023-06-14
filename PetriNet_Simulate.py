import random

# Define the initial marking of places
marking = {
    'p1': 1,
    'p14': 1
}

# Define the enabled transitions and their arcs
transitions = {
    't1': {'input': {'p1': 1}, 'output': {'p2': 1}},
    't2': {'input': {'p2': 1}, 'output': {'p3': 1}},
    't3': {'input': {'p3': 1, 'p14': 1}, 'output': {'p4': 1}},
    't4': {'input': {'p4': 1}, 'output': {'p5': 1}},
    't5': {'input': {'p5': 1}, 'output': {'p6': 1}},
    't6': {'input': {'p6': 1}, 'output': {'p7': 1}},
    't7': {'input': {'p7': 1}, 'output': {'p9': 1}},
    't8': {'input': {'p5': 1}, 'output': {'p8': 1}},
    't10': {'input': {'p8': 1}, 'output': {'p10': 1}},
    't11': {'input': {'p10': 1}, 'output': {'p11': 1}},
    't12': {'input': {'p10': 1}, 'output': {'p12': 1}},
    't13': {'input': {'p11': 1}, 'output': {'p13': 1}},
    't14': {'input': {'p12': 1}, 'output': {'p14': 1}}
}

def simulate():
    print("Initial marking:", marking)

    while True:

        enabled_transitions = []
        for transition, arcs in transitions.items():
            if all(place in marking and marking[place] >= arcs['input'][place] for place in arcs['input']):
                enabled_transitions.append(transition)

        if not enabled_transitions:
            break

        # Choose a random enabled transition
        chosen_transition = random.choice(enabled_transitions)

        # Fire the chosen transition
        for place in transitions[chosen_transition]['input']:
            marking[place] -= transitions[chosen_transition]['input'][place]

        for place in transitions[chosen_transition]['output']:
            if place in marking:
                marking[place] += transitions[chosen_transition]['output'][place]
            else:
                marking[place] = transitions[chosen_transition]['output'][place]

        print("Fired transition:", chosen_transition)
        print("Updated marking:", marking)
        print()

simulate()

