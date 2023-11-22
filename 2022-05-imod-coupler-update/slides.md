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

# iMOD Coupler update

---

# Quick introduction

- iMOD Coupler is a program to couple hydrological kernels
- Started as a prototype reproducing part of Driver's functionality
- Currently applied to couple MODFLOW 6 and MetaSWAP
- Uses the eXtended Model Interface (XMI)

---
layout: center
---

<img src="MF6BMI_coupling.png" class="h-lg">

---
layout: two-cols
---

# How to use it


- Prepare MODFLOW 6 and MetaSWAP models
- Describe coupling via coupling tables
- Configure iMOD Coupler via `imod_coupler.toml`
- Run iMOD Coupler

::right::

```toml {all|14-22}
driver_type = 'metamod'

# modflow 6
[driver.kernels.modflow6]
dll = './kernels/libmf6.dll'
work_dir = './mf6_data'

# metaswap
[driver.kernels.metaswap]
dll = './kernels/MetaSWAP.dll'
dll_dep_dir = './kernels/3rdparty'
work_dir = './msw_data'

# inner model with sprinkling
[[driver.coupling]]
enable_sprinkling = true
...

# outer model, without sprinkling
[[driver.coupling]]
enable_sprinkling = false
...
```


---
layout: center
---

<img src="testbench.png" class="h-lg">

---

# Recent work

- iMOD Coupler has driver `metamod` to couple MetaSWAP and MODFLOW 6
    - Was not ready to be extended with other drivers
    - 👉 Added `Driver` interface to add new coupling scenarios


- IMOD Coupler testbench was hard to modify and to reason about
    - 👉 Changed to `pytest` and iMOD Python based testbench
    - Similar to iMOD Python and iMOD 5 testbench
    - Also tests iMOD Python's MetaSWAP support

---

# (Potential) future work

- Improve validation of user input
    - Return meaningful error messages for user input

- Add more test cases
    - More coupling scenarios

- Add more drivers
    - MODFLOW6/MetaSWAP/D-HYDRO (Lumbricus)
    - MODFLOW6/MetaSWAP/Mozart-DM

- Multimodel support
