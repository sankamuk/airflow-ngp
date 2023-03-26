import json
import os
import tempfile
from datetime import datetime
from ngp.utils.genaral_utils import load_dict_from_json_file, run_host_command


def test_load_dict_from_json_file():
    tmp_fl = os.path.join(tempfile.gettempdir(), str(datetime.now().timestamp()))
    tmp_dict = {"a": 1}

    with open(tmp_fl, 'w') as fl:
        json.dump(tmp_dict, fl)

    loaded_dict = load_dict_from_json_file(tmp_fl)
    os.remove(tmp_fl)

    assert loaded_dict == tmp_dict


def test_run_host_command():
    # Unsuccessful command
    commd_str = ["python", "-c", "time.sleep(2)"]

    exec_result = run_host_command(commd_str)
    assert exec_result["status"] == 1

    # Successful command
    commd_str = ["python", "-c", "import time; time.sleep(2)"]

    exec_result = run_host_command(commd_str)
    assert exec_result["status"] == 0

    # Timeout command
    exec_result = run_host_command(commd_str, timeout=1)
    assert exec_result["status"] == 1
