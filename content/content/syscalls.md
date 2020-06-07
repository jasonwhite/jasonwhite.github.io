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

Note that not all of the syscalls listed below have a valid man page. This is
because they are either undocumented or the symbol name of the syscall in the
Linux kernel is different than the one publicly documented.

You can also [download the full list in JSON format](../syscalls.json).

<table>
<tr>
<th>#</th>
<th>Syscall</th>
</tr>
<tr>
<td align="right">0</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/read.2.html">read</a>(<strong>unsigned int</strong> fd, <strong>char *</strong> buf, <strong>size_t</strong> count)</code></td>
</tr>
<tr>
<td align="right">1</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/write.2.html">write</a>(<strong>unsigned int</strong> fd, <strong>const char *</strong> buf, <strong>size_t</strong> count)</code></td>
</tr>
<tr>
<td align="right">2</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/open.2.html">open</a>(<strong>const char *</strong> filename, <strong>int</strong> flags, <strong>umode_t</strong> mode)</code></td>
</tr>
<tr>
<td align="right">3</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/close.2.html">close</a>(<strong>unsigned int</strong> fd)</code></td>
</tr>
<tr>
<td align="right">4</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/newstat.2.html">newstat</a>(<strong>const char *</strong> filename, <strong>struct stat *</strong> statbuf)</code></td>
</tr>
<tr>
<td align="right">5</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/newfstat.2.html">newfstat</a>(<strong>unsigned int</strong> fd, <strong>struct stat *</strong> statbuf)</code></td>
</tr>
<tr>
<td align="right">6</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/newlstat.2.html">newlstat</a>(<strong>const char *</strong> filename, <strong>struct stat *</strong> statbuf)</code></td>
</tr>
<tr>
<td align="right">7</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/poll.2.html">poll</a>(<strong>struct pollfd *</strong> ufds, <strong>unsigned int</strong> nfds, <strong>int</strong> timeout_msecs)</code></td>
</tr>
<tr>
<td align="right">8</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/lseek.2.html">lseek</a>(<strong>unsigned int</strong> fd, <strong>off_t</strong> offset, <strong>unsigned int</strong> whence)</code></td>
</tr>
<tr>
<td align="right">9</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mmap.2.html">mmap</a>(<strong>unsigned long</strong> addr, <strong>unsigned long</strong> len, <strong>unsigned long</strong> prot, <strong>unsigned long</strong> flags, <strong>unsigned long</strong> fd, <strong>unsigned long</strong> off)</code></td>
</tr>
<tr>
<td align="right">10</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mprotect.2.html">mprotect</a>(<strong>unsigned long</strong> start, <strong>size_t</strong> len, <strong>unsigned long</strong> prot)</code></td>
</tr>
<tr>
<td align="right">11</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/munmap.2.html">munmap</a>(<strong>unsigned long</strong> addr, <strong>size_t</strong> len)</code></td>
</tr>
<tr>
<td align="right">12</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/brk.2.html">brk</a>(<strong>unsigned long</strong> brk)</code></td>
</tr>
<tr>
<td align="right">13</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/rt_sigaction.2.html">rt_sigaction</a>(<strong>int</strong> sig, <strong>const struct sigaction *</strong> act, <strong>struct sigaction *</strong> oact, <strong>size_t</strong> sigsetsize)</code></td>
</tr>
<tr>
<td align="right">14</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/rt_sigprocmask.2.html">rt_sigprocmask</a>(<strong>int</strong> how, <strong>sigset_t *</strong> nset, <strong>sigset_t *</strong> oset, <strong>size_t</strong> sigsetsize)</code></td>
</tr>
<tr>
<td align="right">15</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/rt_sigreturn.2.html">rt_sigreturn</a>()</code></td>
</tr>
<tr>
<td align="right">16</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/ioctl.2.html">ioctl</a>(<strong>unsigned int</strong> fd, <strong>unsigned int</strong> cmd, <strong>unsigned long</strong> arg)</code></td>
</tr>
<tr>
<td align="right">17</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/pread64.2.html">pread64</a>(<strong>unsigned int</strong> fd, <strong>char *</strong> buf, <strong>size_t</strong> count, <strong>loff_t</strong> pos)</code></td>
</tr>
<tr>
<td align="right">18</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/pwrite64.2.html">pwrite64</a>(<strong>unsigned int</strong> fd, <strong>const char *</strong> buf, <strong>size_t</strong> count, <strong>loff_t</strong> pos)</code></td>
</tr>
<tr>
<td align="right">19</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/readv.2.html">readv</a>(<strong>unsigned long</strong> fd, <strong>const struct iovec *</strong> vec, <strong>unsigned long</strong> vlen)</code></td>
</tr>
<tr>
<td align="right">20</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/writev.2.html">writev</a>(<strong>unsigned long</strong> fd, <strong>const struct iovec *</strong> vec, <strong>unsigned long</strong> vlen)</code></td>
</tr>
<tr>
<td align="right">21</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/access.2.html">access</a>(<strong>const char *</strong> filename, <strong>int</strong> mode)</code></td>
</tr>
<tr>
<td align="right">22</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/pipe.2.html">pipe</a>(<strong>int *</strong> fildes)</code></td>
</tr>
<tr>
<td align="right">23</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/select.2.html">select</a>(<strong>int</strong> n, <strong>fd_set *</strong> inp, <strong>fd_set *</strong> outp, <strong>fd_set *</strong> exp, <strong>struct timeval *</strong> tvp)</code></td>
</tr>
<tr>
<td align="right">24</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sched_yield.2.html">sched_yield</a>()</code></td>
</tr>
<tr>
<td align="right">25</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mremap.2.html">mremap</a>(<strong>unsigned long</strong> addr, <strong>unsigned long</strong> old_len, <strong>unsigned long</strong> new_len, <strong>unsigned long</strong> flags, <strong>unsigned long</strong> new_addr)</code></td>
</tr>
<tr>
<td align="right">26</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/msync.2.html">msync</a>(<strong>unsigned long</strong> start, <strong>size_t</strong> len, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">27</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mincore.2.html">mincore</a>(<strong>unsigned long</strong> start, <strong>size_t</strong> len, <strong>unsigned char *</strong> vec)</code></td>
</tr>
<tr>
<td align="right">28</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/madvise.2.html">madvise</a>(<strong>unsigned long</strong> start, <strong>size_t</strong> len_in, <strong>int</strong> behavior)</code></td>
</tr>
<tr>
<td align="right">29</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/shmget.2.html">shmget</a>(<strong>key_t</strong> key, <strong>size_t</strong> size, <strong>int</strong> shmflg)</code></td>
</tr>
<tr>
<td align="right">30</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/shmat.2.html">shmat</a>(<strong>int</strong> shmid, <strong>char *</strong> shmaddr, <strong>int</strong> shmflg)</code></td>
</tr>
<tr>
<td align="right">31</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/shmctl.2.html">shmctl</a>(<strong>int</strong> shmid, <strong>int</strong> cmd, <strong>struct shmid_ds *</strong> buf)</code></td>
</tr>
<tr>
<td align="right">32</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/dup.2.html">dup</a>(<strong>unsigned int</strong> fildes)</code></td>
</tr>
<tr>
<td align="right">33</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/dup2.2.html">dup2</a>(<strong>unsigned int</strong> oldfd, <strong>unsigned int</strong> newfd)</code></td>
</tr>
<tr>
<td align="right">34</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/pause.2.html">pause</a>()</code></td>
</tr>
<tr>
<td align="right">35</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/nanosleep.2.html">nanosleep</a>(<strong>struct __kernel_timespec *</strong> rqtp, <strong>struct __kernel_timespec *</strong> rmtp)</code></td>
</tr>
<tr>
<td align="right">36</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getitimer.2.html">getitimer</a>(<strong>int</strong> which, <strong>struct itimerval *</strong> value)</code></td>
</tr>
<tr>
<td align="right">37</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/alarm.2.html">alarm</a>(<strong>unsigned int</strong> seconds)</code></td>
</tr>
<tr>
<td align="right">38</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setitimer.2.html">setitimer</a>(<strong>int</strong> which, <strong>struct itimerval *</strong> value, <strong>struct itimerval *</strong> ovalue)</code></td>
</tr>
<tr>
<td align="right">39</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getpid.2.html">getpid</a>()</code></td>
</tr>
<tr>
<td align="right">40</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sendfile64.2.html">sendfile64</a>(<strong>int</strong> out_fd, <strong>int</strong> in_fd, <strong>loff_t *</strong> offset, <strong>size_t</strong> count)</code></td>
</tr>
<tr>
<td align="right">41</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/socket.2.html">socket</a>(<strong>int</strong> family, <strong>int</strong> type, <strong>int</strong> protocol)</code></td>
</tr>
<tr>
<td align="right">42</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/connect.2.html">connect</a>(<strong>int</strong> fd, <strong>struct sockaddr *</strong> uservaddr, <strong>int</strong> addrlen)</code></td>
</tr>
<tr>
<td align="right">43</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/accept.2.html">accept</a>(<strong>int</strong> fd, <strong>struct sockaddr *</strong> upeer_sockaddr, <strong>int *</strong> upeer_addrlen)</code></td>
</tr>
<tr>
<td align="right">44</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sendto.2.html">sendto</a>(<strong>int</strong> fd, <strong>void *</strong> buff, <strong>size_t</strong> len, <strong>unsigned int</strong> flags, <strong>struct sockaddr *</strong> addr, <strong>int</strong> addr_len)</code></td>
</tr>
<tr>
<td align="right">45</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/recvfrom.2.html">recvfrom</a>(<strong>int</strong> fd, <strong>void *</strong> ubuf, <strong>size_t</strong> size, <strong>unsigned int</strong> flags, <strong>struct sockaddr *</strong> addr, <strong>int *</strong> addr_len)</code></td>
</tr>
<tr>
<td align="right">46</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sendmsg.2.html">sendmsg</a>(<strong>int</strong> fd, <strong>struct user_msghdr *</strong> msg, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">47</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/recvmsg.2.html">recvmsg</a>(<strong>int</strong> fd, <strong>struct user_msghdr *</strong> msg, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">48</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/shutdown.2.html">shutdown</a>(<strong>int</strong> fd, <strong>int</strong> how)</code></td>
</tr>
<tr>
<td align="right">49</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/bind.2.html">bind</a>(<strong>int</strong> fd, <strong>struct sockaddr *</strong> umyaddr, <strong>int</strong> addrlen)</code></td>
</tr>
<tr>
<td align="right">50</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/listen.2.html">listen</a>(<strong>int</strong> fd, <strong>int</strong> backlog)</code></td>
</tr>
<tr>
<td align="right">51</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getsockname.2.html">getsockname</a>(<strong>int</strong> fd, <strong>struct sockaddr *</strong> usockaddr, <strong>int *</strong> usockaddr_len)</code></td>
</tr>
<tr>
<td align="right">52</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getpeername.2.html">getpeername</a>(<strong>int</strong> fd, <strong>struct sockaddr *</strong> usockaddr, <strong>int *</strong> usockaddr_len)</code></td>
</tr>
<tr>
<td align="right">53</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/socketpair.2.html">socketpair</a>(<strong>int</strong> family, <strong>int</strong> type, <strong>int</strong> protocol, <strong>int *</strong> usockvec)</code></td>
</tr>
<tr>
<td align="right">54</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setsockopt.2.html">setsockopt</a>(<strong>int</strong> fd, <strong>int</strong> level, <strong>int</strong> optname, <strong>char *</strong> optval, <strong>int</strong> optlen)</code></td>
</tr>
<tr>
<td align="right">55</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getsockopt.2.html">getsockopt</a>(<strong>int</strong> fd, <strong>int</strong> level, <strong>int</strong> optname, <strong>char *</strong> optval, <strong>int *</strong> optlen)</code></td>
</tr>
<tr>
<td align="right">56</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/clone.2.html">clone</a>(<strong>unsigned long</strong> clone_flags, <strong>unsigned long</strong> newsp, <strong>int *</strong> parent_tidptr, <strong>int *</strong> child_tidptr, <strong>unsigned long</strong> tls)</code></td>
</tr>
<tr>
<td align="right">57</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fork.2.html">fork</a>()</code></td>
</tr>
<tr>
<td align="right">58</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/vfork.2.html">vfork</a>()</code></td>
</tr>
<tr>
<td align="right">59</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/execve.2.html">execve</a>(<strong>const char *</strong> filename, <strong>const char *const *</strong> argv, <strong>const char *const *</strong> envp)</code></td>
</tr>
<tr>
<td align="right">60</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/exit.2.html">exit</a>(<strong>int</strong> error_code)</code></td>
</tr>
<tr>
<td align="right">61</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/wait4.2.html">wait4</a>(<strong>pid_t</strong> upid, <strong>int *</strong> stat_addr, <strong>int</strong> options, <strong>struct rusage *</strong> ru)</code></td>
</tr>
<tr>
<td align="right">62</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/kill.2.html">kill</a>(<strong>pid_t</strong> pid, <strong>int</strong> sig)</code></td>
</tr>
<tr>
<td align="right">63</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/newuname.2.html">newuname</a>(<strong>struct new_utsname *</strong> name)</code></td>
</tr>
<tr>
<td align="right">64</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/semget.2.html">semget</a>(<strong>key_t</strong> key, <strong>int</strong> nsems, <strong>int</strong> semflg)</code></td>
</tr>
<tr>
<td align="right">65</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/semop.2.html">semop</a>(<strong>int</strong> semid, <strong>struct sembuf *</strong> tsops, <strong>unsigned</strong> nsops)</code></td>
</tr>
<tr>
<td align="right">66</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/semctl.2.html">semctl</a>(<strong>int</strong> semid, <strong>int</strong> semnum, <strong>int</strong> cmd, <strong>unsigned long</strong> arg)</code></td>
</tr>
<tr>
<td align="right">67</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/shmdt.2.html">shmdt</a>(<strong>char *</strong> shmaddr)</code></td>
</tr>
<tr>
<td align="right">68</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/msgget.2.html">msgget</a>(<strong>key_t</strong> key, <strong>int</strong> msgflg)</code></td>
</tr>
<tr>
<td align="right">69</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/msgsnd.2.html">msgsnd</a>(<strong>int</strong> msqid, <strong>struct msgbuf *</strong> msgp, <strong>size_t</strong> msgsz, <strong>int</strong> msgflg)</code></td>
</tr>
<tr>
<td align="right">70</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/msgrcv.2.html">msgrcv</a>(<strong>int</strong> msqid, <strong>struct msgbuf *</strong> msgp, <strong>size_t</strong> msgsz, <strong>long</strong> msgtyp, <strong>int</strong> msgflg)</code></td>
</tr>
<tr>
<td align="right">71</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/msgctl.2.html">msgctl</a>(<strong>int</strong> msqid, <strong>int</strong> cmd, <strong>struct msqid_ds *</strong> buf)</code></td>
</tr>
<tr>
<td align="right">72</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fcntl.2.html">fcntl</a>(<strong>unsigned int</strong> fd, <strong>unsigned int</strong> cmd, <strong>unsigned long</strong> arg)</code></td>
</tr>
<tr>
<td align="right">73</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/flock.2.html">flock</a>(<strong>unsigned int</strong> fd, <strong>unsigned int</strong> cmd)</code></td>
</tr>
<tr>
<td align="right">74</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fsync.2.html">fsync</a>(<strong>unsigned int</strong> fd)</code></td>
</tr>
<tr>
<td align="right">75</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fdatasync.2.html">fdatasync</a>(<strong>unsigned int</strong> fd)</code></td>
</tr>
<tr>
<td align="right">76</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/truncate.2.html">truncate</a>(<strong>const char *</strong> path, <strong>long</strong> length)</code></td>
</tr>
<tr>
<td align="right">77</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/ftruncate.2.html">ftruncate</a>(<strong>unsigned int</strong> fd, <strong>unsigned long</strong> length)</code></td>
</tr>
<tr>
<td align="right">78</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getdents.2.html">getdents</a>(<strong>unsigned int</strong> fd, <strong>struct linux_dirent *</strong> dirent, <strong>unsigned int</strong> count)</code></td>
</tr>
<tr>
<td align="right">79</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getcwd.2.html">getcwd</a>(<strong>char *</strong> buf, <strong>unsigned long</strong> size)</code></td>
</tr>
<tr>
<td align="right">80</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/chdir.2.html">chdir</a>(<strong>const char *</strong> filename)</code></td>
</tr>
<tr>
<td align="right">81</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fchdir.2.html">fchdir</a>(<strong>unsigned int</strong> fd)</code></td>
</tr>
<tr>
<td align="right">82</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/rename.2.html">rename</a>(<strong>const char *</strong> oldname, <strong>const char *</strong> newname)</code></td>
</tr>
<tr>
<td align="right">83</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mkdir.2.html">mkdir</a>(<strong>const char *</strong> pathname, <strong>umode_t</strong> mode)</code></td>
</tr>
<tr>
<td align="right">84</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/rmdir.2.html">rmdir</a>(<strong>const char *</strong> pathname)</code></td>
</tr>
<tr>
<td align="right">85</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/creat.2.html">creat</a>(<strong>const char *</strong> pathname, <strong>umode_t</strong> mode)</code></td>
</tr>
<tr>
<td align="right">86</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/link.2.html">link</a>(<strong>const char *</strong> oldname, <strong>const char *</strong> newname)</code></td>
</tr>
<tr>
<td align="right">87</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/unlink.2.html">unlink</a>(<strong>const char *</strong> pathname)</code></td>
</tr>
<tr>
<td align="right">88</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/symlink.2.html">symlink</a>(<strong>const char *</strong> oldname, <strong>const char *</strong> newname)</code></td>
</tr>
<tr>
<td align="right">89</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/readlink.2.html">readlink</a>(<strong>const char *</strong> path, <strong>char *</strong> buf, <strong>int</strong> bufsiz)</code></td>
</tr>
<tr>
<td align="right">90</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/chmod.2.html">chmod</a>(<strong>const char *</strong> filename, <strong>umode_t</strong> mode)</code></td>
</tr>
<tr>
<td align="right">91</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fchmod.2.html">fchmod</a>(<strong>unsigned int</strong> fd, <strong>umode_t</strong> mode)</code></td>
</tr>
<tr>
<td align="right">92</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/chown.2.html">chown</a>(<strong>const char *</strong> filename, <strong>uid_t</strong> user, <strong>gid_t</strong> group)</code></td>
</tr>
<tr>
<td align="right">93</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fchown.2.html">fchown</a>(<strong>unsigned int</strong> fd, <strong>uid_t</strong> user, <strong>gid_t</strong> group)</code></td>
</tr>
<tr>
<td align="right">94</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/lchown.2.html">lchown</a>(<strong>const char *</strong> filename, <strong>uid_t</strong> user, <strong>gid_t</strong> group)</code></td>
</tr>
<tr>
<td align="right">95</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/umask.2.html">umask</a>(<strong>int</strong> mask)</code></td>
</tr>
<tr>
<td align="right">96</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/gettimeofday.2.html">gettimeofday</a>(<strong>struct timeval *</strong> tv, <strong>struct timezone *</strong> tz)</code></td>
</tr>
<tr>
<td align="right">97</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getrlimit.2.html">getrlimit</a>(<strong>unsigned int</strong> resource, <strong>struct rlimit *</strong> rlim)</code></td>
</tr>
<tr>
<td align="right">98</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getrusage.2.html">getrusage</a>(<strong>int</strong> who, <strong>struct rusage *</strong> ru)</code></td>
</tr>
<tr>
<td align="right">99</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sysinfo.2.html">sysinfo</a>(<strong>struct sysinfo *</strong> info)</code></td>
</tr>
<tr>
<td align="right">100</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/times.2.html">times</a>(<strong>struct tms *</strong> tbuf)</code></td>
</tr>
<tr>
<td align="right">101</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/ptrace.2.html">ptrace</a>(<strong>long</strong> request, <strong>long</strong> pid, <strong>unsigned long</strong> addr, <strong>unsigned long</strong> data)</code></td>
</tr>
<tr>
<td align="right">102</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getuid.2.html">getuid</a>()</code></td>
</tr>
<tr>
<td align="right">103</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/syslog.2.html">syslog</a>(<strong>int</strong> type, <strong>char *</strong> buf, <strong>int</strong> len)</code></td>
</tr>
<tr>
<td align="right">104</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getgid.2.html">getgid</a>()</code></td>
</tr>
<tr>
<td align="right">105</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setuid.2.html">setuid</a>(<strong>uid_t</strong> uid)</code></td>
</tr>
<tr>
<td align="right">106</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setgid.2.html">setgid</a>(<strong>gid_t</strong> gid)</code></td>
</tr>
<tr>
<td align="right">107</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/geteuid.2.html">geteuid</a>()</code></td>
</tr>
<tr>
<td align="right">108</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getegid.2.html">getegid</a>()</code></td>
</tr>
<tr>
<td align="right">109</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setpgid.2.html">setpgid</a>(<strong>pid_t</strong> pid, <strong>pid_t</strong> pgid)</code></td>
</tr>
<tr>
<td align="right">110</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getppid.2.html">getppid</a>()</code></td>
</tr>
<tr>
<td align="right">111</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getpgrp.2.html">getpgrp</a>()</code></td>
</tr>
<tr>
<td align="right">112</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setsid.2.html">setsid</a>()</code></td>
</tr>
<tr>
<td align="right">113</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setreuid.2.html">setreuid</a>(<strong>uid_t</strong> ruid, <strong>uid_t</strong> euid)</code></td>
</tr>
<tr>
<td align="right">114</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setregid.2.html">setregid</a>(<strong>gid_t</strong> rgid, <strong>gid_t</strong> egid)</code></td>
</tr>
<tr>
<td align="right">115</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getgroups.2.html">getgroups</a>(<strong>int</strong> gidsetsize, <strong>gid_t *</strong> grouplist)</code></td>
</tr>
<tr>
<td align="right">116</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setgroups.2.html">setgroups</a>(<strong>int</strong> gidsetsize, <strong>gid_t *</strong> grouplist)</code></td>
</tr>
<tr>
<td align="right">117</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setresuid.2.html">setresuid</a>(<strong>uid_t</strong> ruid, <strong>uid_t</strong> euid, <strong>uid_t</strong> suid)</code></td>
</tr>
<tr>
<td align="right">118</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getresuid.2.html">getresuid</a>(<strong>uid_t *</strong> ruidp, <strong>uid_t *</strong> euidp, <strong>uid_t *</strong> suidp)</code></td>
</tr>
<tr>
<td align="right">119</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setresgid.2.html">setresgid</a>(<strong>gid_t</strong> rgid, <strong>gid_t</strong> egid, <strong>gid_t</strong> sgid)</code></td>
</tr>
<tr>
<td align="right">120</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getresgid.2.html">getresgid</a>(<strong>gid_t *</strong> rgidp, <strong>gid_t *</strong> egidp, <strong>gid_t *</strong> sgidp)</code></td>
</tr>
<tr>
<td align="right">121</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getpgid.2.html">getpgid</a>(<strong>pid_t</strong> pid)</code></td>
</tr>
<tr>
<td align="right">122</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setfsuid.2.html">setfsuid</a>(<strong>uid_t</strong> uid)</code></td>
</tr>
<tr>
<td align="right">123</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setfsgid.2.html">setfsgid</a>(<strong>gid_t</strong> gid)</code></td>
</tr>
<tr>
<td align="right">124</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getsid.2.html">getsid</a>(<strong>pid_t</strong> pid)</code></td>
</tr>
<tr>
<td align="right">125</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/capget.2.html">capget</a>(<strong>cap_user_header_t</strong> header, <strong>cap_user_data_t</strong> dataptr)</code></td>
</tr>
<tr>
<td align="right">126</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/capset.2.html">capset</a>(<strong>cap_user_header_t</strong> header, <strong>const cap_user_data_t</strong> data)</code></td>
</tr>
<tr>
<td align="right">127</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/rt_sigpending.2.html">rt_sigpending</a>(<strong>sigset_t *</strong> uset, <strong>size_t</strong> sigsetsize)</code></td>
</tr>
<tr>
<td align="right">128</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/rt_sigtimedwait.2.html">rt_sigtimedwait</a>(<strong>const sigset_t *</strong> uthese, <strong>siginfo_t *</strong> uinfo, <strong>const struct __kernel_timespec *</strong> uts, <strong>size_t</strong> sigsetsize)</code></td>
</tr>
<tr>
<td align="right">129</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/rt_sigqueueinfo.2.html">rt_sigqueueinfo</a>(<strong>pid_t</strong> pid, <strong>int</strong> sig, <strong>siginfo_t *</strong> uinfo)</code></td>
</tr>
<tr>
<td align="right">130</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/rt_sigsuspend.2.html">rt_sigsuspend</a>(<strong>sigset_t *</strong> unewset, <strong>size_t</strong> sigsetsize)</code></td>
</tr>
<tr>
<td align="right">131</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sigaltstack.2.html">sigaltstack</a>(<strong>const stack_t *</strong> uss, <strong>stack_t *</strong> uoss)</code></td>
</tr>
<tr>
<td align="right">132</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/utime.2.html">utime</a>(<strong>char *</strong> filename, <strong>struct utimbuf *</strong> times)</code></td>
</tr>
<tr>
<td align="right">133</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mknod.2.html">mknod</a>(<strong>const char *</strong> filename, <strong>umode_t</strong> mode, <strong>unsigned</strong> dev)</code></td>
</tr>
<tr>
<td align="right">135</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/personality.2.html">personality</a>(<strong>unsigned int</strong> personality)</code></td>
</tr>
<tr>
<td align="right">136</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/ustat.2.html">ustat</a>(<strong>unsigned</strong> dev, <strong>struct ustat *</strong> ubuf)</code></td>
</tr>
<tr>
<td align="right">137</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/statfs.2.html">statfs</a>(<strong>const char *</strong> pathname, <strong>struct statfs *</strong> buf)</code></td>
</tr>
<tr>
<td align="right">138</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fstatfs.2.html">fstatfs</a>(<strong>unsigned int</strong> fd, <strong>struct statfs *</strong> buf)</code></td>
</tr>
<tr>
<td align="right">140</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getpriority.2.html">getpriority</a>(<strong>int</strong> which, <strong>int</strong> who)</code></td>
</tr>
<tr>
<td align="right">141</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setpriority.2.html">setpriority</a>(<strong>int</strong> which, <strong>int</strong> who, <strong>int</strong> niceval)</code></td>
</tr>
<tr>
<td align="right">142</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sched_setparam.2.html">sched_setparam</a>(<strong>pid_t</strong> pid, <strong>struct sched_param *</strong> param)</code></td>
</tr>
<tr>
<td align="right">143</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sched_getparam.2.html">sched_getparam</a>(<strong>pid_t</strong> pid, <strong>struct sched_param *</strong> param)</code></td>
</tr>
<tr>
<td align="right">144</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sched_setscheduler.2.html">sched_setscheduler</a>(<strong>pid_t</strong> pid, <strong>int</strong> policy, <strong>struct sched_param *</strong> param)</code></td>
</tr>
<tr>
<td align="right">145</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sched_getscheduler.2.html">sched_getscheduler</a>(<strong>pid_t</strong> pid)</code></td>
</tr>
<tr>
<td align="right">146</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sched_get_priority_max.2.html">sched_get_priority_max</a>(<strong>int</strong> policy)</code></td>
</tr>
<tr>
<td align="right">147</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sched_get_priority_min.2.html">sched_get_priority_min</a>(<strong>int</strong> policy)</code></td>
</tr>
<tr>
<td align="right">148</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sched_rr_get_interval.2.html">sched_rr_get_interval</a>(<strong>pid_t</strong> pid, <strong>struct __kernel_timespec *</strong> interval)</code></td>
</tr>
<tr>
<td align="right">149</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mlock.2.html">mlock</a>(<strong>unsigned long</strong> start, <strong>size_t</strong> len)</code></td>
</tr>
<tr>
<td align="right">150</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/munlock.2.html">munlock</a>(<strong>unsigned long</strong> start, <strong>size_t</strong> len)</code></td>
</tr>
<tr>
<td align="right">151</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mlockall.2.html">mlockall</a>(<strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">152</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/munlockall.2.html">munlockall</a>()</code></td>
</tr>
<tr>
<td align="right">153</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/vhangup.2.html">vhangup</a>()</code></td>
</tr>
<tr>
<td align="right">154</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/modify_ldt.2.html">modify_ldt</a>(<strong>int</strong> func, <strong>void *</strong> ptr, <strong>unsigned long</strong> bytecount)</code></td>
</tr>
<tr>
<td align="right">155</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/pivot_root.2.html">pivot_root</a>(<strong>const char *</strong> new_root, <strong>const char *</strong> put_old)</code></td>
</tr>
<tr>
<td align="right">156</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sysctl.2.html">sysctl</a>(<strong>struct __sysctl_args *</strong> args)</code></td>
</tr>
<tr>
<td align="right">157</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/prctl.2.html">prctl</a>(<strong>int</strong> option, <strong>unsigned long</strong> arg2, <strong>unsigned long</strong> arg3, <strong>unsigned long</strong> arg4, <strong>unsigned long</strong> arg5)</code></td>
</tr>
<tr>
<td align="right">158</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/arch_prctl.2.html">arch_prctl</a>(<strong>int</strong> option, <strong>unsigned long</strong> arg2)</code></td>
</tr>
<tr>
<td align="right">159</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/adjtimex.2.html">adjtimex</a>(<strong>struct __kernel_timex *</strong> txc_p)</code></td>
</tr>
<tr>
<td align="right">160</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setrlimit.2.html">setrlimit</a>(<strong>unsigned int</strong> resource, <strong>struct rlimit *</strong> rlim)</code></td>
</tr>
<tr>
<td align="right">161</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/chroot.2.html">chroot</a>(<strong>const char *</strong> filename)</code></td>
</tr>
<tr>
<td align="right">162</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sync.2.html">sync</a>()</code></td>
</tr>
<tr>
<td align="right">164</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/settimeofday.2.html">settimeofday</a>(<strong>struct timeval *</strong> tv, <strong>struct timezone *</strong> tz)</code></td>
</tr>
<tr>
<td align="right">165</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mount.2.html">mount</a>(<strong>char *</strong> dev_name, <strong>char *</strong> dir_name, <strong>char *</strong> type, <strong>unsigned long</strong> flags, <strong>void *</strong> data)</code></td>
</tr>
<tr>
<td align="right">166</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/umount.2.html">umount</a>(<strong>char *</strong> name, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">167</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/swapon.2.html">swapon</a>(<strong>const char *</strong> specialfile, <strong>int</strong> swap_flags)</code></td>
</tr>
<tr>
<td align="right">168</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/swapoff.2.html">swapoff</a>(<strong>const char *</strong> specialfile)</code></td>
</tr>
<tr>
<td align="right">169</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/reboot.2.html">reboot</a>(<strong>int</strong> magic1, <strong>int</strong> magic2, <strong>unsigned int</strong> cmd, <strong>void *</strong> arg)</code></td>
</tr>
<tr>
<td align="right">170</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sethostname.2.html">sethostname</a>(<strong>char *</strong> name, <strong>int</strong> len)</code></td>
</tr>
<tr>
<td align="right">171</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setdomainname.2.html">setdomainname</a>(<strong>char *</strong> name, <strong>int</strong> len)</code></td>
</tr>
<tr>
<td align="right">172</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/iopl.2.html">iopl</a>(<strong>unsigned int</strong> level)</code></td>
</tr>
<tr>
<td align="right">173</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/ioperm.2.html">ioperm</a>(<strong>unsigned long</strong> from, <strong>unsigned long</strong> num, <strong>int</strong> turn_on)</code></td>
</tr>
<tr>
<td align="right">175</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/init_module.2.html">init_module</a>(<strong>void *</strong> umod, <strong>unsigned long</strong> len, <strong>const char *</strong> uargs)</code></td>
</tr>
<tr>
<td align="right">176</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/delete_module.2.html">delete_module</a>(<strong>const char *</strong> name_user, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">179</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/quotactl.2.html">quotactl</a>(<strong>unsigned int</strong> cmd, <strong>const char *</strong> special, <strong>qid_t</strong> id, <strong>void *</strong> addr)</code></td>
</tr>
<tr>
<td align="right">186</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/gettid.2.html">gettid</a>()</code></td>
</tr>
<tr>
<td align="right">187</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/readahead.2.html">readahead</a>(<strong>int</strong> fd, <strong>loff_t</strong> offset, <strong>size_t</strong> count)</code></td>
</tr>
<tr>
<td align="right">188</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setxattr.2.html">setxattr</a>(<strong>const char *</strong> pathname, <strong>const char *</strong> name, <strong>const void *</strong> value, <strong>size_t</strong> size, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">189</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/lsetxattr.2.html">lsetxattr</a>(<strong>const char *</strong> pathname, <strong>const char *</strong> name, <strong>const void *</strong> value, <strong>size_t</strong> size, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">190</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fsetxattr.2.html">fsetxattr</a>(<strong>int</strong> fd, <strong>const char *</strong> name, <strong>const void *</strong> value, <strong>size_t</strong> size, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">191</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getxattr.2.html">getxattr</a>(<strong>const char *</strong> pathname, <strong>const char *</strong> name, <strong>void *</strong> value, <strong>size_t</strong> size)</code></td>
</tr>
<tr>
<td align="right">192</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/lgetxattr.2.html">lgetxattr</a>(<strong>const char *</strong> pathname, <strong>const char *</strong> name, <strong>void *</strong> value, <strong>size_t</strong> size)</code></td>
</tr>
<tr>
<td align="right">193</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fgetxattr.2.html">fgetxattr</a>(<strong>int</strong> fd, <strong>const char *</strong> name, <strong>void *</strong> value, <strong>size_t</strong> size)</code></td>
</tr>
<tr>
<td align="right">194</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/listxattr.2.html">listxattr</a>(<strong>const char *</strong> pathname, <strong>char *</strong> list, <strong>size_t</strong> size)</code></td>
</tr>
<tr>
<td align="right">195</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/llistxattr.2.html">llistxattr</a>(<strong>const char *</strong> pathname, <strong>char *</strong> list, <strong>size_t</strong> size)</code></td>
</tr>
<tr>
<td align="right">196</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/flistxattr.2.html">flistxattr</a>(<strong>int</strong> fd, <strong>char *</strong> list, <strong>size_t</strong> size)</code></td>
</tr>
<tr>
<td align="right">197</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/removexattr.2.html">removexattr</a>(<strong>const char *</strong> pathname, <strong>const char *</strong> name)</code></td>
</tr>
<tr>
<td align="right">198</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/lremovexattr.2.html">lremovexattr</a>(<strong>const char *</strong> pathname, <strong>const char *</strong> name)</code></td>
</tr>
<tr>
<td align="right">199</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fremovexattr.2.html">fremovexattr</a>(<strong>int</strong> fd, <strong>const char *</strong> name)</code></td>
</tr>
<tr>
<td align="right">200</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/tkill.2.html">tkill</a>(<strong>pid_t</strong> pid, <strong>int</strong> sig)</code></td>
</tr>
<tr>
<td align="right">201</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/time.2.html">time</a>(<strong>time_t *</strong> tloc)</code></td>
</tr>
<tr>
<td align="right">202</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/futex.2.html">futex</a>(<strong>u32 *</strong> uaddr, <strong>int</strong> op, <strong>u32</strong> val, <strong>struct __kernel_timespec *</strong> utime, <strong>u32 *</strong> uaddr2, <strong>u32</strong> val3)</code></td>
</tr>
<tr>
<td align="right">203</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sched_setaffinity.2.html">sched_setaffinity</a>(<strong>pid_t</strong> pid, <strong>unsigned int</strong> len, <strong>unsigned long *</strong> user_mask_ptr)</code></td>
</tr>
<tr>
<td align="right">204</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sched_getaffinity.2.html">sched_getaffinity</a>(<strong>pid_t</strong> pid, <strong>unsigned int</strong> len, <strong>unsigned long *</strong> user_mask_ptr)</code></td>
</tr>
<tr>
<td align="right">206</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/io_setup.2.html">io_setup</a>(<strong>unsigned</strong> nr_events, <strong>aio_context_t *</strong> ctxp)</code></td>
</tr>
<tr>
<td align="right">207</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/io_destroy.2.html">io_destroy</a>(<strong>aio_context_t</strong> ctx)</code></td>
</tr>
<tr>
<td align="right">208</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/io_getevents.2.html">io_getevents</a>(<strong>aio_context_t</strong> ctx_id, <strong>long</strong> min_nr, <strong>long</strong> nr, <strong>struct io_event *</strong> events, <strong>struct __kernel_timespec *</strong> timeout)</code></td>
</tr>
<tr>
<td align="right">209</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/io_submit.2.html">io_submit</a>(<strong>aio_context_t</strong> ctx_id, <strong>long</strong> nr, <strong>struct iocb * *</strong> iocbpp)</code></td>
</tr>
<tr>
<td align="right">210</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/io_cancel.2.html">io_cancel</a>(<strong>aio_context_t</strong> ctx_id, <strong>struct iocb *</strong> iocb, <strong>struct io_event *</strong> result)</code></td>
</tr>
<tr>
<td align="right">213</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/epoll_create.2.html">epoll_create</a>(<strong>int</strong> size)</code></td>
</tr>
<tr>
<td align="right">216</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/remap_file_pages.2.html">remap_file_pages</a>(<strong>unsigned long</strong> start, <strong>unsigned long</strong> size, <strong>unsigned long</strong> prot, <strong>unsigned long</strong> pgoff, <strong>unsigned long</strong> flags)</code></td>
</tr>
<tr>
<td align="right">217</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getdents64.2.html">getdents64</a>(<strong>unsigned int</strong> fd, <strong>struct linux_dirent64 *</strong> dirent, <strong>unsigned int</strong> count)</code></td>
</tr>
<tr>
<td align="right">218</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/set_tid_address.2.html">set_tid_address</a>(<strong>int *</strong> tidptr)</code></td>
</tr>
<tr>
<td align="right">219</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/restart_syscall.2.html">restart_syscall</a>()</code></td>
</tr>
<tr>
<td align="right">220</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/semtimedop.2.html">semtimedop</a>(<strong>int</strong> semid, <strong>struct sembuf *</strong> tsops, <strong>unsigned int</strong> nsops, <strong>const struct __kernel_timespec *</strong> timeout)</code></td>
</tr>
<tr>
<td align="right">221</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fadvise64.2.html">fadvise64</a>(<strong>int</strong> fd, <strong>loff_t</strong> offset, <strong>size_t</strong> len, <strong>int</strong> advice)</code></td>
</tr>
<tr>
<td align="right">222</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/timer_create.2.html">timer_create</a>(<strong>const clockid_t</strong> which_clock, <strong>struct sigevent *</strong> timer_event_spec, <strong>timer_t *</strong> created_timer_id)</code></td>
</tr>
<tr>
<td align="right">223</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/timer_settime.2.html">timer_settime</a>(<strong>timer_t</strong> timer_id, <strong>int</strong> flags, <strong>const struct __kernel_itimerspec *</strong> new_setting, <strong>struct __kernel_itimerspec *</strong> old_setting)</code></td>
</tr>
<tr>
<td align="right">224</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/timer_gettime.2.html">timer_gettime</a>(<strong>timer_t</strong> timer_id, <strong>struct __kernel_itimerspec *</strong> setting)</code></td>
</tr>
<tr>
<td align="right">225</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/timer_getoverrun.2.html">timer_getoverrun</a>(<strong>timer_t</strong> timer_id)</code></td>
</tr>
<tr>
<td align="right">226</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/timer_delete.2.html">timer_delete</a>(<strong>timer_t</strong> timer_id)</code></td>
</tr>
<tr>
<td align="right">227</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/clock_settime.2.html">clock_settime</a>(<strong>const clockid_t</strong> which_clock, <strong>const struct __kernel_timespec *</strong> tp)</code></td>
</tr>
<tr>
<td align="right">228</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/clock_gettime.2.html">clock_gettime</a>(<strong>const clockid_t</strong> which_clock, <strong>struct __kernel_timespec *</strong> tp)</code></td>
</tr>
<tr>
<td align="right">229</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/clock_getres.2.html">clock_getres</a>(<strong>const clockid_t</strong> which_clock, <strong>struct __kernel_timespec *</strong> tp)</code></td>
</tr>
<tr>
<td align="right">230</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/clock_nanosleep.2.html">clock_nanosleep</a>(<strong>const clockid_t</strong> which_clock, <strong>int</strong> flags, <strong>const struct __kernel_timespec *</strong> rqtp, <strong>struct __kernel_timespec *</strong> rmtp)</code></td>
</tr>
<tr>
<td align="right">231</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/exit_group.2.html">exit_group</a>(<strong>int</strong> error_code)</code></td>
</tr>
<tr>
<td align="right">232</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/epoll_wait.2.html">epoll_wait</a>(<strong>int</strong> epfd, <strong>struct epoll_event *</strong> events, <strong>int</strong> maxevents, <strong>int</strong> timeout)</code></td>
</tr>
<tr>
<td align="right">233</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/epoll_ctl.2.html">epoll_ctl</a>(<strong>int</strong> epfd, <strong>int</strong> op, <strong>int</strong> fd, <strong>struct epoll_event *</strong> event)</code></td>
</tr>
<tr>
<td align="right">234</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/tgkill.2.html">tgkill</a>(<strong>pid_t</strong> tgid, <strong>pid_t</strong> pid, <strong>int</strong> sig)</code></td>
</tr>
<tr>
<td align="right">235</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/utimes.2.html">utimes</a>(<strong>char *</strong> filename, <strong>struct timeval *</strong> utimes)</code></td>
</tr>
<tr>
<td align="right">237</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mbind.2.html">mbind</a>(<strong>unsigned long</strong> start, <strong>unsigned long</strong> len, <strong>unsigned long</strong> mode, <strong>const unsigned long *</strong> nmask, <strong>unsigned long</strong> maxnode, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">238</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/set_mempolicy.2.html">set_mempolicy</a>(<strong>int</strong> mode, <strong>const unsigned long *</strong> nmask, <strong>unsigned long</strong> maxnode)</code></td>
</tr>
<tr>
<td align="right">239</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/get_mempolicy.2.html">get_mempolicy</a>(<strong>int *</strong> policy, <strong>unsigned long *</strong> nmask, <strong>unsigned long</strong> maxnode, <strong>unsigned long</strong> addr, <strong>unsigned long</strong> flags)</code></td>
</tr>
<tr>
<td align="right">240</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mq_open.2.html">mq_open</a>(<strong>const char *</strong> u_name, <strong>int</strong> oflag, <strong>umode_t</strong> mode, <strong>struct mq_attr *</strong> u_attr)</code></td>
</tr>
<tr>
<td align="right">241</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mq_unlink.2.html">mq_unlink</a>(<strong>const char *</strong> u_name)</code></td>
</tr>
<tr>
<td align="right">242</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mq_timedsend.2.html">mq_timedsend</a>(<strong>mqd_t</strong> mqdes, <strong>const char *</strong> u_msg_ptr, <strong>size_t</strong> msg_len, <strong>unsigned int</strong> msg_prio, <strong>const struct __kernel_timespec *</strong> u_abs_timeout)</code></td>
</tr>
<tr>
<td align="right">243</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mq_timedreceive.2.html">mq_timedreceive</a>(<strong>mqd_t</strong> mqdes, <strong>char *</strong> u_msg_ptr, <strong>size_t</strong> msg_len, <strong>unsigned int *</strong> u_msg_prio, <strong>const struct __kernel_timespec *</strong> u_abs_timeout)</code></td>
</tr>
<tr>
<td align="right">244</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mq_notify.2.html">mq_notify</a>(<strong>mqd_t</strong> mqdes, <strong>const struct sigevent *</strong> u_notification)</code></td>
</tr>
<tr>
<td align="right">245</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mq_getsetattr.2.html">mq_getsetattr</a>(<strong>mqd_t</strong> mqdes, <strong>const struct mq_attr *</strong> u_mqstat, <strong>struct mq_attr *</strong> u_omqstat)</code></td>
</tr>
<tr>
<td align="right">246</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/kexec_load.2.html">kexec_load</a>(<strong>unsigned long</strong> entry, <strong>unsigned long</strong> nr_segments, <strong>struct kexec_segment *</strong> segments, <strong>unsigned long</strong> flags)</code></td>
</tr>
<tr>
<td align="right">247</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/waitid.2.html">waitid</a>(<strong>int</strong> which, <strong>pid_t</strong> upid, <strong>struct siginfo *</strong> infop, <strong>int</strong> options, <strong>struct rusage *</strong> ru)</code></td>
</tr>
<tr>
<td align="right">248</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/add_key.2.html">add_key</a>(<strong>const char *</strong> _type, <strong>const char *</strong> _description, <strong>const void *</strong> _payload, <strong>size_t</strong> plen, <strong>key_serial_t</strong> ringid)</code></td>
</tr>
<tr>
<td align="right">249</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/request_key.2.html">request_key</a>(<strong>const char *</strong> _type, <strong>const char *</strong> _description, <strong>const char *</strong> _callout_info, <strong>key_serial_t</strong> destringid)</code></td>
</tr>
<tr>
<td align="right">250</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/keyctl.2.html">keyctl</a>(<strong>int</strong> option, <strong>unsigned long</strong> arg2, <strong>unsigned long</strong> arg3, <strong>unsigned long</strong> arg4, <strong>unsigned long</strong> arg5)</code></td>
</tr>
<tr>
<td align="right">251</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/ioprio_set.2.html">ioprio_set</a>(<strong>int</strong> which, <strong>int</strong> who, <strong>int</strong> ioprio)</code></td>
</tr>
<tr>
<td align="right">252</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/ioprio_get.2.html">ioprio_get</a>(<strong>int</strong> which, <strong>int</strong> who)</code></td>
</tr>
<tr>
<td align="right">253</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/inotify_init.2.html">inotify_init</a>()</code></td>
</tr>
<tr>
<td align="right">254</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/inotify_add_watch.2.html">inotify_add_watch</a>(<strong>int</strong> fd, <strong>const char *</strong> pathname, <strong>u32</strong> mask)</code></td>
</tr>
<tr>
<td align="right">255</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/inotify_rm_watch.2.html">inotify_rm_watch</a>(<strong>int</strong> fd, <strong>__s32</strong> wd)</code></td>
</tr>
<tr>
<td align="right">256</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/migrate_pages.2.html">migrate_pages</a>(<strong>pid_t</strong> pid, <strong>unsigned long</strong> maxnode, <strong>const unsigned long *</strong> old_nodes, <strong>const unsigned long *</strong> new_nodes)</code></td>
</tr>
<tr>
<td align="right">257</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/openat.2.html">openat</a>(<strong>int</strong> dfd, <strong>const char *</strong> filename, <strong>int</strong> flags, <strong>umode_t</strong> mode)</code></td>
</tr>
<tr>
<td align="right">258</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mkdirat.2.html">mkdirat</a>(<strong>int</strong> dfd, <strong>const char *</strong> pathname, <strong>umode_t</strong> mode)</code></td>
</tr>
<tr>
<td align="right">259</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mknodat.2.html">mknodat</a>(<strong>int</strong> dfd, <strong>const char *</strong> filename, <strong>umode_t</strong> mode, <strong>unsigned int</strong> dev)</code></td>
</tr>
<tr>
<td align="right">260</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fchownat.2.html">fchownat</a>(<strong>int</strong> dfd, <strong>const char *</strong> filename, <strong>uid_t</strong> user, <strong>gid_t</strong> group, <strong>int</strong> flag)</code></td>
</tr>
<tr>
<td align="right">261</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/futimesat.2.html">futimesat</a>(<strong>int</strong> dfd, <strong>const char *</strong> filename, <strong>struct timeval *</strong> utimes)</code></td>
</tr>
<tr>
<td align="right">262</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/newfstatat.2.html">newfstatat</a>(<strong>int</strong> dfd, <strong>const char *</strong> filename, <strong>struct stat *</strong> statbuf, <strong>int</strong> flag)</code></td>
</tr>
<tr>
<td align="right">263</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/unlinkat.2.html">unlinkat</a>(<strong>int</strong> dfd, <strong>const char *</strong> pathname, <strong>int</strong> flag)</code></td>
</tr>
<tr>
<td align="right">264</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/renameat.2.html">renameat</a>(<strong>int</strong> olddfd, <strong>const char *</strong> oldname, <strong>int</strong> newdfd, <strong>const char *</strong> newname)</code></td>
</tr>
<tr>
<td align="right">265</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/linkat.2.html">linkat</a>(<strong>int</strong> olddfd, <strong>const char *</strong> oldname, <strong>int</strong> newdfd, <strong>const char *</strong> newname, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">266</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/symlinkat.2.html">symlinkat</a>(<strong>const char *</strong> oldname, <strong>int</strong> newdfd, <strong>const char *</strong> newname)</code></td>
</tr>
<tr>
<td align="right">267</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/readlinkat.2.html">readlinkat</a>(<strong>int</strong> dfd, <strong>const char *</strong> pathname, <strong>char *</strong> buf, <strong>int</strong> bufsiz)</code></td>
</tr>
<tr>
<td align="right">268</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fchmodat.2.html">fchmodat</a>(<strong>int</strong> dfd, <strong>const char *</strong> filename, <strong>umode_t</strong> mode)</code></td>
</tr>
<tr>
<td align="right">269</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/faccessat.2.html">faccessat</a>(<strong>int</strong> dfd, <strong>const char *</strong> filename, <strong>int</strong> mode)</code></td>
</tr>
<tr>
<td align="right">270</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/pselect6.2.html">pselect6</a>(<strong>int</strong> n, <strong>fd_set *</strong> inp, <strong>fd_set *</strong> outp, <strong>fd_set *</strong> exp, <strong>struct __kernel_timespec *</strong> tsp, <strong>void *</strong> sig)</code></td>
</tr>
<tr>
<td align="right">271</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/ppoll.2.html">ppoll</a>(<strong>struct pollfd *</strong> ufds, <strong>unsigned int</strong> nfds, <strong>struct __kernel_timespec *</strong> tsp, <strong>const sigset_t *</strong> sigmask, <strong>size_t</strong> sigsetsize)</code></td>
</tr>
<tr>
<td align="right">272</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/unshare.2.html">unshare</a>(<strong>unsigned long</strong> unshare_flags)</code></td>
</tr>
<tr>
<td align="right">273</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/set_robust_list.2.html">set_robust_list</a>(<strong>struct robust_list_head *</strong> head, <strong>size_t</strong> len)</code></td>
</tr>
<tr>
<td align="right">274</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/get_robust_list.2.html">get_robust_list</a>(<strong>int</strong> pid, <strong>struct robust_list_head * *</strong> head_ptr, <strong>size_t *</strong> len_ptr)</code></td>
</tr>
<tr>
<td align="right">275</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/splice.2.html">splice</a>(<strong>int</strong> fd_in, <strong>loff_t *</strong> off_in, <strong>int</strong> fd_out, <strong>loff_t *</strong> off_out, <strong>size_t</strong> len, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">276</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/tee.2.html">tee</a>(<strong>int</strong> fdin, <strong>int</strong> fdout, <strong>size_t</strong> len, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">277</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sync_file_range.2.html">sync_file_range</a>(<strong>int</strong> fd, <strong>loff_t</strong> offset, <strong>loff_t</strong> nbytes, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">278</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/vmsplice.2.html">vmsplice</a>(<strong>int</strong> fd, <strong>const struct iovec *</strong> uiov, <strong>unsigned long</strong> nr_segs, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">279</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/move_pages.2.html">move_pages</a>(<strong>pid_t</strong> pid, <strong>unsigned long</strong> nr_pages, <strong>const void * *</strong> pages, <strong>const int *</strong> nodes, <strong>int *</strong> status, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">280</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/utimensat.2.html">utimensat</a>(<strong>int</strong> dfd, <strong>const char *</strong> filename, <strong>struct __kernel_timespec *</strong> utimes, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">281</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/epoll_pwait.2.html">epoll_pwait</a>(<strong>int</strong> epfd, <strong>struct epoll_event *</strong> events, <strong>int</strong> maxevents, <strong>int</strong> timeout, <strong>const sigset_t *</strong> sigmask, <strong>size_t</strong> sigsetsize)</code></td>
</tr>
<tr>
<td align="right">282</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/signalfd.2.html">signalfd</a>(<strong>int</strong> ufd, <strong>sigset_t *</strong> user_mask, <strong>size_t</strong> sizemask)</code></td>
</tr>
<tr>
<td align="right">283</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/timerfd_create.2.html">timerfd_create</a>(<strong>int</strong> clockid, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">284</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/eventfd.2.html">eventfd</a>(<strong>unsigned int</strong> count)</code></td>
</tr>
<tr>
<td align="right">285</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fallocate.2.html">fallocate</a>(<strong>int</strong> fd, <strong>int</strong> mode, <strong>loff_t</strong> offset, <strong>loff_t</strong> len)</code></td>
</tr>
<tr>
<td align="right">286</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/timerfd_settime.2.html">timerfd_settime</a>(<strong>int</strong> ufd, <strong>int</strong> flags, <strong>const struct __kernel_itimerspec *</strong> utmr, <strong>struct __kernel_itimerspec *</strong> otmr)</code></td>
</tr>
<tr>
<td align="right">287</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/timerfd_gettime.2.html">timerfd_gettime</a>(<strong>int</strong> ufd, <strong>struct __kernel_itimerspec *</strong> otmr)</code></td>
</tr>
<tr>
<td align="right">288</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/accept4.2.html">accept4</a>(<strong>int</strong> fd, <strong>struct sockaddr *</strong> upeer_sockaddr, <strong>int *</strong> upeer_addrlen, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">289</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/signalfd4.2.html">signalfd4</a>(<strong>int</strong> ufd, <strong>sigset_t *</strong> user_mask, <strong>size_t</strong> sizemask, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">290</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/eventfd2.2.html">eventfd2</a>(<strong>unsigned int</strong> count, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">291</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/epoll_create1.2.html">epoll_create1</a>(<strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">292</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/dup3.2.html">dup3</a>(<strong>unsigned int</strong> oldfd, <strong>unsigned int</strong> newfd, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">293</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/pipe2.2.html">pipe2</a>(<strong>int *</strong> fildes, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">294</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/inotify_init1.2.html">inotify_init1</a>(<strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">295</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/preadv.2.html">preadv</a>(<strong>unsigned long</strong> fd, <strong>const struct iovec *</strong> vec, <strong>unsigned long</strong> vlen, <strong>unsigned long</strong> pos_l, <strong>unsigned long</strong> pos_h)</code></td>
</tr>
<tr>
<td align="right">296</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/pwritev.2.html">pwritev</a>(<strong>unsigned long</strong> fd, <strong>const struct iovec *</strong> vec, <strong>unsigned long</strong> vlen, <strong>unsigned long</strong> pos_l, <strong>unsigned long</strong> pos_h)</code></td>
</tr>
<tr>
<td align="right">297</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/rt_tgsigqueueinfo.2.html">rt_tgsigqueueinfo</a>(<strong>pid_t</strong> tgid, <strong>pid_t</strong> pid, <strong>int</strong> sig, <strong>siginfo_t *</strong> uinfo)</code></td>
</tr>
<tr>
<td align="right">298</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/perf_event_open.2.html">perf_event_open</a>(<strong>struct perf_event_attr *</strong> attr_uptr, <strong>pid_t</strong> pid, <strong>int</strong> cpu, <strong>int</strong> group_fd, <strong>unsigned long</strong> flags)</code></td>
</tr>
<tr>
<td align="right">299</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/recvmmsg.2.html">recvmmsg</a>(<strong>int</strong> fd, <strong>struct mmsghdr *</strong> mmsg, <strong>unsigned int</strong> vlen, <strong>unsigned int</strong> flags, <strong>struct __kernel_timespec *</strong> timeout)</code></td>
</tr>
<tr>
<td align="right">300</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fanotify_init.2.html">fanotify_init</a>(<strong>unsigned int</strong> flags, <strong>unsigned int</strong> event_f_flags)</code></td>
</tr>
<tr>
<td align="right">301</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fanotify_mark.2.html">fanotify_mark</a>(<strong>int</strong> fanotify_fd, <strong>unsigned int</strong> flags, <strong>__u64</strong> mask, <strong>int</strong> dfd, <strong>const char *</strong> pathname)</code></td>
</tr>
<tr>
<td align="right">302</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/prlimit64.2.html">prlimit64</a>(<strong>pid_t</strong> pid, <strong>unsigned int</strong> resource, <strong>const struct rlimit64 *</strong> new_rlim, <strong>struct rlimit64 *</strong> old_rlim)</code></td>
</tr>
<tr>
<td align="right">303</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/name_to_handle_at.2.html">name_to_handle_at</a>(<strong>int</strong> dfd, <strong>const char *</strong> name, <strong>struct file_handle *</strong> handle, <strong>int *</strong> mnt_id, <strong>int</strong> flag)</code></td>
</tr>
<tr>
<td align="right">304</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/open_by_handle_at.2.html">open_by_handle_at</a>(<strong>int</strong> mountdirfd, <strong>struct file_handle *</strong> handle, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">305</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/clock_adjtime.2.html">clock_adjtime</a>(<strong>const clockid_t</strong> which_clock, <strong>struct __kernel_timex *</strong> utx)</code></td>
</tr>
<tr>
<td align="right">306</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/syncfs.2.html">syncfs</a>(<strong>int</strong> fd)</code></td>
</tr>
<tr>
<td align="right">307</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sendmmsg.2.html">sendmmsg</a>(<strong>int</strong> fd, <strong>struct mmsghdr *</strong> mmsg, <strong>unsigned int</strong> vlen, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">308</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/setns.2.html">setns</a>(<strong>int</strong> fd, <strong>int</strong> nstype)</code></td>
</tr>
<tr>
<td align="right">309</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getcpu.2.html">getcpu</a>(<strong>unsigned *</strong> cpup, <strong>unsigned *</strong> nodep, <strong>struct getcpu_cache *</strong> unused)</code></td>
</tr>
<tr>
<td align="right">310</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/process_vm_readv.2.html">process_vm_readv</a>(<strong>pid_t</strong> pid, <strong>const struct iovec *</strong> lvec, <strong>unsigned long</strong> liovcnt, <strong>const struct iovec *</strong> rvec, <strong>unsigned long</strong> riovcnt, <strong>unsigned long</strong> flags)</code></td>
</tr>
<tr>
<td align="right">311</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/process_vm_writev.2.html">process_vm_writev</a>(<strong>pid_t</strong> pid, <strong>const struct iovec *</strong> lvec, <strong>unsigned long</strong> liovcnt, <strong>const struct iovec *</strong> rvec, <strong>unsigned long</strong> riovcnt, <strong>unsigned long</strong> flags)</code></td>
</tr>
<tr>
<td align="right">313</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/finit_module.2.html">finit_module</a>(<strong>int</strong> fd, <strong>const char *</strong> uargs, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">314</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sched_setattr.2.html">sched_setattr</a>(<strong>pid_t</strong> pid, <strong>struct sched_attr *</strong> uattr, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">315</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/sched_getattr.2.html">sched_getattr</a>(<strong>pid_t</strong> pid, <strong>struct sched_attr *</strong> uattr, <strong>unsigned int</strong> size, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">316</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/renameat2.2.html">renameat2</a>(<strong>int</strong> olddfd, <strong>const char *</strong> oldname, <strong>int</strong> newdfd, <strong>const char *</strong> newname, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">317</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/seccomp.2.html">seccomp</a>(<strong>unsigned int</strong> op, <strong>unsigned int</strong> flags, <strong>void *</strong> uargs)</code></td>
</tr>
<tr>
<td align="right">318</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/getrandom.2.html">getrandom</a>(<strong>char *</strong> buf, <strong>size_t</strong> count, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">319</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/memfd_create.2.html">memfd_create</a>(<strong>const char *</strong> uname, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">320</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/kexec_file_load.2.html">kexec_file_load</a>(<strong>int</strong> kernel_fd, <strong>int</strong> initrd_fd, <strong>unsigned long</strong> cmdline_len, <strong>const char *</strong> cmdline_ptr, <strong>unsigned long</strong> flags)</code></td>
</tr>
<tr>
<td align="right">321</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/bpf.2.html">bpf</a>(<strong>int</strong> cmd, <strong>union bpf_attr *</strong> uattr, <strong>unsigned int</strong> size)</code></td>
</tr>
<tr>
<td align="right">322</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/execveat.2.html">execveat</a>(<strong>int</strong> fd, <strong>const char *</strong> filename, <strong>const char *const *</strong> argv, <strong>const char *const *</strong> envp, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">323</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/userfaultfd.2.html">userfaultfd</a>(<strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">324</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/membarrier.2.html">membarrier</a>(<strong>int</strong> cmd, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">325</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/mlock2.2.html">mlock2</a>(<strong>unsigned long</strong> start, <strong>size_t</strong> len, <strong>int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">326</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/copy_file_range.2.html">copy_file_range</a>(<strong>int</strong> fd_in, <strong>loff_t *</strong> off_in, <strong>int</strong> fd_out, <strong>loff_t *</strong> off_out, <strong>size_t</strong> len, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">327</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/preadv2.2.html">preadv2</a>(<strong>unsigned long</strong> fd, <strong>const struct iovec *</strong> vec, <strong>unsigned long</strong> vlen, <strong>unsigned long</strong> pos_l, <strong>unsigned long</strong> pos_h, <strong>rwf_t</strong> flags)</code></td>
</tr>
<tr>
<td align="right">328</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/pwritev2.2.html">pwritev2</a>(<strong>unsigned long</strong> fd, <strong>const struct iovec *</strong> vec, <strong>unsigned long</strong> vlen, <strong>unsigned long</strong> pos_l, <strong>unsigned long</strong> pos_h, <strong>rwf_t</strong> flags)</code></td>
</tr>
<tr>
<td align="right">329</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/pkey_mprotect.2.html">pkey_mprotect</a>(<strong>unsigned long</strong> start, <strong>size_t</strong> len, <strong>unsigned long</strong> prot, <strong>int</strong> pkey)</code></td>
</tr>
<tr>
<td align="right">330</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/pkey_alloc.2.html">pkey_alloc</a>(<strong>unsigned long</strong> flags, <strong>unsigned long</strong> init_val)</code></td>
</tr>
<tr>
<td align="right">331</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/pkey_free.2.html">pkey_free</a>(<strong>int</strong> pkey)</code></td>
</tr>
<tr>
<td align="right">332</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/statx.2.html">statx</a>(<strong>int</strong> dfd, <strong>const char *</strong> filename, <strong>unsigned</strong> flags, <strong>unsigned int</strong> mask, <strong>struct statx *</strong> buffer)</code></td>
</tr>
<tr>
<td align="right">333</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/io_pgetevents.2.html">io_pgetevents</a>(<strong>aio_context_t</strong> ctx_id, <strong>long</strong> min_nr, <strong>long</strong> nr, <strong>struct io_event *</strong> events, <strong>struct __kernel_timespec *</strong> timeout, <strong>const struct __aio_sigset *</strong> usig)</code></td>
</tr>
<tr>
<td align="right">334</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/rseq.2.html">rseq</a>(<strong>struct rseq *</strong> rseq, <strong>u32</strong> rseq_len, <strong>int</strong> flags, <strong>u32</strong> sig)</code></td>
</tr>
<tr>
<td align="right">424</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/pidfd_send_signal.2.html">pidfd_send_signal</a>(<strong>int</strong> pidfd, <strong>int</strong> sig, <strong>siginfo_t *</strong> info, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">425</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/io_uring_setup.2.html">io_uring_setup</a>(<strong>u32</strong> entries, <strong>struct io_uring_params *</strong> params)</code></td>
</tr>
<tr>
<td align="right">426</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/io_uring_enter.2.html">io_uring_enter</a>(<strong>unsigned int</strong> fd, <strong>u32</strong> to_submit, <strong>u32</strong> min_complete, <strong>u32</strong> flags, <strong>const sigset_t *</strong> sig, <strong>size_t</strong> sigsz)</code></td>
</tr>
<tr>
<td align="right">427</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/io_uring_register.2.html">io_uring_register</a>(<strong>unsigned int</strong> fd, <strong>unsigned int</strong> opcode, <strong>void *</strong> arg, <strong>unsigned int</strong> nr_args)</code></td>
</tr>
<tr>
<td align="right">428</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/open_tree.2.html">open_tree</a>(<strong>int</strong> dfd, <strong>const char *</strong> filename, <strong>unsigned</strong> flags)</code></td>
</tr>
<tr>
<td align="right">429</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/move_mount.2.html">move_mount</a>(<strong>int</strong> from_dfd, <strong>const char *</strong> from_pathname, <strong>int</strong> to_dfd, <strong>const char *</strong> to_pathname, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">430</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fsopen.2.html">fsopen</a>(<strong>const char *</strong> _fs_name, <strong>unsigned int</strong> flags)</code></td>
</tr>
<tr>
<td align="right">431</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fsconfig.2.html">fsconfig</a>(<strong>int</strong> fd, <strong>unsigned int</strong> cmd, <strong>const char *</strong> _key, <strong>const void *</strong> _value, <strong>int</strong> aux)</code></td>
</tr>
<tr>
<td align="right">432</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fsmount.2.html">fsmount</a>(<strong>int</strong> fs_fd, <strong>unsigned int</strong> flags, <strong>unsigned int</strong> attr_flags)</code></td>
</tr>
<tr>
<td align="right">433</td>
<td><code><a href="http://man7.org/linux/man-pages/man2/fspick.2.html">fspick</a>(<strong>int</strong> dfd, <strong>const char *</strong> path, <strong>unsigned int</strong> flags)</code></td>
</tr>
</table>
