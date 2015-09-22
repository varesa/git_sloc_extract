import subprocess
import datetime
import os
import sys

if len(sys.argv) < 2 or not os.path.isdir(os.path.join(sys.argv[1], ".git")):
    print("Please give a git repository as a parameter")
    sys.exit(1)

if len(sys.argv) < 3:
    ref = "master"
else:
    ref = sys.argv[2]

print("WARNING: This will delete any uncommitted changes to your working tree!")
print("Continue? [y/N]")
ans = input()
if ans != "y":
    print("Exiting")
    sys.exit(0)

subprocess.call(["git", "checkout", ref], cwd=sys.argv[1])
log = subprocess.check_output(["git", "log"], cwd=sys.argv[1]).decode()

ID = 0
DATE = 1

commits = []
rows = []


date = None
for line in reversed(log.split("\n")):
    if line.startswith("Date"):
        date = datetime.datetime.strptime(
            " ".join(line.split(" ")[1:]).strip(),
            "%a %b %d %H:%M:%S %Y %z"
        )
    elif line.startswith('commit'):
        commit = line.split(" ")[1]
        if len(commits) == 0 or date - commits[-1][DATE] > datetime.timedelta(days=1):
            commits.append((commit, date))


program_path = os.path.dirname(os.path.abspath(__file__))
sloc_path = os.path.join(program_path, "sloc.sh")

for commit, date in commits:
    subprocess.call(["git", "clean", "-f"], cwd=sys.argv[1])
    subprocess.check_output(["git", "checkout", commit], cwd=sys.argv[1])
    output = subprocess.check_output(["bash", sloc_path], cwd=sys.argv[1]).decode()
    output_filetypes, output_total = output.strip().split("\n")
    output_python, output_pt, output_css, output_js = output_filetypes.split(",")

    lines_python = output_python.split(" ")[2]
    lines_pt = output_pt.split(" ")[2]
    lines_css = output_css.split(" ")[2]
    lines_js = output_js.split(" ")[2]

    lines_total = output_total.split(" ")[1]

    print(str(lines_python) + ", " + str(lines_pt) + ", " + str(lines_css) + ", " + str(lines_js) + ", " + str(lines_total))
