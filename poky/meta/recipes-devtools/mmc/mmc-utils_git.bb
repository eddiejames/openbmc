SUMMARY = "Userspace tools for MMC/SD devices"
HOMEPAGE = "http://git.kernel.org/cgit/linux/kernel/git/cjb/mmc-utils.git/"
LICENSE = "GPLv2"
LIC_FILES_CHKSUM = "file://mmc.c;beginline=1;endline=20;md5=fae32792e20f4d27ade1c5a762d16b7d"

SRCBRANCH ?= "master"
SRCREV = "aef913e31b659462fe6b9320d241676cba97f67b"

PV = "0.1+git${SRCPV}"

SRC_URI = "git://git.kernel.org/pub/scm/linux/kernel/git/cjb/mmc-utils.git;branch=${SRCBRANCH} \
           file://0001-mmc_cmd.c-Use-extra-braces-when-initializing-subobje.patch \
           "
UPSTREAM_CHECK_COMMITS = "1"

S = "${WORKDIR}/git"

CFLAGS_append_powerpc64 = " -D__SANE_USERSPACE_TYPES__"
CFLAGS_append_mipsarchn64 = " -D__SANE_USERSPACE_TYPES__"
CFLAGS_append_mipsarchn32 = " -D__SANE_USERSPACE_TYPES__"

do_install() {
    install -d ${D}${bindir}
    install -m 0755 mmc ${D}${bindir}
}
