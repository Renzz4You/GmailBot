try:
    with open(r'C:\Renzz4You\GmailBot\proxies.txt', 'r') as file:
        proxy = [line.rstrip() for line in file.readlines()]
except FileNotFoundError:
    raise Exception('proxies.txt tidak ada.')
