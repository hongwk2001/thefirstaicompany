# Audiobook Project Roadmap: Modernized Classical Novels for ESL Learners

## 1. Project Vision

To create audiobooks of classical novels (e.g., *The Secret Garden*) translated into modern, engaging English, specifically targeting English as a Second Language (ESL) listeners and modern casual readers who seek to enjoy great literature without the archaic language barriers of original texts.

## 2. Market Validation: Why a Market Exists

*   **The "Language Barrier" for Modern Readers:** Traditional classical literature often uses archaic phrasing, vocabulary, and complex sentence structures, making it challenging even for native English speakers.
*   **Massive ESL/EFL Demographic:** Millions of intermediate-to-advanced English learners desire to consume classic literature for language improvement but are hindered by outdated vocabulary and complex syntax.
*   **Public Domain Advantage:** Utilizing public domain works eliminates licensing and copyright fees, allowing for legal rewriting, recording, and sale of modernized versions.
*   **"Edutainment" Trend:** There's a growing demand for content that educates and entertains simultaneously, enabling busy professionals and adult learners to multitask and feel intellectually stimulated without needing a dictionary.

## 3. Lean Validation Experiment: Investigate and Test the Market

Before committing significant resources to a full novel, a low-cost, low-risk validation experiment will be conducted:

### [x] Step 1: Select a 1-Chapter Pilot
*   **Time:** 2-3 days
*   **Task:** Choose a famous, high-interest scene (approx. 1,000 to 1,500 words) from a public domain classic like *The Secret Garden*.

### [x] Step 2: Dual-Language Adaptation (English & Korean)
*   **Time:** 2 days
*   **Task 2.1:** Rewrite the entire Chapter 1 of *The Secret Garden* into modern, clear, engaging English suitable for an advanced ESL listener or modern casual reader. Keep the emotional depth and plot, but remove archaic vocabulary and overly complex 19th-century sentence structures.
*   **Task 2.2:** Translate the entire Chapter 1 of *The Secret Garden* directly from the original English source text into natural, modern, and engaging Korean, preserving the richness and detail of the original story.

### [x] Step 3: Audio Generation Pipeline - English (Full Chapter 1)
*   **Time:** 2 days
*   **Step 3.1: Voice Selection & Preview:** Identify ElevenLabs voices for each character (Narrator, Mary, Servant, Mother, Officer) and generate previews.
*   **Step 3.2: Structured Script Preparation:** Format the full modernized Chapter 1 text into a structured JSON script. Explicitly replace roman numerals like "CHAPTER I." with phonetic text ("Chapter One") to prevent the TTS from reading it as "Chapter Eye".
*   **Step 3.3: Automated Audio Generation & Stitching:** Programmatically compile the segments into a seamless, multi-voice audiobook file for the entire Chapter 1.

### [x] Step 4: Audio Generation Pipeline - Korean (Full Chapter 1)
*   **Time:** 2-3 days
*   **Task:** Programmatically generate the Korean multi-voice audiobook for the entire Chapter 1 using ElevenLabs' multilingual model. Format roman numerals phonetically (e.g., "제일 장" instead of "제I장") to ensure proper pronunciation, and compile the final file.

### [/] Step 5: Lean Market Smoke Testing (YouTube & YouTube Podcasts)
*   **Time:** 1-2 weeks
*   **Strategy:** Run our pilot primarily on YouTube. By creating a dedicated Podcast playlist in YouTube Studio, we automatically distribute it to YouTube Music listeners (reaching the podcast audience) with zero additional setup or hosting fees.

#### [x] Step 5.1: YouTube & YouTube Podcasts Setup & Launch
*   **[x] Task 5.1.1: Visual Asset Creation:** Generate a high-quality, atmospheric background image representing the garden (e.g., 1920x1080) and a high-CTR thumbnail image.
*   **[x] Task 5.1.2: Video Rendering:** Merge the compiled audiobooks (English/Korean versions) with the background image to produce `.mp4` video files.
*   **[x] Task 5.1.3: Subtitle Integration:** Generate timed subtitle tracks (`.srt` format) or overlay hardcoded styled captions for the listener to follow along.
*   **[x] Task 5.1.4: SEO & Metadata Setup:** Draft video titles, descriptions (including Chapter 1 text/translation), relevant tags (ESL, English listening), and a call-to-action (CTA) link for feedback.
*   **[x] Task 5.1.5: Upload & Launch:** Upload the English and Korean pilots to YouTube.
*   **[x] Task 5.1.6: Podcast Designation:** In YouTube Studio, create a new Podcast playlist, add the uploaded videos as episodes, and publish them to YouTube Music.
*   **[x] Task 5.1.7: Update Video Links:** Replace the description placeholders on YouTube with the live feedback/pre-order landing page link.

#### [/] Step 5.2: Phase 2 Expansion (Traditional Podcasts & Audiobook Platforms)
*Note: Execute this only if the YouTube/YouTube Music pilot shows positive validation metrics (retention and CTR).*
*   **[x] Podcast RSS Distribution:** Published English pilot and Korean pilot on Spotify for Podcasters (both live under a single unified feed).
    *   *Automation Note:* We can fully automate future uploads by hosting our own RSS XML feed on GoDaddy. A script will auto-generate the feed and upload audio files directly to the server.
*   **[/] Audiobook Platforms:** 
    *   *Google Play:* **[x]** Uploaded both English and Korean versions. Currently pending Google's policy/account review (live soon).
    *   *Findaway (Apple Books/etc.):* **[/]** English project created, audio splits (credits/samples) uploaded. Currently waiting on Findaway's 24-hour verification hold to complete tax/payment setup and finalize submission.
    *   *Korean Local Platforms Note:* Domestic platforms like **Welaaa (윌라)** and **Millie's Library (밀리의 서재)** dominate the Korean domestic market instead of Apple/Spotify. Direct submission to these platforms should be pursued if validation metrics look positive for the Korean pilot edition.
*   **[x] Pre-order Landing Page:** Build a responsive landing page and host it on `jigsawpuzzlehelper.com/secret_garden/` to capture emails and host direct pre-order/feedback links.

### [ ] Step 6: Multi-Channel Data Analysis
*   **Time:** 2 weeks (Ongoing monitoring)
*   **Detailed Analytics Checklist:**
    *   **Podcast Analytics (Spotify for Creators):**
        *   *Retention Graphs:* Monitor the second-by-second drop-off curve for Episode 1 (English) and Episode 2 (Korean). Look for steep drops which indicate spelling/pacing issues or off-putting character voice shifts.
        *   *Completion Rate:* Aim for >25% of listeners reaching the end of the 10-minute episode (industry standard for cold podcast discoveries).
    *   **GoDaddy Landing Page & Feedback (Direct Emails):**
        *   *Inbox Review:* Audit incoming emails to `tkprof.ai@gmail.com` daily.
        *   *Rating Breakdown:* Calculate average rating scores (e.g. ratio of "Excellent (Clear & Easy)" to "Good" or "Hard").
        *   *Pre-order Conversion Rate:* Ratio of total landing page visitors to optional email signup subscriptions (Target: >3% signup conversion rate, typical for cold web traffic).
    *   **Google Play Books Dashboard:**
        *   *Acquisition Volume:* Track free downloads (units claimed) for the English and Korean books.
        *   *Store Reviews:* Monitor qualitative store ratings and reviews (important since readers on book stores have different expectations than podcast listeners).
    *   **YouTube Studio & YouTube Music:**
        *   *Visual Optimization:* Compare Impression Click-Through Rate (CTR) between the English and Korean thumbnails (Target: >3.5% CTR, standard for new channel discovery).
        *   *Engagement Rates:* Check Comments, Likes, and Shares to verify organic reach and viewer feedback.
    *   **Decision Point:** If audience retention is stable (>30% average view duration) on YouTube/Spotify and we receive positive ratings/emails via the GoDaddy form, trigger full-book production for Chapter 2.



## 4. Hidden Challenges to Keep in Mind

1.  **Narration Quality is King:** High-quality voice performance is crucial for audiobooks. Robotic or jarring cadences will negatively impact retention. Prioritize premium AI voices or consider professional voice talent for scaling.
2.  **Preserving the "Soul" of the Book:** The modernization process must maintain the original story's magic, setting, and emotional depth without "dumbing down" the content. The goal is to update the language, not diminish the literary essence.
3.  **Discoverability:** The public domain market is saturated with original versions. Marketing efforts must clearly highlight the unique value proposition: "Classic stories told in the language we speak today."

## 5. Production Rules for Chapter Openings (Voiceover Introductions)

For future chapters and revision renders, always prefix the audiobook files with standard opening announcements:

*   **English Audio Intro:**
    *   *Template:* Mention the **Title**, **Author**, **Year Written**, and a brief description explaining that this edition is customized in simple, modern English for middle schoolers and up.
    *   *Example:* `"The Secret Garden, written by Frances Hodgson Burnett in 1911. This edition is adapted into clear, modern English, designed for middle school students and language learners."`
*   **Korean Audio Intro:**
    *   *Template:* Appeal that this is a fresh, modern translation of the original text using AI assistance for 2026.
    *   *Example:* `"고전원문을 AI를 이용한 2026년식 새 번역으로 만나는 비밀의 화원."`
