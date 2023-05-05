# modules
import datetime
import platform
from prettytable import PrettyTable
import fire
import speedtest

class Commands(object):

    def network(self):
        time = datetime.datetime.now().strftime("%H:%M")
        st = speedtest.Speedtest()
        table = PrettyTable()

        table.title = 'newtwork speedtest'

        table.field_names = ["date", "ping", "download", "upload"]

        st.get_best_server()

        table.add_row([
            time,
            f"{st.results.ping} ms",
            f"{round(st.download() / 1000 / 1000, 1)} Mbit/s",
            f"{round(st.upload() / 1000 / 1000, 1)} Mbit/s",
        ])

        print(table)

    def system(self):
        uname = platform.uname()
        
        print(f"System: {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")

if __name__ == '__main__':
    fire.Fire(Commands)