from numpy import random
import numpy as np
from constants import *

def random_next_event_selection(slice_number, current_state, lambda_value):
        if(lambda_value==0):
                if(slice_number == "1"):
                        return random.choice(LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_ATTACKISH_SLICE1[current_state], p = BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS_ATTACKISH_SLICE1[current_state])
                if(slice_number == "2"):
                        return random.choice(LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_ATTACKISH_SLICE2[current_state], p = BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS_ATTACKISH_SLICE2[current_state])
        else:
                if(slice_number == "1"):
                        return random.choice(LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_UNSTABLE_SLICE1[current_state], p = BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS_UNSTABLE_SLICE1[current_state])
                if(slice_number == "2"):
                        return random.choice(LEGAL_NEXT_EVENTS_PER_CURRENT_EVENT_UNSTABLE_SLICE2[current_state], p = BENIGN_PRBABILITIES_OF_LEGAL_NEXT_EVENTS_UNSTABLE_SLICE2[current_state])