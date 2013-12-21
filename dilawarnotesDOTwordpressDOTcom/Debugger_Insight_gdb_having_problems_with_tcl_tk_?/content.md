~~~~ 
title: Debugger Insight (gdb) having problems with tcl/tk ?
type: post
status: publish
id: 524
tag: gdb
tag: insight debugger
tag: tcl tk and insight debugger
category: Uncategorized
~~~~

You may get following error on your linux machine while invoking
[insight debugger](http://sourceware.org/insight/), \

    Tk_Init failed: Can't find a usable tk.tcl in the following directories: /usr/local/share/tk8.4 /usr/local/lib/tk8.4 /usr/lib/tk8.4 /usr/local/library /usr/library /usr/tk8.4.1/library /tk8.4.1/library  /usr/local/share/tk8.4/tk.tcl: no event type or button # or keysym no event type or button # or keysym while executing "bind Text { %W yview scroll [expr {- (%D / 120) * 4}] units }" (file "/usr/local/share/tk8.4/text.tcl" line 461) invoked from within "source /usr/local/share/tk8.4/text.tcl" (in namespace eval "::" script line 1) invoked from within "namespace eval :: [list source [file join $::tk_library $file.tcl]]" (procedure "SourceLibFile" line 2) invoked from within "SourceLibFile text" (in namespace eval "::tk" script line 10) invoked from within "namespace eval ::tk { SourceLibFile button SourceLibFile entry SourceLibFile listbox SourceLibFile menu SourceLibFile panedwindow SourceLibFile ..." invoked from within "if {$::tk_library ne ""} { if {[string equal $tcl_platform(platform) "macintosh"]} { proc ::tk::SourceLibFile {file} { if {[catch { namesp..." (file "/usr/local/share/tk8.4/tk.tcl" line 393) invoked from within "source /usr/local/share/tk8.4/tk.tcl" ("uplevel" body line 1) invoked from within "uplevel #0 [list source $file]"  This probably means that tk wasn't installed properly.

\
The proximate cause is "MouseWheel" event type is not recognized. One
fix, if you don't care about the crazy MouseWheel, is to comment out the
entire "bind" for MouseWheel events. This happens at lines 178 through
198 of "listbox.tcl", and lines 453 through 474 of "text.tcl". These
lines location may be different in your library. Both files in the tk
support directory path listed in the error message. \
 \
After I have commented them out, my application is launching without any
problem.Interestingly, these files "text.tcl" and "listbox.tcl", mention
that these "MouseWheel" events may not work on linux. \
 \
Stupid mouse! Who cares about mouse, I use xmonad.
