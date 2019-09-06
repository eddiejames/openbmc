DESCRIPTION = "Linux kernel for Aspeed"
SECTION = "kernel"
LICENSE = "GPLv2"

PROVIDES += "virtual/kernel"

KCONFIG_MODE="--alldefconfig"

KSRC ?= "git://github.com/openbmc/linux;protocol=git;branch=${KBRANCH}"
SRC_URI = "${KSRC}"
SRC_URI += " file://defconfig"

SRC_URI += " file://0001-dt-bindings-gpio-aspeed-Update-documentation-with-as.patch"
SRC_URI += " file://0002-gpio-aspeed-Fix-incorrect-number-of-banks.patch"
SRC_URI += " file://0003-gpios-Use-ngpio-property-from-device-tree-if-availab.patch"
SRC_URI += " file://0004-gpio-Add-in-ast2600-details-to-Aspeed-driver.patch"
SRC_URI += " file://0001-arch-ARM-Aspeed-AST2600-Add-GPIO-controller.patch"

LINUX_VERSION_EXTENSION ?= "-${SRCREV}"

PV = "${LINUX_VERSION}+git${SRCPV}"

inherit kernel
require recipes-kernel/linux/linux-yocto.inc

# From 4.16+ the COPYING file changed
LIC_FILES_CHKSUM = "file://COPYING;md5=bbea815ee2795b2f4230826c0c6b8814"
