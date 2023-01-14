from colorama import Fore, Back, Style
from backend import interceptor as bk
from rich.progress import track
from logox import logo
import typer
import time


app = typer.Typer()
net = bk()


@app.command()
def speed():
  """
  Test your internet speed!
  """
  print(Fore.GREEN + logo)
  print(Fore.MAGENTA + "Type : 'Ctrl + c' for termination\n\n".upper())
  time.sleep(3)

  total = 0
  for value in track(range(100), description="Processing..."):
     
      time.sleep(0.01)
      total += 1
  print(Fore.RED)

  net.bandwidth()

@app.command()
def sniff(log : bool = False):
  """
  Intercept packets flowing across network
  """

  print(Fore.GREEN + logo)
  print(Fore.MAGENTA + "Type : 'Ctrl + c' for termination\n\n".upper())
  time.sleep(1)

  total = 0
  for value in track(range(100), description="Processing..."):
     
      time.sleep(0.01)
      total += 1


  if log:
    net.sniffandlog()
  else:
    net.sniffonly()


@app.command()
def push():
  pass

if __name__ == "__main__":
    app()
