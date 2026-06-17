<div align="center">

  <h1>Audio Visualizer Remake</h1>

  <p>
    <b>A colorful Python remake of my audio spectrum visualizer, focused on cleaner FFT structure, better UI, and smoother music-reactive bars.</b>
  </p>

  <p>
    <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img alt="Pygame" src="https://img.shields.io/badge/Pygame-0E7A3E?style=for-the-badge&logo=python&logoColor=white" />
    <img alt="NumPy" src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
    <img alt="FFT" src="https://img.shields.io/badge/FFT-FF006E?style=for-the-badge" />
    <img alt="Audio" src="https://img.shields.io/badge/Audio_Reactive-FFB703?style=for-the-badge" />
  </p>

  <p>
    <a href="#features">
      <img alt="Features" src="https://img.shields.io/badge/Features-00C2A8?style=for-the-badge" />
    </a>
    <a href="#demo-video">
      <img alt="Demo video" src="https://img.shields.io/badge/Demo_Video-FF3864?style=for-the-badge" />
    </a>
    <a href="#how-it-works">
      <img alt="How it works" src="https://img.shields.io/badge/How_It_Works-7C3AED?style=for-the-badge" />
    </a>
    <a href="#why-i-built-this">
      <img alt="Why I built this" src="https://img.shields.io/badge/Why_I_Built_This-F59E0B?style=for-the-badge" />
    </a>
  </p>

</div>

---

## Overview

**Audio Visualizer Remake** is a desktop audio visualizer built with Python and Pygame. It has two main modes:

| Mode | What it does |
| --- | --- |
| **Import a file** | Opens a native file picker, plays the selected audio file, reads its samples, extracts metadata/artwork, and renders a live FFT spectrum. |
| **Live mode** | Captures microphone/system input through `sounddevice` and visualizes the incoming audio in real time. |

The visualizer renders `120` rounded spectrum bars across a `1280x720` Pygame window, using a bright red-to-yellow-to-cyan palette inspired by the colorful energy of *In Rainbows*.

## Demo Video

> Demo video placeholder: add the recording link or GitHub uploaded video here.

```md
https://github.com/user-attachments/assets/your-demo-video-id
```

## Preview Space

Add a screenshot or GIF here when the visualizer is ready to show:

```md
<img width="900" alt="Audio Visualizer Remake preview" src="YOUR_SCREENSHOT_URL_HERE" />
```

## Features

<table>
  <tr>
    <td><b>File visualizer</b></td>
    <td>Import a local audio file, play it, and render its spectrum while it runs.</td>
  </tr>
  <tr>
    <td><b>Live visualizer</b></td>
    <td>Capture input audio using <code>sounddevice</code> and display its frequency energy in real time.</td>
  </tr>
  <tr>
    <td><b>FFT processing</b></td>
    <td>Uses NumPy real FFT values and maps them into logarithmic frequency buckets.</td>
  </tr>
  <tr>
    <td><b>120 animated bars</b></td>
    <td>Draws smooth rounded bars with frame-to-frame interpolation.</td>
  </tr>
  <tr>
    <td><b>Album art</b></td>
    <td>Reads embedded artwork through TinyTag and shows it beside the current track info.</td>
  </tr>
  <tr>
    <td><b>Playback progress</b></td>
    <td>Displays elapsed time, total duration, and a progress bar for imported files.</td>
  </tr>
  <tr>
    <td><b>Simple mode menu</b></td>
    <td>Starts with two clear choices: import a file or switch to live mode.</td>
  </tr>
</table>

## Tech Stack

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-1D4ED8?style=flat-square&logo=python&logoColor=white" />
  <img alt="Pygame" src="https://img.shields.io/badge/Pygame-16A34A?style=flat-square&logo=python&logoColor=white" />
  <img alt="NumPy" src="https://img.shields.io/badge/NumPy-2563EB?style=flat-square&logo=numpy&logoColor=white" />
  <img alt="SoundDevice" src="https://img.shields.io/badge/sounddevice-DC2626?style=flat-square" />
  <img alt="SoundFile" src="https://img.shields.io/badge/soundfile-F97316?style=flat-square" />
  <img alt="TinyTag" src="https://img.shields.io/badge/TinyTag-9333EA?style=flat-square" />
  <img alt="Tkinter" src="https://img.shields.io/badge/Tkinter-0F766E?style=flat-square" />
</p>

| Layer | Technology | Role |
| --- | --- | --- |
| Language | `Python` | Main application logic. |
| Window/UI | `pygame` | Window, drawing, buttons, events, text, and playback. |
| FFT/math | `numpy` | Frequency analysis and logarithmic bucket mapping. |
| Live input | `sounddevice` | Microphone/input stream capture. |
| File samples | `soundfile` | Reads audio data for FFT visualization. |
| Metadata/art | `tinytag` | Reads duration, filename metadata, and embedded image data. |
| File picker | `tkinter` | Native file selection dialog. |

## Project Structure

```text
.
|-- app.py           # Main Pygame app, modes, playback, FFT drawing, UI routing
|-- source.py        # Button helper and live audio callback storage
|-- requirements.txt # Python dependency list placeholder
|-- font.ttf         # Custom UI font used by buttons
|-- Radiohead.mp3    # Local test/demo audio file
`-- README.md        # Project documentation
```

## Run Locally

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the Python packages used by the app:

```bash
pip install pygame numpy sounddevice soundfile tinytag
```

Run from the repository root so `font.ttf` and local assets resolve correctly:

```bash
python app.py
```

## Controls

| Input | Action |
| --- | --- |
| Mouse click on **import a file** | Choose an audio file from disk. |
| Mouse click on **live mode** | Start live input visualization. |
| `Esc` in file mode | Stop playback and return to the menu. |
| `Esc` in live mode | Return to the menu. |
| Window close | Quit the app. |

## How It Works

### 1. Mode Selection

The app starts in menu mode with two Pygame buttons:

| Button | Result |
| --- | --- |
| `import a file` | Opens a Tkinter file picker, loads the selected audio, starts playback, and switches to file visualization mode. |
| `live mode` | Switches to the live input spectrum using the active `sounddevice` stream. |

### 2. File Visualization

When a file is imported, `soundfile` reads the sample data while `pygame.mixer.music` handles playback. Each frame takes a `2048` sample chunk, converts stereo data to mono when needed, runs `np.fft.rfft`, and maps the result into `120` logarithmic frequency buckets.

The bars are normalized, smoothed, and drawn from the bottom of the screen upward. Track name, album art, elapsed time, total duration, and a progress bar are drawn on top.

### 3. Live Visualization

Live mode starts an input stream through `sounddevice`. The callback receives incoming audio frames, mixes channels down to mono, computes an FFT snapshot, and stores the latest spectrum in `source.last_s`.

The main Pygame loop reads that latest spectrum, groups it into logarithmic buckets, smooths the values, and renders the same colorful bar display used by file mode.

### 4. Smoothing

The visualizer blends new FFT values with previous frame values so the bars feel responsive without flickering:

```python
smooth_vals = smooth_vals * 0.8 + bar_val * 0.2
```

Live mode uses a slightly slower blend:

```python
smooth_vals = smooth_vals * 0.85 + bar_val * 0.15
```

## Why I Built This

> the previous visualizer was good but not as i wanted it to be , plus my fft understanding didnt reach the desired level ,
>so i rebuilt it in pygame and python , though i didnt rebuild the whole fft fonction just like in the fft versio n , i used >numpy's fonctions and focused on the chunks/channels/ui parts, even with that ,i still gained more understanding abt the fft overall   


## Current Status

| Area | Status |
| --- | --- |
| Menu UI | Working |
| File picker | Working |
| File playback | Working |
| FFT bars | Working |
| Live input mode | Working, but depends on the correct local input device |
| Album art | Works when the selected file has embedded artwork |
| Dependency file | `requirements.txt` exists but still needs package entries |

## Notes

- `app.py` currently opens `sounddevice.InputStream(device=2, ...)`, so live mode may need a different device index on another machine.
- Imported files should include readable audio samples. Album art display expects embedded image data.
- The app is designed around a `1280x720` window.
- Run it from the project root so the font and local files load correctly.

## Roadmap Ideas

| Idea | Why it would help |
| --- | --- |
| Device selector | Avoid hard-coding `device=2` for live mode. |
| Requirements cleanup | Make setup one-command with `pip install -r requirements.txt`. |
| Missing album-art fallback | Prevent crashes when a track has no embedded cover. |
| More visual modes | Add circular spectrum, waveform, particles, or mirrored bars. |
| Theme presets | Keep the current rainbow palette and add selectable alternatives. |

---

<div align="center">
  <sub>Built with Python, Pygame, NumPy FFT, and music-reactive color.</sub>
</div>
