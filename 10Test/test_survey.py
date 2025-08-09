from survey import AnonymousSurvey
import pytest

# 夹具：帮助我们搭建上百个测试的测试环境
# pytest.fixture装饰器，放在函数定以前的指令
# 在运行函数前，python将该指令应用于函数，以修改函数代码的行为

@pytest.fixture
def language():
    question = 'What language do you live in?'
    language = AnonymousSurvey(question)
    return language

# 接收的参数上写上要接受的实例 必须与夹具的方法名相同 这样就会把夹具的返回值传递过来
def test_store_single_response(language):
    # question = 'What language do you live in?'
    # language = AnonymousSurvey(question)
    language.store_response('English')
    assert 'English' in language.answers

