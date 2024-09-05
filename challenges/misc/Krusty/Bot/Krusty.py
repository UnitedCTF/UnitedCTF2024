def set_proc_name(newname):
    from ctypes import cdll, byref, create_string_buffer
    libc = cdll.LoadLibrary('libc.so.6')
    buff = create_string_buffer(len(newname) + 1)
    buff.value = newname
    libc.prctl(15, byref(buff), 0, 0, 0)


if __name__ == '__main__':
    import sys
    import os
    import Krusty

    # check if sys is linux based
    if sys.platform == 'linux':
        set_proc_name('Krusty')

    Krusty.Krusty().run(os.getenv('TOKEN'))
