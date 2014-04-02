#3.2. Top-level Files within the proc File System

Below is a list of some of the more useful virtual files in the top-level of the /proc/ directory.

####Note
In most cases, the content of the files listed in this section are not the same as those installed on your machine. This is because much of the information is specific to the hardware on which Red Hat Enterprise Linux is running for this documentation effort.

###3.2.1. /proc/apm (no Ubuntu)

This file provides information about the state of the Advanced Power Management (APM) system and is used by the apm command. If a system with no battery is connected to an AC power source, this virtual file would look similar to the following:

BUG: apm command and folder are not supported in Ubuntu

1.16 1.2 0x07 0x01 0xff 0x80 -1% -1 ?
Running the apm -v command on such a system results in output similar to the following:

APM BIOS 1.2 (kernel driver 1.16ac) AC on-line, no system battery
For systems which do not use a battery as a power source, apm is able do little more than put the machine in standby mode. The apm command is much more useful on laptops. For example, the following output is from the command cat /proc/apm on a laptop while plugged into a power outlet:

1.16 1.2 0x03 0x01 0x03 0x09 100% -1 ?

When the same laptop is unplugged from its power source for a few minutes, the content of the apm file changes to something like the following:

1.16 1.2 0x03 0x00 0x00 0x01 99% 1792 min

The apm -v command now yields more useful data, such as the following:

APM BIOS 1.2 (kernel driver 1.16) AC off-line, battery status high: 99% (1 day, 5:52)

##3.2.2. /proc/buddyinfo

This file is used primarily for diagnosing memory fragmentation issues. Using the buddy algorithm, each column represents the number of pages of a certain order (a certain size) that are available at any given time. For example, for zone DMA (direct memory access), there are 90 of 2^(0*PAGE_SIZE) chunks of memory. Similarly, there are 6 of 2^(1*PAGE_SIZE) chunks, and 2 of 2^(2*PAGE_SIZE) chunks of memory available.

The DMA row references the first 16 MB on a system, the HighMem row references all memory greater than 4 GB on a system, and the Normal row references all memory in between.

The following is an example of the output typical of /proc/buddyinfo:

Node 0, zone      DMA     90      6      2      1      1      ... 
Node 0, zone   Normal   1650    310      5      0      0      ... 
Node 0, zone  HighMem      2      0      0      1      1      ...

##3.2.3. /proc/cmdline

This file shows the parameters passed to the kernel at the time it is started. A sample /proc/cmdline file looks like the following:

ro root=/dev/VolGroup00/LogVol00 rhgb quiet 3
This tells us that the kernel is mounted read-only (signified by (ro)), located on the first logical volume (LogVol00) of the first volume group (/dev/VolGroup00). LogVol00 is the equivalent of a disk partition in a non-LVM system (Logical Volume Management), just as /dev/VolGroup00 is similar in concept to /dev/hda1, but much more extensible.

For more information on LVM used in Red Hat Enterprise Linux, refer to http://www.tldp.org/HOWTO/LVM-HOWTO/index.html.

Next, rhgb signals that the rhgb package has been installed, and graphical booting is supported, assuming /etc/inittab shows a default runlevel set to id:5:initdefault:.

Finally, quiet indicates all verbose kernel messages are suppressed at boot time.

3.2.4. /proc/cpuinfo

This virtual file identifies the type of processor used by your system. The following is an example of the output typical of /proc/cpuinfo:

processor	: 0 
vendor_id	: GenuineIntel 
cpu family	: 15 
model		: 2 
model name	: Intel(R) Xeon(TM) CPU 2.40GHz 
stepping	: 7 cpu 
MHz		: 2392.371 
cache size	: 512 KB 
physical id	: 0 
siblings	: 2 
runqueue	: 0 
fdiv_bug	: no 
hlt_bug		: no 
f00f_bug	: no 
coma_bug	: no 
fpu		: yes 
fpu_exception	: yes 
cpuid level	: 2 
wp		: yes 
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca  cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm 
bogomips	: 4771.02
processor — Provides each processor with an identifying number. On systems that have one processor, only a 0 is present.

cpu family — Authoritatively identifies the type of processor in the system. For an Intel-based system, place the number in front of "86" to determine the value. This is particularly helpful for those attempting to identify the architecture of an older system such as a 586, 486, or 386. Because some RPM packages are compiled for each of these particular architectures, this value also helps users determine which packages to install.

model name — Displays the common name of the processor, including its project name.

cpu MHz — Shows the precise speed in megahertz for the processor to the thousandths decimal place.

cache size — Displays the amount of level 2 memory cache available to the processor.

siblings — Displays the number of sibling CPUs on the same physical CPU for architectures which use hyper-threading.

flags — Defines a number of different qualities about the processor, such as the presence of a floating point unit (FPU) and the ability to process MMX instructions.

3.2.5. /proc/crypto

This file lists all installed cryptographic ciphers used by the Linux kernel, including additional details for each. A sample /proc/crypto file looks like the following:

name         : sha1 
module       : kernel 
type         : digest 
blocksize    : 64 
digestsize   : 20   
name         : md5 
module       : md5 
type         : digest 
blocksize    : 64 
digestsize   : 16
3.2.6. /proc/devices

This file displays the various character and block devices currently configured (not including devices whose modules are not loaded). Below is a sample output from this file:

Character devices:  
  1 mem   
  4 /dev/vc/0   
  4 tty   
  4 ttyS   
  5 /dev/tty   
  5 /dev/console   
  5 /dev/ptmx   
  7 vcs  
  10 misc  
  13 input  
  29 fb  
  36 netlink 
  128 ptm 
  136 pts 
  180 usb   
  
Block devices:   
  1 ramdisk   
  3 ide0   
  9 md  
  22 ide1 
  253 device-mapper 
  254 mdp
The output from /proc/devices includes the major number and name of the device, and is broken into two major sections: Character devices and Block devices.

Character devices are similar to block devices, except for two basic differences:

Character devices do not require buffering. Block devices have a buffer available, allowing them to order requests before addressing them. This is important for devices designed to store information — such as hard drives — because the ability to order the information before writing it to the device allows it to be placed in a more efficient order.

Character devices send data with no preconfigured size. Block devices can send and receive information in blocks of a size configured per device.

For more information about devices refer to the following installed documentation:

/usr/share/doc/kernel-doc-<version>/Documentation/devices.txt
3.2.7. /proc/dma

This file contains a list of the registered ISA DMA channels in use. A sample /proc/dma files looks like the following:

4: cascade
3.2.8. /proc/execdomains

This file lists the execution domains currently supported by the Linux kernel, along with the range of personalities they support.

0-0   Linux           [kernel]
Think of execution domains as the "personality" for an operating system. Because other binary formats, such as Solaris, UnixWare, and FreeBSD, can be used with Linux, programmers can change the way the operating system treats system calls from these binaries by changing the personality of the task. Except for the PER_LINUX execution domain, different personalities can be implemented as dynamically loadable modules.

3.2.9. /proc/fb

This file contains a list of frame buffer devices, with the frame buffer device number and the driver that controls it. Typical output of /proc/fb for systems which contain frame buffer devices looks similar to the following:

0 VESA VGA
3.2.10. /proc/filesystems

This file displays a list of the file system types currently supported by the kernel. Sample output from a generic /proc/filesystems file looks similar to the following:

nodev   sysfs 
nodev   rootfs 
nodev   bdev 
nodev   proc 
nodev   sockfs 
nodev   binfmt_misc 
nodev   usbfs 
nodev   usbdevfs 
nodev   futexfs 
nodev   tmpfs 
nodev   pipefs 
nodev   eventpollfs 
nodev   devpts         
	ext2 
nodev   ramfs 
nodev   hugetlbfs         
	iso9660 
nodev   mqueue         
	ext3 
nodev   rpc_pipefs 
nodev   autofs
The first column signifies whether the file system is mounted on a block device. Those beginning with nodev are not mounted on a device. The second column lists the names of the file systems supported.

The mount command cycles through the file systems listed here when one is not specified as an argument.

3.2.11. /proc/interrupts

This file records the number of interrupts per IRQ on the x86 architecture. A standard /proc/interrupts looks similar to the following:

  CPU0          
  0:   80448940          XT-PIC  timer   
  1:     174412          XT-PIC  keyboard   
  2:          0          XT-PIC  cascade   
  8:          1          XT-PIC  rtc  
 10:     410964          XT-PIC  eth0  
 12:      60330          XT-PIC  PS/2 Mouse  
 14:    1314121          XT-PIC  ide0  
 15:    5195422          XT-PIC  ide1 
NMI:          0  
ERR:          0
For a multi-processor machine, this file may look slightly different:

	   CPU0       CPU1          
  0: 1366814704          0          XT-PIC  timer   
  1:        128        340    IO-APIC-edge  keyboard   
  2:          0          0          XT-PIC  cascade   
  8:          0          1    IO-APIC-edge  rtc  
 12:       5323       5793    IO-APIC-edge  PS/2 Mouse  
 13:          1          0          XT-PIC  fpu  
 16:   11184294   15940594   IO-APIC-level  Intel EtherExpress Pro 10/100 Ethernet  
 20:    8450043   11120093   IO-APIC-level  megaraid  
 30:      10432      10722   IO-APIC-level  aic7xxx  
 31:         23         22   IO-APIC-level  aic7xxx 
NMI:          0 
ERR:          0
The first column refers to the IRQ number. Each CPU in the system has its own column and its own number of interrupts per IRQ. The next column reports the type of interrupt, and the last column contains the name of the device that is located at that IRQ.

Each of the types of interrupts seen in this file, which are architecture-specific, mean something different. For x86 machines, the following values are common:

XT-PIC — This is the old AT computer interrupts.

IO-APIC-edge — The voltage signal on this interrupt transitions from low to high, creating an edge, where the interrupt occurs and is only signaled once. This kind of interrupt, as well as the IO-APIC-level interrupt, are only seen on systems with processors from the 586 family and higher.

IO-APIC-level — Generates interrupts when its voltage signal is high until the signal is low again.

3.2.12. /proc/iomem

This file shows you the current map of the system's memory for each physical device:

00000000-0009fbff : System RAM
0009fc00-0009ffff : reserved 
000a0000-000bffff : Video RAM area
000c0000-000c7fff : Video ROM 
000f0000-000fffff : System ROM
00100000-07ffffff : System RAM   
00100000-00291ba8 : Kernel code
00291ba9-002e09cb : Kernel data 
e0000000-e3ffffff : VIA Technologies, Inc. VT82C597 [Apollo VP3] e4000000-e7ffffff : PCI Bus #01   
e4000000-e4003fff : Matrox Graphics, Inc. MGA G200 AGP   
e5000000-e57fffff : Matrox Graphics, Inc. MGA G200 AGP 
e8000000-e8ffffff : PCI Bus #01   
e8000000-e8ffffff : Matrox Graphics, Inc. MGA G200 AGP 
ea000000-ea00007f : Digital Equipment Corporation DECchip 21140 [FasterNet]
ea000000-ea00007f : tulip ffff0000-ffffffff : reserved
The first column displays the memory registers used by each of the different types of memory. The second column lists the kind of memory located within those registers and displays which memory registers are used by the kernel within the system RAM or, if the network interface card has multiple Ethernet ports, the memory registers assigned for each port.

3.2.13. /proc/ioports

The output of /proc/ioports provides a list of currently registered port regions used for input or output communication with a device. This file can be quite long. The following is a partial listing:

0000-001f : dma1 
0020-003f : pic1 
0040-005f : timer 
0060-006f : keyboard 
0070-007f : rtc 
0080-008f : dma page reg 
00a0-00bf : pic2 
00c0-00df : dma2 
00f0-00ff : fpu 
0170-0177 : ide1 
01f0-01f7 : ide0 
02f8-02ff : serial(auto) 
0376-0376 : ide1 
03c0-03df : vga+ 
03f6-03f6 : ide0 
03f8-03ff : serial(auto) 
0cf8-0cff : PCI conf1 
d000-dfff : PCI Bus #01 
e000-e00f : VIA Technologies, Inc. Bus Master IDE   
e000-e007 : ide0   
e008-e00f : ide1 
e800-e87f : Digital Equipment Corporation DECchip 21140 [FasterNet]   
e800-e87f : tulip
The first column gives the I/O port address range reserved for the device listed in the second column.

3.2.14. /proc/kcore

This file represents the physical memory of the system and is stored in the core file format. Unlike most /proc/ files, kcore displays a size. This value is given in bytes and is equal to the size of the physical memory (RAM) used plus 4 KB.

The contents of this file are designed to be examined by a debugger, such as gdb, and is not human readable.

Caution
Do not view the /proc/kcore virtual file. The contents of the file scramble text output on the terminal. If this file is accidentally viewed, press Ctrl-C to stop the process and then type reset to bring back the command line prompt.
3.2.15. /proc/kmsg

This file is used to hold messages generated by the kernel. These messages are then picked up by other programs, such as /sbin/klogd or /bin/dmesg.

3.2.16. /proc/loadavg

This file provides a look at the load average in regard to both the CPU and IO over time, as well as additional data used by uptime and other commands. A sample /proc/loadavg file looks similar to the following:

0.20 0.18 0.12 1/80 11206
The first three columns measure CPU and IO utilization of the last one, five, and 10 minute periods. The fourth column shows the number of currently running processes and the total number of processes. The last column displays the last process ID used.

3.2.17. /proc/locks

This file displays the files currently locked by the kernel. The contents of this file contain internal kernel debugging data and can vary tremendously, depending on the use of the system. A sample /proc/locks file for a lightly loaded system looks similar to the following:

1: POSIX  ADVISORY  WRITE 3568 fd:00:2531452 0 EOF 
2: FLOCK  ADVISORY  WRITE 3517 fd:00:2531448 0 EOF 
3: POSIX  ADVISORY  WRITE 3452 fd:00:2531442 0 EOF 
4: POSIX  ADVISORY  WRITE 3443 fd:00:2531440 0 EOF 
5: POSIX  ADVISORY  WRITE 3326 fd:00:2531430 0 EOF 
6: POSIX  ADVISORY  WRITE 3175 fd:00:2531425 0 EOF 
7: POSIX  ADVISORY  WRITE 3056 fd:00:2548663 0 EOF
Each lock has its own line which starts with a unique number. The second column refers to the class of lock used, with FLOCK signifying the older-style UNIX file locks from a flock system call and POSIX representing the newer POSIX locks from the lockf system call.

The third column can have two values: ADVISORY or MANDATORY. ADVISORY means that the lock does not prevent other people from accessing the data; it only prevents other attempts to lock it. MANDATORY means that no other access to the data is permitted while the lock is held. The fourth column reveals whether the lock is allowing the holder READ or WRITE access to the file. The fifth column shows the ID of the process holding the lock. The sixth column shows the ID of the file being locked, in the format of MAJOR-DEVICE:MINOR-DEVICE:INODE-NUMBER. The seventh and eighth column shows the start and end of the file's locked region.

3.2.18. /proc/mdstat

This file contains the current information for multiple-disk, RAID configurations. If the system does not contain such a configuration, then /proc/mdstat looks similar to the following:

Personalities :  read_ahead not set unused devices: <none>
This file remains in the same state as seen above unless a software RAID or md device is present. In that case, view /proc/mdstat to find the current status of mdX RAID devices.

The /proc/mdstat file below shows a system with its md0 configured as a RAID 1 device, while it is currently re-syncing the disks:

Personalities : [linear] [raid1] read_ahead 1024 sectors 
md0: active raid1 sda2[1] sdb2[0] 9940 blocks [2/2] [UU] resync=1% finish=12.3min algorithm 2 [3/3] [UUU] 
unused devices: <none>
3.2.19. /proc/meminfo

This is one of the more commonly used files in the /proc/ directory, as it reports a large amount of valuable information about the systems RAM usage.

The following sample /proc/meminfo virtual file is from a system with 256 MB of RAM and 512 MB of swap space:

MemTotal:       255908 kB 
MemFree:         69936 kB 
Buffers:         15812 kB 
Cached:         115124 kB 
SwapCached:          0 kB 
Active:          92700 kB 
Inactive:        63792 kB 
HighTotal:           0 kB 
HighFree:            0 kB 
LowTotal:       255908 kB 
LowFree:         69936 kB 
SwapTotal:      524280 kB 
SwapFree:       524280 kB 
Dirty:               4 kB 
Writeback:           0 kB 
Mapped:          42236 kB 
Slab:            25912 kB 
Committed_AS:   118680 kB 
PageTables:       1236 kB 
VmallocTotal:  3874808 kB 
VmallocUsed:      1416 kB 
VmallocChunk:  3872908 kB 
HugePages_Total:     0 
HugePages_Free:      0 
Hugepagesize:     4096 kB
Much of the information here is used by the free, top, and ps commands. In fact, the output of the free command is similar in appearance to the contents and structure of /proc/meminfo. But by looking directly at /proc/meminfo, more details are revealed:

MemTotal — Total amount of physical RAM, in kilobytes.

MemFree — The amount of physical RAM, in kilobytes, left unused by the system.

Buffers — The amount of physical RAM, in kilobytes, used for file buffers.

Cached — The amount of physical RAM, in kilobytes, used as cache memory.

SwapCached — The amount of swap, in kilobytes, used as cache memory.

Active — The total amount of buffer or page cache memory, in kilobytes, that is in active use. This is memory that has been recently used and is usually not reclaimed for other purposes.

Inactive — The total amount of buffer or page cache memory, in kilobytes, that are free and available. This is memory that has not been recently used and can be reclaimed for other purposes.

HighTotal and HighFree — The total and free amount of memory, in kilobytes, that is not directly mapped into kernel space. The HighTotal value can vary based on the type of kernel used.

LowTotal and LowFree — The total and free amount of memory, in kilobytes, that is directly mapped into kernel space. The LowTotal value can vary based on the type of kernel used.

SwapTotal — The total amount of swap available, in kilobytes.

SwapFree — The total amount of swap free, in kilobytes.

Dirty — The total amount of memory, in kilobytes, waiting to be written back to the disk.

Writeback — The total amount of memory, in kilobytes, actively being written back to the disk.

Mapped — The total amount of memory, in kilobytes, which have been used to map devices, files, or libraries using the mmap command.

Slab — The total amount of memory, in kilobytes, used by the kernel to cache data structures for its own use.

Committed_AS — The total amount of memory, in kilobytes, estimated to complete the workload. This value represents the worst case scenario value, and also includes swap memory.

PageTables — The total amount of memory, in kilobytes, dedicated to the lowest page table level.

VMallocTotal — The total amount of memory, in kilobytes, of total allocated virtual address space.

VMallocUsed — The total amount of memory, in kilobytes, of used virtual address space.

VMallocChunk — The largest contiguous block of memory, in kilobytes, of available virtual address space.

HugePages_Total — The total number of hugepages for the system. The number is derived by dividing Hugepagesize by the megabytes set aside for hugepages specified in /proc/sys/vm/hugetlb_pool. This statistic only appears on the x86, Itanium, and AMD64 architectures.

HugePages_Free — The total number of hugepages available for the system. This statistic only appears on the x86, Itanium, and AMD64 architectures.

Hugepagesize — The size for each hugepages unit in kilobytes. By default, the value is 4096 KB on uniprocessor kernels for 32 bit architectures. For SMP, hugemem kernels, and AMD64, the default is 2048 KB. For Itanium architectures, the default is 262144 KB. This statistic only appears on the x86, Itanium, and AMD64 architectures.

3.2.20. /proc/misc

This file lists miscellaneous drivers registered on the miscellaneous major device, which is device number 10:

63 device-mapper 175 agpgart 135 rtc 134 apm_bios
The first column is the minor number of each device, while the second column shows the driver in use.

3.2.21. /proc/modules

This file displays a list of all modules loaded into the kernel. Its contents vary based on the configuration and use of your system, but it should be organized in a similar manner to this sample /proc/modules file output:

Note
This example has been reformatted into a readable format. Most of this information can also be viewed via the /sbin/lsmod command.
nfs      170109  0 -          Live 0x129b0000 
lockd    51593   1 nfs,       Live 0x128b0000 
nls_utf8 1729    0 -          Live 0x12830000 
vfat     12097   0 -          Live 0x12823000 
fat      38881   1 vfat,      Live 0x1287b000 
autofs4  20293   2 -          Live 0x1284f000 
sunrpc   140453  3 nfs,lockd, Live 0x12954000 
3c59x    33257   0 -          Live 0x12871000 
uhci_hcd 28377   0 -          Live 0x12869000 
md5      3777    1 -          Live 0x1282c000 
ipv6     211845 16 -          Live 0x128de000 
ext3     92585   2 -          Live 0x12886000 
jbd      65625   1 ext3,      Live 0x12857000 
dm_mod   46677   3 -          Live 0x12833000
The first column contains the name of the module.

The second column refers to the memory size of the module, in bytes.

The third column lists how many instances of the module are currently loaded. A value of zero represents an unloaded module.

The fourth column states if the module depends upon another module to be present in order to function, and lists those other modules.

The fifth column lists what load state the module is in: Live, Loading, or Unloading are the only possible values.

The sixth column lists the current kernel memory offset for the loaded module. This information can be useful for debugging purposes, or for profiling tools such as oprofile.

3.2.22. /proc/mounts

This file provides a list of all mounts in use by the system:

rootfs / rootfs rw 0 0 
/proc /proc proc rw,nodiratime 0 0 none 
/dev ramfs rw 0 0 
/dev/mapper/VolGroup00-LogVol00 / ext3 rw 0 0 
none /dev ramfs rw 0 0 
/proc /proc proc rw,nodiratime 0 0 
/sys /sys sysfs rw 0 0 
none /dev/pts devpts rw 0 0 
usbdevfs /proc/bus/usb usbdevfs rw 0 0 
/dev/hda1 /boot ext3 rw 0 0 
none /dev/shm tmpfs rw 0 0 
none /proc/sys/fs/binfmt_misc binfmt_misc rw 0 0 
sunrpc /var/lib/nfs/rpc_pipefs rpc_pipefs rw 0 0
The output found here is similar to the contents of /etc/mtab, except that /proc/mount is more up-to-date.

The first column specifies the device that is mounted, the second column reveals the mount point, and the third column tells the file system type, and the fourth column tells you if it is mounted read-only (ro) or read-write (rw). The fifth and sixth columns are dummy values designed to match the format used in /etc/mtab.

3.2.23. /proc/mtrr

This file refers to the current Memory Type Range Registers (MTRRs) in use with the system. If the system architecture supports MTRRs, then the /proc/mtrr file may look similar to the following:

reg00: base=0x00000000 (   0MB), size= 256MB: write-back, count=1 
reg01: base=0xe8000000 (3712MB), size=  32MB: write-combining, count=1
MTRRs are used with the Intel P6 family of processors (Pentium II and higher) and control processor access to memory ranges. When using a video card on a PCI or AGP bus, a properly configured /proc/mtrr file can increase performance more than 150%.

Most of the time, this value is properly configured by default. More information on manually configuring this file can be found locally at the following location:

/usr/share/doc/kernel-doc-<version>/Documentation/mtrr.txt
3.2.24. /proc/partitions

This file contains partition block allocation information. A sampling of this file from a basic system looks similar to the following:

major minor  #blocks  name      
  3     0   19531250 hda    
  3     1     104391 hda1    
  3     2   19422585 hda2  
253     0   22708224 dm-0  
253     1     524288 dm-1
Most of the information here is of little importance to the user, except for the following columns:

major — The major number of the device with this partition. The major number in the /proc/partitions, (3), corresponds with the block device ide0, in /proc/devices.

minor — The minor number of the device with this partition. This serves to separate the partitions into different physical devices and relates to the number at the end of the name of the partition.

#blocks — Lists the number of physical disk blocks contained in a particular partition.

name — The name of the partition.

3.2.25. /proc/pci

This file contains a full listing of every PCI device on the system. Depending on the number of PCI devices, /proc/pci can be rather long. A sampling of this file from a basic system looks similar to the following:

Bus  0, device 0, function 0: Host bridge: Intel Corporation 440BX/ZX - 82443BX/ZX Host bridge (rev 3). Master Capable. Latency=64. Prefetchable 32 bit memory at 0xe4000000 [0xe7ffffff].   
Bus  0, device 1, function 0: PCI bridge: Intel Corporation 440BX/ZX - 82443BX/ZX AGP bridge (rev 3).   Master Capable. Latency=64. Min Gnt=128.   
Bus  0, device 4, function 0: ISA bridge: Intel Corporation 82371AB PIIX4 ISA (rev 2).   
Bus  0, device 4, function 1: IDE interface: Intel Corporation 82371AB PIIX4 IDE (rev 1). Master Capable. Latency=32. I/O at 0xd800 [0xd80f].   
Bus  0, device 4, function 2: USB Controller: Intel Corporation 82371AB PIIX4 USB (rev 1). IRQ 5. Master Capable. Latency=32. I/O at 0xd400 [0xd41f].   
Bus  0, device 4, function 3: Bridge: Intel Corporation 82371AB PIIX4 ACPI (rev 2). IRQ 9.  
Bus  0, device 9, function 0: Ethernet controller: Lite-On Communications Inc LNE100TX (rev 33). IRQ 5. Master Capable. Latency=32. I/O at 0xd000 [0xd0ff].   
Bus  0, device 12, function  0: VGA compatible controller: S3 Inc. ViRGE/DX or /GX (rev 1). IRQ 11. Master Capable. Latency=32. Min Gnt=4.Max Lat=255.
This output shows a list of all PCI devices, sorted in the order of bus, device, and function. Beyond providing the name and version of the device, this list also gives detailed IRQ information so an administrator can quickly look for conflicts.

Tip
To get a more readable version of this information, type:
/sbin/lspci -vb
3.2.26. /proc/slabinfo

This file gives full information about memory usage on the slab level. Linux kernels greater than version 2.2 use slab pools to manage memory above the page level. Commonly used objects have their own slab pools.

Instead of parsing the highly verbose /proc/slabinfo file manually, the /usr/bin/slabtop program displays kernel slab cache information in real time. This program allows for custom configurations, including column sorting and screen refreshing.

A sample screen shot of /usr/bin/slabtop usually looks like the following example:

Active / Total Objects (% used)    : 133629 / 147300 (90.7%)  
Active / Total Slabs (% used)      : 11492 / 11493 (100.0%)  
Active / Total Caches (% used)     : 77 / 121 (63.6%)  
Active / Total Size (% used)       : 41739.83K / 44081.89K (94.7%)  
Minimum / Average / Maximum Object : 0.01K / 0.30K / 128.00K
OBJS   ACTIVE USE      OBJ   SIZE     SLABS OBJ/SLAB CACHE SIZE NAME  
44814  43159  96%    0.62K   7469      6     29876K ext3_inode_cache
36900  34614  93%    0.05K    492     75      1968K buffer_head  
35213  33124  94%    0.16K   1531     23      6124K dentry_cache   
7364   6463  87%    0.27K    526      14      2104K radix_tree_node   
2585   1781  68%    0.08K     55      47       220K vm_area_struct   
2263   2116  93%    0.12K     73      31       292K size-128   
1904   1125  59%    0.03K     16      119        64K size-32   
1666    768  46%    0.03K     14      119        56K anon_vma   
1512   1482  98%    0.44K    168       9       672K inode_cache   
1464   1040  71%    0.06K     24      61        96K size-64   
1320    820  62%    0.19K     66      20       264K filp    
678    587  86%    0.02K      3      226        12K dm_io   
678    587  86%    0.02K      3      226        12K dm_tio    
576    574  99%    0.47K     72        8       288K proc_inode_cache    
528    514  97%    0.50K     66        8       264K size-512    
492    372  75%    0.09K     12       41        48K bio    
465    314  67%    0.25K     31       15       124K size-256    
452    331  73%    0.02K      2      226         8K biovec-1    
420    420 100%    0.19K     21       20        84K skbuff_head_cache    
305    256  83%    0.06K      5       61        20K biovec-4    
290      4   1%    0.01K      1      290         4K revoke_table    
264    264 100%    4.00K    264        1      1056K size-4096    
260    256  98%    0.19K     13       20        52K biovec-16    
260    256  98%    0.75K     52        5       208K biovec-64
Some of the more commonly used statistics in /proc/slabinfo that are included into /usr/bin/slabtop include:

OBJS — The total number of objects (memory blocks), including those in use (allocated), and some spares not in use.

ACTIVE — The number of objects (memory blocks) that are in use (allocated).

USE — Percentage of total objects that are active. ((ACTIVE/OBJS)(100))

OBJ SIZE — The size of the objects.

SLABS — The total number of slabs.

OBJ/SLAB — The number of objects that fit into a slab.

CACHE SIZE — The cache size of the slab.

NAME — The name of the slab.

For more information on the /usr/bin/slabtop program, refer to the slabtop man page.

3.2.27. /proc/stat

This file keeps track of a variety of different statistics about the system since it was last restarted. The contents of /proc/stat, which can be quite long, usually begins like the following example:

cpu  259246 7001 60190 34250993 137517 772 0 
cpu0 259246 7001 60190 34250993 137517 772 0 
intr 354133732 347209999 2272 0 4 4 0 0 3 1 1249247 0 0 80143 0 422626 5169433 
ctxt 12547729 
btime 1093631447 
processes 130523 
procs_running 1 
procs_blocked 0 
preempt 5651840  
cpu  209841 1554 21720 118519346 72939 154 27168 
cpu0 42536 798 4841 14790880 14778 124 3117 
cpu1 24184 569 3875 14794524 30209 29 3130 
cpu2 28616 11 2182 14818198 4020 1 3493 
cpu3 35350 6 2942 14811519 3045 0 3659 
cpu4 18209 135 2263 14820076 12465 0 3373 
cpu5 20795 35 1866 14825701 4508 0 3615 
cpu6 21607 0 2201 14827053 2325 0 3334 
cpu7 18544 0 1550 14831395 1589 0 3447 
intr 15239682 14857833 6 0 6 6 0 5 0 1 0 0 0 29 0 2 0 0 0 0 0 0 0 94982 0 286812 
ctxt 4209609 
btime 1078711415 
processes 21905 
procs_running 1 
procs_blocked 0
Some of the more commonly used statistics include:

cpu — Measures the number of jiffies (1/100 of a second for x86 systems) that the system has been in user mode, user mode with low priority (nice), system mode, idle task, I/O wait, IRQ (hardirq), and softirq respectively. The IRQ (hardirq) is the direct response to a hardware event. The IRQ takes minimal work for queuing the "heavy" work up for the softirq to execute. The softirq runs at a lower priority than the IRQ and therefore may be interrupted more frequently. The total for all CPUs is given at the top, while each individual CPU is listed below with its own statistics. The following example is a 4-way Intel Pentium Xeon configuration with multi-threading enabled, therefore showing four physical processors and four virtual processors totaling eight processors.

page — The number of memory pages the system has written in and out to disk.

swap — The number of swap pages the system has brought in and out.

intr — The number of interrupts the system has experienced.

btime — The boot time, measured in the number of seconds since January 1, 1970, otherwise known as the epoch.

3.2.28. /proc/swaps

This file measures swap space and its utilization. For a system with only one swap partition, the output of /proc/swaps may look similar to the following:

Filename                          Type        Size     Used    Priority 
/dev/mapper/VolGroup00-LogVol01   partition   524280   0       -1
While some of this information can be found in other files in the /proc/ directory, /proc/swap provides a snapshot of every swap file name, the type of swap space, the total size, and the amount of space in use (in kilobytes). The priority column is useful when multiple swap files are in use. The lower the priority, the more likely the swap file is to be used.

3.2.29. /proc/sysrq-trigger

Using the echo command to write to this file, a remote root user can execute most System Request Key commands remotely as if at the local terminal. To echo values to this file, the /proc/sys/kernel/sysrq must be set to a value other than 0. For more information about the System Request Key, refer to Section 3.3.9.3, “/proc/sys/kernel/”.

Although it is possible to write to this file, it cannot be read, even by the root user.

3.2.30. /proc/uptime

This file contains information detailing how long the system has been on since its last restart. The output of /proc/uptime is quite minimal:

350735.47 234388.90
The first number is the total number of seconds the system has been up. The second number is how much of that time the machine has spent idle, in seconds.

3.2.31. /proc/version

This file specifies the version of the Linux kernel and gcc in use, as well as the version of Red Hat Enterprise Linux installed on the system:

Linux version 2.6.8-1.523 (user@foo.redhat.com) (gcc version 3.4.1 20040714 \  (Red Hat Enterprise Linux 3.4.1-7)) #1 Mon Aug 16 13:27:03 EDT 2004