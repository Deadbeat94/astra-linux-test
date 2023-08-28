import pytest
import subprocess


path_to_diapason = '/diapason'
# Укажите путь к файлу

@pytest.fixture(scope='function')
def program_output(request):
    print('\nSETUP: Opening "diapason", starting test')
    diapason = subprocess.Popen([path_to_diapason], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, text=True, shell=True)

    diapason.stdin.write(request.param)
    diapason.stdin.close()
    stdout_value = diapason.stdout.read().rstrip()[-1]
    stdout_error = diapason.stderr.read()
    if not stdout_error:
        result = stdout_value
    else:
        result = stdout_error
    yield result
    diapason.stdout.close()
    print('\nTEARDOWN: Test finished, "diapason" closed')
