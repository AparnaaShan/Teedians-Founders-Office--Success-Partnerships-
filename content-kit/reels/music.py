"""Usage: python3 music.py <duration> <cut1,cut2,...> <out.wav>
Original lo-fi backing track, 100 BPM, made from scratch (no samples), with whooshes on the scene cuts."""
import numpy as np, wave, sys
from scipy.signal import butter, sosfilt

SR = 44100
DUR = float(sys.argv[1])  # seconds
BPM = 100
BEAT = 60 / BPM
BAR = 4 * BEAT
CUTS = [float(x) for x in sys.argv[2].split(",")]  # scene cut times
n = int(SR * DUR)
t = np.arange(n) / SR
rng = np.random.default_rng(7)
out = np.zeros(n)

def hz(m): return 440 * 2 ** ((m - 69) / 12)
def lp(x, f, o=2): return sosfilt(butter(o, f, "low", fs=SR, output="sos"), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, "high", fs=SR, output="sos"), x)
def bp(x, a, b, o=2): return sosfilt(butter(o, [a, b], "band", fs=SR, output="sos"), x)
def put(sig, at, gain=1.0):
    i = int(at * SR)
    if i >= n: return
    j = min(n, i + len(sig)); out[i:j] += sig[: j - i] * gain

# chords: Fmaj7, Em7, Dm7, Cmaj7 (MIDI)
CH = [[53, 57, 60, 64], [52, 55, 59, 62], [50, 53, 57, 60], [48, 52, 55, 59]]
ROOT = [41, 40, 38, 36]

pad = np.zeros(n)
bars = int(np.ceil(DUR / BAR))
for b in range(bars):
    st = b * BAR; L = int(BAR * SR) + int(0.4 * SR)
    tt = np.arange(L) / SR
    env = np.minimum(1, tt / 0.25) * np.exp(-np.maximum(0, tt - BAR) / 0.15) * (0.85 + 0.15 * np.cos(2 * np.pi * tt / BAR))
    sig = np.zeros(L)
    for m in CH[b % 4]:
        for det in (-0.08, 0.0, 0.08):
            f = hz(m + 12) * 2 ** (det / 12)
            for h in range(1, 6):
                sig += np.sin(2 * np.pi * f * h * tt + rng.uniform(0, 6.28)) / (h * 1.6)
    i = int(st * SR); j = min(n, i + L)
    pad[i:j] += (sig * env)[: j - i]
pad = lp(pad, 1500, 4)
out += pad / np.max(np.abs(pad)) * 0.20

# bass on beat 1 and the "and" of 2
for b in range(bars):
    for off, ln in ((0, 1.4), (1.5, 0.9)):
        st = b * BAR + off * BEAT
        tt = np.arange(int(ln * BEAT * SR)) / SR
        f = hz(ROOT[b % 4])
        s = np.sin(2 * np.pi * f * tt) + 0.25 * np.sin(4 * np.pi * f * tt)
        s *= np.minimum(1, tt / 0.01) * np.exp(-tt / 0.6)
        put(s, st, 0.28)

beats = int(DUR / BEAT) + 1
for k in range(beats):
    st = k * BEAT
    if k % 2 == 0:  # kick on 1 and 3
        tt = np.arange(int(0.4 * SR)) / SR
        ph = 2 * np.pi * np.cumsum(45 + 75 * np.exp(-tt / 0.03)) / SR
        put(np.sin(ph) * np.exp(-tt / 0.16), st, 0.55)
    else:  # soft snare on 2 and 4
        tt = np.arange(int(0.25 * SR)) / SR
        put(bp(rng.normal(0, 1, len(tt)), 900, 5000) * np.exp(-tt / 0.07), st, 0.16)
    for h in (0, 0.55):  # swung 8th hats
        tt = np.arange(int(0.06 * SR)) / SR
        put(hp(rng.normal(0, 1, len(tt)), 7000) * np.exp(-tt / 0.018), st + h * BEAT, 0.05 if h else 0.07)

# vinyl crackle
cr = np.zeros(n); idx = rng.integers(0, n, 260); cr[idx] = rng.uniform(-1, 1, 260)
out += lp(hp(cr, 1500), 6000) * 0.05

# whooshes into each cut
for c in CUTS:
    L = int(0.42 * SR); tt = np.arange(L) / SR
    nz = rng.normal(0, 1, L)
    s = np.zeros(L)
    for seg in range(12):
        a, b2 = seg * L // 12, (seg + 1) * L // 12
        f0 = 400 + 3200 * (seg / 11) ** 1.6
        s[a:b2] = bp(nz, f0, f0 * 1.8)[a:b2]
    s *= np.sin(np.pi * np.minimum(1, tt / 0.42)) ** 2
    put(s, c - 0.36, 0.22)

# master: gentle low-pass, fade in/out, soft clip, normalise
out = lp(out, 9000, 2)
fade_in = np.minimum(1, t / 0.08); fade_out = np.clip((DUR - t) / 1.4, 0, 1)
out *= fade_in * fade_out
out = np.tanh(out * 1.4) / np.tanh(1.4)
out = out / np.max(np.abs(out)) * 0.89
st = np.stack([out, out * 0.98 + np.roll(out, 220) * 0.02], 1)
with wave.open(sys.argv[3], "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype("<i2").tobytes())
print("ok", DUR)
