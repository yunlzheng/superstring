# coding: utf-8
from blinker import Namespace

signals = Namespace()

volume_create_start = signals.signal('volume.create.start')
volume_create_end = signals.signal('volume.create.end')

vm_create_start = signals.signal('vm.create.start')
vm_create_end = signals.signal('vm.create.end')