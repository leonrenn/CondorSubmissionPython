# CondorSubmissionPython

Python script for submitting jobs via condor on lxplus.

## Short Notice

This script was not written by me (only included comments and automatic generaation of necessary folders) but was passed around in the ATLAS community as a helping tool for submitting multiple jobs.<br>
I have found it useful to make this public since it is an easy to use tool to get condor jobs work.<br>
If anyone knows the original author please let me know, so I can give credits to him/her.

## Usage

To use this tool clone the repository onto your lxplus via:

```sh
git clone https://github.com/leonrenn/CondorSubmissionPython.git
```

Put all your scripts you want to execute in the ***subfiles*** directory and execute the program with:

```sh
python3 subcondor.py
```

For convenience you can out an alias on your .bashrc file with the following content:

```sh
alias subc="cd Path_to_CondorSubmissionPython && python3 subcondor.py && cd -"
```

## Additonal Info

More info can be found under:<br>

[Official](https://batchdocs.web.cern.ch/local/submit.html)<br>

One can modify the submit script within the CondorJobSubmission.py class.





