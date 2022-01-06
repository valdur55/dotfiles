"""
Attach pydevd debuger on py3status load..

@author valdur55 valdur55@gmail.com

SAMPLE OUTPUT
{'full_text': '🐛'}
"""
import debugpy

def connect_to_pycharm():
    try:
        debugpy.listen(8888)
        debugpy.wait_for_client()
        return "🐛"

    except Exception:
        return "🍀"

init_result = connect_to_pycharm()

class Py3status:
    """
    """
    some_config_val = None
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
#        try:
#            pydevd.stoptrace()
#        except Exception:
#            pass

        self._connect_to_pycharm()


if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test

    module_test(Py3status)
