import currency_api.sub_main as currency_api
import forecast.sub_main as forecast
from multiprocessing import Process
import time

def loop_a():
    currency_api.run()

def loop_b():
    forecast.run()

if __name__ == '__main__':
    Process(target = loop_a).start()
    time.sleep(2)
    Process(target = loop_b).start()


