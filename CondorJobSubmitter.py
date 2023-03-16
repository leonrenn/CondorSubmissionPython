"""Class that collects the sh files,
prepares the submit files and submits them.
"""
import os
import subprocess as sp
import time


class CondorJobSubmitter:

    @staticmethod
    def submit_job(job_script_path: str,
                   job_threshold: int = 300,
                   job_flavour: str = "espresso") -> None:
        """Creates submit files and submits them to condor.

        Args:
            job_script_path (str): Path to the sh files
            job_threshold (int, optional): Threshold of jobs
            that can be queued at one. Defaults to 300.
            job_flavour (str, optional): Flavour of the job.
            Defaults to "espresso".
        """

        # check what kind of file we got
        if not os.path.splitext(job_script_path)[1] == ".submit":
            # need to create the submit file
            job_script_base, _ = os.path.splitext(job_script_path)
            job_dir = os.path.dirname(job_script_path)
            submit_file_path = job_script_base + ".submit"

            while True:
                try:
                    with open(submit_file_path, 'w') as submit_file:
                        #########################################
                        # the following shows how the typical   #
                        # submit file will look like by         #
                        # submitting over the current class:    #
                        # ------------------------------------- #
                        # executable = subfiles/your_script.sh  #
                        # universe = vanilla                    #
                        # output = output/your_script.output    #
                        # error = errs/your_script.error        #
                        # log = log/job.log                     #
                        # +JobFlavour = "your_flavour"          #
                        # notification = never                  #
                        # queue 1                               #
                        #########################################
                        submit_file.write(
                            "executable = " +
                            job_script_path + "\n")
                        submit_file.write(
                            "universe = vanilla\n")
                        submit_file.write(
                            "output = output/" +
                            job_script_base.split('/')[-1] +
                            ".output\n")
                        submit_file.write(
                            "error = errs/" +
                            job_script_base.split('/')[-1] +
                            ".error\n")
                        submit_file.write(
                            "log = log/job.log\n")
                        submit_file.write(
                            "+JobFlavour = \"" +
                            job_flavour +
                            "\"\n")
                        submit_file.write(
                            "notification = never\n")
                        submit_file.write(
                            "queue 1")

                    break
                except Exception:
                    print("Problem writing job script -- retrying.")
                    time.sleep(10)

        else:
            # are given the submit file directly
            submit_file_path = job_script_path

        while True:
            running_jobs = CondorJobSubmitter.queued_jobs()
            if running_jobs < job_threshold:
                break
            print("Have {} jobs running - wait a bit".format(running_jobs))
            # wait for 30 seconds before submitting next job
            time.sleep(30)

        while True:
            try:
                # call the job submitter
                sp.check_output(["condor_submit", submit_file_path])
                print("Submitted '" + submit_file_path + "'")
                break
            except Exception:
                print("Problem submitting job - retrying in 10 seconds!")
                time.sleep(10)

        return None

    @staticmethod
    def queued_jobs(queue_status="condor_q") -> int:
        """Returns number of running jobs.

        Args:
            queue_status (str, optional): Command for jobs status.
            Defaults to "condor_q".

        Returns:
            int: Number of running jobs.
        """
        while True:
            try:
                running_jobs = len(sp.check_output(
                    [queue_status]).split('\n')) - 6
                return running_jobs
            except sp.CalledProcessError:
                print("{} error - retrying!".format(queue_status))
                time.sleep(10)

    @staticmethod
    def gen_necessary_directories() -> None:
        """Check if all necessary directories (output, errs, log)
        exist and if they do not create them.
        """
        # existence errs directory
        if os.path.isdir("errs") is not True:
            # create errs directory
            os.mkdir("errs")
        # existence output directory
        if os.path.isdir("output") is not True:
            # create output directory
            os.mkdir("output")
        # existence log directory
        if os.path.isdir("log") is not True:
            # create log directory
            os.mkdir("log")
        return None
