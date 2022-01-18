"""
Attach pydevd compatible debuger on py3status load.
PyDev.Debugger (used in PyDev, PyCharm and VSCode Python)

@author valdur55 valdur55@gmail.com

SAMPLE OUTPUT
{'full_text': '🐛'}
"""
import pydevd

DEFAULT_PORT = 6767

def _connect_to_pydevd(port):
    try:
        pydevd.settrace('localhost', port=port, stdoutToServer=True, stderrToServer=True, suspend=False)
        return "🐛"
    except Exception:
        return "🍀"

init_result = "🍀"
# Useful when you wan to hae import time hook
#init_result = _connect_to_pydevd(DEFAULT_PORT)

class Py3status:
    """
    """
    port = 6767
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
            pydevd.stoptrace()
        except Exception:
            pass

        self._connect_to_pydevd()


if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test

    module_test(Py3status)
