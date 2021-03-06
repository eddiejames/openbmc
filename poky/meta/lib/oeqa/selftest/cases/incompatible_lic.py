from oeqa.selftest.case import OESelftestTestCase
from oeqa.utils.commands import bitbake

class IncompatibleLicenseTests(OESelftestTestCase):

    def lic_test(self, pn, pn_lic, lic):
        error_msg = 'ERROR: Nothing PROVIDES \'%s\'\n%s was skipped: it has an incompatible license: %s' % (pn, pn, pn_lic)

        self.write_config("INCOMPATIBLE_LICENSE += \"%s\"" % (lic))

        result = bitbake('%s --dry-run' % (pn), ignore_status=True)
        if error_msg not in result.output:
            raise AssertionError(result.output)

    # Verify that a package with an SPDX license (from SRC_DISTRIBUTE_LICENSES)
    # cannot be built when INCOMPATIBLE_LICENSE contains this SPDX license
    def test_incompatible_spdx_license(self):
        self.lic_test('incompatible-license', 'GPL-3.0', 'GPL-3.0')

    # Verify that a package with an SPDX license (from SRC_DISTRIBUTE_LICENSES)
    # cannot be built when INCOMPATIBLE_LICENSE contains an alias (in
    # SPDXLICENSEMAP) of this SPDX license
    def test_incompatible_alias_spdx_license(self):
        self.lic_test('incompatible-license', 'GPL-3.0', 'GPLv3')

    # Verify that a package with an alias (from SPDXLICENSEMAP) to an SPDX
    # license cannot be built when INCOMPATIBLE_LICENSE contains this SPDX
    # license
    def test_incompatible_spdx_license_alias(self):
        self.lic_test('incompatible-license-alias', 'GPLv3', 'GPL-3.0')

    # Verify that a package with an alias (from SPDXLICENSEMAP) to an SPDX
    # license cannot be built when INCOMPATIBLE_LICENSE contains this alias
    def test_incompatible_alias_spdx_license_alias(self):
        self.lic_test('incompatible-license-alias', 'GPLv3', 'GPLv3')

    # Verify that a package with a non-SPDX license (neither in
    # SRC_DISTRIBUTE_LICENSES nor in SPDXLICENSEMAP) cannot be built when
    # INCOMPATIBLE_LICENSE contains this license
    def test_incompatible_nonspdx_license(self):
        self.lic_test('incompatible-nonspdx-license', 'FooLicense', 'FooLicense')

class IncompatibleLicensePerImageTests(OESelftestTestCase):
    def default_config(self):
        return """
IMAGE_INSTALL_append = "bash"
INCOMPATIBLE_LICENSE_pn-core-image-minimal = "GPL-3.0 LGPL-3.0"
"""

    def test_bash_default(self):
        self.write_config(self.default_config())
        error_msg = "ERROR: core-image-minimal-1.0-r0 do_rootfs: Package bash has an incompatible license GPLv3+ and cannot be installed into the image."

        result = bitbake('core-image-minimal', ignore_status=True)
        if error_msg not in result.output:
            raise AssertionError(result.output)

    def test_bash_and_license(self):
        self.write_config(self.default_config() + '\nLICENSE_append_pn-bash = " & SomeLicense"')
        error_msg = "ERROR: core-image-minimal-1.0-r0 do_rootfs: Package bash has an incompatible license GPLv3+ & SomeLicense and cannot be installed into the image."

        result = bitbake('core-image-minimal', ignore_status=True)
        if error_msg not in result.output:
            raise AssertionError(result.output)

    def test_bash_or_license(self):
        self.write_config(self.default_config() + '\nLICENSE_append_pn-bash = " | SomeLicense"')

        bitbake('core-image-minimal')

    def test_bash_whitelist(self):
        self.write_config(self.default_config() + '\nWHITELIST_GPL-3.0_pn-core-image-minimal = "bash"')

        bitbake('core-image-minimal')

