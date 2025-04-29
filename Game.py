import Table.py

def main():
    p1 = Table.bot()
    p2 = Table.bot()
    p3 = Table.bot()
    p4 = Table.bot()
    playtable = Table(p1, p2, p3, p4)
    while not playtable.end_game():
        playtable.set_round()
        if playtable.play:
            playtable.play_round(playtable.trump, playtable.teamcall)


if __name__ == "__main__":
    main()