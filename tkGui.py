import tkinter as tk
from tkinter import ttk
from tkmacosx import Button
from api import get_standings

def launch_gui():
    data = get_standings()

    root = tk.Tk()
    root.title("Premier League Standings")
    root.geometry("600x500")

    tree = ttk.Treeview(root, columns=("Position", "Logo", "Team", "Points"), show="headings")
    tree.heading("Position", text="Position")
    tree.heading("Team", text="Team")
    tree.heading("Points", text="Points")

    for team in data:
        tree.insert("", "end", values =(team['rank'], team['team']['name'], team['points']))

    tree.pack(expand=True, fill='both')
    root.mainloop()