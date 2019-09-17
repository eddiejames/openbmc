DESCRIPTION = "Linux kernel for Aspeed"
SECTION = "kernel"
LICENSE = "GPLv2"

PROVIDES += "virtual/kernel"

KCONFIG_MODE="--alldefconfig"

KSRC ?= "git://github.com/openbmc/linux;protocol=git;branch=${KBRANCH}"
SRC_URI = "${KSRC}"
SRC_URI += " file://defconfig"
SRC_URI_append_aspeed-g6 = " \
    file://0001-ARM-aspeed-g6-lpc-add-compatible-strings.patch \
    file://0002-ARM-dts-aspeed-g6-Add-lpc-devices.patch \
    file://0003-ARM-dts-aspeed-add-Rainier-system.patch \
    "

LINUX_VERSION_EXTENSION ?= "-${SRCREV}"

PV = "${LINUX_VERSION}+git${SRCPV}"

inherit kernel
require recipes-kernel/linux/linux-yocto.inc

# From 4.16+ the COPYING file changed
LIC_FILES_CHKSUM = "file://COPYING;md5=bbea815ee2795b2f4230826c0c6b8814"
