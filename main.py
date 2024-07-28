import typer
from pomodoro.main import run_pomodoro

app = typer.Typer()

@app.command()
def pomodoro():
    run_pomodoro()
    
    
@app.command()
def teste():
    print("Pomodoro")
    
@app.command()
def main():
    print("Pomodoro")

if __name__ == "__main__":
    app()