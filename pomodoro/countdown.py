import time
from rich.console import Console

console = Console()

def countdown(duration):
    while duration:
        mins, secs = divmod(duration, 60)
        timeformat = f'{mins:02d}:{secs:02d}'
        console.print(f'Tempo restante: [bold white]{timeformat}[/bold white]', end='\r')
        time.sleep(1)
        duration -= 1
