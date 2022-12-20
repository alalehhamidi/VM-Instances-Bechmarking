
import subprocess
from utilisation import extractResult

def main(bs, count, outputDirectory, fileName):
    command = "dd if=/dev/zero of=sb-io-test bs=" + str(bs) + " count=" + str(count) + " conv=fdatasync"
    path = outputDirectory + "" + fileName + ".txt"
    file = open(path, 'a')
    subprocess.call(command, shell=True, stderr=file)
    file.close()

def getResult(outputDirectory, fileName):

    regexPattern = r'([0-9]*\.?[0-9]*) MB\/s'
    matchObjList = extractResult(outputDirectory, fileName, regexPattern)

    result = "Speed: {}(MB/s)".format(matchObjList[0])

    return "{}".format(result)

if __name__ == "__main__":
    main(2000000,3000,"","IO")

