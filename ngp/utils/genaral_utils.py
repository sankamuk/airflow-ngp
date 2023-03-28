"""
    general_utils.py
    -------

    This module contains general utility functions.
"""
import json
import subprocess


def load_dict_from_json_file(json_fl: str) -> dict:
    """
    Reads a JSON file and load content as a Python dictionary

    :param json_fl: String of JSON files absolute path
    :return: Dictionary of the JSON content
    """

    with open(json_fl) as fl:
        res = json.load(fl)

    return res


def run_host_command(command_str: list, cwd: str = None, timeout: int = 300) -> dict:
    """
    Executes command in host and returns status

    :param command_str: List representing the command to be executed
    :param cwd: String representing work directory for the command
    :param timeout: Integer representing timeout after which the command will be terminated
    :return: Dictionary representing status, example::
        { "status": 0, "message": "details" }

    """

    try:
        result = subprocess.run(command_str,
                                shell=True,
                                capture_output=True,
                                timeout=timeout,
                                cwd=cwd,
                                universal_newlines=True)
    except subprocess.TimeoutExpired as e:
        return {"status": 1,
                "message": "TIMEOUT: Command = {}".format(" ".join(command_str)),
                "stdout": e.stdout,
                "stderr": e.stderr}

    if not result.returncode:
        return {"status": 0,
                "message": "SUCCESSFUL: Command = {}".format(" ".join(command_str)),
                "stdout": result.stdout,
                "stderr": result.stderr}
    else:
        return {"status": 1,
                "message": "FAILED: Command = {}".format(" ".join(command_str)),
                "stdout": result.stdout,
                "stderr": result.stderr}
