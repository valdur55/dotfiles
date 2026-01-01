"""
Sample logging module to test click events and log levels.


@author valdur55 valdur@gmail.com

SAMPLE OUTPUT
{'full_text': '"<sometime>"}
"""
import datetime


class Py3status:
    """
    """
    def logger_sandbox(self):
        return {
            "cached_until": self.py3.CACHE_FOREVER,
            "full_text": f"{datetime.datetime.now().time()}",
        }

    def on_click(self, event):
        """
        Handles click events
        """
        button = event["button"]

        if button == 1:
            self.py3.log("DDDDDDDDDDDDDD", level="debug")
        elif button == 2:
            self.py3.log("IIIIIIIIIIIIIII", level="info")
            self.py3.log("LOG_I_LOG_I", level=self.py3.LOG_INFO)
        elif button == 3:
            self.py3.log("WWWWWWWWWWWWWW", level="warning")
            self.py3.log("LOG_WWWWWWWWWWWWWW", level=self.py3.LOG_WARNING)
        elif button == 4:
            self.py3.log("EEEEEEEEEEEEEE", level="error")
            self.py3.log("LOG_EEEEEEEEEEEEEE", level=self.py3.LOG_ERROR)
        elif button == 5:
            self.py3.log("CCCCCCCCCCCCCC", level="critical")
        elif button == 8:
            raise Exception("EXEXEXEXEXEXEXEX")



if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test

    module_test(Py3status)