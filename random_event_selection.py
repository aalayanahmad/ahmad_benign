from numpy import random

def random_next_event_selection(current_state, legal_next_events_per_current_event, probabilities_of_legal_next_events_per_current_event):
        return random.choice(legal_next_events_per_current_event[current_state], probabilities_of_legal_next_events_per_current_event[current_state])
