"""Script to exectute that collects all
files in the subfiles directory and
submits it to the condor.
"""
import os

from CondorJobSubmitter import CondorJobSubmitter


def main() -> int:
    if os.path.isdir("subfiles") is True:
        # prints all files found in the subfiles directory
        print(os.listdir("subfiles"))
    else:
        print("There is no directory called subfiles. "
              "\nGo and create it.")
        return 1

    # initializing the job submitter class
    cn = CondorJobSubmitter()

    # check existence of necessary directories
    cn.gen_necessary_directories()

    # iterating through all files
    for file in os.listdir("subfiles"):
        # only submitting files with the correct
        # file ending and path
        if ".sh" in file and "~" not in file:
            cn.submit_job("subfiles/"+file)
    return 0


if __name__ == "__main__":
    main()
