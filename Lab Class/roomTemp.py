sensors = [10, 20, 30, 40, 50]
def room_temp(sensors) :
    for sens in sensors:
        if sens < 30:
            print("fan off")
        elif sens > 30:
            print("fan on")
            
    return 0
room_temp(sensors)