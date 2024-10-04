from numpy import random
import numpy as np
from constants import LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT, BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS

def random_next_event_selection(current_state):
        return random.choice(LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT[current_state], p = BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS[current_state])
