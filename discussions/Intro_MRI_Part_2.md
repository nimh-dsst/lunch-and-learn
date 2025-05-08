# Introduction to MRI, Part II

## 4/29/2025

Attendance 7

### Introduction

After a crash course into the basics of how MRIs produce images in [part I](https://github.com/nimh-dsst/lunch-and-learn/blob/main/discussions/Intro_MRI_Part_1.md), DSST members explained how different sequences produce images that highlight different tissues.

#### Protons vs Net Magnitization

Protons have an intrinsic property called spin which gives them angular momentum, which can be described by quantum mechanics, which is outside the scope of this crash course. Rather, we can think of the net magnetization, which is the average angular momenta from all spins the sample, and leave quantum mechanics to the experts, see [Is Quantum Mechanics necessary for understanding Magnetic Resonance?](https://mriquestions.com/uploads/3/4/5/7/34572113/hanson._concept_mri_2008_quantum.pdf). Rather, we will focus this write up on the classical mechanics model of MRI and discuss the behavior of the net magnetization.

### Generating a Magnetic Resonance Signal: A Classical Mechanics Perspective

#### First Polarization then Excitation

When a subject is in the B<sub>0</sub> field, the net magnetization of the subject (really everything in the bore), named M, will align to the magnetic B<sub>0</sub> field. During an MRI, perturbations to M are induced by whacking the subject with pulses of radio waves at the Larmor frequency of hydrogen protons. It tips M away from its longitudinal alignment with B<sub>0</sub> into the transverse plane. This transverse component of the net magnetization is called M<sub>xy</sub>.

#### Precession of Net Magnetization

The RF pulse creates a precessing net magnetization in the transverse plane around the Z-axis. Precessing describes a change in the orientation of an axis of rotation, think a top wobbling as it spins. According to [Faraday's law of induction](https://en.wikipedia.org/wiki/Faraday%27s_law_of_induction), a changing magnetic field passing through a coil of wire will induce an electrical current (a voltage) in that coil. The receiver coils in the MRI scanner are strategically placed to detect the current induced by the precession of the net magnetization. The electrical signal detected by the receiver coils is the raw magnetic resonance signal. It's an oscillating signal whose frequency is the Larmor frequency, and its initial amplitude is proportional to the magnitude of the coherent net transverse magnetization. After turning off the RF pulse the signal decays rapidly, this is called Free Induction Decay (FID). We don't typically want to measure FID for generating a magnetic resonance image. Instead scanners use sequences of additional pulses to refocus the net transverse magnetization to create an echo. Sequences can be described by how the echo is formed, for example Spin Echo and Gradient Echo sequences. Before we dive into spin vs echo, we need to introduce what causes the decay of the precession of the net magnetization, and thus the signal decay.

#### T2<sup>*</sup> vs T2 Relaxation

Once the RF pulse ends, M<sub>xy</sub> starts to decay due to local magnetic field inhomogeneities and direct interactions between the magnetic fields of adjacent spinning protons, called spin-spin interactions. The decay of M<sub>xy</sub> leads to a decrease in amplitude of FID. The observed/effective rate of decay in the transverse direction is called T2<sup>*</sup>. This includes decay due to the "true" T2 relaxation (spin-spin relaxation) as well as imperfections in the B<sub>0</sub> field, differences in magnetic susceptibilities of local tissues and materials in the subject (i.e. implants), and microscopic magnetic field inhomogeneities due to subject's own tissues. Critically, the T2 process is irreversible, but the dephasing due to magnetic field inhomogeneities is, in principle, reversible.

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
