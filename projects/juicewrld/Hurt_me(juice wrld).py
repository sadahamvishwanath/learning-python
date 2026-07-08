import time, sys, os

# ====== SKULL 999 ASCII ======
SKULL = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⠐⠠⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠿⡛⠛⠳⠶⣦⡠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⡛⣿⢁⣀⡀⢀⠄⡀⠀⠉⠉⠂⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣠⣄⡀⣰⣾⠿⣟⣯⣌⢺⣿⡿⢿⡀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡞⣿⠛⣿⣷⣫⣿⣇⣿⣭⡻⣼⣾⠿⣿⣯⢁⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⢿⡇⣿⡁⣿⣿⣿⡿⠿⡼⣯⡟⣇⢇⣳⢹⣯⠑⡠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣲⣿⣅⠸⣯⣿⡇⢋⣿⠋⢤⡀⣧⠀⠙⣾⣆⠈⠺⡙⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⡇⡿⣿⠆⣯⣿⢇⣿⣷⠆⠀⢻⣿⠀⠀⢘⣿⠆⡀⠹⡀⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡼⢋⣇⢧⣾⡆⣿⢻⠸⣻⣿⣄⣀⠀⠉⠀⠰⠟⣿⠀⠀⠁⢀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢻⣸⡿⢾⠻⣇⡟⠘⣦⠏⢻⠊⠨⢿⣆⠀⠀⣴⣿⣶⠢⠄⠈⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣷⢧⣼⡹⡉⠁⠀⠀⢙⣦⣶⢾⣄⣹⠀⠀⠀⠉⠉⠉⠀⠀⠘⢴⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢇⣿⠉⢃⠀⠀⠀⠀⠩⠛⠁⣴⠘⢄⣀⣠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣿⡄⠬⠇⠀⠀⠀⠀⠀⠀⠹⠼⣿⠉⣦⡁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢁⣇⢀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠯⠤⢤⣤⣤⣄⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣾⣿⠣⣀⡀⠀⠀⠀⠀⠀⢨⠶⣏⣉⣅⡄⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢘⣿⠉⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠐⠋⠉⠁⠀⠀⠀⣠⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣀⡼⠁⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠓⠟⠿⣿⠋⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢀⡤⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⢸⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⡴⠊⠁⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡟⡙⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢤⠐⠒⡻⠋⠉⠀⠀⠀⡀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠩⠭⠯⠭⠿⠟⠛⢹⣿⡀⠀⠀⠂⠀⠀⠀⠀⠀⠀
⣤⠀⠀⠁⠢⣄⡀⠀⠀⠀⠀⠁⠀⢣⠀⠀⠀⠀⡀⠠⠤⠾⠷⠾⠧⢖⡒⢼⡟⣹⣧⠀⠀⠀⠀⠈⠀⠀⠀⠄"""

# ====== LYRICS — "Hurt Me" by Juice WRLD ======
# Each line: (word_delay, end_of_line_pause) -- timed to Juice's flow.
# Tune WPM_SPEED up/down to make it faster/slower overall.
WPM_SPEED = 1.00  # <-- set 0.9 = faster, 1.2 = slower

LINES = [
    ("Turned to a whole different person, drive my whip",       0.70),
    ("Crash my whip off the drugs I'm swervin'",                 0.80),
    ("Sticks and stones may break my bones",                     0.55),
    ("But the drugs won't hurt me, the drugs won't hurt me",     0.50),
    ("Ex-girlfriend keeps callin' my phone",                     0.40),
    ("But the bitch can't hurt me, so I'm not worried",          0.55),
    ("All alone, did it on my own",                              0.40),
    ("So I show no mercy, I show no mercy",                      0.60),
    ("With my bros but I got my pole",                           0.55),
    ("Screamin', \"Please don't urge me, please don't urge me,\" yuh", 1.20),
]

RED    = "\033[91m"
BRIGHT = "\033[1;91m"
DIM     = "\033[2;37m"
RESET  = "\033[0m"

os.system("")  # enable ANSI colors on Windows

print(RED + SKULL + RESET)
time.sleep(2)

print(f"\n{BRIGHT}🎵  Juice WRLD \u2014 Hurt Me  🎵{RESET} SV\n")
time.sleep(0.8)

input(f"{DIM}Press ENTER to start the verse (or time it with the song)...{RESET}")
sys.stdout.write("\033[A\033[K")  # erase the "press enter" line
sys.stdout.flush()
time.sleep(0.3)

for text, end_pause in LINES:
    words = text.split()
    for i, w in enumerate(words):
        # per-word timing: longer for multi-syllable words, shorter for tiny ones
        base = 0.28 + 0.035 * max(1, len(w) - 3)
        delay = base / WPM_SPEED
        # little extra commas/periods (rhythmic pause)
        if w.endswith((",", ".", "?", "!")):
            delay += 0.10
        sys.stdout.write(BRIGHT + w + RESET + " ")
        sys.stdout.flush()
        time.sleep(delay)
    print()
    time.sleep(end_pause / WPM_SPEED)

time.sleep(0.8)
print()
print(f"{BRIGHT}🖤   999 forever.   🖤{RESET}")