# yt_clipper

yt_clipper is a relatively simple way to clip videos from popular platforms (for now YouTube, WeVerse, Naver TV, and AfreecaTV).
It provides a graphical UI for video editing that creates instructions in `json` format for clipping the video.
These instruction files are small and in plain text so they can be easily read, modified, and shared with others.
The `clipper script` component provides a way to process these instructions and generate the clips you want.

# Video Quick Start

For a video quickstart check out this video: <https://imgur.com/a/gQ4KItt>

# Quick Start Guide

Visit [this quickstart guide](https://github.com/exwm/yt_clipper/blob/master/quickstart.md) to get up and running with `yt_clipper`.

The contents of the quickstart guide are included here for convenience:

1) First install a user script extension (preferably Tampermonkey) for your browser (preferably chrome).
   - See [this article](https://openuserjs.org/about/Userscript-Beginners-HOWTO) for more information.
2) Next install the `markup script` component of `yt_clipper` by clicking [here](https://openuserjs.org/install/elwm/yt_clipper.user.js).
3) Install the standalone `clipper script` component of `yt_clipper` by visiting [Clipper Script Installation](https://github.com/exwm/yt_clipper#clipper-script-installation).
4) Visit a YouTube video page. Check that the `markup script` is [active on the page](https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_active_on_page.png). Refresh the page if it is not active.
5) Press **Alt+Shift+A** to activate the `markup script` and its hotkeys. You should see a [flash message](https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_hotkeys_activated.png) below the video.
   - Use the various hotkeys to add marker pairs and edit settings to specify how to clip the video.
     - **A** to add markers, **Z** to undo markers, **Shift+Mouseover** a yellow end marker to open [its settings editor](https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_marker_pair_editor.png).
     - **W** to open global settings editor, **Shift+W** to toggle additional settings.
   - Click the [shortcuts reference toggle](https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_shortcuts_table.png) in the video player bar for an overview of all shortcuts.
   - Hover over an option in a settings editor to see a [tooltip](https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_tooltip.png) describing the option.
6) Use the **S** key to save markers data in `.json` format.
7) Generate webms using the saved markers data and the `clipper script`.
   - **Windows:** Drag and drop the saved markers data onto the `yt_clipper_auto.bat`.
   - **Mac:** Launch the `yt_clipper_auto.sh` program, drag and drop the saved markers data onto the terminal, and hit **Enter**.
   - Find generated webms in `yt_clipper/webms/title-suffix` folder where `title-suffix` is the file name stem of the markers data file.
   - See [this section](https://github.com/exwm/yt_clipper#additional-helper-scripts) for details on the other helper scripts available.
8) See the [full instructions](https://github.com/exwm/yt_clipper) for more detail and advanced usage as well as changelogs.
9) Check the [GitHub Releases](https://github.com/exwm/yt_clipper/releases) and the [changelog](https://github.com/exwm/yt_clipper/blob/master/changelog.md) for updates as there is not yet an automated mechanism.
10) Join the [`yt_clipper` discord server](https://discord.gg/5RVGNCU) if you want further help or want to contribute.

# Notices

- Windows users getting ffmpeg crashes may want to try the following:
  - Update visual c++ redistributables:
    - For 64-bit Windows: <https://aka.ms/vs/16/release/vc_redist.x64.exe>
    - For other Windows versions and older redistributables check this page: <https://support.microsoft.com/help/2977003/the-latest-supported-visual-c-downloads>.
  - Switch to static ffmpeg build: <https://github.com/BtbN/FFmpeg-Builds/releases> and find the latest release titled something like `ffmpeg-N-101776-gd4575982f4-win64-gpl.zip`.
    - Replace contents of `yt_clipper_win_*/bin` with the contents of the `bin` folder in the ffmpeg zip.

# Browser Support

- Works best on Chrome with the Tampermonkey extension and YouTube video in theater mode.
- You may need to refresh the video page and ensure this user script is active.
- FireFox, Opera, and most Chromium-based browsers not fully tested, but reportedly work as intended.
  - FireFox audio slowdown stutters and in mainline FireFox has a min speed of 0.5.
- Other browsers may or may not work as intended.

# Video Platform Support

YouTube is the primary video platform supported by yt_clipper. Other supported platforms are listed below.

1. YouTube
2. Weverse (at least Weverse Lives)
3. Naver TV
4. AfreecaTV (at least VODs)
5. Local storage videos (<https://exwm.github.io/yt_clipper/>)
    1. If the platform you want to use isn't directly supported, you can download the video manually and then use the yt_clipper generic video platform.
    2. Load a video from local storage by dragging and dropping the video onto the player, then activate the yt_clipper markup script as usual.

## AfreecaTV Support Notes

* AfreecaTV clips use the hls (http live streaming) protocol which is not as reliable as other protocols.
* Short AfreecaTV clips (about 1 second or shorter) may produce empty video files when.
* AfreecaTV VODs come in multiple video file parts and clips that span multiple parts are not currently supported.

# Related Scripts

- Check out the companion script with tools for making some tasks on `gfycat.com` easier (e.g., quickly tagging multiple gfys, copying gfy links in various formats) at <https://openuserjs.org/scripts/elwm/gfy-tools>.

# Table of Contents

- [yt\_clipper](#yt_clipper)
- [Video Quick Start](#video-quick-start)
- [Quick Start Guide](#quick-start-guide)
- [Notices](#notices)
- [Browser Support](#browser-support)
- [Video Platform Support](#video-platform-support)
  - [AfreecaTV Support Notes](#afreecatv-support-notes)
- [Related Scripts](#related-scripts)
- [Table of Contents](#table-of-contents)
- [Terminology and Installation](#terminology-and-installation)
- [Markup Script Shortcuts](#markup-script-shortcuts)
  - [Marker Shortcuts](#marker-shortcuts)
  - [Cropping Shortcuts](#cropping-shortcuts)
  - [Video Playback and Preview Shortcuts](#video-playback-and-preview-shortcuts)
  - [Frame Capturing Shortcuts](#frame-capturing-shortcuts)
  - [Save and Load Shortcuts](#save-and-load-shortcuts)
  - [Miscellaneous Shortcuts](#miscellaneous-shortcuts)
  - [Dynamic Speed and Crop Shortcuts](#dynamic-speed-and-crop-shortcuts)
    - [Common Dynamic Chart Shortcuts](#common-dynamic-chart-shortcuts)
    - [Dynamic Speed Chart Shortcuts](#dynamic-speed-chart-shortcuts)
    - [Dynamic Crop Chart Shortcuts](#dynamic-crop-chart-shortcuts)
    - [ZoompPan Mode](#zoomppan-mode)
    - [Dynamic Crop Tips](#dynamic-crop-tips)
- [Useful YouTube Controls](#useful-youtube-controls)
- [Tips](#tips)
  - [User Script Tips](#user-script-tips)
  - [Clipper Script Tips](#clipper-script-tips)
- [Encoding Settings Guide](#encoding-settings-guide)
  - [Video Codecs](#video-codecs)
  - [Articles on CRF and vp9 Encoding](#articles-on-crf-and-vp9-encoding)
  - [Tips and Settings](#tips-and-settings)
    - [Markup Script Tips](#markup-script-tips)
    - [Clipper Script Tips](#clipper-script-tips-1)
  - [Gamma Correction](#gamma-correction)
- [Clipper Script Source](#clipper-script-source)
- [Clipper Script Usage](#clipper-script-usage)
  - [Clipper Default Arguments Files](#clipper-default-arguments-files)
- [Clipper Script Preview Shortcuts](#clipper-script-preview-shortcuts)
- [Clipper Script Installation](#clipper-script-installation)
  - [Linux Installation](#linux-installation)
  - [Manual and Beta/Alpha Version Installation](#manual-and-betaalpha-version-installation)
  - [Additional Helper Scripts](#additional-helper-scripts)
    - [Utility Scripts](#utility-scripts)
      - [Merge Utility Script](#merge-utility-script)
- [All Releases](#all-releases)
- [Clipper Script Dependencies](#clipper-script-dependencies)
- [Changelog](#changelog)

# Terminology and Installation

- `Markup script` refers to the user script installed in your browser through a user script extension. It is used to mark up videos (e.g. on YouTube) before creating webm clips.
  - The required user script extension, for example_Tampermonkey_, can be installed from the appropriate add-on store from your browser.
  - See <https://openuserjs.org/about/Userscript-Beginners-HOWTO> for more information on user scripts.
- `Clipper script` refers to the python script (`.py` )or the installation that consumes marker data in `json` format to generate webm clips.
  - See [Clipper Script Usage](#clipper-script-usage) for usage instructions.
  - See [Clipper Script Installation](#clipper-script-installation) for installation instructions.

# Markup Script Shortcuts

First ensure the script is active on the page by checking your user script extension.

- ![yt_clipper_active_on_page](https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_active_on_page.png)

**Alt+Shift+A:** Toggle hotkeys on/off. A green message will flash below the video indicating hotkeys are enabled.

A shortcuts reference can be toggled by clicking the scissor icon in the video controls bar.

- ![yt_clipper_shortcuts_table](https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_shortcuts_table.png)

## Marker Shortcuts

**A:** Add marker at current time (start = green, end = yellow, selected = black center). Multiple marker pairs can be added simultaneously.

**Z:** Undo last marker.

**Shift+Z:** Redo last undone marker.

**Ctrl+Shift+Alt+Z:** Delete currently selected marker pair. Does nothing if no pair selected.

**Shift+Mouseover End Marker (Yellow) or Left-Click Any Marker Numbering:** Toggle marker pair editor. Selected marker pairs have a black center.
  ![yt_clipper_marker_pair_editor](https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_marker_pair_editor.png)

- Modified marker pair settings are accented orange while settings redundant with a global setting are accented red.
- Reorder marker pairs using the input box in the title of the marker pair settings panel.
- Edit pair crop or speed multiplier.
- Edit `Title Prefix` that will be prepended to the `Title Suffix` and used in the webm name for the marker pair.

**Ctrl+Up**: Select/deselect the most recently selected marker pair or else the first available pair.

**Ctrl+Down**: Toggle auto-hiding of unselected marker pairs. Hidden marker pairs cannot be selected with the mouse.

**Adjusting marker position/time:**

- While a pair is selected use **Shift+Q/Shift+A** to move the start/end marker to current time.
  - Adjust marker position more precisely by first using the **<** and **>** keys to seek videos frame by frame.
- Use **Alt+Shift+Mousewheel** and scroll up/down to move marker one frame forward/backward.
  - When performed on the left half of the window moves the start marker and on the right half the end marker.
- **Alt+Click+Drag** a marker numbering to quickly make rough adjustments to the marker's time.
- Use **Alt+Z/Alt+Shift+Z** to undo/redo marker moves as well as speed and crop changes.
  - Undo/redo history is kept separately for each marker pair.
**Navigating marker pairs without the mouse:**

- Jumping to and selecting marker pairs without the mouse
  - **Ctrl+Left/Right:** Jumps to the nearest previous/next marker.
  - **Alt+Left/Right:** Select the next/previous marker pair relative to the currently or previously selected pair.
  - **Ctrl+Alt+Left/Right:** Select the next/previous marker pair _and jump to its start marker_.

**W:** Global settings editor:
  ![yt_clipper_globals_editor](https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_globals_editor.png)

1. Modified global settings are accented red.
2. Change default new marker speed or crop.
   - Any new markers added will use these defaults, but this will not update existing markers.
   - To update existing markers to the default new marker speed/crop use **Alt+Shift+Q/Alt+Shift+X**.
3. Specify crop resolution (automatically scales any existing crops on change).
   - This resolution must match the downloaded video's resolution.
   - By default the max available video resolution is downloaded by the `clipper script` and the crop resolution auto-scaled if a mismatch is detected.
4. Specify any webms you want to merge from the clipped webms.
   - Very fast as it does not require re-encoding webms.
   - The format is similar to that for printer page ranges:
     - Each merge is a comma separated list of marker pair numbers or ranges (e.g., '1-3,5,9' = '1,2,3,5,9').
     - Multiple merges are separated with semicolons (e.g., '1-3,5,9;4-6,8' will create two merged webms).
5. Specify `Title Suffix` appended to each marker pair `Title Prefix` to produce its `Full Title`.
   - By default the `Title Suffix` is the YouTube video ID in square brackets (e.g., \[Bey4XXJAqS8\]).
   - The `Title Suffix` is used for the name of the folder containing all generated webms.

**Shift+W:** Open additional settings when the global settings editor or a marker pair editor is open.

- Settings left blank with a placeholder of `Auto` will be automatically calculated based on the input video bitrate and other video properties. This is the recommended default.
- Marker pair settings are overrides that if set will override the global value for that marker pair only.
- Marker pair settings set to `Inherit` will get their value from the global settings.
- Global settings set to `Inherit` will get their value from the command line options or the `yt_clipper_options` helper script prompt.
- See [Encoding Settings Guide](#encoding-settings-guide) for more information and tips about the possible settings.
- Marker Pair Overrides:
  - ![yt_clipper_marker_pair_editor_overrides](https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_marker_pair_editor_overrides.png)
- Global Encode Settings:
  - ![yt_clipper_globals_editor_additional_settings](https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_globals_editor_additional_settings.png)

**Alt+Shift+Q/alt+Shift+X:** Update all existing markers to default new marker speed (**Q**) or crop (**X**).

- Set the default new marker speed or crop using **W**.

## Cropping Shortcuts

**X:** When marker or defaults editor is open, begin drawing crop.

- **Click+Drag** on the video to set draw a rectangular crop.

- While drawing crop, pressing **X** again will cancel drawing.

- Crop is given as `x-offset:y-offset:width:height`. Each value is a positive integer in pixels. `Width` and `height` can also be `iw` and `ih` respectively for input width and input height.

**Ctrl+X:** Cycle crop dim opacity by 25% plus one stop point at 90%.
**Ctrl+Shift+X:** Toggle crop crosshair.

**Mouse-Based crop Adjustment:**

- **Ctrl+Hover:** Indicate potential drag action when hovering over crop.
- **Ctrl+Click+Drag:** Drag and move crop or resize crop in the indicated directions.
  - Can release **Ctrl** after dragging begins. Dragging ends when mouse is released.
- **Ctrl+Alt+Drag:** Approximately aspect-ratio-locked mouse resizing of crop.
- **Ctrl+Shift+Drag:** Center-out resize/draw of crop.
- **Ctrl+Shift+Drag:** Horizontally-fixed (Y-only) drag of crop.
- **Ctrl+Alt+Drag:** Vertically-fixed (X-only) drag of crop.

  ![yt_clipper_crop_preview.png](https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_crop_preview.png)

**Arrow Key Crop Adjustment**:

- When a crop input box has focus:
  - **UpArrow/DownArrow:** Increment/decrement the value indicated by the current cursor position by `10`.
- When a crop input box does not have focus:
  - **Alt+X:** Toggle crop adjustment with arrow keys.
  - **UpArrow/DownArrow:** Increment/decrement the `y offset` by `10`.
  - **LeftArrow/RightArrow:** Increment/decrement the `x offset` by `10`.
  - **Ctrl** modifier key changes target from `y offset` to `height` or from `x offset` to `width`.
- The **Alt** and **Shift** modifier keys alter the increment/decrement amount.
  - **Alt** sets the amount to `1`, **Shift** to `50`, **Alt+Shift** to `100`.
- The resulting crop values are clamped to valid values.

## Video Playback and Preview Shortcuts

**Shift+Mouse-Wheel:** Scroll the mouse wheel up/down over the video to skip forward/backward one frame per tick.

**Alt+Click+Drag:** Scrub/seek video time backward or forward by dragging left or right respectively.

**C:** Toggle previewing marker pair speed.

- Video playback speed is automatically set to the speed of the current marker pair.
- When outside of a marker pair the playback speed is force set to 1. Toggle off the speed preview to change the player speed manually.

**Shift+C:** Toggle auto looping of currently selected marker pair.

**Ctrl+Alt+X:** Toggle previewing crop in modal window. The modal window can be left+clicked to play/pause and right-clicked to seek the video.

**Ctrl+Shift+C:** Toggle auto crop chart section looping. This setting takes precedence over auto marker pair looping.

**Alt+C:** Toggle auto previewing gamma correction setting when between a marker pair.

**Alt+Shift+C:** Toggle fade loop previewing.

- Note that fade duration defaults to 0.7 seconds and is clamped to a minimum of 0.1 seconds and a maximum of 40% of the output clip duration.

**Ctrl+Alt+Shift+C:** Toggle all previews.

- If any preview feature is disabled, turns it on. If all preview features are enabled, disables all of them.

- Works only when in fullscreen mode or theater mode.
- **Note that this does not yet work with drawing and previewing crops and should be disabled when doing so.**
- **This feature is only for watching or previewing the video, and does not affect webm output.**

**Shift+R:** Toggle big video previews on video progress bar hover.

**Q:** Toggle auto force setting of video playback speed. Takes precedence over any marker pair speed. This can be useful to try out different playback speeds without modifying settings.

**Alt+Q:** Cycle the force-set video speed down by 0.25. Use **Q** to toggle force settings video speed.

**R/Alt+R:** Toggle between a 90 degree clockwise/counter-clockwise rotation and no rotation.

- Note that this is only a preview and you must set the rotation in the global settings editor opened with **W** to rotate the output video.

## Frame Capturing Shortcuts

**E:** Capture frame at current time of video at currently selected video quality/resolution.

- Frame must be buffered and loaded.
- Opens a pop-up window where captured frames are saved.
  - **Download** and **Delete** buttons are provided above each captured frame.
  - You may need to allow pop-ups from `https://www.youtube.com` in your browser settings.

  ![yt_clipper_frame_capturer](https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_frame_capturer.png)

**Alt+E** Trigger zipping of all captured frames for download.

## Save and Load Shortcuts

**S:** Save markers info to a `.json` file.

- Can be dropped onto the clipper script installation's helper scrips like `yt_clipper_auto` on Windows. On Mac, run the helper script and try dragging and dropping in the window that opens up when prompted.
- When using the python source of the `clipper script` use`--json/-j` and pass the path of the markers data file.

**Alt+S:** Copy markers `json` data to clipboard. Useful if saving breaks.

**G:** Toggle markers data commands UI. Allows for uploading and loading markers data files in `.json` format and for restoring markers data auto-saved in browser local storage.

- To upload and reload markers data, click `Choose File`, pick your markers `json` file, then click `Load`.
  - ![yt_clipper_load_markers](https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_load_markers.png)

## Miscellaneous Shortcuts

**Shift+F:** Flatten a VR video to make it easier to crop.

## Dynamic Speed and Crop Shortcuts

### Common Dynamic Chart Shortcuts

**D:** Toggle dynamic speed chart.

**Alt+D:** Toggle dynamic crop chart.

**Shift+Click:** Add a point at the clicked location.

**Alt+A:** Add a point at the current time.

**Alt+Shift+Click:** Delete a point.

**Right-Click:** Seek to time on bottom time-axis when clicking anywhere in chart area.

**Alt+Right-Click/Ctrl+Alt+Right-Click:** Set chart looping start/end marker.

**Shift+D:** Toggle chart loop markers

- Note that chart loop markers only work when speed previewing is on with **C**.

**Ctrl+Mousewheel:** Zoom in and out of chart.

**Ctrl+Click:** Reset zoom.

**Click+Drag:** Drag a point to move it or drag chart area to pan when zoomed in.

**Alt+Z/Alt+Shift+Z:** Undo/redo marker moves as well as speed and crop changes.

- Undo/redo history is kept separately for each marker pair.

### Dynamic Speed Chart Shortcuts

See [Common Dynamic Chart Shortcuts](#common-dynamic-chart-shortcuts) for shortcuts shared between dynamic charts
like adding and removing points.

**D:** Toggle dynamic speed chart.

<img src="https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_speed_chart.jpg" alt="yt_clipper_speed_chart" style="width:500px;"/>

**Notes:**

- Points are auto-sorted based on their time value on adding or removing points or on drag-end when moving points.
- YouTube playback speed can only be set to a multiple of `0.05` and greater than or equal to `0.25`.
- Audio is not compatible with dynamic speed.

### Dynamic Crop Chart Shortcuts

See [Common Dynamic Chart Shortcuts](#common-dynamic-chart-shortcuts) for shortcuts shared between dynamic charts
like adding and removing points.

Dynamic crop allows for panning a crop in the default `pan-only` mode.
In `pan-only` mode the crops of all crop chart points are maintained equal.
For zooming and panning, enable  `zoompan` mode from the marker pair settings extended options (**Shift+W**).
In `zoompan` mode crops can change size for a zooming effect, but their aspect ratios are maintained equal.

**Alt+D:** Toggle dynamic crop chart.

**Left-Click:** Left-click a crop chart point to seek to it's time.

**Left-Click+Drag:** Left-click and drag a crop chart point to change it's time and seek/scrub the video.

**Ctrl+Shift+C:** Toggle auto crop chart section looping.

- A crop chart section is any two points on the chart.
- The current section is between a green start point and yellow end point. All other points are red.
- As the video time changes, the current crop chart section is automatically updated.
- Takes precedence over marker pair looping.

**Ctrl/Alt+Mouseover:** Select point as start/end of crop section.

- When the currently selected point is green then you are in start mode, and if it is yellow you are in end mode.
- The selected point's crop is editable and it's crop appears more brightly in a matching color (green or yellow).
- As the video time changes, the currently selected point is automatically updated to the start or end point of the new section maintaining the current mode where possible.
- Selected points have a black border and are square. Unselected points are circular.

**Alt+Mousewheel-Up/Down:** Intelligently toggle modes or select points. More specifically:

- **Alt+Mousewheel-Up:** If in end mode, toggle to start mode. If already in start mode, select next point and toggle to end mode.
- **Alt+Mousewheel-Down:** If in start mode, toggle to end mode. If already in end mode, select previous point and toggle to start mode.

**Ctrl+Alt+Shift+Mousewheel-Up/Down:** Set current crop point's crop to that of the next/previous point's crop.

**Ctrl+Shift+Click:** Toggle crop point easing between auto and instant.

- Points with instant easing enabled are darkened.
- Instant easing means that any pan or zoom from a previous point will happen instantly, causing the crop to jump. This is useful if there is a scene change in the video or very fast movement.

**A/Shift+A:** Set target crop component of all points following/preceding the currently selected point. Select crop components by placing your cursor in the crop input field in the marker pair settings.

- For example, let's say you want to align the X-position of all points following the currently selected point. Place your cursor by clicking in the crop input field in the first value. For example  `10|0:100:920:1080` where the `|` represents your cursor. Now hit the **A** key and all following crop points will have an X-Position of `100`.

### ZoompPan Mode

In `zoompan` mode crops can change size for a zooming effect, but their aspect ratios are maintained equal.
The usual crop shortcuts have different effects than usual in this mode as described here.

**Ctrl+Drag:** Resize crop while maintaining aspect ratio.

**Ctrl+Alt+Drag:** Freely resize the crop, updating the aspect ratio of all other crop points to match automatically.

**X:** Draw crop.

- **Click+Drag:** Draw crop while maintaining aspect ratio.
- **Alt+Click+Drag:** Freely draw crop, updating the aspect ratio of all other crop points to match automatically.

### Dynamic Crop Tips

- Use as few points as possible for smoother motion (each point with a crop different from its neighbors causes the crop motion to stop and then start again).
- Try enabling video stabilization to smooth out the motion, especially if many points are used.
- Pause the video and **Right-Click+Drag** to seek/scrub through the video. Use this to preview the crop movement with precise control.

# Useful YouTube Controls

1. Use **[space_bar]** or **K** to pause/play the video.
2. Use **<** and **>** to view a video frame by frame.
3. Use **Left-Arrow** and **Right-Arrow** to jump backwards or forwards by 5 seconds.

# Tips

## User Script Tips

1. If you're new to userscripts check out <https://openuserjs.org/about/Userscript-Beginners-HOWTO> for instructions.
2. Check out the companion script for copying gfy links from gfycat as reddit markdown at <https://openuserjs.org/scripts/elwm/gfy2md>.
3. Refresh the page if the script doesn't load and to clear markers when switching videos in the same window.
4. Videos can be marked up and the markers json or clipper script can be saved before higher quality levels are available, but the final generated webm quality depends on the quality formats available.

## Clipper Script Tips

1. The `clipper script` skips regenerating any existing webms.
   - This makes it easy to delete webms you want regenerated and by rerunning the script.
   - Use this to work incrementally, saving markers data, starting a batch encode, continuing to mark up, overwriting the markers data, and then rerunning the encoding.

# Encoding Settings Guide

## Video Codecs

The default video codec used by yt_clipper for encoding video clips is vp9 which is typically stored in a webm container in a file with the `.webm` extension. h264 and the newer h265/hevc are typically stored in an mp4 container.

You can use the `--video-codec` option to change video codecs. The clipper script help text (`yt_clipper --help`) is kept updated with the available video codecs.

Hardware-accelerated codecs use your GPU (or sometimes other hardware like your CPU) for faster encodes at the cost of some quality. Support for these codecs depends on your hardware and your operating system.

The Vulkan technology is supported by Linux and Windows across most modern GPUs (AMD/NVIDIA/Intel). MacOS and iOS are not yet supported. It requires ffmpeg >= 7.1.

Newer NVIDIA drivers may not work with vulkan-accelerated codecs. As of 2025-06-24 at least the following driver versions are confirmed to work:  565.90, 572.16.


yt_clipper supports `h264_vulkan` for Vulkan-based hardware-accleration of h264 encoding.

yt_clipper also supports `h264_nvenc` for NVIDIA GPU hardware-accelerated h264 encoding. This requires an NVIDIA GPU with NVENC support (most modern NVIDIA GPUs) and ffmpeg compiled with nvenc support. It is supported on Windows and Linux.

## Articles on CRF and vp9 Encoding

1. [Basic crf guide](https://slhck.info/video/2017/02/24/crf-guide.html)
2. [ffmpeg vp9 encoding guide](https://trac.ffmpeg.org/wiki/Encode/VP9)
3. [Google vp9 basic encoding](https://developers.google.com/media/vp9/the-basics/)
4. [vp9 encoding tests](https://github.com/deterenkelt/Nadeshiko/wiki/Tests.-VP9:-encoding-to-size,-part%C2%A01)

## Tips and Settings

### Markup Script Tips

1. Move between input fields with **Tab** and **Shift+Tab**.
2. Numeric input fields can be set using the **Up/Down** arrow keys or the **Mousewheel**.
3. Access additional settings, including various encoding settings using the **Shift+W** additional settings editors.
4. Hover over settings in the `markup script` to view tooltips describing each setting.
  ![yt_clipper_tooltip](https://raw.githubusercontent.com/exwm/yt_clipper/master/assets/image/yt_clipper_tooltip.png)

### Clipper Script Tips

1. The `clipper script` is set to use the vp9 encoder by default (encoding used for webm videos on YouTube).
2. Use `--help`, `-h`, or the `yt_clipper_options` helper script for additional options that can be enabled on the command line.
3. Encoding settings will be automatically selected, unless overridden, based on the detected bitrate and other properties of the input video.

## Gamma Correction

- Play around with the `gamma` setting to bring back shadow or highlight detail.
- Use **Alt+C** to preview `gamma values` with the `markup script`.
- A value of 1 does nothing. Use a value between 0 and 1 to bring back shadow detail and a value greater than 1 to bring back highlight detail.
- Refer to this [gamma correction guide](https://www.cambridgeincolour.com/tutorials/gamma-correction.htm) for more details.

# Clipper Script Source

- You can find the latest mainline clipper script python source file here: <https://github.com/exwm/yt_clipper/blob/master/src/clipper/yt_clipper.py>

# Clipper Script Usage

On the command line, the clipper script can be be used as a typical CLI program assuming you've installed it and added it to your PATH.

Example commands:

```sh
yt_clipper -h # Prints help. Details all options and arguments.

yt_clipper --markers-json markers.json # automatically generate webms using markers json

yt_clipper -j markers.json --input-video ./clip.webm  # provide a local input video

yt_clipper -j markers.json --preview  # preview marker pairs using ffplay

yt_clipper -j markers.json --format bestvideo[width<=1080] # specify download format used by youtube-dl
```

## Clipper Default Arguments Files

Default arguments for the `clipper` script may be set using a simple file format.
A `default_args.txt` file with comments explaining the usage is provided with the clipper script installation.
The file contents are copied below for convenience:

```txt
# By default, this args file will be read by yt_clipper to set default arguments.
# To see all arguments use the `yt_clipper_options` helper script or the `-h` argument.
# Lines that begin with a `#` in this file are comments and are ignored.
# To use other arg files use the `--arg-files` argument outside of an arg file.


# The following commented lines provide an example of how to use this file.
# The lines can be uncommented (by removing the `#`) to test their effects.

# --audio
# --two-pass
# -di -dn 2
# --youtube-dl-alternative yt_dlp
```

# Clipper Script Preview Shortcuts

See <https://ffmpeg.org/ffplay.html#While-playing>.

# Clipper Script Installation

There is an installation that does not require the dependencies below.

1. Extract the appropriate zip file anywhere:
   - Go to <https://github.com/exwm/yt_clipper/releases> and pick a release. In the assets, find the appropriate file for your platform.
2. Simply drag and drop the markers .json file onto the `yt_clipper_auto.bat` file on Windows or at the terminal prompt after executing `yt_clipper_auto` on Mac.
3. Use `Ctrl+C` if you need to cancel the process.
4. All generated webm clips will be placed in `./webms/<markers-json-filename>`.
5. Windows users may require [Microsoft Visual C++ 2010 Redistributable Package (x86)](https://www.microsoft.com/en-US/download/details.aspx?id=5555).

## Linux Installation

The clipper script requires Python version 3.8, while many distros will have a more recent version of python. This can be dealt with using [pipx](https://pipx.pypa.io):
```bash
pipx install git+https://github.com/exwm/yt_clipper --python 3.8 --fetch-missing-python
```

The package can be updated by running `pipx upgrade clipper`.

## Manual and Beta/Alpha Version Installation

**Markup script (js):** (1) Find the `yt_clipper*.js` file in the github release assets, (2) right-click > `copy address`, (3) open user script extension dashboard, (4) find and use option to add a script via url (in tampermonkey, utilities tab > `install from url`; in violentmonkey, `+` button at top > `install from url`).

_Alternatively_, (1) Download the `yt_clipper*.js` file from the github release assets, (2) open user script extension dashboard, (3) open yt_clipper for editing, (4) click inside the editor and select everything with `Ctrl+A`, (5) delete everything with say `backspace`, (6) drag and drop the markup script js file into the editor, (7) `Ctrl+S` to save.

**Clipper script (platform-specific zip):** Install as usual by extracting the zip file to a convenient location.

## Additional Helper Scripts

There are some alternative helper scripts for more options:

- Use `yt_clipper_options` to print all the available options and to be prompted for a string with additional options before running the script. This allows you to combine options (e.g., include audio and rotate and denoise).
  - The other helper scripts provide preconfigured subsets of these options.
- Use `yt_clipper_preview` to locally preview markers `json` data with `ffplay`.
  - _Cannot preview audio, video stabilization, or expanded color range._
- Use `yt_clipper_auto_download` to download video before processing markers.
- Use `yt_clipper_auto_input_video` to specify both markers `json` data and an input video for processing.
  - On Windows simply drag and drop both the `json` and the input video onto `yt_clipper_auto_input_video`.
  - On Mac, `yt_clipper_auto_input_video` will prompt for the `json` then the input video.

The helper scripts have a simple format. Copy and edit `yt_clipper_auto` in a text editor to create custom automated versions. For example you could add `--deinterlace` to enable deinterlacing or use `--only 2,5` to process only marker pairs 2 and 5.

- On Windows:

  ```bat
  @echo off
  chcp 65001
  cd /D "%~dp0"

  FOR %%A IN (%*) DO (
    REM you can add options after %%A of the next line as shown
    .\yt_clipper.exe --markers-json %%A
  )

  pause
  ```

- On Mac

  ```bash
  #!/bin/bash
  cd "$(dirname "$0")" || exit

  read -rp "First enter the paths of 1 or more markers json data files (you may be able to drag and drop files at the prompt): " JSONPROMPT

  IFS=$'\n' JSONS=( $(xargs -n1 <<< "$JSONPROMPT") )

  for JSON in "${JSONS[@]}"
  do
    if [ -f "$JSON" ]; then
      # you can add options after $JSON of the next line as shown
      ./yt_clipper --markers-json "$JSON"
    else
      echo "$JSON does not exist"
    fi
  done
  ```

### Utility Scripts

There several utility scripts provided as well that wrap ffmpeg or other tools either for convenience or additional functionality.

1. The `fast_trim` utility script takes a single video file as input and trims it quickly BUT approximately. The script prompts for a start time and an end time to trim the input video file. The output file name will be suffixed with `-trim`.
2. The `vid2gif` utility script converts an input video file to a `gif` with a small file size and resolution. The script will prompt for the output gif fps and scale/resolution.
3. The `preprocess_hevc` utility script preprocesses an input video file (likely `mp4`) with an `hevc` video stream to ensure compatibility with ffmpeg. You may need to use this script if you see errors like `Invalid data found when processing input` from ffmpeg when using `hevc` with the `--input-video`/`-i` option or the `yt_clipper_auto_input_video` helper script. The preprocessed output file name will be suffixed with `-preproc`.

#### Merge Utility Script

The `merge` utility script can be used to merge any webm files in any order:

- On mac, follow the prompts after running the utility script, providing the paths of 2 or more input files in the other you want them merged.
- On Windows:
  - Rename the webm files so they sort in desired lexicographic order.
  - Select/highlight all webms to be merged in your file explorer and drag and drop them onto the `merge.bat` script.
  - The output file name will be `-merged` appended to the first input file name.
  - Check the `merge.txt` file to confirm the correct videos were merged in the correct order.

# All Releases

Since clipper script `v3.6.1`, releases can be tracked here: <https://github.com/exwm/yt_clipper/releases>.

# Clipper Script Dependencies

These dependencies must be manually installed when not using the clipper script installation:

- ffmpeg must be in your path: (<https://www.ffmpeg.org/download.html>).
- install required python packages as listed in the `requirements.txt`:
  - `pip install -r ./src/clipper/requirements.txt`

# Changelog

For a complete changelog, including beta and alpha releases,
see <https://github.com/exwm/yt_clipper/blob/master/changelog.md>.

For pre-version-unification (between `markup` and `clipper` scripts) changelogs see <https://github.com/exwm/yt_clipper/blob/master/changelog-pre-version-unification.md>.
