# CondorSubmissionPython

Python script for submitting jobs via condor on lxplus.

## Short Notice

Credits to the original author: Philipp Windischhofer<br>
Link to his [Github](https://github.com/philippwindischhofer)<br>
I just extended the code a bit and found it useful to make this public since it is an easy to use tool to get condor jobs work.<br>


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





