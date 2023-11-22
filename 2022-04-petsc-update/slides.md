---
# try also 'default' to start simple
theme: seriph
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: prism
# show line numbers in code blocks
lineNumbers: false
---

# PETSc Status Update 

---

# Let PETSc imitate MODFLOW IMS behavior

- Parse IMS config file:
  - `linear_acceleration` option sets `KSPCG` or `KSPBCGSL`
  - `inner_dvclose` option sets custom convergence tests
- We set preconditioner to `ILU`



---
layout: fact
---

## 75% of large tests now give same numerical results

---
layout: full
---

<img src="/petsc_largetests_comparison.PNG" />

---


# Failing large tests

```shellsession
FAILED test1004_mvlake_lak_tr - AssertionError: head comparison 2
FAILED test2001_gwtbuy-elderRa400 - AssertionError: MODFLOW 6 model did not terminate normally
FAILED test1201_gwtbuy-elderRa60 - AssertionError: MODFLOW 6 model did not terminanate normally
FAILED test1004_mvlake_laksfr_tr - AssertionError: head comparison 2
FAILED test1200_gwtbuy-goswami - AssertionError: MODFLOW 6 model did not terminate normally
```

---

# We have a basic CI workflow

- Compiles and caches PETSc
- Compiles and installs MODFLOW
- Runs regression test with biscayne model

 
```yaml
env:
  PETSC_VERSION: "v3.16.6" # Change that variable to update PETScs
jobs:
  test:
    steps:
    - uses: actions/cache@v1
      id: cache
      with:
        path: ../petsc/arch-linux-c-opt
        key: ${{ runner.os }}-${{ matrix.GCC_V }}-petsc-${{ env.PETSC_VERSION }}

    - name: Compile PETSc
      if: steps.cache.outputs.cache-hit != 'true'
      working-directory: ../petsc
      run: |
        ./configure --with-debugging=no
        make all check
```

---

# Include PETSc in next MODFLOW release

- How far would we go there?
  - Documentation
  - CI
---

# Work on a parallel solver prototype

- Martijn & I plan to free two days to work on it
- Only a prototype
- Not intended to be included in a release

---

# Joe's work

- Compile PETSc on macOS
- Link Modflow to PETSC
- Run models with it

---
layout: fact
---

## Moving on to XMI

---

# Add version API to XMI

- Add a function call returning the version string
- Extend `xmipy`
