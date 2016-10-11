# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-10-11 13:20:36
# @Last Modified 2016-10-11
# @Last Modified time: 2016-10-11 13:38:41

import sys
import sublime
import sublime_plugin

package_name = 'snippet_maker'

# ============================ upgrader ===================================
# this handles the upgrading of the package
# and really doesnt need to be messed with.


def plugin_loaded():
    from package_control import events

    if events.install(package_name):
        print('Installed %s!' % events.install(package_name))
    elif events.post_upgrade(package_name):
        print('Upgraded to %s!' % events.post_upgrade(package_name))

def plugin_unloaded():
    from package_control import events

    if events.pre_upgrade(package_name):
        print('Upgrading from %s!' % events.pre_upgrade(package_name))
    elif events.remove(package_name):
        print('Removing %s!' % events.remove(package_name))
# Compat with ST2
if sys.version_info < (3,):
    plugin_loaded()
    unload_handler = plugin_unloaded

# ============================ upgrader ===================================


#==========================================================================
#     creates a new snippet out of the current file being viewed
#==========================================================================
class new_snippet_from_file(sublime_plugin.TextCommand):
    def run(self, edit):
        # gives the range of the text in the file
        allcontent = lambda: sublime.Region(0, self.view.size())

        # returns the full text of the file
        get_text = lambda: self.view.substr(allcontent())

        print("text recieved:\n\n{}".format(get_text()))
