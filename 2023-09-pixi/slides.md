---
# try also 'default' to start simple
theme: seriph
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# show line numbers in code blocks
lineNumbers: false
background: deltares.jpg
---

# What is Pixi

and how it improves development experience with Python

---

# Introducing Pixi

- Pixi is a package manager for the conda ecosystem
- Created by the same people behind mamba
- Killer features:
    - Easy to install
    - Lock file
    - Task runner
    - Global installs

---
layout: center
---

# Installation experience

---


# Installation experience of conda

<v-clicks>

- Follow an installation wizard
- Afterwards basically nothing works:
    - Conda is not in your PATH
    - Shell is not prepared

- How colleagues deal with that:
    - Modify environment variables and use cmd
    - Allow startup scripts and run `conda init` in the conda console
    - Exclusively use the conda console

</v-clicks>

---

# Installation experience of pixi

- Running an install script
- That's it!


---
layout: center
---

# Environment management

---
layout: two-cols
---

# Environment management with conda

- This `environment.yml` is not reproducible
- Evaluating the environment takes a long time
- Doesn't resolve for all supported platforms

<v-click>

- Other ecosystems like JavaScript, Rust and Julia already solved that problem:
    - They use lock files

</v-click>

::right::

`environment.yml` of Ribasim

```yaml
name: ribasim
channels: [conda-forge]
dependencies:
  - datamodel-code-generator
  - geopandas
  - jupyterlab
  - matplotlib
  - mypy
  - pandas!=2.1.0
  - pandera
  - pre-commit
  - pyarrow
  - pydantic=1
  - pyogrio
  - pytest
  - pytest-cov
  - python>=3.9
  - shapely<=2.0
  - xarray
  - xmipy
```


---
layout: two-cols
---

# Environment management with pixi


- `pixi.toml` specifies:
    - platforms
    - tasks
    - direct dependencies
- `pixi.lock` pins all transitive dependencies to a specific version
- Team members and CI all use the exact same environment

::right::

`pixi.toml` of Ribasim

```toml
[project]
name = "Ribasim"
version = "0.2.0"
channels = ["conda-forge"]
platforms = ["win-64", "linux-64", "osx-64"]

[tasks]
pre-commit = "pre-commit run --all-files"
# and many more tasks

[dependencies]
datamodel-code-generator = "*"
geopandas = "*"
jupyterlab = "*"
matplotlib = "*"
pandas = "!=2.1.0"
pre-commit = "*"
pyarrow = "*"
pydantic = "~=1.0"
pyogrio = "*"
pytest = "*"
python = ">=3.9"
shapely = ">=2.0"
xarray = "*"
```

---
layout: center
---

# Running tasks

---

# Running tasks with conda

- No task runner built-in
- Options:
    - Run tasks manually
    - Use tox
- Tox:
    - doesn't support conda natively
    - creates an environment for each task

---
layout: two-cols
---

# Running tasks with pixi


- Tasks:
    - encoded in `pixi.toml`
    - run inside the environment
    - reproducible between colleagues and on CI

- Docs are generated with `pixi run docs`

::right::

`pixi.toml` of Ribasim

```toml
[tasks]
instantiate-julia-docs = {
  cmd = "julia --project=docs -e \
        \"using Pkg; Pkg.instantiate()\""
}
build-julia-docs = { 
  cmd = "julia --project=docs docs/make.jl", 
  depends_on = [ "instantiate-julia-docs"]
}
quartodoc-build = {
  cmd = "cd docs && quartodoc build && rm objects.json"
}
quarto-preview = { 
  cmd = "quarto preview docs", 
  depends_on = ["quartodoc-build"] 
}
docs = { 
  depends_on = ["build-julia-docs", "quarto-preview"] 
}
```

---

# Global install

- It is convenient to install CLI apps globally
- Problem: installing them in the same environment may lead to version conflicts
- Solution: install them in separate environments
  - pipx, condax and pixi do that out of the box
- Run `pixi global install ipython`
- `ipython` is available in your `PATH`

---
layout: center
---

# How does it relate to other tools


---


# Containers

- Great for deploying to servers
- Creating containers is not reproducible

- Containers with pixi:
  - Pixi's lockfile makes containers reproducible
  - Containers not needed for development or for users to download

    


---

# Deltaforge

- Useful for situations without (good) internet connection
- Not needed for setting up PCs of modelers
- Pixi covers the use cases of Deltares colleagues


---

# QGIS

- It's hard to support QGIS plugins for many QGIS versions
- We might be able to use pixi for distributing:
  - QGIS
  - Our QGIS plugins
  - Our hydrological kernels
- Still investigation needed

---

# Conclusion

- Pixi:
  - replaces conda
  - makes contributing to your product easy
  - reduces maintenance burden
