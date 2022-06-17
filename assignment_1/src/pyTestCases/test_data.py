import pytest
from _pytest.fixtures import SubRequest


# @pytest.mark.parametrize('username,password',[('','xiaoming123434'),('',''),('xiaowang','')])
# def test_ddt(username,password):
#     print(f'{username}--{password}')


# @pytest.mark.parametrize('username,password',[('','xiaoming123434'),('',''),('xiaowang','')])
# def test_ddt1(username,password):
#     assert username == 'xiaowang'
#     print(f'{username}--{password}')


########################################################
# @pytest.mark.parametrize('combined_csv',['combined.csv','hello.csv','JgcC4HsilyY4sNNJ2ElyqZgO3OPwKN6hAoDVm5O6.csv'])
# def test_getAwsS3BucketBody(combined_csv):
#     assert combined_csv == 'combined.csv'
#     print(combined_csv)
#     print(s3.getS3BucketBodyInfo(combined_csv))


@pytest.fixture
def pytestRequest(request:SubRequest):
    yield
    #print("name:",request.node.name,request.node.rep_call.outcome)
    outcome = request.node.rep_call.outcome
    name = request.node.name
    if(outcome == 'failed'):
        print(name,"用例失败...")
    elif(outcome == 'passed'):
        print(name,"用例成功...")
    else:
        print(name,"用例 未执行或有问题...")

# @pytest.fixture
# def test_1(pytestRequest):
#     return 1

# @pytest.mark.parametrize('val',[1])
# def test_demo(test_1,val):
#     assert test_1 == val
#     print("result",test_1)


def test_1(pytestRequest):
    assert 1==1

def test_2(pytestRequest):
    assert 1==2

def test_3(pytestRequest):
    assert 1==2
    
def test_4(pytestRequest):
    assert 1==2

def test_5(pytestRequest):
    assert 1==1

if __name__=='__main__':
     pytest.main()