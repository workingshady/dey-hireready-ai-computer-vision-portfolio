
# 🎵 Spotify Tracks Dataset — Feature Summary, Priority & Predictive Effect

## 🎯 Objective

This dataset can serve **two main predictive tasks**:

* **Regression:** Predicting **track popularity**
* **Classification:** Predicting **track genre**

Below is a complete breakdown of each feature, including:

* **Meaning:** What the feature represents
* **Priority (⚙️ Importance Level):** [High | Medium | Low] — based on potential predictive power
* **Effect on Popularity:** How the feature may influence the popularity score
* **Effect on Genre:** How the feature may influence genre classification

---

## 🧩 Feature Descriptions

### 1. `track_id`

* **Meaning:** Unique Spotify identifier for the track
* **Priority:** Low
* **Effect on Popularity:** None (identifier only)
* **Effect on Genre:** None

---

### 2. `artists`

* **Meaning:** Name(s) of artist(s) performing the track (can include multiple, separated by `;`)
* **Priority:** High
* **Effect on Popularity:** High — well-known artists, collaborations, or trending artists often correlate with higher popularity
* **Effect on Genre:** High — artists usually specialize in specific genres; strong genre-indicative feature

---

### 3. `album_name`

* **Meaning:** Album where the track appears
* **Priority:** Medium
* **Effect on Popularity:** Medium — album reputation and release timing may influence popularity
* **Effect on Genre:** Low — albums may mix genres but usually maintain a consistent style

---

### 4. `track_name`

* **Meaning:** Title of the track
* **Priority:** Low
* **Effect on Popularity:** Indirect — certain title keywords (e.g., “Remix”, “Live”) can affect popularity trends
* **Effect on Genre:** Low — text-based signal only if NLP or embedding features are extracted

---

### 5. `popularity`

* **Meaning:** Target variable for regression — measures overall play count and recency of listens
* **Priority:** Target (Regression)
* **Effect on Popularity:** N/A (target variable)
* **Effect on Genre:** Can be used for correlation but not as an input

---

### 6. `duration_ms`

* **Meaning:** Track length in milliseconds
* **Priority:** Medium
* **Effect on Popularity:** Moderate — tracks too short or too long can have lower popularity
* **Effect on Genre:** Medium — some genres (e.g., classical, jazz) have longer average durations

---

### 7. `explicit`

* **Meaning:** Indicates if a track contains explicit content
* **Priority:** Medium
* **Effect on Popularity:** Mixed — may boost popularity in certain genres (rap, hip-hop) but reduce in others
* **Effect on Genre:** High — strong signal for genre classification, especially hip-hop, rap, trap

---

### 8. `danceability`

* **Meaning:** Suitability for dancing (0.0–1.0) based on rhythm and beat
* **Priority:** High
* **Effect on Popularity:** Strong positive — higher danceability often increases mainstream appeal
* **Effect on Genre:** High — differentiates genres like EDM, pop, and house from acoustic or classical

---

### 9. `energy`

* **Meaning:** Perceptual measure of intensity and activity (0.0–1.0)
* **Priority:** High
* **Effect on Popularity:** Positive — energetic tracks often trend better
* **Effect on Genre:** High — helps separate high-energy genres (rock, metal, EDM) from mellow ones (jazz, acoustic)

---

### 10. `key`

* **Meaning:** Musical key (0–11) using pitch class notation
* **Priority:** Low
* **Effect on Popularity:** Minimal — not strongly correlated with listener preference
* **Effect on Genre:** Low — may weakly relate to genre tendencies (e.g., major/minor preferences)

---

### 11. `loudness`

* **Meaning:** Average loudness in decibels (dB)
* **Priority:** Medium
* **Effect on Popularity:** Positive — louder tracks can sound more energetic and modern
* **Effect on Genre:** Medium — metal and rock are louder; classical and acoustic are quieter

---

### 12. `mode`

* **Meaning:** Musical mode (1 = major, 0 = minor)
* **Priority:** Low
* **Effect on Popularity:** Minor tracks can be perceived as sad; effect may depend on context
* **Effect on Genre:** Medium — pop and dance are often major; jazz and classical can vary

---

### 13. `speechiness`

* **Meaning:** Degree of spoken words presence (0.0–1.0)
* **Priority:** High
* **Effect on Popularity:** Positive in spoken or rap genres
* **Effect on Genre:** Very High — key indicator for rap, hip-hop, and podcasts

---

### 14. `acousticness`

* **Meaning:** Confidence that a track is acoustic (0.0–1.0)
* **Priority:** High
* **Effect on Popularity:** Genre-dependent — may reduce popularity in mainstream pop; increase in indie/acoustic niches
* **Effect on Genre:** High — separates acoustic/folk/jazz from electronic genres

---

### 15. `instrumentalness`

* **Meaning:** Likelihood that the track has no vocals (0.0–1.0)
* **Priority:** High
* **Effect on Popularity:** Often negative — purely instrumental tracks generally have niche audiences
* **Effect on Genre:** Very High — helps detect instrumental genres (classical, ambient, cinematic)

---

### 16. `liveness`

* **Meaning:** Probability that the track was performed live (0.0–1.0)
* **Priority:** Medium
* **Effect on Popularity:** Low — live versions tend to have lower streams than studio versions
* **Effect on Genre:** Medium — jazz, rock, and indie often have higher liveness

---

### 17. `valence`

* **Meaning:** Positiveness of the musical mood (0.0–1.0)
* **Priority:** High
* **Effect on Popularity:** Moderate positive correlation — happy, upbeat songs are often more popular
* **Effect on Genre:** High — differentiates emotional tone (sad = blues, happy = pop)

---

### 18. `tempo`

* **Meaning:** Speed of the track in beats per minute (BPM)
* **Priority:** Medium
* **Effect on Popularity:** Indirect — moderate tempos (~100–130 BPM) tend to perform better commercially
* **Effect on Genre:** High — genres have characteristic tempo ranges (e.g., EDM fast, ballads slow)

---

### 19. `time_signature`

* **Meaning:** Beats per bar (3–7)
* **Priority:** Low
* **Effect on Popularity:** Minimal — most tracks use 4/4, so variance is small
* **Effect on Genre:** Low to Medium — certain genres experiment with complex meters (e.g., jazz, progressive rock)

---

### 20. `track_genre`

* **Meaning:** Target variable for classification — main musical genre of the track
* **Priority:** Target (Classification)
* **Effect on Popularity:** Useful for stratified analysis; genre often influences base popularity
* **Effect on Genre:** N/A (target variable)

---

## 🔑 Summary Table

| Feature          | Priority | Effect on Popularity | Effect on Genre |
| ---------------- | -------- | -------------------- | --------------- |
| artists          | High     | High                 | High            |
| album_name       | Medium   | Medium               | Low             |
| explicit         | Medium   | Mixed                | High            |
| danceability     | High     | High                 | High            |
| energy           | High     | High                 | High            |
| loudness         | Medium   | Positive             | Medium          |
| speechiness      | High     | Positive (rap)       | Very High       |
| acousticness     | High     | Genre-dependent      | High            |
| instrumentalness | High     | Negative             | Very High       |
| valence          | High     | Moderate             | High            |
| tempo            | Medium   | Moderate             | High            |
| liveness         | Medium   | Low                  | Medium          |
| duration_ms      | Medium   | Moderate             | Medium          |
| key              | Low      | Low                  | Low             |
| mode             | Low      | Low                  | Medium          |
| time_signature   | Low      | Low                  | Low             |

