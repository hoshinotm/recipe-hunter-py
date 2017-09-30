################
# class CmdLineArgs
# Represents command line consisting of:
#   script-name [arg1[, arg2[, [arg3 [...]]]]]
#
import sys


class CmdLineArgs(object):

    def num_of_params(self):
        return len(sys.argv)-1

    def script_name(self):
        return sys.argv[0]

    def param_list(self):
        if len(sys.argv) > 1:
            return sys.argv[1:]

