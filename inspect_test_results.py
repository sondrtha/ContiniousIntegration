from UnitTestRunInfo import UnitTestRunInfo


def find_num_success_and_total(test_results):
    num_success = 0
    total_tests = len(test_results)
    for unit_test_result in test_results:
        if unit_test_result.was_success:
            num_success += 1
    return (num_success, total_tests)


def print_test_result_info(test_results):
    success, total_tests = find_num_success_and_total(test_results)
    failed_tests = []

    for unit_test_result in test_results:
        if not unit_test_result.was_success:
            failed_tests.append(unit_test_result.function_name)

    print(f"num unit tests that ran successfully: {success}, num tests run in total: {total_tests}")
    print("tests that failed where: ", end = "")
    print(", ".join(failed_tests))




