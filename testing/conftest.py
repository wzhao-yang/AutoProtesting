import pytest


# 共享数据，方法fixture方法放置在这个文件下 ，改写执行顺序
def pytest_collection_modifyitems(session, config, items: list):
    # print("这是个conftest")
    # print(items)
    # print(type(items))
    for item in items:
        if '_01' in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif '_2' in item.nodeid:
            item.add_marker(pytest.mark.div)
