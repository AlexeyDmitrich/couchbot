from time import gmtime, strftime

def dump (user, request, response, exception=0):
    date = str(strftime("%d.%m.%Y %H:%M:%S", gmtime()))
    with open('logger.csv', 'a') as log:
        log.writelines(f"\n'{str(user)}','{str(date)}','{str(request)}','{str(response)}','{str(exception)}'")
