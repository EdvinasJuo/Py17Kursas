import logging
import asmenys
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG, filename="aritmetika.log", format="%(asctime)s:%(levelname)s:%(message)s")
logger = logging.getLogger(__name__)
file_hander = logging.FileHandler("aritmetika.log")
logger.addHandler(file_hander)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file_hander.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
def dalyba(a, b):
    return a / b


a = 10
b = 5

result = dalyba(10, 5)
print(f"Dalyba: 10 / 5 = {result}")         # INFORMACINIS PRANESIMAS!!!

# logging.info(f"Dalyba: 10 / 5 = {result}")         # INFORMACINIS PRANESIMAS, REIKIA NUSTATYTI CONFIG VIRSUJE

logger.debug(f"Dalyba: 10 / 5 = {result}")         # DEBUG PRANESIMAS, REIKIA NUSTATYTI CONFIG VIRSUJE