# parašykite funkciją, kuri į args priimtų url eilučių sąrašą ir grąžintų
# kokį serverį naudoja svetainė.

import requests
def server_info(*args):
    print("{:<30} {:<40}".format("URL", "Server"))
    print("-" * 50)
    for url in args:
        r = requests.get(url)
        server = r.headers["Server"]
        print(f'{url:<30} {server:<40}')

server_info("https://www.delfi.lt/",
            "https://www.lrytas.lt/",
            "http://www.google.com/",
            "https://open.spotify.com/",
            "https://github.com/")