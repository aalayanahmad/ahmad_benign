def violating_ues(data):
    # Dictionary to keep track of the last event for each UE in each lambda
    ue_last_event = {}

    for entry in data:
        ue, event, _, lambda_ = entry

        # Convert event and lambda to integers for comparison
        event = int(event)
        lambda_ = int(lambda_)

        if event == 1:  # Registration event
            # Check if UE is in the last lambda and if it was deregistered
            if ue in ue_last_event:
                last_lambda, last_event = ue_last_event[ue]
                # Check if last event was not deregistration (6) in the last lambda
                if last_lambda == lambda_ - 1 and last_event != 6:
                    print(f"Violation: UE '{ue}' is registering in lambda '{lambda_}' without deregistering from lambda '{last_lambda}'")
        
        # Update last event for the UE
        ue_last_event[ue] = (lambda_, event)