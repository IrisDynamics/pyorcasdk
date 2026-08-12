venv/scripts/activate

$DocDir = "docs"

mkdir temp/
cp pyorcasdk/_pyorcasdk.pyi temp/pyorcasdk.py

pdoc -t . -o $DocDir --no-include-undocumented --favicon ./favicon.ico temp/pyorcasdk.py
cp favicon.ico $DocDir/favicon.ico

Remove-Item -Path temp -Recurse -Force