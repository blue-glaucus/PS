# 프로그래머스 No.42583 다리를 지나는 트럭


def solution(bridge_length, weight, truck_weights):
    answer, current_weight = 1, 0
    queue = []

    while truck_weights:
        if current_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            current_weight += truck
            queue.append((answer, truck))
            answer += 1
        else:
            time, truck = queue.pop(0)
            current_weight -= truck
            answer = max(answer, time + bridge_length)
    answer -= 1
    return answer if not queue else answer + bridge_length


bridge_length = 5
weight = 5
truck_weights = [2, 2, 2, 2, 1, 1, 1, 1, 1]
print(solution(bridge_length, weight, truck_weights))

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))
