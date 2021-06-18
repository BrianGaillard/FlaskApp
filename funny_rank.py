
import json


def FunnyRankings():
    f = open('data.json')

    data = json.load(f)

    f.close()

    ranks = []

    for user in range(len(data)):
        funnyval = 0
        for convo in range(len(data[user]['conversations'])):
            for sens in range(len(data[user]['conversations'][convo])):
                for sen in range(len(data[user]['conversations'][convo]['sentences'])):
                    if data[user]['conversations'][convo]['sentences'][sen]['speaker_type'] == 'sales_rep':
                        if data[user]['conversations'][convo]['sentences'][sen]['funny'] == True:
                            funnyval = funnyval + 1
        ranks.append([data[user]['user'], funnyval])

    ranks.sort(key= lambda ranks : ranks[1])

    return ranks
