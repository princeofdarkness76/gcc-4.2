#
# This spec file is read by gcj when linking.
# It is used to specify the standard libraries we need in order
# to link with libgcj.
#
%rename startfile startfileorig
*startfile:  %(startfileorig)

%rename lib liborig
*lib:  %{s-bc-abi:} -lgcj  -lm -liconv  -lpthread    -ldl %(libgcc) %(liborig)

*jc1: -fhash-synchronization -fuse-divide-subroutine -fcheck-references -fuse-boehm-gc    -fkeep-inline-functions
