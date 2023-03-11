"""
    email_template.py
    -------

    This module contains NGP framework email template.
"""

NGP_EMAIL_TEMPLATE = """
<html>
    <body>
        <h1> <center>NGP Notification Service</center> </h1> <br>

        <br>&nbsp;
        <table style="width:80%"  border="1" align="center">
        <tr>
        <td colspan="3" align="center" bgcolor="{{ ngp_job_color }}"><b>Status: {{ ngp_job_status }}</b></td>
        </tr>
        <tr bgcolor="BBF1FA">
            <th ></th>
            <th></th>
        </tr>
        <tr>
            <td align="center">Time</td>
            <td bgcolor="BBF1FA" align="center" width="20%">{{ ngp_job_time }}</td>
        </tr>
        <tr>
            <td align="center">DAG</td>
            <td bgcolor="BBF1FA" align="center" width="20%">{{ ngp_job_dag }}</td>
        </tr>
        <tr>
            <td align="center">Task</td>
            <td bgcolor="BBF1FA" align="center" width="20%">{{ ngp_job_task }}</td>
        </tr>
        <tr>
            <td align="center">Run</td>
            <td bgcolor="BBF1FA" align="center" width="20%">{{ ngp_job_run }}</td>
        </tr>
        <tr>
            <td align="center">Remark</td>
            <td bgcolor="BBF1FA" align="center" width="20%">{{ ngp_job_remark }}</td>
        </tr>
        </table>
    </body>
</html>
"""