def baseline(state):
    queue_lengths = state["queue_lengths"]
    
    # pick lane with max traffic
    best_lane = queue_lengths.index(max(queue_lengths))
    
    return {"lane": best_lane}