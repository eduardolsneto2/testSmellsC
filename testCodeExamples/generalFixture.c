#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define LEN 30

struct tst {
	int result_len;
	const char *input;
	const char *output;
};

int rv;
size_t len;

void setup() {
	len = LEN;
	rv = sc_hex_to_bin(t->input, res, &len);
}

static void torture_cachedir_default_empty_home(void **state)
{
	sc_context_t *ctx = NULL;
	char buf[PATH_MAX] = {0};
	size_t buflen = sizeof(buf);
	int rv;

	rv = sc_establish_context(&ctx, "cachedir");
	assert_int_equal(rv, SC_SUCCESS);
	assert_non_null(ctx);

	/* Keep configuration empty */
	setenv("OPENSC_CONF", "/nonexistent", 1);
	setenv("XDG_CACHE_HOME", "", 1);
	setenv("HOME", "", 1);

	rv = sc_get_cache_dir(ctx, buf, buflen);
	assert_int_equal(rv, SC_ERROR_INTERNAL);

	sc_release_context(ctx);
}

static void torture_cachedir_default_empty(void **state)
{
	sc_context_t *ctx = NULL;
	char buf[PATH_MAX] = {0};
	size_t buflen = sizeof(buf);
	int rv;

	rv = sc_establish_context(&ctx, "cachedir");
	assert_int_equal(rv, SC_SUCCESS);
	assert_non_null(ctx);

	/* Keep configuration empty */
	setenv("OPENSC_CONF", "/nonexistent", 1);
	setenv("XDG_CACHE_HOME", "", 1);
	setenv("HOME", "/home/test", 1);

	rv = sc_get_cache_dir(ctx, buf, buflen);
	assert_int_equal(rv, SC_SUCCESS);
	assert_string_equal(buf, "/home/test/.cache/opensc");

	sc_release_context(ctx);
}

int main() {
    setup();
    torture_cachedir_default_empty_home();
    return 0;
}