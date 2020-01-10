# there are no binaries for -debuginfo in this package
%define debug_package %{nil}

Name:           seabios
Version:        0.6.1.2
%define pkgrelease 30
Release:        %{pkgrelease}%{?dist}
Summary:        Open-source legacy BIOS implementation

Group:          Applications/Emulators
License:        LGPLv3
URL:            http://www.coreboot.org/SeaBIOS
# Source0:        http://linuxtogo.org/~kevin/SeaBIOS/%{name}-%{version}.tar.gz
# The source for this package was pulled from upstream's git.  Use the
# following commands to generate the tarball:
# git archive --format=tar --prefix=seabios-0.5.1/ 669c991 | gzip > seabios-0.5.1-669c991.tar.gz
Source0:        http://www.linuxtogo.org/~kevin/SeaBIOS/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: python
BuildRequires: iasl
ExclusiveArch: x86_64

Patch1: seabios-1-Set-CONFIG_S3_RESUME_VGA_INIT-to-1.patch
Patch2: seabios-2-do-not-advertise-hpet-to-a-guest-OS.patch
Patch3: seabios-3-smbios-allow-vendor-manufacturer-version-product-nam.patch
Patch4: seabios-4-smbios-set-bios-vendor-version-fields-to-Seabios-0.5.patch
Patch5: seabios-5-smbios-set-system-manufacturer-product-name-to-Red-H.patch
Patch6: seabios-6-smbios-set-Type-3-chassis-manufacturer-information-t.patch
Patch7: seabios-7-fix-resume-from-S3-with-QXL-device.patch
Patch8: seabios-8-remove-acpi-dsdt.hex-file-from-source-tree.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch9: seabios-Create-separate-IPL-entry-for-each-CD-DVD-qemu-in-se.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch10: seabios-Provide-full-EDD-3.0-info-for-virtio-disk.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch11: seabios-Add-romfile_name-function.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch12: seabios-Add-strchr-function.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch13: seabios-Read-bootorder-file-into-memory.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch14: seabios-Add-romfile_loadfile-helper-function.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch15: seabios-Breakup-boot_setup-bootorder-code-into-its-own-funct.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch16: seabios-Support-qemu-based-romfile-wrappers-called-out-of-or.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch17: seabios-Track-the-source-of-each-optionrom-deployed.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch18: seabios-Populate-drive_g-desc-prior-to-calling-add_bcv_inter.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch19: seabios-Simplify-boot-ordering-by-building-an-inclusive-boot.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch20: seabios-Add-stubs-to-permit-devices-to-specify-their-boot-pr.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch21: seabios-Rename-add_ordered_drive-to-add_drive-and-use-in-map.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch22: seabios-Call-setup_translation-from-map_hd_drive.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch23: seabios-Simplify-keyboard-reading-code-in-the-interactive-bo.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch24: seabios-Don-t-access-drive_g-desc-from-boot_cdrom.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch25: seabios-Remove-Drives-global-struct-in-favor-of-independent-.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch26: seabios-Move-IPL.checkfloppysig-to-a-global-CheckFloppySig-i.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch27: seabios-Move-IPL.bev-to-static-variables-in-boot.c.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch28: seabios-Move-IPL.fw_bootorder-to-static-variables-in-boot.c.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch29: seabios-Minor-reorganization-of-some-of-the-boot_xxx-code-in.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch30: seabios-Remove-drive-desc-field.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch31: seabios-Use-bootprio_find_named_rom-for-ramdisk-and-cbfs-pay.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch32: seabios-Add-functions-for-boot-device-path-parsing.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch33: seabios-Extend-usb_pipe-to-track-the-controller-and-ports-of.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch34: seabios-Add-support-for-finding-the-boot-priority-of-USB-dri.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch35: seabios-re-nitialize-global-variables-on-reboot.patch
# For bz#643688 - Allow to specify boot order on qemu command line.
Patch36: seabios-Initialize-FloppyCount-and-CDCount-on-reboot.patch
# For bz#671544 - seabios: Too many devices are available for unplug in Windows XP (and we don't support that)
Patch37: seabios-acpi-add-_RMV-control-method-for-PCI-devices.patch
# For bz#673751 - Provide EDD3.0 info in accordance with T13 spec.
Patch38: seabios-support-T13-EDD3.0-spec.patch
# For bz#663240 - [WHQL] pwrtest failed in the job "CHAOS-Concurrent Hardware And OS test"
Patch39: seabios-lets-pretend-that-RTC-can-be-used-to-wakeup-from-S4.patch
# For bz#727328 - [RHEL6.1] - Windows2008 32-bit guest installation fails.
Patch40: seabios-increase-smp_mtrr-array-size-v2.patch
# For bz#736522 - Patch bios to remove S3/S4 for mitigate power management issues
Patch41: seabios-do-not-advertise-S4-S3-in-DSDT.patch
# For bz#733028 - Failed to reboot guest due to "key event queue full"
Patch42: seabios-usb-move-hid-initialization.patch
# For bz#630975 - KVM guest limited to 40bit of physical address space
Patch43: seabios-add-40-48-bit-RAM-range-to-seabios.patch
# For bz#750191 - Wrong LINT1/NMI ACPI and mptable descriptors
Patch44: seabios-Add-Local-APIC-NMI-Structure-to-ACPI-MADT-wa.patch
# For bz#750191 - Wrong LINT1/NMI ACPI and mptable descriptors
Patch45: seabios-fix-mptable-nmi-entry-was-Re-Qemu-devel-PATC.patch
# For bz#771946 - mask interrupts on S3 resume
Patch46: seabios-mask-interrupts-on-S3-resume.patch
# For bz#786142 - Windows guest shows HPET device, but qemu has none.
Patch47: seabios-Remove-HPET-from-DSDT.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch48: seabios-usb-fix-boot-paths.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch49: seabios-usb-uhci-reorganize-wait_qh-into-wait_pipe.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch50: seabios-usb-uhci-Be-sure-to-wrap-pipe-iobase-in-GET_FLATPTR.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch51: seabios-usb-uhci-fix-race-against-host-controller.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch52: seabios-usb-ehci-Fix-races-with-controller-on-updates-to-QH.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch53: seabios-usb-msc-support-commands-without-payload.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch54: seabios-usb-msc-add-usb_msc_send.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch55: seabios-usb-msc-move-READ-CAPACITY-to-usb_msc_init-fix-off-b.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch56: seabios-usb-msc-pass-drive-to-setup_drive_.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch57: seabios-usb-msc-support-WRITE-commands.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch58: seabios-Extract-space-trimming-code-from-ATA-and-use-in-USB-.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch59: seabios-usb-msc-rename-INQUIRY-types.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch60: seabios-cdrom-use-TEST-UNIT-READY-to-detect-ready-medium.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch61: seabios-usb-msc-go-through-TEST-UNIT-READY-for-hard-disks.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch62: seabios-usb-msc-move-common-scsi-code-to-blockcmd.c.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch63: seabios-usb-msc-move-cdb-dispatch-to-block.c.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch64: seabios-scsi-get-physical-chs-geometry-from-mode-page-0x04.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch65: seabios-always-specify-virtio-blk-rather-than-virtio.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch66: seabios-virtio-pci-include-pci.h-and-pci_regs.h.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch67: seabios-virtio-pci-introduce-vp_init_simple.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch68: seabios-virtio-pci-allocate-vq-in-vp_find_vq.patch
# For bz#782028 - [RFE] virtio-scsi boot support in SeaBIOS
Patch69: seabios-add-virtio-scsi-driver.patch
# For bz#761586 - Patch bios to restore S3/S4
Patch70: seabios-enable-S3-S4.patch
# For bz#802033 - kvm guest hangs on reboot after cpu-hotplug
# For bz#805168 - seabios should not spin on cpu if started cpu count != cmos value at 0x5f
Patch71: seabios-Halt-if-number-of-started-cpus-are-more-then-expecte.patch
# For bz#804933 - RTC wake up does not work with windows guests
Patch72: seabios-Drop-FIX_RTC-flag-from-FADT.patch
# For bz#801293 - fix boot from host or redirected USB pen drives
Patch73: seabios-scsi-do-not-send-MODE-SENSE-except-to-QEMU-disks.patch
# For bz#801293 - fix boot from host or redirected USB pen drives
Patch74: seabios-Use-OUT-mode-for-all-zero-byte-scsi-transfers.patch
# For bz#801293 - fix boot from host or redirected USB pen drives
Patch75: seabios-virtio-scsi-Fix-virtio-scsi-after-cdb_is_read-change.patch
# For bz#801293 - fix boot from host or redirected USB pen drives
Patch76: seabios-ata-send-TEST-UNIT-READY-correctly.patch
# For bz#808033 - kvm guest doesn't see all hotplugged vcpus when 'virsh setvcpus 64 --live ' or hot-plugged devices when they added fast enough
Patch77: seabios-Replace-level-gpe-event-with-edge-gpe-event-for-hot-.patch
# For bz#809797 - Create a seabios binary that supports s3/s4
Patch78: seabios-Revert-enable-S3-S4.patch
# For bz#810471 - boot fails while starting guest with sockets>62 and cores=1 and threads=1 option  and 10 virtio disks
Patch79: seabios-increase-f-segment-memory-pool.patch
# For bz#851245 - SeaBIOS: support non-contiguous APIC IDs
Patch80: seabios-report-real-I-O-APIC-ID-0-on-MADT-and-MP-table.patch
# For bz#851245 - SeaBIOS: support non-contiguous APIC IDs
Patch81: seabios-allow-CPUs-to-have-non-contiguous-Local-APIC-IDs.patch
# For bz#831273 - RFE: reboot VM if no bootable device found
Patch82: seabios-Add-romfile-code-to-assist-with-extract-integer-conf.patch
# For bz#831273 - RFE: reboot VM if no bootable device found
Patch83: seabios-Automatically-reboot-after-60-second-delay-on-failed.patch
# For bz#827500 - Config s3/s4 per VM - in seabios
Patch84: seabios-Revert-do-not-advertise-S4-S3-in-DSDT.patch
# For bz#827500 - Config s3/s4 per VM - in seabios
Patch85: seabios-acpi-generate-and-parse-mixed-asl-aml-listing.patch
# For bz#827500 - Config s3/s4 per VM - in seabios
Patch86: seabios-acpi-extract-aml-from-.lst.patch
# For bz#827500 - Config s3/s4 per VM - in seabios
Patch87: seabios-Fix-aml_name_string-to-recognize-block-name-modifier.patch
# For bz#827500 - Config s3/s4 per VM - in seabios
Patch88: seabios-Add-ACPI_EXTRACT_PKG_START-macro-parsing.patch
# For bz#827500 - Config s3/s4 per VM - in seabios
Patch89: seabios-acpi-add-ssdt-for-pci-hotplug.patch
# For bz#827500 - Config s3/s4 per VM - in seabios
Patch90: seabios-Get-system-state-configuration-from-QEMU-and-patch-D.patch
# For bz#854448 - add pmtimer support
Patch91: seabios-add-acpi-pmtimer-support.patch
# For bz#771616 - Too big value of QXL-VGA ram_size and vram_size cause VM paused (internal-error)
Patch92: seabios-pci-use-u64-for-pci-address-space-math.patch
# For bz#876250 - Display 'SMBIOS GUID' at the BIOS post screen.
Patch93: seabios-Use-coreboot-smbios-table-if-found.patch
# For bz#876250 - Display 'SMBIOS GUID' at the BIOS post screen.
Patch94: seabios-maininit-print-machine-UUID-under-seabios-version-me.patch
# For bz#876250 - Display 'SMBIOS GUID' at the BIOS post screen.
Patch95: seabios-display_uuid-fix-incomplete-check-after-the-loop.patch
# For bz#876250 - Display 'SMBIOS GUID' at the BIOS post screen.
Patch96: seabios-Minor-Separate-UUID-display-from-F12-boot-prompt.patch
# For bz#846519 - [virtio-win][scsi]Guest  BSOD (9F) during s3/s4 while guest running crystal benchmark
# For bz#846912 - [virtio-win][scsi] Disabling/enabling scsi driver stuck after S3/S4
# For bz#846912, - [virtio-win][scsi] Disabling/enabling scsi driver stuck after S3/S4
# For bz#846519 - [virtio-win][scsi]Guest  BSOD (9F) during s3/s4 while guest running crystal benchmark
Patch97: seabios-acpi-do-not-let-guest-OSes-enable-disable-the-SCI.patch
# For bz#888633 - don't boot from un-selected devices
Patch98: seabios-boot-Support-halt-in-the-boot-order-to-prevent-defau.patch
# For bz#963312 - [Hitachi 6.5 FEAT] (SeaBIOS) "virsh dump" support for automatic capturing and automatic actions after capturing.
Patch99: seabios-Add-pvpanic-device-driver.patch
# For bz#1129930 - fail to assign correct order for the boot device in seabios as we specified the bootindex in qemu-kvm cli(under the same virtio-scsi-pci)
Patch100: seabios-boot-Fix-boot-order-for-SCSI-target-lun-9.patch
# For bz#1131530 - Provide a platform agnostic approach to invoking the BIOS, boot menu, or other BIOS functions
Patch101: seabios-boot.c-delay-exiting-boot-if-menu-key-is-ESC.patch
# For bz#1131530 - Provide a platform agnostic approach to invoking the BIOS, boot menu, or other BIOS functions
Patch102: seabios-boot-allow-pressing-ESC-to-enter-the-menu.patch

%description
SeaBIOS is an open-source legacy BIOS implementation which can be used as
a coreboot payload. It implements the standard BIOS calling interfaces
that a typical x86 proprietary BIOS implements.


%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1

%build
chmod 755 tools/*.py
make VERSION="%{name}-%{version}-%{release}" DSDT_CPP_FLAGS=-DDSDT_PM


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/seabios
install -m 0644 out/bios.bin $RPM_BUILD_ROOT%{_datadir}/seabios


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/seabios/
%doc COPYING COPYING.LESSER README TODO
%{_datadir}/seabios/bios.bin



%changelog
* Wed Mar 18 2015 Jeff E. Nelson <jen@redhat.com> - 0.6.1.2-30.el6
- seabios-boot.c-delay-exiting-boot-if-menu-key-is-ESC.patch [bz#1131530]
- seabios-boot-allow-pressing-ESC-to-enter-the-menu.patch [bz#1131530]
- Resolves: bz#1131530
  (Provide a platform agnostic approach to invoking the BIOS, boot menu, or other BIOS functions)

* Tue Dec 23 2014 Jeff E. Nelson <jen@redhat.com> - 0.6.1.2-29.el6
- seabios-boot-Fix-boot-order-for-SCSI-target-lun-9.patch [bz#1129930]
- Resolves: bz#1129930
  (fail to assign correct order for the boot device in seabios as we specified the bootindex in qemu-kvm cli(under the same virtio-scsi-pci))

* Thu May 30 2013 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-28.el6
- seabios-Add-pvpanic-device-driver.patch [bz#963312]
- Resolves: bz#963312
  ([Hitachi 6.5 FEAT] (SeaBIOS) "virsh dump" support for automatic capturing and automatic actions after capturing.)

* Tue Apr 16 2013 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-27.el6
- seabios-Use-coreboot-smbios-table-if-found.patch [bz#876250]
- seabios-maininit-print-machine-UUID-under-seabios-version-me.patch [bz#876250]
- seabios-display_uuid-fix-incomplete-check-after-the-loop.patch [bz#876250]
- seabios-Minor-Separate-UUID-display-from-F12-boot-prompt.patch [bz#876250]
- seabios-acpi-do-not-let-guest-OSes-enable-disable-the-SCI.patch [bz#846912]
- seabios-boot-Support-halt-in-the-boot-order-to-prevent-defau.patch [bz#888633]
- Resolves: bz#846912
  ([virtio-win][scsi] Disabling/enabling scsi driver stuck after S3/S4)
- Resolves: bz#876250
  (Display 'SMBIOS GUID' at the BIOS post screen.)
- Resolves: bz#888633
  (don't boot from un-selected devices)

* Mon Dec 10 2012 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-26.el6
- seabios-pci-use-u64-for-pci-address-space-math.patch [bz#771616]
- Resolves: bz#771616
  (Too big value of QXL-VGA ram_size and vram_size cause VM paused (internal-error))

* Mon Oct 15 2012 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-25.el6
- Fix data in the spec file
- Related: bz#839674
  (Revert back to a single seabios binary once s3/s4 configuration is in)

* Mon Oct 15 2012 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-24.el6
- revert-seabios-to-single-binary [bz#839674]
- Resolves: bz#839674
  (Revert back to a single seabios binary once s3/s4 configuration is in)

* Thu Sep 27 2012 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.6.1.2-23.el6
- seabios-add-acpi-pmtimer-support.patch [bz#854448]
- Resolves: bz#854448
  (add pmtimer support)

* Tue Sep 11 2012 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-21.el6
- seabios-Revert-do-not-advertise-S4-S3-in-DSDT.patch [bz#827500]
- seabios-acpi-generate-and-parse-mixed-asl-aml-listing.patch [bz#827500]
- seabios-acpi-extract-aml-from-.lst.patch [bz#827500]
- seabios-Fix-aml_name_string-to-recognize-block-name-modifier.patch [bz#827500]
- seabios-Add-ACPI_EXTRACT_PKG_START-macro-parsing.patch [bz#827500]
- seabios-acpi-add-ssdt-for-pci-hotplug.patch [bz#827500]
- seabios-Get-system-state-configuration-from-QEMU-and-patch-D.patch [bz#827500]
- Resolves: bz#827500
  (Config s3/s4 per VM - in seabios)

* Thu Sep 06 2012 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-20.el6
- seabios-Add-romfile-code-to-assist-with-extract-integer-conf.patch [bz#831273]
- seabios-Automatically-reboot-after-60-second-delay-on-failed.patch [bz#831273]
- Resolves: bz#831273
  (RFE: reboot VM if no bootable device found)

* Tue Aug 28 2012 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-19.el6_3
- seabios-report-real-I-O-APIC-ID-0-on-MADT-and-MP-table.patch [bz#851245]
- seabios-allow-CPUs-to-have-non-contiguous-Local-APIC-IDs.patch [bz#851245]
- Resolves: bz#851245
  (SeaBIOS: support non-contiguous APIC IDs)

* Wed Apr 18 2012 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-19.el6
- seabios-increase-f-segment-memory-pool.patch [bz#810471]
- Resolves: bz#810471
  (boot fails while starting guest with sockets>62 and cores=1 and threads=1 option  and 10 virtio disks)

* Wed Apr 11 2012 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.6.1.2-18.el6
- seabios-Revert-enable-S3-S4.patch [bz#809797]
- add S3/S4 seabios binary [bz#809797]
- Resolves: bz#809797
  (Create a seabios binary that supports s3/s4)

* Tue Apr 10 2012 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-17.el6
- seabios-Replace-level-gpe-event-with-edge-gpe-event-for-hot-.patch [bz#808033]
- Resolves: bz#808033
  (kvm guest doesn't see all hotplugged vcpus when 'virsh setvcpus 64 --live ' or hot-plugged devices when they added fast enough)

* Fri Mar 30 2012 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.6.1.2-16.el6
- Restore seabios-Drop-FIX_RTC-flag-from-FADT.patch [bz#804933]
- Resolves: bz#804933
  (RTC wake up does not work with windows guests)

* Thu Mar 22 2012 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-15.el6
- seabios-scsi-do-not-send-MODE-SENSE-except-to-QEMU-disks.patch [bz#801293]
- seabios-Use-OUT-mode-for-all-zero-byte-scsi-transfers.patch [bz#801293]
- seabios-virtio-scsi-Fix-virtio-scsi-after-cdb_is_read-change.patch [bz#801293]
- seabios-ata-send-TEST-UNIT-READY-correctly.patch [bz#801293]
- Resolves: bz#801293
  (fix boot from host or redirected USB pen drives)

* Wed Mar 21 2012 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.6.1.2-14.el6
- seabios-Halt-if-number-of-started-cpus-are-more-then-expecte.patch [bz#802033 bz#805168]
- seabios-Drop-FIX_RTC-flag-from-FADT.patch [bz#804933]
- Resolves: bz#802033
  (kvm guest hangs on reboot after cpu-hotplug)
- Resolves: bz#804933
  (RTC wake up does not work with windows guests)
- Resolves: bz#805168
  (seabios should not spin on cpu if started cpu count != cmos value at 0x5f)

* Mon Mar 19 2012 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-13.el6
- seabios-enable-S3-S4.patch [bz#761586]
- Resolves: bz#761586
  (Patch bios to restore S3/S4)
- Resolves: bz#804603
  (specfile: Put seabios version into banner)

* Tue Mar 06 2012 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-12.el6
- seabios-usb-fix-boot-paths.patch [bz#782028]
- seabios-usb-uhci-reorganize-wait_qh-into-wait_pipe.patch [bz#782028]
- seabios-usb-uhci-Be-sure-to-wrap-pipe-iobase-in-GET_FLATPTR.patch [bz#782028]
- seabios-usb-uhci-fix-race-against-host-controller.patch [bz#782028]
- seabios-usb-ehci-Fix-races-with-controller-on-updates-to-QH.patch [bz#782028]
- seabios-usb-msc-support-commands-without-payload.patch [bz#782028]
- seabios-usb-msc-add-usb_msc_send.patch [bz#782028]
- seabios-usb-msc-move-READ-CAPACITY-to-usb_msc_init-fix-off-b.patch [bz#782028]
- seabios-usb-msc-pass-drive-to-setup_drive_.patch [bz#782028]
- seabios-usb-msc-support-WRITE-commands.patch [bz#782028]
- seabios-Extract-space-trimming-code-from-ATA-and-use-in-USB-.patch [bz#782028]
- seabios-usb-msc-rename-INQUIRY-types.patch [bz#782028]
- seabios-cdrom-use-TEST-UNIT-READY-to-detect-ready-medium.patch [bz#782028]
- seabios-usb-msc-go-through-TEST-UNIT-READY-for-hard-disks.patch [bz#782028]
- seabios-usb-msc-move-common-scsi-code-to-blockcmd.c.patch [bz#782028]
- seabios-usb-msc-move-cdb-dispatch-to-block.c.patch [bz#782028]
- seabios-scsi-get-physical-chs-geometry-from-mode-page-0x04.patch [bz#782028]
- seabios-always-specify-virtio-blk-rather-than-virtio.patch [bz#782028]
- seabios-virtio-pci-include-pci.h-and-pci_regs.h.patch [bz#782028]
- seabios-virtio-pci-introduce-vp_init_simple.patch [bz#782028]
- seabios-virtio-pci-allocate-vq-in-vp_find_vq.patch [bz#782028]
- seabios-add-virtio-scsi-driver.patch [bz#782028]
- Resolves: bz#782028
  ([RFE] virtio-scsi boot support in SeaBIOS)

* Fri Feb 17 2012 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-10.el6
- seabios-Remove-HPET-from-DSDT.patch [bz#786142]
- Resolves: bz#786142
  (Windows guest shows HPET device, but qemu has none.)

* Mon Feb 13 2012 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-9.el6
- seabios-mask-interrupts-on-S3-resume.patch [bz#771946]
- Resolves: bz#771946
  (mask interrupts on S3 resume)

* Tue Nov 01 2011 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-8.el6
- seabios-Add-Local-APIC-NMI-Structure-to-ACPI-MADT-wa.patch [bz#750191]
- seabios-fix-mptable-nmi-entry-was-Re-Qemu-devel-PATC.patch [bz#750191]
- Resolves: bz#750191
  (Wrong LINT1/NMI ACPI and mptable descriptors)

* Tue Oct 18 2011 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-7.el6
- seabios-add-40-48-bit-RAM-range-to-seabios.patch [bz#630975]
- Resolves: bz#630975
  (KVM guest limited to 40bit of physical address space)

* Wed Oct 05 2011 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-6.el6
- seabios-usb-move-hid-initialization.patch [bz#733028]
- Resolves: bz#733028
  (Failed to reboot guest due to "key event queue full")

* Wed Sep 21 2011 Michal Novotny <minovotn@redhat.com> - seabios-0.6.1.2-5.el6
- seabios-do-not-advertise-S4-S3-in-DSDT.patch [bz#736522]
- Resolves: bz#736522
  (Patch bios to remove S3/S4 for mitigate power management issues)

* Tue Aug 02 2011 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.6.1.2-4.el6
- seabios-increase-smp_mtrr-array-size-v2.patch [bz#727328]
- Resolves: bz#727328
  ([RHEL6.1] - Windows2008 32-bit guest installation fails.)

* Thu Feb 03 2011 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.6.1.2-3.el6
- seabios-support-T13-EDD3.0-spec.patch [bz#673751]
- seabios-lets-pretend-that-RTC-can-be-used-to-wakeup-from-S4.patch [bz#663240]
- Resolves: bz#663240
  ([WHQL] pwrtest failed in the job "CHAOS-Concurrent Hardware And OS test")
- Resolves: bz#673751
  (Provide EDD3.0 info in accordance with T13 spec.)

* Thu Jan 27 2011 Luiz Capitulino <lcapitulino@redhat.com> - seabios-0.6.1.2-2.el6
- seabios-Create-separate-IPL-entry-for-each-CD-DVD-qemu-in-se.patch [bz#643688]
- seabios-Provide-full-EDD-3.0-info-for-virtio-disk.patch [bz#643688]
- seabios-Add-romfile_name-function.patch [bz#643688]
- seabios-Add-strchr-function.patch [bz#643688]
- seabios-Read-bootorder-file-into-memory.patch [bz#643688]
- seabios-Add-romfile_loadfile-helper-function.patch [bz#643688]
- seabios-Breakup-boot_setup-bootorder-code-into-its-own-funct.patch [bz#643688]
- seabios-Support-qemu-based-romfile-wrappers-called-out-of-or.patch [bz#643688]
- seabios-Track-the-source-of-each-optionrom-deployed.patch [bz#643688]
- seabios-Populate-drive_g-desc-prior-to-calling-add_bcv_inter.patch [bz#643688]
- seabios-Simplify-boot-ordering-by-building-an-inclusive-boot.patch [bz#643688]
- seabios-Add-stubs-to-permit-devices-to-specify-their-boot-pr.patch [bz#643688]
- seabios-Rename-add_ordered_drive-to-add_drive-and-use-in-map.patch [bz#643688]
- seabios-Call-setup_translation-from-map_hd_drive.patch [bz#643688]
- seabios-Simplify-keyboard-reading-code-in-the-interactive-bo.patch [bz#643688]
- seabios-Don-t-access-drive_g-desc-from-boot_cdrom.patch [bz#643688]
- seabios-Remove-Drives-global-struct-in-favor-of-independent-.patch [bz#643688]
- seabios-Move-IPL.checkfloppysig-to-a-global-CheckFloppySig-i.patch [bz#643688]
- seabios-Move-IPL.bev-to-static-variables-in-boot.c.patch [bz#643688]
- seabios-Move-IPL.fw_bootorder-to-static-variables-in-boot.c.patch [bz#643688]
- seabios-Minor-reorganization-of-some-of-the-boot_xxx-code-in.patch [bz#643688]
- seabios-Remove-drive-desc-field.patch [bz#643688]
- seabios-Use-bootprio_find_named_rom-for-ramdisk-and-cbfs-pay.patch [bz#643688]
- seabios-Add-functions-for-boot-device-path-parsing.patch [bz#643688]
- seabios-Extend-usb_pipe-to-track-the-controller-and-ports-of.patch [bz#643688]
- seabios-Add-support-for-finding-the-boot-priority-of-USB-dri.patch [bz#643688]
- seabios-re-nitialize-global-variables-on-reboot.patch [bz#643688]
- seabios-Initialize-FloppyCount-and-CDCount-on-reboot.patch [bz#643688]
- seabios-acpi-add-_RMV-control-method-for-PCI-devices.patch [bz#671544]
- Resolves: bz#643688
  (Allow to specify boot order on qemu command line.)
- Resolves: bz#671544
  (seabios: Too many devices are available for unplug in Windows XP (and we don't support that))

* Tue Jan 11 2011 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.6.1.2-1.el6
- Update to upstream seabios-0.6.1.2 (from git tag rel-0.6.1.2)
- Resolves: bz#666922
  (Rebase seabios to latest upstream version)
- Resolves: bz#668707
  (Guest moved used index from 0 to 580" occur when guest load to grub during reboot)

* Thu Jan 06 2011 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.6.1-1.el6
- Update to upstream seabios-0.6.1
- Resolves: bz#666922
  (Rebase seabios to latest upstream version)

* Wed Aug 18 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-3.el6
- seabios-add-write-support-to-virtio-blk.patch [bz#607500]
- Resolves: bz#607500
  (An unexpected error occurs during winxp installation with virtio disk.)

* Tue Jun 29 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-2.el6
- seabios-Support-USB-keyboard-auto-repeat.patch [bz#561324]
- seabios-Support-USB-interrupt-schedules-on-OHCI-and-UHCI.patch [bz#561324]
- Resolves: bz#561324
  (USB keyboard misbehaves with BIOS driver)

* Mon Jun 28 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-1.el6
- seabios-Update-version-to-0.5.1.patch [bz#606411]
- Resolves: bz#606411
  (Update version info to match upstream 0.5.1)

* Wed Jun 23 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.15.20100108git669c991.el6
- seabios-remove-acpi-dsdt.hex-file-from-source-tree.patch [bz#603677]
- Add BuildRequires: iasl
- Resolves: bz#603677
  (Windows7 hangs during resume from S3 when using QXL device)

* Mon Jun 21 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.14.20100108git669c991.el6
- seabios-fix-resume-from-S3-with-QXL-device.patch [bz#603677]
- Resolves: bz#603677
  (Windows7 hangs during resume from S3 when using QXL device)

* Mon Jun 21 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.13.20100108git669c991.el6
- seabios-smbios-allow-vendor-manufacturer-version-product-nam.patch [bz#593317]
- seabios-smbios-set-bios-vendor-version-fields-to-Seabios-0.5.patch [bz#593317]
- seabios-smbios-set-system-manufacturer-product-name-to-Red-H.patch [bz#593317]
- seabios-smbios-set-Type-3-chassis-manufacturer-information-t.patch [bz#593317]
- Resolves: bz#593317
  (seabios: SMBIOS data is different from that shown in RHEL5, even with -M rhel5.4.0)

* Wed Jun 16 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.12.20100108git669c991.el6
- seabios-do-not-advertise-hpet-to-a-guest-OS.patch [bz#602177]
- Resolves: bz#602177
  (Failed to install rhel3.9-64 guest)

* Wed Jun 09 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.11.20100108git669c991.el6
- seabios-Support-for-booting-from-virtio-disks-reapply.patch [bz#578752]
- seabios-zero-memory-before-use.patch [bz#578752 bz#596881]
- Resolves: bz#578752
  (Need to show "hard disk" menu item when pressing F12 during POST)
- Related: bz#596881
  (Unable to install RHEL virtual machines)

* Wed Jun 02 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.10.20100108git669c991.el6
- seabios-Revert-Support-for-booting-from-virtio-disks.patch [bz#578752 bz#596881]
- Resolves: bz#596881
  (Unable to install RHEL virtual machines)
- Related: bz#578752
  (Need to show "hard disk" menu item when pressing F12 during POST)

* Wed May 19 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.9.20100108git669c991.el6
- seabios-Support-for-booting-from-virtio-disks.patch [bz#578752]
- Resolves: bz#578752
  (Need to show "hard disk" menu item when pressing F12 during POST)

* Mon May 17 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.8.20100108git669c991.el6
- seabios-smbios-avoid-counting-io-hole-as-ram.patch [bz#561290]
- Resolves: bz#561290
  (`dmidecode' shows wrong memory which is assigned to VM.)

* Thu Apr 29 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.7.20100108git669c991.el6
- Disable -debuginfo package generation
- Related: bz#564482
  (empty debuginfo packages)

* Thu Apr 22 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.6.20100108git669c991.el6
- seabios-Set-CONFIG_S3_RESUME_VGA_INIT-to-1.patch [bz#567910]
- Resolves: bz#567910
  (Make seabios configuration parameter CONFIG_S3_RESUME_VGA_INIT default to 1)

* Tue Mar 16 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.5.20100108git669c991.el6
- seabios-Fix-PkgLength-calculation-for-the-SSDT.patch [bz#571553]
- Resolves: bz#571553
  (Backport 0.5.1-stable seabios.git fixes)

* Tue Mar 9 2010 Glauber Costa <glommer@redhat.com> - seabios-0.5.1-0.4.20100108git669c991.el6
- Go back to using 0xf0000000 for PCI memory start
- Resolves: bz#571553
  (Backport 0.5.1-stable seabios.git fixes)

* Wed Jan 13 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.3.20100108git669c991.el6
- Build only on x86_64
- Resolves: bz#554866
  (seabios should not be shipped on i686/ppc64/s390x, only x86_64)

* Tue Jan 12 2010 Eduardo Habkost <ehabkost@redhat.com> - seabios-0.5.1-0.2.20100108git669c991.el6
- Regenerate tarball from git (it contained an extra .pyc file that doesn't belong there)

* Thu Jan 07 2010 Justin M. Forbes <jforbes@redhat.com> 0.5.1-0.1.20100108git669c991
- Created initial package
