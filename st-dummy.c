#include <sys/types.h>
#include <stddef.h>
#include <stdarg.h>
#include <stdio.h>
#include <time.h>
#include <signal.h>
#ifdef size_t
typedef size_t Xsize_t;
#elif defined(__SIZE_TYPE__)
typedef __SIZE_TYPE__ Xsize_t;
#endif
#ifdef va_list
typedef va_list XXXva_list;
#endif
