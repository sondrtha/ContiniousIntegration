import os
import sys
import importlib
import time
from inspect import getmembers, isfunction
from UnitTestRunInfo import UnitTestRunInfo


def add_surronding_folder_to_path(file_in_folder_path):
    #folder_path is the path of the folder that contains the file named file_in_folder_path
    folder_path = os.path.dirname(os.path.abspath(file_in_folder_path))
    sys.path.insert(len(sys.path), folder_path)


def find_test_functions(module):
    """
    Args:
        module : a python module
    Returns:
        test_functions : a list of python functions
    """
    functions_in_module = getmembers(module, isfunction)

    test_functions_names = []
    for function in functions_in_module:
        function_name, _ = function
        if function_name.startswith("test"):
            test_functions_names.append(function_name)

    test_functions = []
    for function_name in test_functions_names:
        func = getattr(module, function_name)
        test_functions.append(func)
    return test_functions


def run_unit_test(unit_test_function, file_name):
    time_start_run = time.time()

    error = None
    success = True
    try:
        unit_test_function()
    except AssertionError as err:
        error = str(err)
        success = False
    except BaseException as base_error:
        function_name = unit_test_function.__name__
        print(f"ERROR running {function_name}!!!  Stopping..")
        print(base_error)
        quit()



    execution_time = time.time() - time_start_run
    function_name = unit_test_function.__name__
    unit_test_run = UnitTestRunInfo(function_name, file_name, time_start_run, execution_time, success, error)
    return unit_test_run



def run_tests(file_path):
    """
    This messy function runs the unit tests in the file given by file_path.
    It returns the test_results which is a list of UnitTestRunInfo-objects.
    """

    #The code below is messy. Don't assume it is supposed to make sense.
    add_surronding_folder_to_path(file_path)
    file_name = os.path.basename(file_path)[:-3]
    importlib.invalidate_caches()
    module = importlib.import_module(file_name)
    importlib.invalidate_caches()
    importlib.reload(module)
    importlib.invalidate_caches()
    test_functions = find_test_functions(module)
    importlib.invalidate_caches()



    test_results = []
    for test_function in test_functions:
        test_result = run_unit_test(test_function, file_path)
        test_results.append(test_result)

    return test_results
