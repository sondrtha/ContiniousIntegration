import os
import time
from find_files import get_files_in_folder, get_test_files_in_folder
from inspect_test_results import print_test_result_info
import run_tests


class CI:
    def __init__(self, folder_to_track):
        self.folder_to_track = folder_to_track                              # the project folder we are running automated tests for
        self.unit_test_files = get_test_files_in_folder(folder_to_track)    # the files containing the unit tests.


    def find_time_since_last_change(self):
        """
        Returns:
             time_since_last_change : the time in seconds since the last change happend to any of the files in the folder that is tracked
        """

        files = get_files_in_folder(self.folder_to_track)
        change_times = []
        for file in files:
            last_change_time = os.path.getmtime(file)
            delta_time = time.time() -  last_change_time
            change_times.append(delta_time)
        time_since_last_change = min(change_times)
        return time_since_last_change


    def run_unit_tests(self):
        unit_tests_file  = self.unit_test_files[0]  # here only use one unittests-file.
        test_results = run_tests.run_tests(unit_tests_file)
        return test_results



    def run_CI(self):
        time_between_unit_test_runs = 8    # the time the program will sleep before checking for updates (and potentially running unit tests)

        print(f"the folder named {self.folder_to_track} is currently being tracked", end = "\n\n")
        while True:
            time_since_change = self.find_time_since_last_change()
            print(f"time since last change in the {self.folder_to_track}-folder: {time_since_change} seconds")
            if time_since_change < time_between_unit_test_runs:
                print("running unit tests")
                test_results = self.run_unit_tests()
                print_test_result_info(test_results)
            else:
                print("will not run unit tests now")
                print("make a change to any file in dummyProject and save, in order to re-run the unit tests")
            print("")

            time.sleep(time_between_unit_test_runs)




if __name__ == "__main__":
    folder_path = "dummyProject"
    ci = CI(folder_to_track=folder_path)
    ci.run_CI()










