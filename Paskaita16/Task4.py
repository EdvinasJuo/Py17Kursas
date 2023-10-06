import requests  # importuojame requests
from time import time  # importuojame time modulį

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        execution_time = end_time - start_time
        print(f"Vykdymo laikas atidarant {args} yra {execution_time:.2f} s.")
        return result
    return wrapper


@execution_time
def get_status_code(url):
    r = requests.get(url)
    return r.status_code

status_code = get_status_code('http://www.cnn.com')


start_time = time()  # fiksuojame starto laiką
r = requests.get('http://www.cnn.com')  # sukuriame http užklausą
print(r.status_code)  # spausdiname status code (200 = OK, 404 = Not Found, ir t.t. galima pasiguglinti http status codes)
end_time = time()  # fiksuojame pabaigos laiką
print(end_time - start_time)  # atspausdiname laiką, per kurį gaovme atsakymą