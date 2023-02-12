from datetime import datetime
import os

temp = []


def logs_tg(event, path):
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{datetime.now()} - {event.__dict__}\n")


def events(url_list, client_tg):
    for url in url_list:
        channel = client_tg.get_chat(url)
        events_list = client_tg.get_chat_event_log(channel.id)

        path = os.path.normpath(
            os.path.expanduser(os.path.join('temp_date_files', f"temp_last_date_events_{channel.id}.txt")))

        if not os.path.exists(path):
            with open(path, 'w'): pass

        with open(path, "r", encoding="utf-8") as file:
            temp_date = datetime(1970, 1, 1, 0, 0, 1)
            temp_date_max = temp_date
            row = file.read()
            if row:
                temp_date = datetime.strptime(row, "%Y-%m-%d %H:%M:%S")

            for i in events_list:
                if temp_date_max < i.__dict__['date']:
                    temp_date_max = i.__dict__['date']

                if temp_date < i.__dict__['date']:
                    chat_log_path = os.path.normpath(os.path.expanduser(os.path.join('logs_tg', f"log_telegram_events_{channel.id}.log")))
                    logs_tg(i, chat_log_path)

        with open(path, "w", encoding="utf-8") as file:
            file.truncate()
            file.write(temp_date_max.strftime("%Y-%m-%d %H:%M:%S"))
