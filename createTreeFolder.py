from pathlib import Path
import os

SOURCE_FILE=Path(__file__).resolve()
SOURCE_DIR=SOURCE_FILE.parent
SOURCE_WORK=SOURCE_DIR/"TREEFOLDER"

folders=[
    "Media/interface",
    {"Media/movie/poster":["original","150_520"]},
    {"Media/movie/fanart":["original","520_150"]},
    {"Media/cast":["original","60_60","150_520"]},
]

def create_fodlers(folders_list,base_dir):
    for thePath in folders_list:
        if isinstance(thePath,dict):
            for k,v in thePath.items():
                for i in v:
                    p=SOURCE_DIR / f"""{k}/{i}"""
                    try:
                        p.mkdir(parents=True,exist_ok=True)
                    except OSError as e:
                        print(f"Failed to create Folder {p}: {e}")

        else:
            p = SOURCE_DIR / thePath
            try:
                p.mkdir(parents=True,exist_ok=True)
            except OSError as e:
                print(f"Failed to create Folder {p}: {e}")


create_fodlers(folders,SOURCE_DIR)  
    

