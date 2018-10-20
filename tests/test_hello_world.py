import sample_python_package.sample as s


def test_main():
    msg = s.main()
    right_msg = 'Hello, world!'
    assert msg == right_msg, 'This is a dummy test :)'
