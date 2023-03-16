import pandas as pd

log = pd.read_csv('logger.csv', sep=';')
print(log.tail())

# err_log = log[log['exception']!=0]
# print(err_log.tail(20))