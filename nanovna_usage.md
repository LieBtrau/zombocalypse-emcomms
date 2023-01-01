## NanoVNA misery
### NanoVNA saver doesn't work correctly
#### Linux : doesn't run
Bug in VNA-Saver 0.5.3 : waiting for update

#### Windows : COM-port doesn't want to detect
1. Make sure pyserial is installed.
2. Connect VNA
3. Device Manager → Universal Serial Bus controllers → remove "USB UART adapter"
4. Disconnect & reconnect VNA

### Calibration incorrect
**Problem** : Standalone VNA calibration works ok.  Measurement results in VNA-QT and VNA-saver are different from the results shown on the NanoVNA's screen.

**Solution** : Use Nanovna-saver → Calibration... → Calibration assistant

# Touchstone files
* s1p : 1 port parameter only (s11)
* s2p : 2 port parameter : s11 & s21 : It doesn't make sense to save a s1p-file when you're also saving a s2p-file for the same measurement
