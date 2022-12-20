import subprocess
from utilisation import extractResult


def main(outputDirectory, fileName):
    command = "sysbench --test=cpu --cpu-max-prime= 1000000  --events=44000 --num_threads=2000 run"
    path = outputDirectory + "/" + fileName + ".txt"
    subprocess.call(command, shell=True, stdout=file)
    file.close()


def getResult(outputDirectory, fileName):
    regexPattern = r'([0-9]*\.[0-9]*)s'
    matchObjList = extractResult(outputDirectory, fileName, regexPattern)

    result = "Total time: {}(s)".format(matchObjList[0])

    return "{}".format(result)


