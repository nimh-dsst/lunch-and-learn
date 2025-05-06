# Introduction to MRI, Part II

## 4/29/2025

Attendance 7

### Introduction

After a crash course into the physics of how MRIs produce images in [part I](https://github.com/nimh-dsst/lunch-and-learn/blob/main/discussions/Intro_MRI_Part_1.md), DSST members explained how different sequences produce images that highlight different tissues.

### Sequences

When a subject is in the B<sub>0</sub> field, the protons will align to the magnetic B<sub>0</sub> field in either a parallel (low energy state) or anti-parallel (high energy state). During an MRI, perturbations to the proton alignment are induced by whacking them with pulses of radio waves at the Larmor frequency of hydrogen protons. The protons absorb the energy from the radio waves they do a few important things. Firstly, some of the parallel protons flip to an anti-parallel alignment with the B<sub>0</sub> field. This weakens the alignment of the net magnetization vector M (the overall magnetic field created by the presence of the subject in the machine) along longitudinal axis of B<sub>0</sub>. It also tips M away from its alignment with M perpendicular with B<sub>0</sub>. Finally, we need to cover the concept of proton precession before describing phase coherence.

#### Proton Precession

A key concept to MRI is the precession, or wobbling, of protons in a magnetic field. Protons have an intrinsic property called spin which gives them angular momentum so they don't just snap into static alignment with the magnetic B<sub>0</sub> field. Rather they wobble around the magnetic B<sub>0</sub> field at the Larmor frequency which is dependent on the strength of the B<sub>0</sub> field and gyromagnetic ratio of the proton (a constant for hydrogen nuclei, 42.58 MHz/T). Prior to the RF pulse, the precessional paths of the protons are not synchronized. Think of the wobbling of individual protons as runners going around a track. They all go at the same speed, but they are all at different points along the track at any given time. The RF pulse forces all of the runners to start running in sync.

#### Net Magnetization

The synchronization of the hydrogen atoms creates an oscillating magnetic field in the transverse plan, this is called the net transverse magnetization (M<sub>xy</sub>). According to [Faraday's law of induction](https://en.wikipedia.org/wiki/Faraday%27s_law_of_induction), a changing magnetic field passing through a coil of wire will induce an electrical current (a voltage) in that coil. The receiver coils in the MRI scanner are strategically placed to detect this induced current. The electrical signal detected by the receiver coils is the raw MRI signal, often called the Free Induction Decay (FID). It's an oscillating signal whose frequency is the Larmor frequency, and its initial amplitude is proportional to the magnitude of the coherent net transverse magnetization.

#### T2<sup>*</sup> vs T2 Relaxation

Once the RF pulse ends, M<sub>xy</sub> starts to decay due to local magnetic field inhomogeneities and direct interactions between the magnetic fields of adjacent spinning protons, called spin-spin interactions. The decay of M<sub>xy</sub> leads to a decrease in amplitude of FID. The observed/effective rate of decay in the transverse direction is called T2<sup>*</sup>. This includes decay due to the "true" T2 relaxation (spin-spin relaxation) as well as imperfections in the B<sub>0</sub> field, differences in magnetic susceptibilities of local tissues and materials in the subject (i.e. implants), and microscopic magnetic field homogeneities due to subject's own tissues. Critically, the T2 process is irreversible, but the dephasing due to magnetic field homogeneities is, in principle, reversible.

#### Spin Echo and Gradient Echo Sequences

##### Spin Echo

Spin echo sequences involve "refocusing" the transverse magnetization by first applying a 90-degree pulse, allowing some dephasing to occur, and then applying a 180-degree pulse to "refocus" the phasing back. This results in an echo formation. This signal T2 and proton-density weighted as the field inhomogeneities are accounted for by the echo. Remember, T2 dephasing is random and irreversible, so simply flipping the field won't eliminate them, but it will for local field inhomogeneities. Depending on the parameters of the spin echo, the resultant images can be weighted for T1 (relaxation along B<sub>0</sub> field), T2, or proton density. Effectively giving radiologists tuning parameters to better visualize structures in the body.

##### Gradient Echo

Instead of using a 180° RF pulse to rephase spins, gradient echo sequences use a pair of magnetic field gradients with opposite polarities to dephase and then rephase the transverse magnetization to form an echo. The sequence starts with an RF pulse, but unlike spin echo, the "flip angle" of the pulse can be more shallow than 90-degrees.  Immediately after the RF pulse, a dephasing magnetic field gradient is applied. This gradient intentionally introduces a rapid and controlled dephasing of the spins in the transverse plane by making the magnetic field strength vary spatially. After a short period, this dephasing gradient is turned off, and a rephasing gradient with the opposite polarity (but often the same strength and duration) is applied along the same axis. When the areas under the dephasing and rephasing gradient lobes are equal, the spins come back into phase, forming a gradient echo. This echo is then measured. Gradient echo sequences can vary parameters to be T1 weighted, T2<sup>*</sup> weighted, or proton density weighted. Typically gradient echo sequences are faster than spin echo sequences.

### Artifacts

Tattoos, implants, and orthodontic braces can interfere with the generation of an MRI signal. In addition motion can create artifacts in MRI images. This includes motion from breathing. Field homogeneities can also cause dark bands to appear in MRI images.

### Recommended Resources

- [Spin Echo Imaging Methods](http://www.sprawls.org/mripmt/MRI06/index.html)
- [Gradient Echo Imaging Methods](http://www.sprawls.org/mripmt/MRI07/index.html)
