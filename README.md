# Binary Stellar Evolution - Dormant BH in binary system

This repo collects the material related to the project "Dormant Black Holes in Binaries from Gaia DR3" carried out during the Laboratory of Computational Physics (Mod B) course at the University of Padua.  
The supervisors are Dr. [Giuliano Iorio](mailto:giuliano.iorio@unipd.it) and [Erika Korb](mailto:erika.korb@studenti.unipd.it) from the [DEMOBLACK](http://demoblack.com/) group, whose PI is Prof. Michela Mapelli.  

## The project
With the advent of gravitational wave astrophysics and advances in precise astrometry of numerous stellar sources, the search for compact objects is thriving. Rarely seen massive binaries containing a compact object play a vital role in the evolution towards compact object mergers. With the [Gaia Data Release 3](https://www.cosmos.esa.int/web/gaia/data-release-3) (DR3), the first Gaia astrometric orbital solutions for binary sources have become available, revealing a large amount of such binary candidates. In the present notebook, we are interested in the rare cases in which a black hole (BH) is evolving in a binary system with a Main Sequence star (MS). 

Since the systems are extremely difficult to observe, we deal with Binary System Evolution (BSE) simulations, obtained via the [SEVN](https://arxiv.org/abs/2211.11774) (Stellar EVolution for N-body), a rapid binary population-synthesis code. In this way we can compare the few candidates found with a large synthetic dataset. It gets as input the initial conditions of stars or binaries (masses, spin, semi-major axis, eccentricity, etc.) and evolves them. Stellar evolution is calculated by interpolating pre-computed sets of PARSEC stellar tracks [(Bressan et al., 2012)](https://academic.oup.com/mnras/article/427/1/127/1027734?login=false). On the other hand, binary evolution is implemented by means of analytic and semi-analytic prescriptions. The implementation proves to be flexible so that every model can be easily changed or updated.

We aim to understand what kind of processes these systems are likely to experience during their lifetime: using machine learning techniques, such as Deep Neural Network and XGBoost, we tried to infer and label the properties of the known sources and understand the importance that each feature has had in the evolution of systems. We tried, moreover, to match some of the candidates to the simulated systems in order to retrieve the guessed full evolution history of those candidates.

### Files
1. `bse_bhms_classification.ipynb`: complete notebook about the project.
2. `bse_bhms_predict_history.ipynb`: attempt to find a metric to evaluate quantitatively the similarity between the simulated systems with the observed ones.
3. `bse_bhms_report.pdf`: report/paper about about the project and its final results.
4. `bse_bhms_presentation.pdf`: presentation about the project and its final results.  

- `dev_nb`: folder containing many notebooks used during the development of the project. Some of them were merged in the final notebook.
- `models`: folder containing the trained classification models.
- `candidates_clean.csv`: CSV file containing usefull features about the GAIA BH+MS candidates (+ 4 confirmed systems).
- `real_candidates.ipynb`: notebook used to generate the above file.
- `sample_df.py`: Python script to generate normal samples, starting from the values of the candidates (used for classification purposes inside the final notebook).

## SEVN 
SEVN (Stellar EVolution for 𝑁-body) is a rapid binary population synthesis code. It gets as input the initial conditions of stars or binaries (masses, spin, semi-major axis, eccentricity) and evolve them. SEVN calculates stellar evolution by interpolating pre-computed sets of stellar tracks. Binary evolution is implemented by means of analytic and semi-analytic prescriptions. The main advantage of this strategy is that it makes the implementation more general and flexible: the stellar evolution models adopted in sevn can easily be changed or updated just by loading a new set of look-up tables. SEVN allows to choose the stellar tables at runtime, without modifying the internal structure of the code or even recompiling it.  

SEVN is written entirely in C++ (without external dependencies) following the object-oriented programming paradigm. SEVN exploits the CPU-parallelisation through OpenMP.  

Additional information on the technical details of  SEVN can be found in the presentation paper ([Iorio et al., 2022](https://ui.adsabs.harvard.edu/abs/2022arXiv221111774I/abstract), see also [Spera et al., 2019](https://ui.adsabs.harvard.edu/abs/2019MNRAS.485..889S/abstract)) and in the [user guide](https://gitlab.com/sevncodes/sevn/-/blob/SEVN/resources/SEVN_userguide.pdf).

### Authors and acknowledgment
The original version of SEVN was developed by  Mario Spera, Michela Mapelli and Alessandro Alberto Trani.  

The current updated version is developed and mantained by Giuliano Iorio (main developer), Mario Spera, Michela Mapelli, Guglielmo Costa and Gaston Escobar.  

The developers thanks all the people in the DEMOBLACK group for all the valuable comments and suggestions during the code development.

---

##### Mark
30 with Lode