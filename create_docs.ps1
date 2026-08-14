venv/scripts/activate

$DocDir = "docs"

mkdir temp/
cp pyorcasdk/_pyorcasdk.pyi temp/pyorcasdk.py

pdoc -t . -o $DocDir --no-include-undocumented --favicon ./favicon.ico --logo ./iris_squid.svg temp/pyorcasdk.py
cp favicon.ico $DocDir/favicon.ico
cp iris_squid.svg $DocDir/iris_squid.svg

Remove-Item -Path temp -Recurse -Force