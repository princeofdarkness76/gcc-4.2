#
# This spec file is read by gcj when linking.
# It is only used by the testing harnesses (in libjava and gdb).
#
%rename lib liborig2
*lib: -L/Users/stevenjames/gcc-4.2/.libs -rpath /Users/stevenjames/gcc-4.2/.libs -L/Users/stevenjames/gcc-4.2/../boehm-gc/.libs -rpath /Users/stevenjames/gcc-4.2/../boehm-gc/.libs  %(liborig2)

