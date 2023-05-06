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

        table.field_names = ["hora", "ping", "bajada", "subida"]

        st.get_best_server()

        table.add_row([
            time,
            f"{st.results.ping} ms",
            f"{round(st.download() / 1000 / 1000, 1)} Mbit/s",
            f"{round(st.upload() / 1000 / 1000, 1)} Mbit/s",
        ])

        print(table)

    def system(self):
        system_table = PrettyTable()
        os = platform.uname()

        system_table.header = False

        system_table.add_rows([
            ["Sistema", os.system],
            ["Lanzamiento", os.release],
            ["Versión", os.version],
            ["Arquitectura", os.machine],
            ["Procesador", os.processor]
        ])
        
        if os.system == 'Windows': 
            system_table.add_row(["Edicion", platform.win32_edition()])
        
        print(system_table)

if __name__ == '__main__':
    fire.Fire(Commands)