"""
Attach pydevd compatible debugger on py3status load.
PyDev.Debugger (used in PyDev, PyCharm and VSCode Python)

@author valdur55 valdur55@gmail.com

SAMPLE OUTPUT
{'full_text': '🐛'}
"""
import pydevd_pycharm

DEFAULT_PORT = 6767
RESULT_CONNECTED = "🐛"
RESULT_DISCONNECTED = "🍀"

def _connect_to_pydevd(port):
    try:
        pydevd_pycharm.settrace('localhost', port=port, stdout_to_server=True, stderr_to_server=True, suspend=False)
        return RESULT_CONNECTED
    except Exception:
        return RESULT_DISCONNECTED

init_result = _connect_to_pydevd(DEFAULT_PORT)

# Useful when you wan to have import time hook
#init_result = _connect_to_pydevd(DEFAULT_PORT)

class Py3status:
    """
    """
    port = DEFAULT_PORT
    _connection_result = init_result

    def _connect_to_pydevd(self):
        self._connection_result = _connect_to_pydevd(self.port)

    def post_config_hook(self):
        self._connect_to_pydevd()

    def pydev_debug(self):
        return {
            "cached_until": self.py3.CACHE_FOREVER,
            "full_text":   self._connection_result,
        }


    def on_click(self, event):
        try:
            pydevd_pycharm.stoptrace()
        except Exception:
            pass

        self._connect_to_pydevd()


if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test

    module_test(Py3status)