##Launching

Run manually:

```bash
python launcher.py


Run with keybind:

The launcher does not set it's own keybind. This should be configured by the user's desktop environment, window manager, or compositor.

For example on labwc you can add this to ~/.config/labwc/rc.xml :

		<keybind key="W-space"> #or whatever keybind you want
			<action name="Execute">
				<command>python /home/USER/apps/special-launcher/launcher.py</command> #whatever your path is
			</action>
		</keybind>
