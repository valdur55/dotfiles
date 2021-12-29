"""
Attach pydevd debuger on py3status load..

@author valdur55 valdur55@gmail.com

SAMPLE OUTPUT
{'full_text': '🐛'}
"""

import pydevd_pycharm
import pydevd

def connect_to_pycharm():
    result = "🍀"
    try:
        pydevd_pycharm.settrace('localhost', port=6767, stdoutToServer=True, stderrToServer=True, suspend=False)
        result = "🐛"
    except Exception:
        pass
    return result

init_result = connect_to_pycharm()

class Py3status:
    """
    """
    _connection_result = init_result

    def _post_config_hoop(self):
        pass

    def _connect_to_pycharm(self):
        self._connection_result = connect_to_pycharm()

    def idea_debug(self):
        return {
            "cached_until": self.py3.CACHE_FOREVER,
            "full_text":   self._connection_result,
        }


    def on_click(self, event):
        try:
            pydevd.stoptrace()
        except Exception:
            pass

        self._connect_to_pycharm()
        self.py3.update()
        return


if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test

    module_test(Py3status)
