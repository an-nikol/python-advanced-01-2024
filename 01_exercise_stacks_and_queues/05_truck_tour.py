# start from different idx
# rotate a deck, if the first is not okay, it goes to the end

from collections import deque

pumps_data = deque([[int(x) for x in input().split()]for i in range(int(input()))])

# when you want to check if there is a final lap
pumps_data_copy = pumps_data.copy()
gas_in_tank = 0
index = 0

while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()
    gas_in_tank += petrol
    # check if it goes to the last station
    if gas_in_tank >= distance:
        gas_in_tank -= distance
    else:
        pumps_data.rotate(-1) # [1,2,3] => [2,3,1]
        # reset and start from another point
        pumps_data_copy = pumps_data.copy()
        index += 1
        gas_in_tank = 0
print(index)







#for i in range(int(input())):
    # pump_data[i] = []
    # for x in input().split():

    #pump_data[i].append(int(x))