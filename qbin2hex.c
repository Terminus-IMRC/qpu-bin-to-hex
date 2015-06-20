#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <inttypes.h>

int main()
{
	int i, j;
	int linenum = 0;
	char str[0x10000], str2[0x10000];

	while (fgets(str, 0x10000, stdin) != NULL) {
		uint64_t u = 0;
		int len;
		_Bool break_flag = 0;

		linenum ++;

		for (i = 0, j = 0; i < 0x10000 && !break_flag; i ++) {
			switch (str[i]) {
				case ' ':
				case '\t':
				case ',':
					break;
				case '/':
					if (i == 0 || str[i - 1] != '/')
						break;
				case ';':
				case '\0':
				case '\n':
					break_flag = !0;
					break;
				default:
					str2[j++] = str[i];
			}
		}
		str2[j] = '\0';
		len = strlen(str2);
		switch (len) {
			case 0:
				continue;
			case 64:
				break;
			default:
				fprintf(stderr, "%s:%d: error: %d: input string core size is not 64 but %d\n", __FILE__, __LINE__, linenum, len);
				exit(EXIT_FAILURE);
		}
		for (i = 0; i < len; i ++) {
			if (str2[i] != '0' && str2[i] != '1') {
				fprintf(stderr, "%s:%d: error: %d: invalid character: %c\n", __FILE__, __LINE__, linenum, str2[i]);
				exit(EXIT_FAILURE);
			}
			u |= ((uint64_t) (str2[i] - '0') << (63 - i));
		}
		printf("0x%08" PRIx32 ", 0x%08" PRIx32 ",\n", (uint32_t) (u & 0x00000000ffffffff), (uint32_t) ((u & 0xffffffff00000000) >> 32));
	}

	return 0;
}
