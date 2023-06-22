import csv

# with open('data.csv', 'r') as f:
#     reader = csv.reader(f)
#     print(reader)
#     next(reader)
#     for line in reader:
#         print(line)

# with open('data.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     for line in reader:
#         print(line)


# data_to_write = [['test_id', 'p1', 'p2'], ['ID1', 23, 43], ['ID2', 45, 5]]
# with open('data_out.csv', 'w') as f:
#     writer = csv.writer(f)
#     #writer.writerows(data_to_write)
#     writer.writerow(data_to_write[0])
#     writer.writerow(data_to_write[1])

data_to_write = [{'test_id': 'ID1', 'p1':54, 'p2':45}, {'test_id': 'ID2', 'p1':2323, 'p2':567}]
with open('data_out.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=data_to_write[0].keys())
    writer.writerows(data_to_write)
