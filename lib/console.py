"""console.py"""

import os
import time
import sys


class Console(object):
    """Console class"""

    def clear(self):
        """Clear"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def simulate_typing(self, message):
        """Simulate typeing"""
        for offset in range(0, len(message)):
            time.sleep(0.04)
            sys.stdout.write(message[offset])
            sys.stdout.flush()
        print
