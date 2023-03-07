import time

def dump (user, request, response, exception=0):
    date = time.localtime
    with open('logger.csv', 'a+') as log:
        log.writelines(f"\n{str(user)},{str(date)},{str(request)},{str(response)},{str(exception)}")
        log.close