class UnitTestRunInfo():
    """
    contains information about one execution of one unit-test.
    """


    def __init__(self, function_name, file_name, time_start_run, execution_time, was_success, error_message):
        self.function_name = function_name
        self.file_name = file_name
        self.time_when_run = time_start_run
        self.execution_time = execution_time
        self.was_success = was_success
        self.error_message = error_message

