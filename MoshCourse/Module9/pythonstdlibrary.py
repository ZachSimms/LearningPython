from pathlib import Path
from time import ctime
import shutil

def videoTwo():
    path = Path("/Users/BioHaze/PycharmProjects/ProjectAlpha/MoshCourse/Module7-8/ecommerce/sales.py")

    print(path.exists())
    print(path.is_file())
    print(path.is_dir())
    print(path.name)
    print(path.stem)
    print(path.suffix)
    print(path.parent)

    path2 = path.with_name("file.txt")
    print(path2.absolute())
    print(path.with_suffix(".ext"))


def videoThree():
    path = Path("/Users/BioHaze/PycharmProjects/ProjectAlpha/MoshCourse/Module7-8/ecommerce")

    # path.mkdir()
    # path.rmdir()
    # path.rename("ecommerce2")
    for x in path.iterdir():
        print(x)

    path_list = [x for x in path.iterdir() if x.is_dir()]
    print(path_list)

    # Get all the .py files in the directory
    py_files = [p for p in path.glob("*.py")]
    # Recursive. Get all the .py files in the directory and its children
    py2_files = [p for p in path.rglob("*.py")]
    print(py_files)
    print(py2_files)


def videoFour():
    path = Path("/Users/BioHaze/PycharmProjects/ProjectAlpha/MoshCourse/Module7-8/ecommerce")
    source = Path("/Users/BioHaze/PycharmProjects/ProjectAlpha/MoshCourse/Module7-8/ecommerce")
    target = Path( / "__init__.py")

    # Copies text from one file to another
    shutil.copy(source, target)
    print(ctime(path.stat().st_ctime))
    # Returns content as bypes object for binary data
    path.read_bytes
    # Returns content as a string
    path.read_text()
    # path.write_text("....")
    # path.write_bytes()

videoFour()









