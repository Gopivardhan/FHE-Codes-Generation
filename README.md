# FHE‑Codes‑Generation 🔏

**Fully Homomorphic Encryption Code Generator**

---

## 🚀 Overview

**FHE‑Codes‑Generation** is a toolkit that automates the generation of fully homomorphic encryption (FHE) code snippets. Given a high-level description of operations (e.g. add, multiply, evaluate encrypted data), this project scaffolds working example code using your choice of FHE library (e.g. Microsoft SEAL, HElib).

---

## 🧠 Features

- Interpret structured JSON/YAML configs defining variables and operations  
- Generate template-ready C++/Python source files for:
  - Key generation
  - Encryption/decryption
  - Homomorphic operations  
- Support for multiple FHE backends via pluggable templates  
- Designed for educational demonstrations or rapid prototyping

---

## 🛠️ Installation

Clone the repo and set up the environment:

```bash
git clone https://github.com/Gopivardhan/FHE-Codes-Generation.git
cd FHE-Codes-Generation

pip install -r requirements.txt        # For Python tooling
npm install                            # If there’s a web UI component
```

---

## ⚙️ Usage

1. **Create** a specification, e.g., `specs/example.json`:

```json
{
  "backend": "seal",
  "vars": {
    "a": "plaintext",
    "b": "ciphertext"
  },
  "operations": [
    { "op": "encrypt", "var": "a" },
    { "op": "add", "out": "c", "args": ["a_encrypted", "b"] },
    { "op": "decrypt", "var": "c" }
  ]
}
```

2. **Generate code**:

```bash
python gen_fhe_code.py --spec specs/example.json
```

3. **Output**:

The tool outputs source files (`.cpp`, `.py`, `.h`) in a new directory, e.g.:

```
output/seal_example/
├── main.cpp
├── utils.h
├── build.sh
└── README.generated.md
```

4. **Compile & run**:

```bash
cd output/seal_example
./build.sh       # configures and compiles
./fhe_demo       # run the demo
```

---

## 📐 Supported Backends

- [ ] Microsoft SEAL  
- [ ] HElib  
- [ ] PALISADE  

*To add more backends, create a new template folder and extend the code generator.*

---

## 🧪 Testing

```bash
pytest tests/                 # Run core parser and generation tests
```

Make sure all backends build and execute successfully.

---

## 🧩 Architecture

1. **Parser**: Reads spec file (JSON/YAML → AST)  
2. **Templater**: Renders code via Jinja2 templates  
3. **Output Writer**: Saves code to structured output folder

---

## 🤝 Contributing

Contributions are welcome! 🙌 Open issues or PRs for:

- New backend support  
- Feature requests (e.g. bootstrapping, batching)  
- Bug reports  

Before contributing, please sign the Contributor License Agreement (CLA).

---

## 📚 Resources

- [Microsoft SEAL](https://github.com/Microsoft/SEAL)  
- [HElib](https://github.com/homenc/HElib)  
- [PALISADE](https://github.com/openfheorg/openfhe)

---

## 📝 License

This project is licensed under the **MIT License**. See `LICENSE` for details.

---

