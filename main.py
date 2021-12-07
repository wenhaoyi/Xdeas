import json
import time


def trans(a):
    ti = time.mktime(time.strptime(a, '%Y-%m-%d %H:%M:%S'))
    return ti


def interval_time_between_same_topic(load_dict, standard_interval):
    counts = 0
    print(load_dict[0]['topic'], "counts:", len(load_dict))
    for i in range(len(load_dict) - 1):
        difference = abs(trans(load_dict[i + 1]['createAt']) - trans(load_dict[i]['createAt']) - standard_interval)
        if 100 > difference > 2:
            counts = counts + 1
            print(load_dict[i]['topic'], load_dict[i]['createAt'], difference)
    print("standard_interval(sec):", standard_interval)
    print("Total count for more than 2 sec difference:", counts, ',percent: {:.2%}'.format(counts / len(load_dict)))
    print("")
    return


def difference_between_send_and_receive_time(load_dict):
    counts = 0
    print(load_dict[0]['topic'], "counts:", len(load_dict))
    for i in range(len(load_dict) - 1):
        difference = abs(trans(json.loads(load_dict[i]['payload'])['time']) - trans(load_dict[i]['createAt']))
        if 100 > difference > 4:
            counts = counts + 1
            print(load_dict[i]['topic'], load_dict[i]['createAt'], difference)
    print("Total Count for send and receive difference more than 3 sec :", counts,
          ',percent: {:.2%}'.format(counts / len(load_dict)))
    print("")
    return


#
with open(r"C:\Users\11055\Desktop\正式环境2.json", 'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)
    load_dict1 = {"/data/00/01": [], "/data/00/02": [], "/data/00/1003011211129001": []}
    for i in range(len(load_dict['messages']) - 1):
        load_dict1[load_dict['messages'][i]['topic']].append(load_dict['messages'][i])
    interval_time_between_same_topic(load_dict1['/data/00/1003011211129001'], 20)
    interval_time_between_same_topic(load_dict1['/data/00/01'], 1)
    interval_time_between_same_topic(load_dict1['/data/00/02'], 10)
    difference_between_send_and_receive_time(load_dict1['/data/00/1003011211129001'])
    difference_between_send_and_receive_time(load_dict1['/data/00/01'])
    difference_between_send_and_receive_time(load_dict1['/data/00/02'])

    # for i in range(len(load_dict['messages']) - 1):
    #     load_dict1[load_dict['messages'][i]['topic']].append(load_dict['messages'][i])
    #     # if i == 100:
    #     #     print(load_dict['messages'][i]['createAt'])
    #     #     print(len(load_dict['messages'][i]['createAt']))
    #     #     for j in range(len(load_dict['messages'][i]['createAt'])):
    #     #         print(load_dict['messages'][i]['createAt'][j])
    #     # if i == 100:
    #     #     print(json.loads(load_dict['messages'][i]['payload']))
    #     #     print(len(json.loads(load_dict['messages'][i]['payload'])))
    #     #     print(json.loads(load_dict['messages'][i]['payload']))
    #     #     dicts = json.loads(load_dict['messages'][i]['payload'])
    #     #     dicts2 = {'1801010211129001_p1', [0, 3, 0, 6]}
    #     #     for j in dicts.keys():
    #     #         print(j)
    #     #         print(dicts[j])
    #     #
    #     #     for k in dicts.items():
    #     #         print(k)
    #
    #     if trans(load_dict['messages'][i]['createAt']) - trans(
    #             json.loads(load_dict['messages'][i]['payload'])['time']) == -1:
    #         # print(load_dict['messages'][i]['mid'])
    #         counts2 = counts2 + 1
    #     interval2 = abs(trans(json.loads(load_dict['messages'][i + 1]['payload'])['time']) - trans(
    #         json.loads(load_dict['messages'][i]['payload'])['time']) - 20)
    #     if 2 <= interval2 < 100:
    #         print(load_dict['messages'][i + 1]['mid'])
    #         print("interval2: " + str(interval2))
    #         counts3 = counts3 + 1
    # # print("count1: " + str(counts1))
    # # print("count2: " + str(counts2))
    # # print("count3: " + str(counts3))
    # duration = trans(load_dict['messages'][len(load_dict['messages']) - 1]['createAt']) - trans(
    #     load_dict['messages'][0]['createAt'])
    # print(duration / 20)
