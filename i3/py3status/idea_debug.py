"""
Attach pydevd debuger on py3status load..

@author valdur55 valdur55@gmail.com

SAMPLE OUTPUT
{'full_text': '🐛'}
"""

import pydevd_pycharm
result = "F"
try:
    pydevd_pycharm.settrace('localhost', port=6767, stdoutToServer=True, stderrToServer=True, suspend=False)
    result = "🐛"
except Exception:
    pass

class Py3status:
    """
    """
    someConfigParam = ""
    def _post_config_hoop(self):
        pass


    def idea_debug(self):
        return {
            "cached_until": self.py3.CACHE_FOREVER,
            "full_text":   result,
        }


if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test

    module_test(Py3status)
