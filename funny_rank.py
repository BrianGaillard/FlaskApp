
import json


def FunnyRankings():
    f = open('data.json')

    data = json.load(f)

    f.close()

    users = []

    for i in range(len(data)):
        users.append(data[i]['user'])


    # for user in data:
    #     for converstaions in users:

    return users
