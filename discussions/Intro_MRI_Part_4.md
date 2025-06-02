# Introduction to MRI, Part IV

## 5/27/2025

Attendance 5

### Introduction

DSST members and friends discussed the digitization and pre-processing of MRI signals.

### 3D Coordinates

MRI images use different coordinate systems to describe the orientation of anatomical axes. The most common systems are RPI, RAI, and RAS:

- **RPI (Right-Posterior-Inferior):** The axes are oriented so that the x-axis increases to the right, the y-axis increases to the back (posterior), and the z-axis increases downward (inferior).
- **RAI (Right-Anterior-Inferior):** The x-axis increases to the right, the y-axis increases to the front (anterior), and the z-axis increases downward (inferior).
- **RAS (Right-Anterior-Superior):** The x-axis increases to the right, the y-axis increases to the front (anterior), and the z-axis increases upward (superior).

These conventions are important for interpreting and comparing MRI data, as different software and datasets may use different coordinate systems.

### Neurological vs Radiogical Space

- RAS (Right-Anterior-Superior) is considered the neurological convention (or neurological space). In this convention, the image is displayed so that the right side of the image corresponds to the right side of the patient. This matches the orientation a neurologist would expect when viewing the brain as if looking from above, with the patient's right on the viewer's right.
- Radiological space (or radiological convention) is typically LPS (Left-Posterior-Superior) or sometimes LPI (Left-Posterior-Inferior). In this convention, the left side of the image corresponds to the right side of the patient (i.e., the image is flipped left-to-right compared to neurological space). This is the traditional orientation used by radiologists, matching the way X-rays are viewed.

### Magnet Isocenter and Patient Space

In MRI, the magnet isocenter is the central point of the scanner's magnetic field and serves as the reference origin for image acquisition. However, to interpret images in anatomical (patient) space, the coordinates must be transformed from the scanner's coordinate system to the patient's anatomical orientation.

This transformation uses information about the patient's position within the scanner, which is recorded in the image metadata. The DICOM header contains fields that specify the patient's orientation and position relative to the scanner, such as:

- **Patient Position (0018,5100):** This DICOM tag records how the patient was placed in the scanner. Common values include:
  - **HFS:** Head First Supine (lying on back, head entering first)
  - **HFP:** Head First Prone (lying on stomach, head entering first)
  - **FFS:** Feet First Supine
  - **FFP:** Feet First Prone
  - **HFDR/FFDR:** Head/Feet First Decubitus Right (lying on right side)
  - **HFDL/FFDL:** Head/Feet First Decubitus Left (lying on left side)

- **Image Orientation (Patient) (0020,0037):** This tag provides the direction cosines of the image rows and columns with respect to the patient.
- **Image Position (Patient) (0020,0032):** This tag gives the x, y, z coordinates of the upper-left hand corner of the image, in patient space.

By combining these DICOM fields, software can accurately map the acquired image data from the scanner's coordinate system to the patient's anatomical space, ensuring correct orientation and localization for diagnosis and analysis.

### NIFTI Header Transformations: Q-form and S-form

The NIFTI file format, commonly used for storing MRI data, includes a header that can encode spatial transformations between voxel coordinates and real-world (patient or scanner) space. Two key transformation matrices are stored in the NIFTI header:

- **Q-form (Quaternion Transform):** This encodes a rotation and translation using a quaternion representation. The Q-form is typically used to describe the orientation and position of the image in scanner or patient space, based on the original acquisition.

- **S-form (Affine Transform, sometimes called H-form):** This encodes a full 3D affine transformation using a 4x4 matrix. The S-form can represent scaling, shearing, rotation, and translation, and is often used to store transformations resulting from post-processing or registration to a standard space.

Both Q-form and S-form are stored in the NIFTI header, and each has an associated code indicating the coordinate system it refers to (e.g., scanner, anatomical, or template space). Software reading a NIFTI file can use these transforms to map voxel indices to real-world coordinates, ensuring correct spatial interpretation and alignment with other datasets.

### Left-Right Swap Issue

A common problem in MRI imaging is the left-right swap issue, where the orientation information in the image header is incorrect or misinterpreted, causing the left and right sides of the brain (or body) to be flipped. This can lead to serious errors in diagnosis or research if not detected.

One practical way to prevent or detect left-right swaps is to place a vitamin E capsule (or similar marker) on a known side of the patient's head (usually the right side) before scanning. The capsule appears as a bright spot on the MRI image, providing a clear, physical reference for left-right orientation. By checking the location of the capsule in the images, clinicians and researchers can verify that the image orientation matches the actual patient anatomy, helping to avoid left-right confusion.

### From Scanner to BIDS: Image Acquisition and Standardization

MRI scanners acquire raw imaging data and reconstruct it into images, which are typically stored in the DICOM (Digital Imaging and Communications in Medicine) format. DICOM files contain both the image data and extensive metadata about the scan, patient, and acquisition parameters.

For research and analysis, DICOM files are often converted to the NIFTI (Neuroimaging Informatics Technology Initiative) format, which is more suitable for neuroimaging workflows. NIFTI files store the image data along with spatial orientation information, but in a simpler and more accessible format than DICOM.

To facilitate data sharing, reproducibility, and automated analysis, NIFTI files and their associated metadata are organized according to the Brain Imaging Data Structure (BIDS). BIDS is a community-driven standard that prescribes a specific directory structure, file naming conventions, and metadata requirements for neuroimaging datasets.

The adoption of BIDS enables standardization across studies and sites, making it easier to share and analyze data. It also supports the development of BIDS Applications—software tools that can automatically process, analyze, or validate datasets that conform to the BIDS standard. This standardization accelerates research, improves reproducibility, and fosters collaboration in the neuroimaging community.

### Pre-processing of MRI Data in BIDS Format

Once MRI data is organized in BIDS format, it can be efficiently pre-processed using a variety of specialized neuroimaging software packages. Pre-processing steps may include motion correction, spatial normalization, artifact removal, and brain extraction, among others.

Several major software distributions are widely used for these tasks:

- **AFNI (Analysis of Functional NeuroImages):** Developed by the National Institute of Mental Health, AFNI provides a comprehensive suite of tools for processing, analyzing, and visualizing functional MRI data. AFNI also has its own file format (BRIK/HEAD) and supports conversion from and to NIFTI.

- **FSL (FMRIB Software Library):** Developed at the University of Oxford, FSL offers tools for analysis of structural, functional, and diffusion MRI data. It is known for its user-friendly interface and robust algorithms for brain extraction, registration, and statistical analysis.

- **FreeSurfer (FSM):** FreeSurfer is a software package for the analysis and visualization of structural and functional neuroimaging data from cross-sectional or longitudinal studies. It is particularly well-known for its surface-based analysis and cortical reconstruction capabilities.

To streamline and automate complex workflows, the **NiPype** pipeline system allows users to create reproducible, modular processing pipelines that integrate tools from AFNI, FSL, FreeSurfer, and other packages. NiPype leverages the BIDS standard to ensure compatibility and reproducibility across different datasets and software tools.

These software distributions and pipeline systems enable researchers to perform standardized, reproducible pre-processing and analysis of MRI data, facilitating collaboration and accelerating scientific discovery in neuroimaging.

### Common Pre-Processing Tasks

Pre-processing of MRI data involves a series of steps to prepare images for analysis. Some of the most common tasks include:

- **Bias Correction:** MRI images often suffer from intensity inhomogeneities (bias fields) caused by scanner imperfections. Bias correction algorithms adjust the image to produce uniform intensity across the brain, improving the accuracy of subsequent analyses.

- **Skull Stripping:** This process removes non-brain tissues (such as the skull and scalp) from MRI images, isolating the brain for further analysis. Accurate skull stripping is essential for tasks like segmentation and registration.

- **White Matter Segmentation:** Segmentation algorithms classify different tissue types in the brain, such as white matter, gray matter, and cerebrospinal fluid. White matter segmentation is crucial for studying brain connectivity and structure.

- **Image Registration:** Registration aligns images from different scans, subjects, or modalities into a common space. FSL provides two widely used registration tools:
  - **FLIRT (FMRIB's Linear Image Registration Tool):** Performs linear (affine) registration, aligning images using translation, rotation, scaling, and shearing.
  - **FNIRT (FMRIB's Nonlinear Image Registration Tool):** Performs nonlinear registration, allowing for more flexible warping to account for anatomical differences between subjects.

- **GIFTI Files:** The GIFTI (Geometry-Informed Functional Imaging) file format is used to store surface-based neuroimaging data, such as cortical surfaces and functional data mapped onto those surfaces. GIFTI files facilitate the analysis and visualization of brain surface geometry.

- **Spherification and Ballooning of Brain Surfaces:** These techniques involve transforming the complex geometry of the brain's cortical surface into simpler shapes (like spheres or inflated surfaces). Spherification and ballooning make it easier to visualize, compare, and analyze cortical features across subjects.

These pre-processing tasks are foundational for accurate and reproducible neuroimaging analyses, enabling researchers to extract meaningful information from MRI data.

### fMRI Preprocessing

Preprocessing of functional MRI (fMRI) data involves several specialized steps to ensure data quality and prepare the images for statistical analysis. Key fMRI preprocessing tasks include:

- **Motion Correction:** Head movement during scanning can introduce significant artifacts in fMRI data. Motion correction algorithms estimate and correct for these movements, typically using a 6-degrees of freedom (translation and rotation in 3D) rigid-body transformation. A reference image—often the first or the mean image in the time series—is used as the target for alignment. In multi-band scanners, a single band reference (SBRef) image is often acquired to provide a high-quality reference for motion correction.

- **Slice Timing Correction:** fMRI data are acquired in slices, one after another, within each repetition time (TR). Slice timing correction adjusts the time series data to account for the differences in acquisition time between slices, improving temporal alignment across the brain.

- **Geometric Distortion Correction:** Echo-planar imaging (EPI), commonly used in fMRI, is susceptible to geometric distortions caused by magnetic field inhomogeneities. Distortion correction methods use field maps or reverse phase-encoded images to correct these spatial warping effects.

- **Co-registration with Anatomical MRI:** Functional images are often co-registered (aligned) with high-resolution anatomical MRI scans from the same subject. This step ensures that functional data can be accurately localized to anatomical structures and facilitates group-level analyses.

- **Noise/Nuisance Regression:** fMRI data contain various sources of noise, such as physiological fluctuations (e.g., heartbeat, respiration), scanner drift, and head motion. Nuisance regression techniques model and remove these unwanted signals from the data, improving the sensitivity and specificity of subsequent analyses.

These preprocessing steps are essential for producing reliable and interpretable fMRI results, enabling robust investigation of brain function.
