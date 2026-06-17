# Step-by-Step Audiobook Platform Distribution Guide

This guide details how to publish your modernized *The Secret Garden Chapter 1* pilot as a free book or sample on **Google Play Books** and **Apple Books (via Findaway Voices)**.

---

## 1. Google Play Books (Direct Upload - 100% Free)

Google Play Books allows you to upload and sell/give away audiobooks directly to listeners on Android devices.

### Steps to Register & Publish:
1. **Log in to Partner Center:**
   Go to [https://play.google.com/books/publish/](https://play.google.com/books/publish/) and sign in with your Google account.
2. **Add a New Book:**
   * Click **Add Book**.
   * Under "Book Type", select **Audiobook**.
   * Under "Book Format", choose **Digital Only**.
   * Enter the Title: `The Secret Garden - Modernized Edition for ESL (Chapter 1 Graded Pilot)`.
3. **Upload Content:**
   * **Cover Art:** Upload `D:\git_repo\thefirstaicompany\secret_garden_pilot\podcast\podcast_cover.png` (which is already resized to 3000x3000px).
   * **Audio File:** Upload `D:\git_repo\thefirstaicompany\secret_garden_pilot\audiobook\secret_garden_chapter_1_audiobook_en.mp3`.
4. **Fill in Metadata:**
   * **Author:** Frances Hodgson Burnett (Adapted by TKPROF.AI)
   * **Description:** Add a description explaining that this is a modernization pilot. **Crucial:** Include a clean HTML link back to your landing page: 
     `Pre-order the full audiobook and share feedback at <a href="https://jigsawpuzzlehelper.com/secret_garden/">jigsawpuzzlehelper.com</a>`
   * **Categories:** `Juvenile Fiction / Classics` or `Language Arts & Disciplines / English as a Second Language`.
5. **Set Pricing:**
   * Go to the **Pricing** tab and set the price to **$0.00** (Free Graded Pilot).
6. **Publish:** Review and click **Publish**. (Typically live in 24-72 hours).

---

## 2. Apple Books & Others (via Findaway Voices)

Findaway Voices (owned by Spotify) distributes audiobooks to Apple Books, Barnes & Noble, Kobo, Scribd, and 40+ other platforms. There is no upfront registration cost; they take a percentage of sales (which is $0 since our pilot is free).

### Steps to Register & Publish:
1. **Create Account:**
   Go to [https://findawayvoices.com/](https://findawayvoices.com/) and register.
2. **Create New Project:**
   * Click **Create a Title**.
   * Under "How are you creating this audiobook?", select **"I have the audio files"**.
3. **Fill in Metadata:**
   * **Title:** `The Secret Garden - Modernized Edition for ESL (Chapter 1 Graded Pilot)`
   * **Language:** `English` (Do a separate project for `Korean` if distributing both).
   * **Description:** Use the description from `podcast_metadata.md` and include your feedback landing page URL.
   * **Publisher:** `TKPROF.AI`
4. **Upload Cover Art:**
   * Upload `D:\git_repo\thefirstaicompany\secret_garden_pilot\podcast\podcast_cover.png` (perfectly fits their 3000x3000px requirement).
5. **Upload Audio Tracks:**
   Findaway requires tracks to be split:
   * **Introduction (Opening Credits):** Upload the first 10-15 seconds of the audiobook or render a separate short intro. If not available, you can upload `secret_garden_chapter_1_audiobook_en.mp3` as the main chapter track.
   * **Chapter 1 Track:** Upload `secret_garden_chapter_1_audiobook_en.mp3`.
6. **Distribution Rights & Pricing:**
   * Set the price to **Free / $0.00** if you want it as a lead generator, or set a low promo price.
   * Click **Submit** for distribution review. Findaway's QA team will inspect the audio file specs (which our script automatically matched) and push it live to Apple Books and others in 7-14 days.

---

## 3. Strategic Considerations & Analytics Insights

When launching a single-chapter audiobook pilot, keep these factors in mind for market validation:

### Audiobook Analytics vs. Podcast Analytics
* **Audiobook Platforms (Google Play / Apple Books):**
  * *Metrics Provided:* **Downloads/Units Claimed** (shows general demand) and **Ratings/Reviews** (shows reader feedback).
  * *Limitations:* These platforms **do not** provide granular play-duration graphs. You will not know if users stop listening after the first minute or finish the entire chapter.
* **Podcast Platforms (Spotify / Apple Podcasts):**
  * *Metrics Provided:* Second-by-second **audience retention graphs**. This shows you exactly where listeners lose interest (e.g. at a specific AI voice transition or a complex sentence).

### Avoid Customer Backlash on Length
Because customers on Google Play or Apple Books expect full novels, a 10-minute file can trigger negative reviews if not clearly framed.
* **Action:** Always include words like `Chapter 1 Pilot`, `Free Sample`, or `Graded Reader Preview` directly in the title and the first line of the description.

### Recommended Hybrid Strategy
1. Use **Podcast distribution** as your core **quality-testing tool** to analyze listener retention and drop-off points.
2. Use **Google Play Books (Audiobook)** as a **marketing funnel** to test search demand and drive traffic to your GoDaddy pre-order/feedback landing page via the book description link.
