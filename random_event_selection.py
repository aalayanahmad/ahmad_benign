from numpy import random
from constants import LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT, PRBABILITIES_OF_LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_BENIGN

def random_next_event_selection(current_state):
        return random.choice(LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT[current_state], p = PRBABILITIES_OF_LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_BENIGN[current_state])
