# -*- coding: utf-8 -*-

import platform
import sys

import pymssql
import _mssql

def main():

    print("System:")
    print("platform.system()       :", platform.system())
    print("platform.architecture() :", platform.architecture())
    if platform.system() != 'Windows':
        print("platform.libc_ver()     :", platform.libc_ver())

    print("Python:")
    print("sys.version             :", sys.version)

    print("pymssql:")
    print("VERSION            :", pymssql.VERSION)
    print("version            :", pymssql.__version__)
    print("full_version       :", pymssql.__full_version__)
    print("dbversion          :", pymssql.get_dbversion())
    try:
        print("get_freetds_version :", pymssql.get_freetds_version())
    except AttributeError:
        pass

    print("_mssql:")
    print("VERSION            :", _mssql.VERSION)
    print("version            :", _mssql.__version__)
    print("full_version       :", _mssql.__full_version__)
    print("dbversion          :", _mssql.get_dbversion())
    print("login_timeout      :", _mssql.login_timeout)
    print("min_error_severity :", _mssql.min_error_severity)



if __name__ == '__main__':

    main()
