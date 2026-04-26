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
		config = json.loads(CONFIG_FILE.read_text())
		self.apps = config["apps"]
		self.selected=0

	def do_activate(self):
		self.win = Gtk.ApplicationWindow(application=self)
		self.win.set_title("Special Launcher")
		self.win.set_default_size(700, 400)
		self.win.set_focusable(True)

		self.area = Gtk.DrawingArea()
		self.area.set_focusable(True)
		self.area.set_draw_func(self.draw)
		
		key = Gtk.EventControllerKey()
		key.connect("key-pressed", self.on_key)
		self.win.add_controller(key)
		
		self.win.set_child(self.area)
		self.win.present()
		self.area.grab_focus()

	def on_key(self, _controller, keyval, _keycode, _state):
		if keyval == Gdk.KEY_Right:
			self.selected = (self.selected + 1) % len(self.apps)
			self.area.queue_draw()
			return True

		if keyval == Gdk.KEY_Left:
			self.selected = (self.selected - 1) % len(self.apps)
			self.area.queue_draw()
			return True

		if keyval == Gdk.KEY_Return:
			cmd = self.apps[self.selected]["command"]
			run_cmd(cmd)
			self.win.close()
			return True

		if keyval == Gdk.KEY_Escape:
			self.win.close()
			return True

	def draw(self, area, cr: cairo.Context, width, height):
		#background
		cr.set_source_rgba(0.02, 0.02, 0.02, 0.82)
		cr.rectangle(0, 0, width, height)
		cr.fill()

		#title
		cr.set_source_rgba(0, 0, 0, 1)
		cr.select_font_face("Sans")
		cr.set_font_size(32)
		cr.move_to(40, 60)
		cr.show_text("SPECIAL LAUNCHER")

		#test app text
		cr.set_font_size(22)
		y=120

		for i, app in enumerate(self.apps[:6]):
			if i ==self.selected:
				cr.set_source_rgba(1, 1, 0.2, 1)#highlighted
			else:
				cr.set_source_rgba(1, 1, 1, 1)
			
			cr.move_to(60, y)
			cr.show_text(app["name"])
			y += 40

app = Launcher()
app.run()
