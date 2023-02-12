from config import client_tg, urls_list
from utils import events
import schedule


def start_poling_events():
    schedule.every().hour.do(lambda: events(urls_list, client_tg))
    while True:
        schedule.run_pending()


if __name__ == "__main__":
    client_tg.start()
    start_poling_events()
