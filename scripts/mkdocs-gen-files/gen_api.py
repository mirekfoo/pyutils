import os
import sys
import ast
from pathlib import Path
import mkdocs_gen_files


def get_module_docstring(path: str | Path) -> str | None:
    source = Path(path).read_text(encoding="utf-8")
    tree = ast.parse(source)
    return ast.get_docstring(tree)

def get_first_doc_sentence(doc : str) -> str:
    """Get first sentence from doc string."""
    if not doc:
        return ""
    doc = doc.strip()
    doc = doc.strip("")
    sentence = doc.strip().split(".")[0].split("\n")[0].strip()
    return f"{sentence}." if sentence else ""

def multiplex_write(fs : list, s : str):
    for f in fs:
        f.write(s)

def multiplex_close(fs : list, s : str):
    for f in fs:
        f.close()

print("CWD = ", os.getcwd())

SRC_DIR = Path("src/pyutils")
API_DIR = Path("api")

#print("SRC_DIR = ", SRC_DIR)
#print("API_DIR = ", API_DIR)

echoMDFiles = False
persistMDFiles = False
PERSISTENT_API_DIR = Path("docs-web/api")

nav = mkdocs_gen_files.Nav()

# ------------ API docs ------------
for path in sorted(SRC_DIR.rglob("*.py")):
    if path.name.startswith("_"):
        continue

    #print("Processing ", path)

    module_path = path.relative_to(SRC_DIR.parent).with_suffix("")
    module_name = ".".join(module_path.parts)

    if persistMDFiles:
        # Persist generated markdown under docs/api/ so files remain on disk
        persistent_doc_path = PERSISTENT_API_DIR.joinpath(*module_path.parts).with_suffix(".md")
        #print("mkdir: ", persistent_doc_path.parent)
        persistent_doc_path.parent.mkdir(parents=True, exist_ok=True)

    nav_path = Path(*module_path.parts).with_suffix(".md")
    nav[module_name] = nav_path.as_posix()

    f = mkdocs_gen_files.open(Path(API_DIR, nav_path), "w")
    fs = [f]
    if persistMDFiles:
        persistent_doc_md_f = open(persistent_doc_path, "w")
        fs.append(persistent_doc_md_f)
    if echoMDFiles:
        fs.append(sys.stdout)

    multiplex_write(fs, f"# {module_name}\n\n")
    multiplex_write(fs, f"::: {module_name}\n")

    f.close()
    if persistMDFiles:
        persistent_doc_md_f.close()
# ------------ API docs ------------

# ------------ API index ------------
if persistMDFiles:
    persistent_index_path = PERSISTENT_API_DIR / "index.md"
    persistent_index_path.parent.mkdir(parents=True, exist_ok=True)

f = mkdocs_gen_files.open(Path(API_DIR, "index.md"), "w")
fs = [f]
if persistMDFiles:
    persistent_index_md_f = open(persistent_index_path, "w")
    fs.append(persistent_index_md_f)
if echoMDFiles:
    fs.append(sys.stdout)

multiplex_write(fs, "# API Reference\n\n")
multiplex_write(fs, "| Page | Info |\n| --- | --- |\n")
for (nav_line, item) in zip(nav.build_literate_nav(), nav.items()):
    #print(nav_line, item)
    src_file = Path(SRC_DIR.parent, item.filename.replace(".md", ".py"))
    docstring = get_module_docstring(src_file)
    info = get_first_doc_sentence(docstring)
    multiplex_write(fs, f"| {nav_line.strip()} | {info} |\n")

f.close()
if persistMDFiles:
    persistent_index_md_f.close()
# ------------ API index ------------

mkdocs_gen_files.set_edit_path(Path(API_DIR, "index.md"), "scripts/mkdocs-gen-files/gen_api.py")
