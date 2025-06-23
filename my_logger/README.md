# 📦 my_logger - Simple CSV Logging Tool

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)

A lightweight and flexible Python tool to log journal entries, moods, tasks, and more - all saved to a CSV file. Built for quick note-taking and analysis.

---

## ✅ Features
- Log events with a timestamp
- Track mood, task, and journal in one place
- Save structured entries to a CSV file
- Easy-to-extend architecture (with utils)
- CLI-ready (just run `python -m my_logger`)

---

## 📂 Project Structure

```text
my_logger/
├── __init__.py
├── logger_core.py
└── utils/
    └── reusable_functions.py
```

## 🚀 Installation & Run

1. **Install the package locally (editable mode):**

   ```bash
   pip install -e .
   ```

2. **Run the logger:**

   ```bash
   python -m my_logger
   ```

3. **Your file will be saved as:**

   ```plaintext
   log.csv
   ```

## 🧾 Example Log Entry (CSV)

```csv
title,date,time,mood,task,journal
third note,2025-06-19,17:38:37,happy,walk the dog,He didn't want to walk
```

## 🌌 Screenshots
   ![Main Menu](logger_1.png)
   ![View logs](logger_2.png)
   
## 📌 Notes
- Make sure log.csv is in your working directory or will be created on first run.
- You can extend this tool easily using the utility methods in **utils/reusable_functions.py**.

## 🙋🏻 About
Built as part of a summer programming warm-up plan. See the full [Learning Plan](https://github.com/riderBruce/programming-warmup/wiki/Learning-Plan) for weekly milestones.

---
## 📄 License

This project is licensed under the terms of the [MIT License](../LICENSE).