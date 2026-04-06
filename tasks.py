from env import TrafficEnv


def make_env(task="medium"):
    if task == "easy":
        return TrafficEnv(arrival_rate=0.1)

    elif task == "medium":
        return TrafficEnv(arrival_rate=0.3)

    elif task == "hard":
        return TrafficEnv(arrival_rate=0.6)

    else:
        raise ValueError("Invalid task")