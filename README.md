# EQ Maker for pipewire

### Requirements
- python3
- python3-gi
- pipewire

> [!NOTE]
> pw_eq_maker_autoeq.py is a version that can load [AutoEQ](https://www.autoeq.app/) Files (use EasyEffects on ***select equalizer app***)

### Usage
```python3 pw_eq_maker.py```

or

```python3 pw_eq_maker_autoeq.py```

- adjust the slider values for gain
- you can change the Q-Factor above the slider (click to open popup or use mouse wheel)
- you can change the frequency below the slider (click to open popup or use mouse wheel)
- choose ***Save*** from the menu at the headerbar

>a file named sink-eq10.conf will be created in the script folder

>copy the file 'sink-eq10.conf' to the folder ~/.config/pipewire/pipewire.conf.d

- restart pipewire or restart computer
- open your sound settings app
- choose ***Pipewire Equalizer*** as output

![screenshot](https://github.com/Axel-Erfurt/pipewire-eq-maker/blob/main/screenshot.png?raw=true)

### Credits
Thanks to [demonich](https://github.com/demonich)
