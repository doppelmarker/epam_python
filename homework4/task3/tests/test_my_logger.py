from homework4.task3.my_logger.my_logger import my_logger


def test_my_logger_prints_to_stdout(capsys):
    msg = "todo bien mi amigo!"
    my_logger(msg)
    captured = capsys.readouterr()
    assert captured.out.strip() == msg


def test_my_logger_prints_to_stderr(capsys):
    msg = "error occurred!"
    my_logger(msg)
    captured = capsys.readouterr()
    assert captured.err.strip() == msg
