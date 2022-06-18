import pytest

# @pytest.fixture(scope="session", autouse=True)
# def session():
#     print("session start...")
#     yield
#     print("session end...")

# @pytest.fixture(scope="module", autouse=True)
# def module():
#     print("module start...")
#     yield
#     print("module end...")

# @pytest.fixture(scope="class", autouse=True)
# def classT():
#     print("class start...")
#     yield
#     print("class end...")

# @pytest.fixture(scope="function", autouse=True)
# def func():
#     print("function start...")
#     yield
#     print("function end...")






@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    out = yield
    
    
    report = out.get_result()
    if(report.when == "call"):
        print("\n====================================================")
        print('Test Result:\t%s' % out)    
        print('Test Report:\t%s' % report)
        print('Process:\t%s' % report.when)
        print('id:\t%s' % report.nodeid)
        print('description:\t%s' % str(item.function.__doc__))
        print('result:\t%s' % report.outcome)
    
    