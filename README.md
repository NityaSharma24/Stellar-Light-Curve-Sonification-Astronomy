# Stellar-Light-Curve-Sonification-Astronomy
Cyg X-1: X-Ray Data Sonification

This project explores sonification—the process of translating data into sound—using X-ray measurements from **Cygnus X-1**, a black hole system observed through X-rays. The goal is to transform an astronomical light curve into an audible sequence of notes, allowing patterns in the data to be explored through sound rather than visual graphs alone. This project is part of my broader exploration of accessible scientific data interpretation, particularly for blind and visually impaired people.

## How It Works
The Python notebook processes an approximate dataset of X-ray counts over time and converts the measurements into audio.

1. **Load the data:** Import the CSV file containing approximate time and X-ray count values.
2. **Visualize the light curve:** Plot X-ray counts against time to examine variations in the signal.
3. **Normalize the measurements:** Scale the count values to a range between 0 and 1.
4. **Map values to pitch:** Convert normalized measurements into MIDI notes spanning 36 semitones, then calculate their corresponding frequencies in hertz.
5. **Generate audio:** Create sine-wave tones for each measurement, apply short fade-in and fade-out envelopes, and combine the tones into an audio sequence.
6. **Export the sonification:** Save the generated audio as a WAV file.

In this implementation, **X-ray counts control pitch**, while each note has a fixed duration and approximately consistent base amplitude. The audio preserves the order of the measurements but does not reproduce the original time intervals.

## Technologies
- Python
- Google Colab
- Pandas and NumPy
- Matplotlib
- SciPy
- IPython Audio

## Files
- `cyg_x1_approx_1000s_intervals.csv` — Input dataset containing approximate time and X-ray count values.
- `cyg_x1_continuous_sonification.wav` — Generated audio output.

The code demonstrates a possible approach to translating numerical measurements into sound; it does not establish that sonification is universally more effective than visual data interpretation or text descriptions.

## Future Directions
Potential extensions include preserving actual time intervals, incorporating additional data dimensions into sound, and evaluating how effectively listeners can interpret the resulting audio.
