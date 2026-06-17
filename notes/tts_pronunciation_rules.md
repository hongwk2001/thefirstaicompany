# TTS Pronunciation & Formatting Rules

To ensure high-quality audiobook output, always preprocess source texts before feeding them to Text-to-Speech (TTS) models:

### 1. Roman Numeral Chapter Headings
* **Problem:** TTS models read "CHAPTER I." as "Chapter Eye", "CHAPTER II." as "Chapter Eye Eye", and so on.
* **Rule:** Convert all Roman numerals in titles/headings to their phonetic equivalent:
  * `CHAPTER I.` ➡️ `Chapter One`
  * `CHAPTER II.` ➡️ `Chapter Two`
  * `CHAPTER III.` ➡️ `Chapter Three`
  * `CHAPTER IV.` ➡️ `Chapter Four`
  * `CHAPTER V.` ➡️ `Chapter Five`

### 2. Korean Chapter Headings
* **Problem:** TTS models read "제I장" or "제1장" incorrectly if not spelled out.
* **Rule:** Phonetically spell out chapter headers in Korean scripts:
  * `제I장` or `제1장` ➡️ `제일 장` (Je-il jang)
  * `제II장` or `제2장` ➡️ `제이 장` (Je-i jang)
