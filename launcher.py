import json
import subprocess
import sys
from pathlib import Path
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gdk

#constraints
APP_DIR = Path(__file__).parent
CONFIG_FILE = APP_DIR / "launcher-config.json"

#helpers
def run_cmd(command):
	subprocess.Popen(command, shell=True)

#app class
class Launcher(Gtk.Application):
	def __init__(self):
		super().__init__(application_id="local.special.launcher")
		self.apps = json.loads(CONFIG_FILE.read_text())
		self.selected = 0

	def do_activate(self):
		win = Gtk.ApplicationWindow(application=self)
		win.set_title("Special Launcher")
		win.set_default_size(500, 250)

		label = Gtk.Label(label="Special launcher is running")
		win.set_child(label)

		win.present()

app = Launcher()
app.run()
