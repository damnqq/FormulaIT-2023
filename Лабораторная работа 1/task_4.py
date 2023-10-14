users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

users_length = len(users)
unique_visits = set(users)
unique_visits_length = len(unique_visits)

visit_statistics = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

visit_statistics["Общее количество"] = users_length
visit_statistics["Уникальные посещения"] = unique_visits_length

print(visit_statistics)
