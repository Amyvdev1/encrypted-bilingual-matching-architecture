"""Pure credit state transition reference, with no payment side effects."""
def transition(state, event):
    if state not in {"RESERVED", "CONSUMED", "RESTORED"}: raise ValueError("unknown state")
    targets = {"complete":"CONSUMED", "cancel":"RESTORED", "expire":"RESTORED"}
    if event not in targets: raise ValueError("unknown event")
    target = targets[event]
    if state == "RESERVED" or state == target: return target
    raise ValueError("conflicting terminal transition")
