---
# try also 'default' to start simple
theme: seriph
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# show line numbers in code blocks
lineNumbers: false
---

# MODFLOW 6 & Conda

---

# What is conda?

- Conda is a package manager mostly used for scientific software
- Anaconda Python distribution is a set of packages maintained by Anaconda Inc.
- Conda-Forge is a set of packages maintained by the community

<v-click>

<img src="modflow_conda_forge.PNG">

</v-click>

---

# Why do we want that?

- Can be added as dependencies to other conda packages
- Can be bundled into a distribution similar to Anaconda Python distribution
- Easy to install and update

<v-click>

Everything the user has to do is to run:
```
$ conda install -c conda-forge modflow6
```
Then the binaries are readily available whenever the conda environment is activated:
```
$ mf6 --version

mf6.exe: 6.3.0 03/04/2022 Release
```

</v-click>

---

# How does that work?

- The modflow conda package is a zipped file containing:
  - mf6.exe
  - libmf6.dll
  - mf5to6.exe
  - zbud6.exe

- During installation those file get copied into the correct location 

---

# Disclaimer: There are still things to do

- Linux build work fine and also passes the autotests suite
- macOS and Windows binaries show unexpected runtime errors

➡️ We should test our binares with conda forge's CI


---

# Autotests are hard to reproduce

- Autotests on develop are tested on CI and are always green
- Autotests for the last release aren't easy to reproduce (probably because of changes in flopy)
- ➡️ Test dependencies would need to be locked

---
layout: center
---

# Ideas Time!

---

# Python preprocessor

- flopy and imod Python
- Users currently have to obtain and maintain MODFLOW6 executable themselves
- Alternative:
    - Add `modflow6` conda package as dependency, or
    - Instruct users to run `conda install modflow6`

---

# Python preprocessor

You can still specify your own MODFLOW 6 executable

```python
import flopy

sim = flopy.mf6.MFSimulation(exe_name='/path/to/mf6')

# Do stuff

sim.write_simulation()
sim.run_simulation()
```

<v-click>

But alternatively you can just rely on the one provided by conda

```python {3}
import flopy

sim = flopy.mf6.MFSimulation()

# Do stuff

sim.write_simulation()
sim.run_simulation()
```

</v-click>


---

# MODFLOW API

```python
from modflowapi import ModflowApi

mf6 = ModflowApi("/path/to/libmf6.so")
mf6.initialize()

current_time = mf6.get_current_time()
end_time = mf6.get_end_time()

while current_time < end_time:
    mf6.update()
    current_time = mf6.get_current_time()

mf6.finalize()
```

---

# MODFLOW API

```python {3}
from modflowapi import ModflowApi

mf6 = ModflowApi()
mf6.initialize()

current_time = mf6.get_current_time()
end_time = mf6.get_end_time()

while current_time < end_time:
    mf6.update()
    current_time = mf6.get_current_time()

mf6.finalize()
```

---


# Current way of distributing MODFLOW 6


- People download the official release 
- Put the executable somewhere in their `PATH` environment variable
- Hopefully record which version they used to reproduce later
- Manually update if they need features of a new version

---

# Custom conda distributions

- Create distribution similar to Anaconda Python distribution
- Same usage as a "normal" Anaconda distribution
- Could include runtime dependencies we might add in the future like NetCDF or MPI
- Could even include flopy and MODFLOW API
- Would simplify reproducible model runs

---

# Use conda to simplify development workflow

- Create `environment.yml` which includes everything to:
    - Build MODFLOW 6
    - Run its autotests
    - Get IDE support with language server, linting and formatting


---
layout: center
---

# Questions? Comments?
