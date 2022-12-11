import click
import socket
import time
from rich.console import Console
from rich.progress import track

from mov_cli.__main__ import movcli

import os
os.system("color")

console = Console()

@click.group(invoke_without_command=True)
@click.pass_context
def python_cli(ctx:click.Context):
    
    if ctx.invoked_subcommand is None:
        console.input("WElCOME!\nPress enter to continue")
        #Progress Loading bars
        #-------------
        
        for x in track(range(20), description="setting up BIOS..."):
            time.sleep(0.03)

        for x in track(range(10), description="Loading commands..."):
            time.sleep(0.03)

        for x in track(range(25), description="Loading all packages..."):
            time.sleep(0.03)

        for x in track(range(10), description="Setting up python..."):
            time.sleep(0.03)

        for x in track(range(20), description="Getting ip address..."):
            time.sleep(0.05)

        for x in range(4):
            print("Getting kernel access")
            time.sleep(0.04)

        for x in range(4):
            print("Loading terminal into command line")
            time.sleep(0.04)

            
        title = """
                * *       *                           *       * * 
             *            * *                       * *       *    *
          *               *   *                   *   *       *      *
       *                  *     *               *     *       *        *
     *                    *       *           *       *       *          *
    *                     *         *       *         *       *           *
    *                     *           *   *           *       *           *
    *                     *             *             *       *           *
    *                     *                           *       *           *
     *                    *                           *       *          *
       *                  *                           *       *        *
          *               *                           *       *      *
             *            *                           *       *    *
                * *       *                           *       * *
"""
        print("\033[34m" + title + "\033[0m")

# Subcommands
#---------------

@python_cli.command()
def hello():
    """Says hello."""
    print("hewwo")

@python_cli.command()
def ip():
    host_name = socket.gethostname()
    local_ip = socket.gethostbyname(host_name)
    print(local_ip)

@python_cli.command()
def movies():
    movcli()