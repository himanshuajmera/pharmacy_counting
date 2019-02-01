# About
This repository is created for submission towards qualification to Insight Data Engineering Fellowship program. I have included 4 folders and 1 shell script. Below I have described content of each folder. To checkout the problem statement and sample input-output please visit [here](https://github.com/InsightDataScience/pharmacy_counting)

# input
Right now this folder contains a txt file names itcont.txt. To create the hirarchy as per guideline. Sample input is available in [insight_testsuite] (README.md#insight_testsuite). About input, Raw data could be found [here](https://drive.google.com/file/d/1fxtTLR_Z5fTO-Y91BnKOQd6J0VC9gPO3/view?usp=sharing).

# insight_testsuite
This folder contain test cases for the script. Though, it has only one test case for now as provided by Insight. My tested files are larger and hence not included here. The shell script in this folder check for repo structure.

You can run the test with the following command from within the `insight_testsuite` folder:

    insight_testsuite~$ ./run_tests.sh 
    
On a failed test, the output of `run_tests.sh` should look like:

    [FAIL]: test_1
    [Thu Mar 30 16:28:01 PDT 2017] 0 of 1 tests passed

On success:

    [PASS]: test_1
    [Thu Mar 30 16:25:57 PDT 2017] 1 of 1 tests passed
  
# output
In this folder, script will store the outputs for the data from input folder. This folder contain .txt file with title: top_cost_drug

# src
This folder contain my python script that produce the txt file for given input txt data. In the python script I have used one function which produce the desired results.

**Please feel free to ask questions at: [himanshuajmera8@gmail.com](himanshuajmera8@gmail.com)**
