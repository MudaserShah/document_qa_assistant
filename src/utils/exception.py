import sys


class CustomException(Exception):

    def __init__(self, error_message, error_detail=None):
        super().__init__(error_message)

        # get exception info properly
        _, _, exc_tb = sys.exc_info()

        if exc_tb is not None:
            self.line_number = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.line_number = None
            self.file_name = None

        self.error_message = error_message

    def __str__(self):
        return f"""
Error occurred in:
{self.file_name}

Line Number:
{self.line_number}

Error:
{self.error_message}
"""