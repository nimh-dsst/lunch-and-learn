# Introduction to MRI, Part I

## 4/22/2025

Attendance: 10

### Introduction

DSST Members gave a crash course into how MRI's work. The following is a very brief overview of the components of an MRI scanner.

### The Main Magnet

A key component to an MRI scanner is the main magnet. The main magnet is super cooled with liquid helium and can come in a variety of strengths. The strength of the magnetic field is given in [Teslas](https://en.wikipedia.org/wiki/Tesla_(unit)) (the SI unit, not the car). Clinical scanners are usually a little weaker at strengths like 1.5 T or 3 T, whereas research scanners are often greater strengths. Portable MRI scanners can have weaker magnets. The strongest MRI scanner known at NIH was 11.7 T. To put this in perspective, Junk Yard magnets, like the [Giant Magnet](https://disney.fandom.com/wiki/Giant_Magnet), the climactic antagonist of the classic 1987 film [The Brave Little Toaster](https://en.wikipedia.org/wiki/The_Brave_Little_Toaster) is 1.5 T. The Earth's magnetic field strength at its surface is approximately 50 microtesla (50 μT), a.k.a. 0.5 gauss (G) [1 T = 10,000 G]. Mentioning Gauss here as the "5-gauss line" is the boundary where the magnetic field strength is 5 gauss or less, and considered a safe level for general public exposure in MRI safety zones.

Another defining characteristic of the MRI scanner is the bore size, which is the size of the hole where the subject or sample goes into. MRI scanners' bore size can vary depending on if the scanner is intended for clinical use on human patients, is a research scanner, or is intended for animal use.

#### B<sub>0</sub> field and proton alignment

The big magnet in the MRI scanner produces a magnetic field, called B<sub>0</sub>. The field is directed along the bore of the MRI scanner but can extend past the scanner. This is why the MRI scanner is placed in a containment area with warning signs about strong magnetic fields. The homogeneity of the field is important for producing uniform images. The B<sub>0</sub> field is adjusted when a subject is in the scanner to help promote homogeneity and limit image distortion.

The purpose of the B<sub>0</sub> field is to align the protons, the nuclei of Hydrogen atoms in water especially. Protons can be either aligned in an "up" or "down" spin.

### Radiofrequency Coils

In order to generate a measurable signal from the subject's aligned protons, these protons have to be deliberately misaligned. This misalignment is caused by the transmit radiofrequency coil. This coil generates "rotating transverse magnetization in the patient's body."[Kwok, 2022](https://pubs.rsna.org/doi/full/10.1148/rg.210110). This field is called the B<sub>1</sub> field and is applied perpendicular to the B<sub>0</sub> field. The B<sub>1</sub> field is applied as a pulse of radio waves at a specific frequency, known as the Larmor frequency. Note, this is a field of electromagnetic energy that is transmitted into a subject's body.

### Relaxing protons

When the transmit radiofrequency coil is turned off, the protons will realign back to the static B<sub>0</sub> field in a process called "relaxation." During relaxation, protons emit some of the energy that was applied to them during the B<sub>1</sub> field pulse in the form of radio waves. These are picked up by receiver radiofrequency coils. Relaxation is a three-dimensional process but can be divided into two main components, the relaxation along the B<sub>0</sub> field, called T1, and the relaxation perpendicular to the B<sub>0</sub> field, called T2. T1 and T2 have different rates depending on the tissue and provide contrast to the resultant MRI image.

### Gradient Coils

In order to encode the signals generated by the relaxation of the protons, 3 gradient coils are used to spatially encode signal. These 3 coils, one for each X, Y, and Z dimension, are quickly turned on and off during acquisition. The cycling of the gradient coils is the loud banging that occurring during MRI scans. How the signals are spatially encoded is beyond the scope of this crash course, but look up "slice selection", "frequency encoding" and "phase encoding" in MRI for more. See [this video](https://youtu.be/r3LHXIzCXAY) too.

### K-space and Image Reconstruction

The spatially encoded signals must be converted from a representation of spatial frequencies into an image by using an inverse Fourier transform. This is what actually generates the image.

## Next Session

In this write-up we covered how the signal is generated, by perturbing aligned protons in a subject's body, and how the spatial information is encoded using gradient coils. Next session, we will talk about these steps are used in sequences to generate MRI images and talk about functional MRI.

## Suggested References

- [MRI Physics for Radiologists: A Visual Approach](https://doi.org/10.1007/978-1-4612-0785-6) by Alfred L. Horowitz. NIH has access to the entire book via Springer.
