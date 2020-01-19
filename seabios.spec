Name:           seabios
Version:        1.11.0
Release:        2%{?dist}
Summary:        Open-source legacy BIOS implementation

Group:          Applications/Emulators
License:        LGPLv3
URL:            http://www.coreboot.org/SeaBIOS


Source0: https://code.coreboot.org/p/seabios/downloads/get/seabios-1.11.0.tar.gz

Source10:       config.vga.cirrus
Source11:       config.vga.isavga
Source12:       config.vga.qxl
Source13:       config.vga.stdvga
Source14:       config.vga.vmware
Source15:       config.base
Source16:       config.base-256k
Source17:       config.vga.virtio


Patch0002: 0002-allow-1TB-of-RAM.patch
Patch0003: 0003-smbios-set-bios-vendor-version-fields-to-Seabios-0.5.patch
Patch0004: 0004-Workaround-for-a-win8.1-32-S4-resume-bug.patch
Patch0005: 0005-redhat-reserve-more-memory-on-fseg.patch
Patch0006: 0006-vgabios-Reorder-video-modes-to-work-around-a-Windows.patch
# For bz#1523166 - [Q35] guest kernel panic when boot with 9 nics
Patch7: seabios-pci-fix-io-hints-capability-for-RedHat-PCI-bridges.patch
BuildRequires: python iasl
ExclusiveArch: x86_64 %{power64}

Requires: %{name}-bin = %{version}-%{release}
Requires: seavgabios-bin = %{version}-%{release}

# Seabios is noarch, but required on architectures which cannot build it.
# Disable debuginfo because it is of no use to us.
%global debug_package %{nil}

# You can build a debugging version of the BIOS by setting this to a
# value > 1.  See src/config.h for possible values, but setting it to
# a number like 99 will enable all possible debugging.  Note that
# debugging goes to a special qemu port that you have to enable.  See
# the SeaBIOS top-level README file for the magic qemu invocation to
# enable this.
%global debug_level 1


%description
SeaBIOS is an open-source legacy BIOS implementation which can be used as
a coreboot payload. It implements the standard BIOS calling interfaces
that a typical x86 proprietary BIOS implements.


%package bin
Summary: Seabios for x86
BuildArch: noarch

%description bin
SeaBIOS is an open-source legacy BIOS implementation which can be used as
a coreboot payload. It implements the standard BIOS calling interfaces
that a typical x86 proprietary BIOS implements.


%package -n seavgabios-bin
Summary: Seavgabios for x86
BuildArch: noarch

Obsoletes: vgabios < 0.6c-10
Provides: vgabios = 0.6c-10


%description -n seavgabios-bin
SeaVGABIOS is an open-source VGABIOS implementation.


%prep
%setup -q

%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch7 -p1

%build
%ifarch x86_64
export CFLAGS="$RPM_OPT_FLAGS"
mkdir binaries

build_bios() {
    make clean distclean
    cp $1 .config
    echo "CONFIG_DEBUG_LEVEL=%{debug_level}" >> .config
    make oldnoconfig V=1 EXTRAVERSION="-%release"

    make V=1 $4 EXTRAVERSION="-%release"

    cp out/$2 binaries/$3
}


# seabios 128k
build_bios %{SOURCE15} bios.bin bios.bin

# seabios 256k
build_bios %{SOURCE16} bios.bin bios-256k.bin

# seavgabios
for config in %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE17}; do
	name=${config#*config.vga.}
    build_bios ${config} vgabios.bin vgabios-${name}.bin out/vgabios.bin
done


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/seabios
mkdir -p $RPM_BUILD_ROOT%{_datadir}/seavgabios
install -m 0644 binaries/bios*.bin $RPM_BUILD_ROOT%{_datadir}/seabios
install -m 0644 binaries/vgabios*.bin $RPM_BUILD_ROOT%{_datadir}/seavgabios


%files
%doc COPYING COPYING.LESSER README


%files bin
%dir %{_datadir}/seabios/
%{_datadir}/seabios/bios*.bin

%files -n seavgabios-bin
%dir %{_datadir}/seavgabios/
%{_datadir}/seavgabios/vgabios*.bin
%endif

%changelog
* Tue Jan 30 2018 Miroslav Rezanina <mrezanin@redhat.com> - 1.11.0-2.el7
- seabios-pci-fix-io-hints-capability-for-RedHat-PCI-bridges.patch [bz#1523166]
- Resolves: bz#1523166
  ([Q35] guest kernel panic when boot with 9 nics)

* Wed Nov 15 2017 Miroslav Rezanina <mrezanin@redhat.com> - 1.11.0-1.el7
- Rebase to 1.11.0 [bz#1470751]
- Resolves: bz#1470751
  (Rebase seabios for RHEL-7.5)

* Fri Oct 20 2017 Miroslav Rezanina <mrezanin@redhat.com> - 1.10.2-5.el7
- seabios-boot-Rename-drive_g-to-drive.patch [bz#1452603]
- seabios-disk-Don-t-require-the-struct-drive_s-to-be-in-the-f.patch [bz#1452603]
- seabios-block-Rename-disk_op_s-drive_gf-to-drive_fl.patch [bz#1452603]
- seabios-virtio-Allocate-drive_s-storage-in-low-memory.patch [bz#1452603]
- Resolves: bz#1452603
  (can't bootup from image when attached multi-virtio-scsi disks with multi-luns)

* Thu Sep 28 2017 Wainer dos Santos Moschetta <wainersm@redhat.com> - 1.10.2-4.el7
- seabios-virtio-IOMMU-support.patch [bz#1463163, bz#1467811]
- Resolves: bz#1463163
  (Guest OS will down when disk enable the IOMMU for Virtio)
- Resolves: bz#1467811
  (Guest OS will down when disk enable the IOMMU for virtio-scsi)

* Fri May 12 2017 Miroslav Rezanina <mrezanin@redhat.com> - 1.10.2-3.el7
- seabios-blockcmd-accept-only-disks-and-CD-ROMs.patch [bz#1020622]
- seabios-blockcmd-generic-SCSI-luns-enumeration.patch [bz#1020622]
- seabios-virtio-scsi-enumerate-luns-with-REPORT-LUNS.patch [bz#1020622]
- seabios-usb-uas-enumerate-luns-with-REPORT-LUNS.patch [bz#1020622]
- Resolves: bz#1020622
  (seabios fail to recognize virtio-scsi device if specify LUN not 0)

* Thu Mar 30 2017 Miroslav Rezanina <mrezanin@redhat.com> - 1.10.2-2.el7
- seabios-resume-Don-t-attempt-to-use-generic-reboot-mechanism.patch [bz#1428347]
- Resolves: bz#1428347
  (reboot hangs on rhel6 machine types (~1/20 times))

* Fri Mar 10 2017 Miroslav Rezanina <mrezanin@redhta.com> - 1.10.2-1.el7
- Rebase to 1.10.2 [bz#1392821]
- Resolves:  bz#1392821
 (Rebase seabios to 1.10.1)

* Fri Feb 03 2017 Miroslav Rezanina <mrezanin@redhat.com> - 1.10.1-2.el7
- seabios-smm-disable-by-default.patch [bz#1378006]
- seabios-ahci-Set-upper-32-bit-registers-to-zero.patch [bz#1418320]
- Resolves: bz#1378006
  (guest paused on target host sometimes when do migration during guest boot)
- Resolves: bz#1418320
  (Seabios does not fully reset AHCI adapters)

* Tue Jan 10 2017 Miroslav Rezanina <mrezanin@redhat.com> - 1.10.1-1.el7
- Rebase to seabios 1.10.1 [bz#1392821]
- Resolves: bz#1392821
  (Rebase seabios to 1.10.1)

* Tue Nov 29 2016 Miroslav Rezanina <mrezanin@redhat.com> - 1.9.1-5.el7_3.1
- seabios-vgabios-Reorder-video-modes-to-work-around-a-Windows.patch [bz#1392028]
- Resolves: bz#1392028
  ([virtio-win][svvp][ws2016] cannot generate dump file when using nmi on ws2016 and win10-32/64)

* Thu Sep 15 2016 Miroslav Rezanina <mrezanin@redhat.com> - 1.9.1-5.el7
- seabios-pci-don-t-map-virtio-1.0-storage-devices-above-4G.patch [bz#1373154]
- Resolves: bz#1373154
  (Guest fails boot up with ivshmem-plain and virtio-pci device)

* Wed May 11 2016 Miroslav Rezanina <mrezanin@redhat.com> - 1.9.1-4.el7
- seabios-Build-vgabios-virtio.bin.patch [bz#1327001]
- Resolves: bz#1327001
  (vgabios-virtio.bin should be included  in seavgabios-bin package)

* Tue Apr 26 2016 Miroslav Rezanina <mrezanin@redhat.com> - 1.9.1-3.el7
- seabios-redhat-reserve-more-memory-on-fseg.patch [bz#1327060]
- seabios-redhat-turn-off-some-config-options.patch [bz#1327060]
- Resolves: bz#1327060
  ([Seabios]Limited boot number supported for SCSI/SATA)

* Wed Apr 06 2016 Miroslav Rezanina <mrezanin@redhat.com> - 1.9.1-2.el7
- seabios-fw-pci-add-Q35-S3-support.patch [bz#1185721]
- Resolves: bz#1185721
  (win7 guest (boot with q35) show dark screen after do S3)

* Tue Feb 16 2016 Miroslav Rezanina <mrezanin@redhat.com> - 1.9.1-1.el7
- Rebase to 1.9.1 [bz#1257052]
- Resolves: bz#1257052
  (rebase seabios to 1.9)

* Wed Jul 15 2015 Yash Mankad <ymankad@redhat.com> - 1.7.5-11.el7
- seabios-bootorder-Update-extra-pci-root-buses-bootorder-form.patch [bz#1242968]
- Resolves: bz#1242968
  (pci: support booting of devices behind PXB)

* Tue Jul 07 2015 Miroslav Rezanina <mrezanin@redhat.com> - 1.7.5-10.el7
- seabios-fw-pci-scan-all-buses-if-extraroots-romfile-is-prese.patch [bz#1235381]
- seabios-fw-pci-map-memory-and-IO-regions-for-multiple-pci-ro.patch [bz#1235381]
- Resolves: bz#1235381
  (RFE: configure guest NUMA node locality for guest PCI devices)

* Thu Apr 23 2015 Miroslav Rezanina <mrezanin@redhat.com> - 1.7.5-9.el7_1
- seabios-boot.c-delay-exiting-boot-if-menu-key-is-ESC.patch [bz#841638]
- seabios-boot-switch-default-menu-key-to-ESC.patch [bz#841638]
- Resolves: bz#841638
  (Provide a platform agnostic approach to invoking the BIOS, boot menu, or other BIOS functions)

* Tue Jan 20 2015 Miroslav Rezanina <mrezanin@redhat.com> - 1.7.5-8.el7
- seabios-turn-off-stack-switching-for-vgabios.patch [bz#1182634]
- Resolves: bz#1182634
  (Remove CONFIG_VGA_ALLOCATE_EXTRA_STACK)

* Thu Nov 20 2014 Miroslav Rezanina <mrezanin@redhat.com> - 1.7.5-6.el7
- seabios-Extend-ExclusiveArch-to-power64-architectures.patch [bz#1163924]
- Resolves: bz#1163924
  (seabios is needed for ppc64 and ppc64le but marked ExclusiveArch aarch64)

* Tue Aug 26 2014 Miroslav Rezanina <mrezanin@redhat.com> - 1.7.5-5.el7
- seabios-Workaround-for-a-win8.1-32-S4-resume-bug.patch [bz#1050775]
- seabios-boot-Fix-boot-order-for-SCSI-target-lun-9.patch [bz#1096560]
- Resolves: bz#1096560
  (fail to assign correct order for the boot device in seabios as we specified the bootindex in qemu-kvm cli(under the same virtio-scsi-pci))

* Wed Aug 13 2014  Miroslav Rezanina <mrezanin@redhat.com> - 1.7.5-4.el7
- seabios-smbios-set-bios-vendor-version-fields-to-Seabios-0.5.patch [bz#1123299]
- Resolves: bz#1123299
  (smbios table 0 vendor string should be Seabios (for rhel6 compatibility) [7.1+7.0.z])

* Sat Aug 02 2014 Miroslav Rezanina <mrezanin@redhat.com> - 1.7.5-2.el7
- seabios-Build-seabios-as-noarch.patch [bz#1118380]
- Resolves: bz#1118380
  (Seabios build required for ppc64)

* Wed May 28 2014 Gerd Hoffmann <kraxel@redhat.com> - 1.7.5-1.el7
- rebase to seabios 1.7.5

* Wed Feb 05 2014 Miroslav Rezanina <mrezanin@redhat.com> - 1.7.2.2-11.el7
- seabios-init_virtio_scsi-reset-the-HBA-before-freeing-its-vi.patch [bz#1013418]
- seabios-smbios-catch-zero-length-strings.patch [bz#1052837]
- seabios-resume-restore-piix-pm-config-registers-after-resume.patch [bz#1049860]
- seabios-pci-align-64bit-pci-regions-to-1G.patch [bz#1055832]
- seabios-pci-log-pci-windows.patch [bz#1055832]
- seabios-pci-improve-io-address-space-allocation.patch [bz#1055832]
- Resolves: bz#1013418
  (qemu-kvm with a virtio-scsi controler without devices attached quits after stop/cont in HMP/QMP)
- Resolves: bz#1049860
  (Guest agent command hang there after restore the guest from the save file)
- Resolves: bz#1052837
  (The wrong DMI structures could not be decoded while booting vm with -smbios params)
- Resolves: bz#1055832
  (can not see seabios GUI when boot with 155 virtio-blk-pci disks via pci-bridge)

* Mon Jan 13 2014 Miroslav Rezanina <mrezanin@redhat.com> - 1.7.2.2-10.el7
- Fixed seavgabios-bin obsoletes/provides [bz#1035452]
- Resolves: bz#1035452
  ( seavgabios-bin has bad obsoletes/provides for "vgabios")

* Mon Jan 13 2014 Miroslav Rezanina <mrezanin@redhat.com> - 1.7.2.2-8.el7
- seabios-vgabios-Fix-cirrus-memory-clear-on-mode-switch.patch [bz#979898]
- Resolves: bz#979898
  ([qemu-kvm]The win2k3-32 guest display is abnormal when using -vga cirrus)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.7.2.2-7
- Mass rebuild 2013-12-27

* Tue Dec 17 2013 Michal Novotny <minovotn@redhat.com> - seabios-1.7.2.2-6.el7
- seabios-biostables-support-looking-up-RSDP.patch [bz#1034877]
- seabios-romfile_loader-utility-to-patch-in-memory-ROM-files.patch [bz#1034877]
- seabios-acpi-load-and-link-tables-through-romfile-loader.patch [bz#1034877]
- Resolves: bz#1034877
  (export acpi tables to guests (seabios))

* Tue Dec 10 2013 Miroslav Rezanina <mrezanin@redhat.com> - 1.7.2.2-5.el7
- seabios-build-explicitly-set-ROM-size.patch [bz#1038604]
- Resolves: bz#1038604
  (make seabios 256k for rhel7 machine types)

* Tue Nov 05 2013 Miroslav Rezanina <mrezanin@redhat.com> - 1.7.2.2-4.el7
- seabios-Introduce-and-convert-pmm-code-to-use-standard-list-.patch [bz#947051]
- seabios-Fix-error-in-hlist_for_each_entry_safe-macro.patch [bz#947051]
- seabios-Another-fix-for-hlist_for_each_entry_safe.patch [bz#947051]
- seabios-uas-add-temporary-superspeed-stopgap.patch [bz#947051]
- seabios-usb-add-usb_update_pipe.patch [bz#947051]
- seabios-usb-add-xhci-support.patch [bz#947051]
- seabios-xhci-adaptions-for-old-rhel7-seabios-codebase.patch [bz#947051]
- seabios-allow-1TB-of-RAM.patch [bz#1016974]
- Resolves: bz#1016974
  ([HP 7.0 FEAT]: Increase KVM guest supported memory to 4TiB)
- Resolves: bz#947051
  ([RFE] implement xhci support in seabios)

* Tue Sep 24 2013 Miroslav Rezanina <mrezanin@redhat.com> - seabios-1.7.2.2-3.el7
- seabios-floppy-Introduce-struct-floppy_pio_s-for-floppy-PIO-.patch [bz#920140]
- seabios-floppy-Cleanup-floppy-irq-wait-handling.patch [bz#920140]
- seabios-floppy-Implement-media-format-sensing.patch [bz#920140]
- seabios-Place-rpm-version-info-into-version-banner.patch [bz#894979]
- seabios-ahci-add-missing-check-for-allocation-failure.patch [bz#1005747]
- Resolves: bz#1005747
  (fail to boot rhel7 guest with >126(21 ahci controller) ahci disks)
- Resolves: bz#894979
  (place rpm version info into version banner)
- Resolves: bz#920140
  (qemu-kvm emulation of 2.88M floppy fails)

* Wed Jun 26 2013 Miroslav Rezanina <mrezanin@redhat.com> - 1.7.2.2-2
- Disable options not used / not supported by RHEL-7 (rhbz 927582)
- Add pvpanic device driver (rhbz 967777)
- Obsolete vgabios (rhbz 976340)

* Tue Jun 04 2013 Miroslav Rezanina <mrezanin@redhat.com> - 1.7.2.2-1
- Rebase to 1.7.2.2

* Tue Dec 18 2012 Michal Novotny <minovotn@redhat.com> - 1.7.1-5
- Remove the cross compilation code as we compile it on x86_64 always

* Thu Dec  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> 1.7.1-4
- Root seabios package is noarch too because it only contains docs

* Fri Oct 19 2012 Cole Robinson <crobinso@redhat.com> - 1.7.1-3
- Add seavgabios subpackage

* Wed Oct 17 2012 Paolo Bonzini <pbonzini@redhat.com> - 1.7.1-2
- Build with cross compiler.  Resolves: #866664.

* Wed Sep 05 2012 Cole Robinson <crobinso@redhat.com> - 1.7.1-1
- Rebased to version 1.7.1
- Initial support for booting from USB attached scsi (USB UAS) drives
- USB EHCI 64bit controller support
- USB MSC multi-LUN device support
- Support for booting from LSI SCSI controllers on emulators
- Support for booting from AMD PCscsi controllers on emulators

* Mon Aug 13 2012 Richard W.M. Jones <rjones@redhat.com> - 1.7.0-4
- Modernise and tidy up the RPM.
- Allow debug versions of SeaBIOS to be built easily.

* Mon Aug 06 2012 Cole Robinson <crobinso@redhat.com> - 1.7.0-3
- Enable S3/S4 support for guests (it's an F18 feature after all)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 28 2012 Cole Robinson <crobinso@redhat.com> - 1.7.0-1
- Rebased to version 1.7.0
- Support for virtio-scsi
- Improved USB drive support
- Several USB controller bug fixes and improvements

* Wed Mar 28 2012 Paolo Bonzini <pbonzini@redhat.com> - 1.6.3-2
- Fix bugs in booting from host (or redirected) USB pen drives

* Wed Feb 08 2012 Justin M. Forbes <jforbes@redhat.com> - 1.6.3-1
- Update to 1.6.3 upstream
- Add virtio-scsi

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 05 2011 Justin M. Forbes <jforbes@redhat.com> - 0.6.2-3
- Stop advertising S3 and S4 in DSDT (bz#741375)
- incdule iasl buildreq

* Wed Jul 13 2011 Justin M. Forbes <jforbes@redhat.com> - 0.6.2-2
- Fix QXL bug in 0.6.2

* Wed Jul 13 2011 Justin M. forbes <jforbes@redhat.com> - 0.6.2-1
- Update to 0.6.2 upstream for a number of bugfixes

* Mon Feb 14 2011 Justin M. forbes <jforbes@redhat.com> - 0.6.1-1
- Update to 0.6.1 upstream for a number of bugfixes

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 10 2010 Justin M. Forbes <jforbes@redhat.com> 0.6.0-1
- Update seabios to latest stable so we can drop patches.

* Tue Apr 20 2010 Justin M. Forbes <jforbes@redhat.com> 0.5.1-2
- Ugly hacks to make package noarch and available for arch that cannot build it.
- Disable useless debuginfo

* Wed Mar 03 2010 Justin M. Forbes <jforbes@redhat.com> 0.5.1-1
- Update to 0.5.1 stable release
- Pick up patches required for current qemu

* Thu Jan 07 2010 Justin M. Forbes <jforbes@redhat.com> 0.5.1-0.1.20100108git669c991
- Created initial package
