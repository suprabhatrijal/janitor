import os
import logging
import subprocess

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

path="/home/suppe/Downloads"
for file in files(path):
    ext = file.split(".")[-1] 
    if ext == "crdownload" : break
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename=f"{path}/logs/watchman.log", filemode="a", format = log_format, level= logging.INFO)
    logger = logging.getLogger()
    root_path = os.path.join(path,file)
    result = str(subprocess.run(["file", root_path], stdout=subprocess.PIPE).stdout)
    result = result.split(":")[1].split(",")[0].strip()
    result_path = f"{path}/{result}"
    subprocess.run(["mkdir", "-p", f"{result_path}"])        
    subprocess.run(["mv", f"{root_path}", f"{result_path}"])
    logger.info(f"moved '{file}' from Downloads to '{result}' folder in Downloads")



