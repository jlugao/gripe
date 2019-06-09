import subprocess
import sys
import re

arguments = sys.argv
keyword = " ".join(sys.argv[1:])

p = subprocess.Popen(
    ["grep", keyword], stdout=subprocess.PIPE, stdin=sys.stdin
)

output = p.communicate()[0].decode("utf-8")
gripado = output.replace("p", "b")
gripado = re.sub(r"(\s)[mM]", r"\1b", gripado)

print(gripado)
