---
theme: seriph
class: "text-center"
highlighter: shiki
lineNumbers: false
fonts:
  sans: Dosis
  mono: "Fira Mono"
colorSchema: dark
themeConfig:
  primary: "#facc15"
title: Pixi, the Missing Companion to Cargo
---

<h1 style="color: var(--slidev-theme-primary)">Pixi,</h1>

the Missing Companion to Cargo

---
layout: image-right
image: julian.jpg
---

# About Me

- 👤 Julian Hofer
- ⚛️ Background in Physics
- 💬 Thinks that languages are cool
- 🤓 Loves to talk about dependency management

---
layout: image-right
image: original-ferris.png
backgroundSize: 20em
---

# Scientific Rust

- Strengths
  - Speed
  - Thread safety
  - Memory safety

<v-click>

- Weaknesses:
  - Steep learning curve
  - Lack of high quality libraries
  - Difficult to depend on libraries *not* written in Rust

</v-click>

---
layout: image-right
image: cargo-logo-small.png
backgroundSize: 20em
---

# Cargo is Not Enough

- Strengths
  - Speed
  - Thread safety
  - Memory safety

<v-click>

- Weaknesses:
  - Steep learning curve
  - Lack of high quality libraries
  - Difficult to depend on libraries *not* written in Rust

</v-click>



---
layout: image-right
image: numpylogo.svg
backgroundSize: 30em
---

# Installing NumPy via Pip

From the NumPy contributor docs:


- Install NumPy as a user:

```bash
pip install numpy
```

<div v-click>

- Install NumPy as a developer:

```bash
# Debian
sudo apt build-dep numpy
# Fedora
sudo dnf builddep numpy
# Arch
sudo pacman -S gcc-fortran openblas pkgconf
# macOS
brew install openblas pkg-config gfortran
```
Finally
```bash
pip install . --no-build-isolation
```
</div>

---
layout: image-right
image: numpylogo.svg
backgroundSize: 30em
---

# Installing NumPy via Conda

From the NumPy contributor docs:
> If you are using Conda, you can skip the steps in this section - with the exception of installing compilers for Windows or the Apple Developer Tools for macOS. All other dependencies will be installed automatically [...] 


```bash
conda env create -f environment.yml

# or
pixi init --import environment.yml
```


---
layout: center
---

# Ecosystem Comparison

<div class="w-lg">

| Feature                    | Conda | PyPI        |
|----------------------------|-------|-------------|
| Official Python Index      | ⚠️    | ✅          |
| Cross-Platform             | ✅    | ✅          |
| Cross-Language             | ✅    | ⚠️          |
| Decentralized              | ✅    | ⚠️          |
| Traditional Package Manager| conda | pip (conda) |
| Modern Package Manager     | pixi  | uv (pixi)   |


</div>

---
layout: image-right
image: paxton-text-in-circle.svg
backgroundSize: 40em
---

# Introducing Pixi

- ⚡ Fast
- 🆓 Open-Source
- 🛠️ Workflow management
- 🌐 Multi-environments
- 🔒 Reproducible thanks to lock-files

---
layout: image-right
image: paxton-text-in-circle.svg
backgroundSize: 30em
---

# Conclusion

- **Dependency management** becomes easier with modern tools
- **Conda**: Cross-platform & cross-language with decentralized channels
- **Pixi**: Package and workflow manager, built on the Conda ecosystem

---
layout: end
---

# Thank you for your attention!


<div class="text-center mt-15">
  <div class="flex justify-center mt-4">
    <div class="mx-16">
      <a href="https://pixi.sh/latest/" target="_blank">
        <img src="/pixi-qr-code.png" alt="Pixi QR Code" class="w-32 h-32">
      </a>
      <p class="mt-2"> Pixi Website</p>
    </div>
    <div class="mx-16">
      <a href="https://www.linkedin.com/in/hofer-julian/" target="_blank">
        <img src="/linkedin-qr-code.png" alt="LinkedIn QR Code" class="w-32 h-32">
      </a>
      <p class="mt-2"><mdi-linkedin /> LinkedIn</p>
    </div>
    <div class="mx-16">
      <a href="https://discord.gg/SQBR8dA5mF" target="_blank">
        <img src="/discord-qr-code.png" alt="Discord QR Code" class="w-32 h-32">
      </a>
      <p class="mt-2"><mdi-discord /> Discord</p>
    </div>
  </div>
</div>
