import time
import subprocess
from utils import get_test_files_in_folder


class UnitTester():
    def __init__(self, folder_to_be_tracked):
        self.folder_to_be_tracked = folder_to_be_tracked
        self.time_of_last_commit = 0    # setting this to 0 ensures that we always run tests once on startup (even when no commits are made)
        self.testing_wait_duration = 5  # how long the program will sleep before re-checking if any new commits have been made.

    def get_test_files(self):
        """
        Returns:
            test_files : list of names of files that start with "test"
        the name and amount of test-files can change while the UnitTester is running
        """
        test_files = get_test_files_in_folder(self.folder_to_be_tracked)
        return test_files


    def get_time_of_last_commit(self):
        """
        Returns epoch time for when the last git commit was executed
        """
        dir_command = "cd "+self.folder_to_be_tracked              # windows command-line command to move to the folder that is being tracked
        commands = f"{dir_command} && git log -1 --format=%ct"     # move to folder and then ask git for the last time a git commit was made
        p1 = subprocess.run(commands, capture_output=True, shell=True, text=True)
        return float(p1.stdout)


    def check_if_should_run(self):
        """
        return True if new commits have occured in the folder that is tracked since the last time unit tests were run
        """
        last_commit_time = self.get_time_of_last_commit()
        should_run_tests = last_commit_time != self.time_of_last_commit
        self.time_of_last_commit = last_commit_time
        return should_run_tests


    def execute_tests(self):
        """
        Run tests using pytest and print the result to console
        """
        test_files = self.get_test_files()
        for test_file in test_files:
            p1 = subprocess.run(f"pytest {test_file}", capture_output=True, shell=True, text=True)
            print(p1.stdout)


    def one_loop_iteration(self):
        """
        check if the program should run any unit tests
        if not then
            sleep for self.testing_wait_duration number of seconds
        """

        time_when_entring_loop = time.time()
        should_run_tests_now = self.check_if_should_run()

        if should_run_tests_now:
            self.execute_tests()
        else:
            time_of_last_commit = self.get_time_of_last_commit()
            time_since_last_commit = time_when_entring_loop - time_of_last_commit
            print(f"no tests to run, will now sleep for {self.testing_wait_duration} seconds. ", end = "")
            print(f"Time since last commit {time_since_last_commit:.1f} s")
            time.sleep(self.testing_wait_duration)


    def run_loop(self):
        while True:
            self.one_loop_iteration()



if __name__ == "__main__":
    unitTester = UnitTester("..\\dummyProject")
    unitTester.run_loop()