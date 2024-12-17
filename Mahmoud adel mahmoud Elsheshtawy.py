conflict_data = [
    {"subject_id": 100, "conflict_subject_id": 200, "intersection_count": 30},
    {"subject_id": 100, "conflict_subject_id": 300, "intersection_count": 15},
    {"subject_id": 200, "conflict_subject_id": 300, "intersection_count": 20},
]
level_data = [
    {"subject_id": 100, "level": 1},
    {"subject_id": 200, "level": 2},
    {"subject_id": 300, "level": 3},
]
level_patterns = [
    [1, 2, 3],  
    [3, 2, 1],  ]

level_to_subjects = {}
for item in level_data:
    if item["level"] not in level_to_subjects:
        level_to_subjects[item["level"]] = []
    level_to_subjects[item["level"]].append(item["subject_id"])

def calculate_total_cost(order, conflicts):
    total_cost = 0
    for conflict in conflicts:
        if conflict["subject_id"] in order and conflict["conflict_subject_id"] in order:
            index1 = order.index(conflict["subject_id"])
            index2 = order.index(conflict["conflict_subject_id"])
            if abs(index1 - index2) == 1:  
                total_cost += conflict["intersection_count"]
    return total_cost
optimal_order = None
minimum_cost = float('inf')

for pattern in level_patterns:
   
    subjects_in_pattern = []
    for level in pattern:
        subjects_in_pattern.extend(level_to_subjects.get(level, []))
    
    
    permutations = itertools.permutations(subjects_in_pattern)
    
    for perm in permutations:
        cost = calculate_total_cost(perm, conflict_data)
        if cost < minimum_cost:
            minimum_cost = cost
            optimal_order = perm


print("Optimal order:", optimal_order)
print("Minimum cost:",minimum_cost)