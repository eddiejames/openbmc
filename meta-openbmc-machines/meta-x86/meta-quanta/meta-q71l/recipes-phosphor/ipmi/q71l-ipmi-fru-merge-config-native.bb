inherit native
inherit obmc-phosphor-license

DEPENDS += "virtual/phosphor-ipmi-fru-inventory"
PROVIDES += "virtual/phosphor-ipmi-fru-merge-config"

# Put the fru_config in the right place with the right name.
# Pull the IPMI FRU YAML config to use it in the IPMI HOST YAML.
do_install_append() {
  IPMI_FRU_SRC=${datadir}/phosphor-ipmi-fru/config
  IPMI_HOST_DEST=${D}${datadir}/phosphor-ipmi-host/config
  install -d ${IPMI_HOST_DEST}
  cat ${IPMI_FRU_SRC}/config.yaml > ${IPMI_HOST_DEST}/fru_config.yaml
}
