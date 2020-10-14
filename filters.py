import statistics
data = [56, 78, 89, 37, 90, 19, 99]
mean = statistics.mean(data)
print(list(filter(lambda x : x > mean, data)))
