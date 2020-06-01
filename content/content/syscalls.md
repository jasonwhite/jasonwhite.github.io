+++
title = "List of Linux Syscalls"
date = 2020-05-24

[taxonomies]
tags = ["linux", "sycalls"]
+++

A complete list of all Linux system calls. This list was generated using [this
code](https://github.com/jasonwhite/gen-syscalls) which reads a vmlinux ELF
image for its `__syscall_meta_*` symbols.

<!-- more -->

<table>
  <tr>
    <th>#</th>
    <th>Syscall</th>
  </tr>
  <tr>
    <td align="right">1</td>
    <td><code><a href="http://man7.org/linux/man-pages/man2/write.2.html">write</a>(<strong>int</strong> fd, <strong>const void*</strong> buf, <strong>size_t</strong> count)</code></td>
  </tr>
  <tr>
    <td align="right">2</td>
    <td><code><a href="http://man7.org/linux/man-pages/man2/open.2.html">open</a>(<strong>const char*</strong> filename, <strong>int</strong> flags, <strong>mode_t</strong> mode)</code></td>
  </tr>
</table>

