#Filesystem Hierarchy Standard

##Filesystem Hierarchy Standard Group

###Edited by

####Rusty Russell

#####Daniel Quinlan

#####Christopher Yeoh

http://www.pathname.com/fhs/pub/fhs-2.3.html

Copyright © 1994-2004 Daniel Quinlan

Copyright © 2001-2004 Paul 'Rusty' Russell

Copyright © 2003-2004 Christopher Yeoh

This standard consists of a set of requirements and guidelines for file and directory placement under UNIX-like operating systems. The guidelines are intended to support interoperability of applications, system administration tools, development tools, and scripts as well as greater uniformity of documentation for these systems.

All trademarks and copyrights are owned by their owners, unless specifically noted otherwise. Use of a term in this document should not be regarded as affecting the validity of any trademark or service mark.

Permission is granted to make and distribute verbatim copies of this standard provided the copyright and this permission notice are preserved on all copies.

Permission is granted to copy and distribute modified versions of this standard under the conditions for verbatim copying, provided also that the title page is labeled as modified including a reference to the original standard, provided that information on retrieving the original standard is included, and provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one.

Permission is granted to copy and distribute translations of this standard into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by the copyright holder.

Table of Contents
1. Introduction
Purpose
Conventions
2. The Filesystem
3. The Root Filesystem
Purpose
Requirements
Specific Options
/bin : Essential user command binaries (for use by all users)
Purpose
Requirements
Specific Options
/boot : Static files of the boot loader
Purpose
Specific Options
/dev : Device files
Purpose
Specific Options
/etc : Host-specific system configuration
Purpose
Requirements
Specific Options
/etc/opt : Configuration files for /opt
/etc/X11 : Configuration for the X Window System (optional)
/etc/sgml : Configuration files for SGML (optional)
/etc/xml : Configuration files for XML (optional)
/home : User home directories (optional)
Purpose
Requirements
/lib : Essential shared libraries and kernel modules
Purpose
Requirements
Specific Options
/lib<qual> : Alternate format essential shared libraries (optional)
Purpose
Requirements
/media : Mount point for removeable media
Purpose
Specific Options
/mnt : Mount point for a temporarily mounted filesystem
Purpose
/opt : Add-on application software packages
Purpose
Requirements
/root : Home directory for the root user (optional)
Purpose
/sbin : System binaries
Purpose
Requirements
Specific Options
/srv : Data for services provided by this system
Purpose
/tmp : Temporary files
