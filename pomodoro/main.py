from .countdown import countdown
from .notify import notify
from rich.console import Console

console = Console()

def run_pomodoro():
    work_duration = 25 * 60
    break_duration = 5 * 60 
    cycles = 4

    for cycle in range(1, cycles + 1):
        console.print(f"[bold red]Pomodoro[/bold red] {cycle} [bold white]- Hora de trabalhar![/bold white] :tomato:")
        countdown(work_duration)
        notify("Hora de descansar! Faça uma pausa de 5 minutos.", "attachments/sound.mp3")
        
        if cycle < cycles:
            console.print(f"Hora de descansar! Faça uma pausa de {break_duration // 60} minutos. :coffee:", style="bold green")
            countdown(break_duration)
            notify("Hora de voltar ao trabalho!", "attachments/sound.mp3")
        else:
            console.print("Sessão de Pomodoro concluída! :tada:", style="bold blue")
            notify("Sessão de Pomodoro concluída! Ótimo trabalho!", "attachments/sound.mp3")

    console.print("Ótimo trabalho! Você completou sua sessão de Pomodoro. :clap:", style="bold yellow")
