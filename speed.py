def calculate_Speed (distance , time):
    if time == 0 or time < 0 :
        raise ValueError("Time cannot be zero or negative")
        return -1
    return (distance / time ) *3.6


print(calculate_Speed(6,-2))