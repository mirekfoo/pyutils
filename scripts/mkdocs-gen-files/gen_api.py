from pathlib import Path
import mkdocs_gen_files

SRC_DIR = Path("src/pyutils")
API_DIR = Path("api")

print("SRC_DIR = ", SRC_DIR)
print("API_DIR = ", API_DIR)

nav = mkdocs_gen_files.Nav()

for path in sorted(SRC_DIR.rglob("*.py")):
    if path.name.startswith("_"):
        continue

    print("Processing ", path)

    module_path = path.relative_to(SRC_DIR.parent).with_suffix("")
    module_name = ".".join(module_path.parts)

    nav_path = Path(*module_path.parts).with_suffix(".md")
    nav[module_name] = nav_path.as_posix()

    with mkdocs_gen_files.open(Path(API_DIR, nav_path), "w") as f:
        f.write(f"# {module_name}\n\n")
        f.write(f"::: {module_name}\n")

# API index
with mkdocs_gen_files.open(Path(API_DIR, "index.md"), "w") as f:
    f.write("# API Reference\n\n")
    f.write("".join(nav.build_literate_nav()))

mkdocs_gen_files.set_edit_path(Path(API_DIR, "index.md"), "scripts/mkdocs-gen-files/gen_api.py")
