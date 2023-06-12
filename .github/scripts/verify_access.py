import os
import json
import sys

#
def getEnvInfo ():

    env_file = os.getenv('GITHUB_ENV')

    test_var = os.getenv('Test_Parameter')

    print ("Test parameter from env: {}".format(test_var))

    with open(env_file, "a") as myfile:
        myfile.write("MY_VAR=MY_FLUCAST_VALUE")
        print ("MyFile: {}".format(myfile))



#
def run (jsonInputFile):

    print ("Running check")

    getEnvInfo()

    with open(jsonInputFile) as f_json_input:
        j_in = json.load(f_json_input)
        if j_in == None :
            print("Failed to open input file")
        else :
            print("Input file opened: {}".format(j_in))

        teams = j_in['mapping']['teams']

        for team in teams:
            print ("Team content: {}".format(team))



if __name__ == "__main__":
    print ("Testing script")

    if len(sys.argv) <= 1 :
      print ("Missing input. Abort!")
      exit(0)

    input_data_json = sys.argv[1]
    print ("Input data: \n {}".format(input_data_json))

    runningPath = os.path.dirname(__file__)

    jsonInputFile = os.path.join(runningPath, '..', 'assets', 'repo_access_mapping.json')

    print ("Running path: {0}, file: {1}".format(runningPath, jsonInputFile))
    run(jsonInputFile)
