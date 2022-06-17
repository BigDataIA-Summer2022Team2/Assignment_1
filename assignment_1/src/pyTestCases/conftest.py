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
    #print("Calling pytest runtest makereport hook...")
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    #print(rep)
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item,"rep_" + rep.when, rep)