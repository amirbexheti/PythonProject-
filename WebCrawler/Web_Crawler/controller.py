

from crawler import *


def crawl(*urls):

    for link in urls:
        current_worker = Worker(link)
        load = threading.Thread(target=current_worker.work)
        load.start()
